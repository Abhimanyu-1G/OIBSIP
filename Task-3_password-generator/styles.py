
NEW_THEME = """
QWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    font-family: 'Poppins', sans-serif;
    font-size: 14px;
}

QMainWindow {
    background-color: #1a1826;
}

QFrame#Card {
    background-color: #1a1826;
    border: 1px solid #302d41;
    border-radius: 15px;
    padding: 15px;
}

QLabel#Title {
    font-size: 36px;
    font-weight: 900;
    color: #cba6f7;
    margin-bottom: 10px;
}

QLineEdit#PasswordDisplay {
    background-color: #302d41;
    border: 2px solid #575268;
    border-radius: 10px;
    color: #abe9b3;
    font-family: 'JetBrains Mono', monospace;
    font-size: 22px;
    padding: 15px;
    font-weight: bold;
}

QPushButton {
    background-color: #cba6f7;
    color: #1e1e2e;
    border: none;
    border-radius: 8px;
    padding: 12px 15px;
    font-weight: bold;
    font-size: 16px;
}

QPushButton:hover {
    background-color: #e8a2f7;
}

QCheckBox {
    spacing: 10px;
    font-size: 14px;
}

QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border-radius: 7px;
    border: 2px solid #575268;
    background-color: #302d41;
}

QCheckBox::indicator:checked {
    background-color: #f5c2e7;
    border-color: #f5c2e7;
}

QSlider::groove:horizontal {
    border: 1px solid #575268;
    height: 8px;
    background: #302d41;
    margin: 2px 0;
    border-radius: 4px;
}

QSlider::handle:horizontal {
    background: #f5c2e7;
    border: 2px solid #f5c2e7;
    width: 20px;
    height: 20px;
    margin: -8px 0;
    border-radius: 10px;
}

QSpinBox, QLineEdit {
    background-color: #302d41;
    border: 1px solid #575268;
    border-radius: 8px;
    padding: 8px;
    font-size: 14px;
}

QTabWidget::pane {
    border: none;
    background-color: #1a1826;
}

QTabBar::tab {
    background: #1a1826;
    border: 1px solid #302d41;
    border-bottom: none;
    padding: 10px 20px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font-size: 16px;
    font-weight: bold;
    color: #b4befe;
}

QTabBar::tab:selected {
    background: #302d41;
    color: #cba6f7;
}

QToolTip {
    background-color: #302d41;
    color: #cdd6f4;
    border: 1px solid #575268;
    padding: 5px;
    border-radius: 5px;
}
"""

def get_strength_color(strength):
    if strength == "Very Weak" or strength == "Weak":
        return "#f38ba8"  # Red
    elif strength == "Okay":
        return "#fab387"  # Orange
    elif strength == "Good":
        return "#a6e3a1"  # Green
    elif strength == "Strong":
        return "#89b4fa"  # Blue
    else:
        return "#45475a"  # Default

