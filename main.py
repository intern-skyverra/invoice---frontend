import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    QSizePolicy
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

# Import Pages

from frontend.ui.dashboard_page import DashboardPage
from frontend.ui.invoice_page import InvoicePage
from frontend.ui.customers_page import CustomersPage
from frontend.ui.inventory_page import InventoryPage
from frontend.ui.whatsapp_page import WhatsAppPage
from frontend.ui.email_page import EmailPage
from frontend.ui.print_center_page import PrintCenterPage
from frontend.ui.reports_page import ReportsPage
from frontend.ui.settings_page import SettingsPage
from frontend.ui.company_profile_page import CompanyProfilePage
from backend.database.db import create_tables



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SkyVerra Invoice Solution")
        self.resize(1400, 850)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # ==========================
        # SIDEBAR
        # ==========================

        sidebar = QWidget()
        sidebar.setFixedWidth(260)

        sidebar.setStyleSheet("""
            background-color: #0D5A9C;
        """)

        sidebar_layout = QVBoxLayout(sidebar)

        # ==========================
        # LOGO
        # ==========================

        logo = QLabel()

        pixmap = QPixmap("assets/icons/logo.png")

        if not pixmap.isNull():
            logo.setPixmap(
                pixmap.scaled(
                    70,
                    70,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

        logo.setAlignment(Qt.AlignCenter)

        sidebar_layout.addWidget(logo)

        # ==========================
        # APP TITLE
        # ==========================

        title = QLabel("SkyVerra")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            color:white;
            font-size:24px;
            font-weight:bold;
        """)

        sidebar_layout.addWidget(title)

        sidebar_layout.addSpacing(20)

        # ==========================
        # PAGES
        # ==========================

        self.stack = QStackedWidget()

        self.dashboard_page = DashboardPage(
            self.change_page
        )
        self.invoice_page = InvoicePage()
        self.customers_page = CustomersPage()
        self.inventory_page = InventoryPage()
        self.whatsapp_page = WhatsAppPage()
        self.email_page = EmailPage()
        self.print_page = PrintCenterPage()
        self.reports_page = ReportsPage()
        self.settings_page = SettingsPage()
        self.company_page = CompanyProfilePage()

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.invoice_page)
        self.stack.addWidget(self.customers_page)
        self.stack.addWidget(self.inventory_page)
        self.stack.addWidget(self.whatsapp_page)
        self.stack.addWidget(self.email_page)
        self.stack.addWidget(self.print_page)
        self.stack.addWidget(self.reports_page)
        self.stack.addWidget(self.settings_page)
        self.stack.addWidget(self.company_page)

        # ==========================
        # MENU BUTTONS
        # ==========================

        self.menu_buttons = []

        menu_items = [
            ("Dashboard", 0),
            ("Invoices", 1),
            ("Customers", 2),
            ("Inventory", 3),
            ("WhatsApp", 4),
            ("Email", 5),
            ("Print Center", 6),
            ("Reports", 7),
            ("Settings", 8),
            ("Company Profile", 9)
        ]

        for text, index in menu_items:

            btn = QPushButton(text)

            btn.setMinimumHeight(48)

            btn.setStyleSheet("""
                QPushButton{
                    color:white;
                    background:transparent;
                    border:none;
                    text-align:left;
                    padding-left:20px;
                    font-size:15px;
                    border-radius:8px;
                }

                QPushButton:hover{
                    background:#18A8E0;
                }
            """)

            btn.clicked.connect(
                lambda checked=False, i=index:
                self.change_page(i)
            )

            self.menu_buttons.append(btn)

            sidebar_layout.addWidget(btn)

        # Dashboard selected by default
        self.change_page(0)

        sidebar_layout.addStretch()

        # ==========================
        # FOOTER
        # ==========================

        footer = QLabel("© skyverra")

        footer.setAlignment(Qt.AlignCenter)

        footer.setStyleSheet("""
            color:white;
            padding:10px;
        """)

        sidebar_layout.addWidget(footer)

        # ==========================
        # CONTENT AREA
        # ==========================

        content_area = QWidget()

        content_layout = QVBoxLayout(content_area)
        content_layout.setContentsMargins(0, 0, 0, 0)

        content_layout.addWidget(self.stack)

        # ==========================
        # MAIN LAYOUT
        # ==========================

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content_area)

        content_area.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    # ==========================
    # PAGE SWITCHING + ACTIVE MENU
    # ==========================

    def change_page(self, index):

        self.stack.setCurrentIndex(index)

        normal_style = """
            QPushButton{
                color:white;
                background:transparent;
                border:none;
                text-align:left;
                padding-left:20px;
                font-size:15px;
                border-radius:8px;
            }

            QPushButton:hover{
                background:#18A8E0;
            }
        """

        active_style = """
            QPushButton{
                color:white;
                background:#18A8E0;
                border:none;
                text-align:left;
                padding-left:20px;
                font-size:15px;
                font-weight:bold;
                border-radius:8px;
            }
        """

        for button in self.menu_buttons:
            button.setStyleSheet(normal_style)

        self.menu_buttons[index].setStyleSheet(active_style)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    try:
        with open("styles/skyverra.qss", "r") as file:
            app.setStyleSheet(file.read())
    except Exception:
        pass

    create_tables()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())