import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QCheckBox, QSlider, QSpinBox, 
    QFrame, QApplication, QLineEdit, QDialog, QFormLayout, 
    QDialogButtonBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import pyperclip
from generator import PasswordGenerator
from styles import DARK_THEME
from database import PasswordDatabase
from passwords_window import PasswordsWindow

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.generator = PasswordGenerator()
        self.db = PasswordDatabase()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 500, 600)
        self.setStyleSheet(DARK_THEME)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card = QFrame()
        card.setObjectName("Card")
        card.setFixedWidth(450)
        main_layout.addWidget(card)

        layout = QVBoxLayout(card)
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        title_label = QLabel("Password Generator")
        title_label.setObjectName("Title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        self.password_display = QLabel("Click Generate")
        self.password_display.setObjectName("PasswordDisplay")
        self.password_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_display.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        layout.addWidget(self.password_display)

        self.strength_label = QLabel("Strength: N/A")
        self.strength_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.strength_label)

        controls_layout = QVBoxLayout()
        controls_layout.setSpacing(10)
        layout.addLayout(controls_layout)

        length_layout = QHBoxLayout()
        length_label = QLabel("Length:")
        self.length_slider = QSlider(Qt.Orientation.Horizontal)
        self.length_slider.setRange(4, 64)
        self.length_slider.setValue(12)
        
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(4, 64)
        self.length_spinbox.setValue(12)

        self.length_slider.valueChanged.connect(self.length_spinbox.setValue)
        self.length_spinbox.valueChanged.connect(self.length_slider.setValue)

        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_slider)
        length_layout.addWidget(self.length_spinbox)
        controls_layout.addLayout(length_layout)

        options_layout = QHBoxLayout()
        options_layout.setSpacing(10)
        self.check_upper = QCheckBox("Uppercase (A-Z)")
        self.check_upper.setChecked(True)
        self.check_lower = QCheckBox("Lowercase (a-z)")
        self.check_lower.setChecked(True)
        self.check_digits = QCheckBox("Numbers (0-9)")
        self.check_digits.setChecked(True)
        self.check_symbols = QCheckBox("Symbols (#$&)")
        self.check_symbols.setChecked(True)
        options_layout.addWidget(self.check_upper)
        options_layout.addWidget(self.check_lower)
        options_layout.addWidget(self.check_digits)
        options_layout.addWidget(self.check_symbols)
        controls_layout.addLayout(options_layout)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)
        
        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self.generate_password)
        
        self.copy_btn = QPushButton("Copy")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save_password)

        self.view_passwords_btn = QPushButton("View Saved Passwords")
        self.view_passwords_btn.clicked.connect(self.view_passwords)

        buttons_layout.addWidget(self.generate_btn)
        buttons_layout.addWidget(self.copy_btn)
        buttons_layout.addWidget(self.save_btn)
        buttons_layout.addWidget(self.view_passwords_btn)
        layout.addLayout(buttons_layout)
        
        self.generate_password()

    def generate_password(self):
        length = self.length_spinbox.value()
        use_upper = self.check_upper.isChecked()
        use_lower = self.check_lower.isChecked()
        use_digits = self.check_digits.isChecked()
        use_symbols = self.check_symbols.isChecked()

        password = self.generator.generate(length, use_upper, use_lower, use_digits, use_symbols)
        self.password_display.setText(password)

        if "Error" not in password:
            strength, color = self.generator.check_strength(password)
            self.strength_label.setText(f"Strength: {strength}")
            self.strength_label.setStyleSheet(f"color: {color}; font-weight: bold;")
        else:
            self.strength_label.setText("Error")
            self.strength_label.setStyleSheet("color: #ff4d4d; font-weight: bold;")

    def copy_to_clipboard(self):
        password = self.password_display.text()
        if "Error" not in password:
            pyperclip.copy(password)
            self.copy_btn.setText("Copied!")
            from PyQt6.QtCore import QTimer
            QTimer.singleShot(2000, lambda: self.copy_btn.setText("Copy"))

    def save_password(self):
        password = self.password_display.text()
        if "Error" in password:
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Save Password")
        layout = QFormLayout(dialog)

        site_input = QLineEdit()
        layout.addRow("Site/Service:", site_input)
        username_input = QLineEdit()
        layout.addRow("Username:", username_input)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        if dialog.exec():
            site = site_input.text()
            username = username_input.text()
            if site:
                self.db.add_password(site, password, username)

    def view_passwords(self):
        self.passwords_window = PasswordsWindow(self.db)
        self.passwords_window.show()

