from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QGroupBox,
    QFormLayout,
    QComboBox
)


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Settings")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#0D5A9C;
        """)

        layout.addWidget(title)

        theme_group = QGroupBox("Application Settings")

        form = QFormLayout()

        self.theme = QComboBox()
        self.theme.addItems([
            "skyverra Light",
            "skyverra Dark"
        ])

        form.addRow("Theme:", self.theme)

        theme_group.setLayout(form)

        layout.addWidget(theme_group)

        backup_btn = QPushButton("Backup Data")
        restore_btn = QPushButton("Restore Data")

        layout.addWidget(backup_btn)
        layout.addWidget(restore_btn)