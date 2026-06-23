from PySide6.QtWidgets import (
    QWidget, QLabel,
    QVBoxLayout, QTableWidget
)


class EmailPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Email Center")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#0D5A9C;
        """)

        layout.addWidget(title)

        table = QTableWidget()
        table.setColumnCount(4)

        table.setHorizontalHeaderLabels(
            ["Invoice", "Customer", "Email", "Status"]
        )

        layout.addWidget(table)