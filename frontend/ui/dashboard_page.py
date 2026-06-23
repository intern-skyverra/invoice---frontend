from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton
)


class DashboardPage(QWidget):
    def __init__(self, navigate_callback=None):
        super().__init__()

        self.navigate_callback = navigate_callback

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 10, 20, 20)
        layout.setSpacing(10)

        grid = QGridLayout()

        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(20)

        cards = [
            ("Create Invoice", 1),
            ("Customers", 2),
            ("Inventory", 3),
            ("WhatsApp", 4),
            ("Email", 5),
            ("Reports", 7),
            ("Print Center", 6)
        ]

        row = 0
        col = 0

        for text, page_index in cards:

            btn = QPushButton(text)

            btn.setMinimumHeight(100)

            btn.setStyleSheet("""
                QPushButton{
                    background:white;
                    border:2px solid #DCEFFF;
                    border-radius:18px;
                    font-size:18px;
                    font-weight:bold;
                    color:#0D5A9C;
                }

                QPushButton:hover{
                    background:#F0FAFF;
                    border:2px solid #18A8E0;
                }
            """)

            btn.clicked.connect(
                lambda checked=False, i=page_index:
                self.open_page(i)
            )

            grid.addWidget(btn, row, col)

            col += 1

            if col > 1:
                col = 0
                row += 1

        layout.addLayout(grid)

        layout.addStretch()

    def open_page(self, page_index):

        if self.navigate_callback:
            self.navigate_callback(page_index)