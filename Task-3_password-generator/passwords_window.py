import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QTableWidget, QTableWidgetItem, 
    QLineEdit, QHeaderView, QMessageBox
)
from PyQt6.QtCore import Qt
from styles import NEW_THEME as THEME

class PasswordsWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Saved Passwords")
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet(THEME)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search...")
        self.search_input.textChanged.connect(self.filter_passwords)
        search_layout.addWidget(self.search_input)
        layout.addLayout(search_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Site/Service", "Username", "Password"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        layout.addWidget(self.table)

        delete_btn = QPushButton("Delete Selected")
        delete_btn.clicked.connect(self.delete_password)
        layout.addWidget(delete_btn)

        self.load_passwords()

    def load_passwords(self):
        self.table.setRowCount(0)
        passwords = self.db.get_all_passwords()
        for site, data in passwords.items():
            self.add_row(site, data.get("username", ""), data["password"])

    def add_row(self, site, username, password):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(site))
        self.table.setItem(row_position, 1, QTableWidgetItem(username))
        self.table.setItem(row_position, 2, QTableWidgetItem(password))

    def filter_passwords(self):
        search_text = self.search_input.text().lower()
        for i in range(self.table.rowCount()):
            site_item = self.table.item(i, 0)
            username_item = self.table.item(i, 1)
            if site_item and username_item:
                site_match = search_text in site_item.text().lower()
                username_match = search_text in username_item.text().lower()
                self.table.setRowHidden(i, not (site_match or username_match))

    def delete_password(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            return

        reply = QMessageBox.question(self, 'Delete Password', 
                                     "Are you sure you want to delete the selected password(s)?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            for row in sorted([r.row() for r in selected_rows], reverse=True):
                site = self.table.item(row, 0).text()
                self.db.delete_password(site)
                self.table.removeRow(row)
