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

from backend.database.inventory_db import (
add_inventory,
get_inventory
)

class InventoryPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # ==========================
        # TITLE
        # ==========================

        title = QLabel("Inventory")

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
            "Search Inventory..."
        )

        self.search.textChanged.connect(
            self.search_inventory
        )

        layout.addWidget(self.search)

        # ==========================
        # INPUT AREA
        # ==========================

        form = QHBoxLayout()

        self.item_name = QLineEdit()
        self.item_name.setPlaceholderText(
            "Item Name"
        )

        self.sku = QLineEdit()
        self.sku.setPlaceholderText(
            "SKU"
        )

        self.qty = QLineEdit()
        self.qty.setPlaceholderText(
            "Quantity"
        )

        self.price = QLineEdit()
        self.price.setPlaceholderText(
            "Price"
        )

        self.gst = QLineEdit()
        self.gst.setPlaceholderText(
            "GST %"
        )

        self.date = QLineEdit()
        self.date.setPlaceholderText(
            "Entry Date"
        )

        self.sale_date = QLineEdit()
        self.sale_date.setPlaceholderText(
            "Sale Date"
        )

        form.addWidget(self.item_name)
        form.addWidget(self.sku)
        form.addWidget(self.qty)
        form.addWidget(self.price)
        form.addWidget(self.gst)
        form.addWidget(self.date)
        form.addWidget(self.sale_date)

        layout.addLayout(form)

        # ==========================
        # SAVE BUTTON
        # ==========================

        save_btn = QPushButton(
            "Save Inventory Item"
        )

        save_btn.clicked.connect(
            self.save_item
        )

        layout.addWidget(save_btn)

        # ==========================
        # TABLE
        # ==========================

        self.table = QTableWidget()

        self.table.setColumnCount(10)

        self.table.setHorizontalHeaderLabels([
            "Item",
            "SKU",
            "Qty",
            "Price",
            "GST %",
            "Amount",
            "Total",
            "Pending Stock",
            "Date",
            "Sale Date"
        ])

        layout.addWidget(self.table)

        self.load_inventory()

    # ==========================
    # SAVE ITEM
    # ==========================

    def save_item(self):

        item = self.item_name.text().strip()
        sku = self.sku.text().strip()

        if not item:

            QMessageBox.warning(
                self,
                "Error",
                "Item Name Required"
            )

            return

        try:

            qty = int(
                self.qty.text()
            )

            price = float(
                self.price.text()
            )

            gst = float(
                self.gst.text()
            )

        except ValueError:

            QMessageBox.warning(
                self,
                "Error",
                "Enter valid values"
            )

            return

        entry_date = self.date.text().strip()

        sale_date = self.sale_date.text().strip()

        add_inventory(
            item,
            sku,
            qty,
            price,
            gst,
            entry_date,
            sale_date
        )

        self.item_name.clear()
        self.sku.clear()
        self.qty.clear()
        self.price.clear()
        self.gst.clear()
        self.date.clear()
        self.sale_date.clear()

        self.load_inventory()

        QMessageBox.information(
            self,
            "Saved",
            "Inventory Saved Successfully"
        )

    # ==========================
    # LOAD INVENTORY
    # ==========================

    def load_inventory(self):

        data = get_inventory()

        self.table.setRowCount(
            len(data)
        )

        for row, item in enumerate(data):

            values = [
                item[1],   # item_name
                item[2],   # sku
                item[3],   # quantity
                item[4],   # price
                item[5],   # gst_percent
                item[7],   # amount
                item[8],   # total
                item[9],   # pending_stock
                item[10],  # entry_date
                item[11]   # sale_date
            ]

            for col, value in enumerate(values):

                self.table.setItem(
                    row,
                    col,
                    QTableWidgetItem(
                        str(value)
                    )
                )

    # ==========================
    # SEARCH INVENTORY
    # ==========================

    def search_inventory(self):

        text = self.search.text().lower()

        data = get_inventory()

        filtered = []

        for item in data:

            if (
                text in str(item[1]).lower()
                or
                text in str(item[2]).lower()
            ):

                filtered.append(item)

        self.table.setRowCount(
            len(filtered)
        )

        for row, item in enumerate(filtered):

            values = [
                item[1],
                item[2],
                item[3],
                item[4],
                item[5],
                item[7],
                item[8],
                item[9],
                item[10],
                item[11]
            ]

            for col, value in enumerate(values):

                self.table.setItem(
                    row,
                    col,
                    QTableWidgetItem(
                        str(value)
                    )
                )

