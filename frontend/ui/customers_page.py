from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox
)

from backend.database.customers_db import (
    add_customer,
    get_customers
)


class CustomersPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # ==========================
        # TITLE
        # ==========================

        title = QLabel("Customers")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#0D5A9C;
        """)

        layout.addWidget(title)

        # ==========================
        # SEARCH
        # ==========================

        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "Search Customer..."
        )

        self.search.textChanged.connect(
            self.search_customers
        )

        layout.addWidget(self.search)

        # ==========================
        # FORM
        # ==========================

        form_layout = QHBoxLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText(
            "Customer Name"
        )

        self.phone = QLineEdit()
        self.phone.setPlaceholderText(
            "Phone Number"
        )

        self.email = QLineEdit()
        self.email.setPlaceholderText(
            "Email"
        )

        self.gst = QLineEdit()
        self.gst.setPlaceholderText(
            "GST Number"
        )

        self.address = QLineEdit()
        self.address.setPlaceholderText(
            "Address"
        )

        form_layout.addWidget(self.name)
        form_layout.addWidget(self.phone)
        form_layout.addWidget(self.email)
        form_layout.addWidget(self.gst)
        form_layout.addWidget(self.address)

        layout.addLayout(form_layout)

        # ==========================
        # SAVE BUTTON
        # ==========================

        self.save_btn = QPushButton(
            "Save Customer"
        )

        self.save_btn.clicked.connect(
            self.save_customer
        )

        layout.addWidget(self.save_btn)

        # ==========================
        # TABLE
        # ==========================

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Name",
            "Phone",
            "Email",
            "GST Number",
            "Address"
        ])

        layout.addWidget(self.table)

        self.load_customers()

    # ==========================
    # SAVE CUSTOMER
    # ==========================

    def save_customer(self):

        name = self.name.text().strip()
        phone = self.phone.text().strip()
        email = self.email.text().strip()
        gst = self.gst.text().strip()
        address = self.address.text().strip()

        if not name:

            QMessageBox.warning(
                self,
                "Warning",
                "Customer Name Required"
            )

            return

        add_customer(
            name,
            phone,
            email,
            gst,
            address
        )

        self.name.clear()
        self.phone.clear()
        self.email.clear()
        self.gst.clear()
        self.address.clear()

        self.load_customers()

        QMessageBox.information(
            self,
            "Success",
            "Customer Saved Successfully"
        )

    # ==========================
    # LOAD CUSTOMERS
    # ==========================

    def load_customers(self):

        customers = get_customers()

        self.table.setRowCount(
            len(customers)
        )

        for row, customer in enumerate(customers):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    str(customer[1])
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(customer[2])
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    str(customer[3])
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    str(customer[4])
                )
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    str(customer[5])
                )
            )

    # ==========================
    # SEARCH
    # ==========================

    def search_customers(self):

        search_text = self.search.text().lower()

        customers = get_customers()

        filtered = []

        for customer in customers:

            if (
                search_text in str(customer[1]).lower()
                or search_text in str(customer[2]).lower()
                or search_text in str(customer[3]).lower()
                or search_text in str(customer[4]).lower()
                or search_text in str(customer[5]).lower()
            ):
                filtered.append(customer)

        self.table.setRowCount(
            len(filtered)
        )

        for row, customer in enumerate(filtered):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    str(customer[1])
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(customer[2])
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    str(customer[3])
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    str(customer[4])
                )
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    str(customer[5])
                )
            )