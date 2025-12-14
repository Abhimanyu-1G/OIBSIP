
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QCheckBox, QSlider, QSpinBox, QFrame, QApplication, QLineEdit,
    QDialog, QFormLayout, QDialogButtonBox, QTabWidget, QGridLayout,
    QToolTip
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
import pyperclip
from generator import PasswordGenerator
from styles import NEW_THEME, get_strength_color
from database import PasswordDatabase
from passwords_window import PasswordsWindow

class ModernPasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.generator = PasswordGenerator()
        self.db = PasswordDatabase()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Super Pass")
        self.setGeometry(100, 100, 600, 700)
        self.setStyleSheet(NEW_THEME)
        self.setWindowIcon(QIcon("icon.png"))

        # Fun title
        title_label = QLabel("Super Pass")
        title_label.setObjectName("Title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(title_label)
        main_layout.addSpacing(20)

        # Tabs for generator and saved passwords
        tabs = QTabWidget()
        tabs.addTab(self.create_generator_tab(), "Password Generator")
        tabs.addTab(self.create_passwords_tab(), "Saved Passwords")
        main_layout.addWidget(tabs)

        # Fun footer
        footer_label = QLabel("Have a super day!")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_label.setStyleSheet("font-size: 12px; color: #fab387;")
        main_layout.addWidget(footer_label)

    def create_generator_tab(self):
        generator_widget = QWidget()
        layout = QVBoxLayout(generator_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Password display
        self.password_display = QLineEdit("Click Generate")
        self.password_display.setObjectName("PasswordDisplay")
        self.password_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_display.setReadOnly(True)
        layout.addWidget(self.password_display)
        QToolTip.setFont(QFont("Segoe UI", 10))
        self.password_display.setToolTip("Your generated password will appear here.")

        # Strength indicator
        self.strength_bar = QFrame()
        self.strength_bar.setFixedHeight(10)
        self.strength_bar.setStyleSheet("background-color: #45475a; border-radius: 5px;")
        layout.addWidget(self.strength_bar)

        # Controls in a grid layout
        controls_frame = QFrame()
        controls_frame.setObjectName("Card")
        controls_layout = QGridLayout(controls_frame)
        controls_layout.setSpacing(15)
        layout.addWidget(controls_frame)

        # Length control
        length_label = QLabel("Password Length:")
        self.length_slider = QSlider(Qt.Orientation.Horizontal)
        self.length_slider.setRange(4, 64)
        self.length_slider.setValue(16)
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(4, 64)
        self.length_spinbox.setValue(16)
        self.length_slider.valueChanged.connect(self.length_spinbox.setValue)
        self.length_spinbox.valueChanged.connect(self.length_slider.setValue)
        controls_layout.addWidget(length_label, 0, 0)
        controls_layout.addWidget(self.length_slider, 0, 1)
        controls_layout.addWidget(self.length_spinbox, 0, 2)
        self.length_slider.setToolTip("Drag to set the password length.")

        # Character type checkboxes
        self.check_upper = QCheckBox("Uppercase (A-Z)")
        self.check_upper.setChecked(True)
        self.check_lower = QCheckBox("Lowercase (a-z)")
        self.check_lower.setChecked(True)
        self.check_digits = QCheckBox("Numbers (0-9)")
        self.check_digits.setChecked(True)
        self.check_symbols = QCheckBox("Symbols (#$&)")
        self.check_symbols.setChecked(True)
        self.check_memorable = QCheckBox("Memorable (words)")
        self.check_upper.setToolTip("Include uppercase letters.")
        self.check_lower.setToolTip("Include lowercase letters.")
        self.check_digits.setToolTip("Include numbers.")
        self.check_symbols.setToolTip("Include symbols.")
        self.check_memorable.setToolTip("Generate a password made of words.")
        
        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(self.check_upper)
        checkbox_layout.addWidget(self.check_lower)
        checkbox_layout.addWidget(self.check_digits)
        checkbox_layout.addWidget(self.check_symbols)
        checkbox_layout.addWidget(self.check_memorable)
        controls_layout.addLayout(checkbox_layout, 1, 0, 1, 3)

        # Action buttons
        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self.generate_password)
        self.copy_btn = QPushButton("Copy")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save_password)
        self.generate_btn.setToolTip("Generate a new password.")
        self.copy_btn.setToolTip("Copy the password to your clipboard.")
        self.save_btn.setToolTip("Save the password for later.")
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.generate_btn)
        button_layout.addWidget(self.copy_btn)
        button_layout.addWidget(self.save_btn)
        layout.addLayout(button_layout)
        
        # Initial password generation
        self.generate_password()
        
        return generator_widget

    def create_passwords_tab(self):
        passwords_widget = QWidget()
        layout = QVBoxLayout(passwords_widget)
        
        self.passwords_window = PasswordsWindow(self.db)
        layout.addWidget(self.passwords_window)
        
        return passwords_widget

    def generate_password(self):
        length = self.length_spinbox.value()
        use_upper = self.check_upper.isChecked()
        use_lower = self.check_lower.isChecked()
        use_digits = self.check_digits.isChecked()
        use_symbols = self.check_symbols.isChecked()
        is_memorable = self.check_memorable.isChecked()

        if is_memorable:
            password = self.generator.generate_memorable(num_words=4)
        else:
            password = self.generator.generate(length, use_upper, use_lower, use_digits, use_symbols)
        
        self.password_display.setText(password)

        if "Error" not in password:
            strength, _ = self.generator.check_strength(password)
            self.update_strength_bar(strength)
        else:
            self.update_strength_bar("Error")

    def update_strength_bar(self, strength):
        color = get_strength_color(strength)
        self.strength_bar.setStyleSheet(f"background-color: {color}; border-radius: 5px;")

    def copy_to_clipboard(self):
        password = self.password_display.text()
        if "Error" not in password:
            pyperclip.copy(password)
            self.copy_btn.setText("Copied!")
            QApplication.processEvents()
            from PyQt6.QtCore import QTimer
            QTimer.singleShot(2000, lambda: self.copy_btn.setText("Copy"))

    def save_password(self):
        password = self.password_display.text()
        if "Error" in password:
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Save Password")
        dialog.setStyleSheet(NEW_THEME)
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

def main():
    app = QApplication(sys.argv)
    window = ModernPasswordGeneratorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
