from PySide6.QtWidgets import (
    QWidget, QLabel,
    QVBoxLayout, QTableWidget
)


class WhatsAppPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("WhatsApp Center")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#0D5A9C;
        """)

        layout.addWidget(title)

        table = QTableWidget()
        table.setColumnCount(3)

        table.setHorizontalHeaderLabels(
            ["Invoice", "Customer", "Status"]
        )

        layout.addWidget(table)