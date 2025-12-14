DARK_THEME = """
QWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    font-family: 'Segoe UI', sans-serif;
    font-size: 14px;
}

QFrame#Card {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 15px;
}

QLabel#Title {
    font-size: 24px;
    font-weight: bold;
    color: #89b4fa;
    margin-bottom: 10px;
}

QLabel#PasswordDisplay {
    background-color: #181825;
    border: 1px solid #45475a;
    border-radius: 10px;
    color: #a6e3a1;
    font-family: 'Consolas', monospace;
    font-size: 18px;
    padding: 10px;
}

QPushButton {
    background-color: #89b4fa;
    color: #1e1e2e;
    border: none;
    border-radius: 8px;
    padding: 12px 15px;
    font-weight: bold;
    font-size: 15px;
}

QPushButton:hover {
    background-color: #b4befe;
}

QCheckBox {
    spacing: 10px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border-radius: 5px;
    border: 1px solid #45475a;
    background-color: #181825;
}

QCheckBox::indicator:checked {
    background-color: #89b4fa;
    border-color: #89b4fa;
}

QSlider::groove:horizontal {
    border: 1px solid #45475a;
    height: 6px;
    background: #181825;
    margin: 2px 0;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #89b4fa;
    border: 1px solid #89b4fa;
    width: 18px;
    height: 18px;
    margin: -7px 0;
    border-radius: 9px;
}

QSpinBox, QLineEdit {
    background-color: #181825;
    border: 1px solid #45475a;
    border-radius: 8px;
    padding: 8px;
}

QTableWidget {
    background-color: #181825;
    border: 1px solid #45475a;
    border-radius: 8px;
    gridline-color: #45475a;
}

QHeaderView::section {
    background-color: #313244;
    border: 1px solid #45475a;
    padding: 5px;
}
"""

