import os
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QHBoxLayout,
    QMessageBox,
    QCompleter
)

from PySide6.QtCore import Qt
from datetime import datetime
import sqlite3
from backend.config import DATABASE_PATH

from backend.pdf.invoice_generator import generate_invoice
from backend.printing.print_service import print_file

from backend.database.customers_db import (
    get_customer_by_name,
    get_customer_names
)


class InvoicePage(QWidget):

    def __init__(self):
        super().__init__()

        self.pdf_file = "SkyVerra_Invoice.pdf"

        self.init_ui()

    def generate_invoice_number(self):

        conn = sqlite3.connect(
            DATABASE_PATH
        )

        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM invoices"
        )

        count = cursor.fetchone()[0]

        conn.close()

        return f"SV-{count + 1:04d}"

    def init_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Create Invoice")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#0D5A9C;
        """)

        layout.addWidget(title)

        # ==========================
        # Invoice Details
        # ==========================

        self.invoice_no = QLineEdit()

        self.invoice_no.setText(
            self.generate_invoice_number()
        )

        self.invoice_no.setReadOnly(True)

        self.date = QLineEdit()

        self.date.setText(
            datetime.now().strftime("%d-%m-%Y")
        )

        self.date.setReadOnly(True)

        layout.addWidget(self.invoice_no)
        layout.addWidget(self.date)

        # ==========================
        # Customer Name
        # ==========================

        self.customer_name = QLineEdit()

        self.customer_name.setPlaceholderText(
            "Customer Name"
        )

        customer_names = get_customer_names()

        self.completer = QCompleter(
            customer_names
        )

        self.completer.setCaseSensitivity(
            Qt.CaseInsensitive
        )

        self.completer.setFilterMode(
            Qt.MatchContains
        )

        self.customer_name.setCompleter(
            self.completer
        )

        self.completer.activated.connect(
            self.autofill_customer
        )

        layout.addWidget(
            self.customer_name
        )

        # ==========================
        # Customer Details
        # ==========================

        self.customer_address = QLineEdit()

        self.customer_address.setPlaceholderText(
            "Customer Address"
        )

        self.customer_gstin = QLineEdit()

        self.customer_gstin.setPlaceholderText(
            "Customer GSTIN"
        )

        self.phone = QLineEdit()

        self.phone.setPlaceholderText(
            "Phone Number"
        )

        self.email = QLineEdit()

        self.email.setPlaceholderText(
            "Customer Email"
        )

        layout.addWidget(
            self.customer_address
        )

        layout.addWidget(
            self.customer_gstin
        )

        layout.addWidget(
            self.phone
        )

        layout.addWidget(
            self.email
        )

        # ==========================
        # Product Table
        # ==========================

        self.table = QTableWidget()

        self.table.setRowCount(10)

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Product",
            "HSN/SAC",
            "Qty",
            "Rate",
            "GST %"
        ])

        layout.addWidget(self.table)

        # ==========================
        # Buttons
        # ==========================

        btn_layout = QHBoxLayout()

        generate_btn = QPushButton(
            "Generate Invoice PDF"
        )

        print_btn = QPushButton(
            "Print Invoice"
        )

        btn_layout.addWidget(
            generate_btn
        )

        btn_layout.addWidget(
            print_btn
        )

        layout.addLayout(
            btn_layout
        )

        generate_btn.clicked.connect(
            self.generate_pdf
        )

        print_btn.clicked.connect(
            self.print_invoice
        )

    # ==========================
    # AUTO FILL CUSTOMER
    # ==========================

    def autofill_customer(self):

        customer_name = (
            self.customer_name.text().strip()
        )

        if not customer_name:
            return

        customer = get_customer_by_name(
            customer_name
        )

        if not customer:
            return

        self.phone.setText(
            str(customer[2] or "")
        )

        self.email.setText(
            str(customer[3] or "")
        )

        self.customer_gstin.setText(
            str(customer[4] or "")
        )

        self.customer_address.setText(
            str(customer[5] or "")
        )

    # ==========================
    # GENERATE PDF
    # ==========================

    def generate_pdf(self):

        items = []

        grand_total = 0

        for row in range(
            self.table.rowCount()
        ):

            product = self.table.item(row, 0)
            hsn = self.table.item(row, 1)
            qty = self.table.item(row, 2)
            rate = self.table.item(row, 3)
            gst = self.table.item(row, 4)

            if product and qty and rate:

                try:

                    qty_value = float(
                        qty.text()
                    )

                    rate_value = float(
                        rate.text()
                    )

                except ValueError:
                    continue

                total = qty_value * rate_value

                grand_total += total

                items.append({

                    "product":
                    product.text(),

                    "hsn":
                    hsn.text() if hsn else "",

                    "qty":
                    qty.text(),

                    "rate":
                    rate.text(),

                    "gst":
                    gst.text() if gst else "0",

                    "total":
                    total
                })

        if not items:

            QMessageBox.warning(
                self,
               "Warning",
               "Please add at least one product"
            )

            return

    # ==========================
    # CREATE DATE-WISE FOLDER
    # ==========================

        today_folder = datetime.now().strftime(
            "%d-%m-%Y"
        )

        documents_path = os.path.join(
            os.path.expanduser("~"),
            "OneDrive",
            "Documents"
        )

        invoice_folder = os.path.join(
            documents_path,
            "SkyVerra Invoices",
            today_folder
        )
        
        os.makedirs(
            invoice_folder,
            exist_ok=True
        )

        pdf_file = os.path.join(
            invoice_folder,
            f"{self.invoice_no.text()}.pdf"
        )

        data = {

            "invoice_no":
            self.invoice_no.text(),

            "date":
            self.date.text(),

            "customer":
            self.customer_name.text(),

            "address":
            self.customer_address.text(),

            "gstin":
            self.customer_gstin.text(),

            "phone":
            self.phone.text(),

            "email":
            self.email.text(),

            "items":
            items,

            "total":
            grand_total
        }

        try:

            generate_invoice(
                data,
                pdf_file
            )

        except Exception as e:

            QMessageBox.warning(
                self,
                "PDF Error",
                str(e)
            )

            return

        self.pdf_file = pdf_file

        from backend.database.db import get_connection

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO invoices
            (
                invoice_no,
                customer_name,
                subtotal,
                gst,
                grand_total,
                invoice_date
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                data["invoice_no"],
                data["customer"],
                data["total"],
                0,
                data["total"],
                data["date"]
            )
        )

        conn.commit()
        conn.close()

        QMessageBox.information(
            self,
            "Success",
            "Invoice Generated Successfully"
        )

        self.invoice_no.setText(
            self.generate_invoice_number()
        )

        self.date.setText(
            datetime.now().strftime("%d-%m-%Y")
        )

        self.customer_name.clear()
        self.customer_address.clear()
        self.customer_gstin.clear()
        self.phone.clear()
        self.email.clear()

        self.table.clearContents()

    # ==========================
    # OPEN PDF
    # ==========================

    def open_pdf(self):

        import os

        if os.path.exists(
            self.pdf_file
        ):

            os.startfile(
                self.pdf_file
            )

        else:

            QMessageBox.warning(
                self,
                "Error",
                "Generate invoice first"
            )

    # ==========================
    # PRINT
    # ==========================

    def print_invoice(self):

        try:

            print_file(
                self.pdf_file
            )

            QMessageBox.information(
                self,
                "Success",
                "Invoice Sent To Printer"
            )

        except Exception as e:

            QMessageBox.warning(
                self,
                "Print Error",
                str(e)
            )