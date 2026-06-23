from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QMessageBox
)

from backend.database.company_db import (
    save_company,
    get_company
)


class CompanyProfilePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)


        # ==========================
        # TITLE
        # ==========================

        title = QLabel("Company Profile")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#0D5A9C;
        """)

        layout.addWidget(title)



        # ==========================
        # INPUTS
        # ==========================

        self.company_name = QLineEdit()
        self.company_name.setPlaceholderText(
            "Company Name"
        )


        self.gstin = QLineEdit()
        self.gstin.setPlaceholderText(
            "GSTIN Number"
        )


        self.email = QLineEdit()
        self.email.setPlaceholderText(
            "Company Email"
        )


        self.phone = QLineEdit()
        self.phone.setPlaceholderText(
            "Company Phone"
        )


        self.address = QTextEdit()
        self.address.setPlaceholderText(
            "Company Address"
        )


        self.logo_path = QLineEdit()

        self.logo_path.setPlaceholderText(
            "Logo Path"
        )



        # ==========================
        # LOGO BUTTON
        # ==========================

        logo_btn = QPushButton(
            "Upload Company Logo"
        )

        logo_btn.clicked.connect(
            self.upload_logo
        )



        # ==========================
        # SAVE BUTTON
        # ==========================

        save_btn = QPushButton(
            "Save Company Profile"
        )


        save_btn.clicked.connect(
            self.save_profile
        )



        layout.addWidget(self.company_name)
        layout.addWidget(self.gstin)
        layout.addWidget(self.email)
        layout.addWidget(self.phone)
        layout.addWidget(self.address)
        layout.addWidget(self.logo_path)
        layout.addWidget(logo_btn)
        layout.addWidget(save_btn)



        # Load Existing Data

        self.load_profile()



    # ==========================
    # UPLOAD LOGO
    # ==========================

    def upload_logo(self):

        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select Logo",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )


        if file:

            self.logo_path.setText(
                file
            )



    # ==========================
    # SAVE PROFILE
    # ==========================

    def save_profile(self):

        name = self.company_name.text()
        gst = self.gstin.text()
        email = self.email.text()
        phone = self.phone.text()
        address = self.address.toPlainText()


        if not name:

            QMessageBox.warning(
                self,
                "Error",
                "Company name required"
            )

            return



        save_company(
            name,
            gst,
            email,
            phone,
            address
        )


        QMessageBox.information(
            self,
            "Saved",
            "Company Profile Saved"
        )



    # ==========================
    # LOAD PROFILE
    # ==========================

    def load_profile(self):

        data = get_company()


        if data:


            self.company_name.setText(
                str(data[1])
            )


            self.gstin.setText(
                str(data[2])
            )


            self.email.setText(
                str(data[3])
            )


            self.phone.setText(
                str(data[4])
            )


            self.address.setText(
                str(data[5])
            )