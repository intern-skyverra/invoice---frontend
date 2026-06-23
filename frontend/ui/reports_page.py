from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton
)


class ReportsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Same spacing as Dashboard
        layout.setContentsMargins(20, 5, 20, 20)
        layout.setSpacing(10)

        grid = QGridLayout()

        reports = [
            "Daily Sales",
            "Weekly Sales",
            "Monthly Sales",
            "Top Customers",
            "Top Inventory",
            "GST Reports"
        ]

        row = 0
        col = 0

        for report in reports:

            btn = QPushButton(report)

            # Same height as Dashboard cards
            btn.setMinimumHeight(120)

            btn.setStyleSheet("""
                QPushButton{
                    background:white;
                    border:2px solid #18A8E0;
                    border-radius:15px;
                    font-size:16px;
                    font-weight:bold;
                    color:#0D5A9C;
                }

                QPushButton:hover{
                    background:#EAF7FF;
                }
            """)

            grid.addWidget(btn, row, col)

            col += 1

            if col > 1:
                col = 0
                row += 1

        layout.addLayout(grid)

        # Keep everything aligned to the top
        layout.addStretch()