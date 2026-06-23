from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QGroupBox,
    QFormLayout,
    QComboBox
)


class PrintCenterPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        title = QLabel("Print Center")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#0D5A9C;
        """)

        main_layout.addWidget(title)

        printer_box = QGroupBox("Printer Settings")

        form = QFormLayout()

        self.printer_combo = QComboBox()
        self.printer_combo.addItems([
            "HP LaserJet",
            "Canon Printer",
            "Epson Printer"
        ])

        form.addRow("Connected Printer:", self.printer_combo)

        printer_box.setLayout(form)

        main_layout.addWidget(printer_box)

        test_btn = QPushButton("Print Test Page")
        main_layout.addWidget(test_btn)

        queue_label = QLabel("Print Queue")
        queue_label.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        main_layout.addWidget(queue_label)

        self.queue_table = QTableWidget()
        self.queue_table.setColumnCount(3)

        self.queue_table.setHorizontalHeaderLabels(
            ["Invoice No", "Customer", "Status"]
        )

        main_layout.addWidget(self.queue_table)