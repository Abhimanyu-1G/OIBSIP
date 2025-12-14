from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from bmi_calculator.ui.custom_widgets import show_message_box, show_question_box
from .input_widget import InputWidget
from .history_widget import HistoryWidget
from ..database import DatabaseManager
from ..logic import BMILogic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 800, 800) # Adjusted for vertical layout

        self.db_manager = DatabaseManager()
        
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)

        # Input Widget (Top)
        self.input_widget = InputWidget(self.db_manager)
        self.input_widget.calculate_signal.connect(self.calculate_bmi)
        self.input_widget.user_changed_signal.connect(self.load_history)
        self.input_widget.add_user_signal.connect(self.add_user)
        self.input_widget.remove_user_signal.connect(self.remove_user)
        main_layout.addWidget(self.input_widget, 1) # Stretch factor 1

        # History Widget (Bottom)
        self.history_widget = HistoryWidget()
        self.history_widget.clear_btn.clicked.connect(self.clear_history)
        main_layout.addWidget(self.history_widget, 2) # Stretch factor 2
        
        # Trigger initial load if users exist
        if self.input_widget.user_combo.count() > 0:
            self.input_widget.on_user_changed()

    def add_user(self, name):
        user_id = self.db_manager.add_user(name)
        if user_id:
            show_message_box(self, QMessageBox.Icon.Information, "Success", f"User '{name}' added successfully!")
            self.input_widget.refresh_users()
        else:
            show_message_box(self, QMessageBox.Icon.Warning, "Error", f"User '{name}' already exists!")

    def remove_user(self, user_id):
        user_name = self.input_widget.user_combo.currentText()
        reply = show_question_box(
            self, 'Confirm Delete',
            f"Are you sure you want to delete the user '{user_name}' and all their records?"
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.db_manager.delete_user(user_id)
            self.input_widget.refresh_users()
            self.history_widget.update_data([]) # Clear history view
            show_message_box(self, QMessageBox.Icon.Information, "Success", f"User '{user_name}' deleted successfully.")



    def calculate_bmi(self, weight, height):
        try:
            bmi = BMILogic.calculate_bmi(weight, height)
            category = BMILogic.get_category(bmi)
            
            user_id = self.input_widget.user_combo.currentData()
            if user_id is None:
                show_message_box(self, QMessageBox.Icon.Warning, "Error", "Please select or add a user first.")
                return

            # Save record
            self.db_manager.add_record(user_id, weight, height, bmi)
            
            # Show result
            show_message_box(self, QMessageBox.Icon.Information, "BMI Result", f"Your BMI is {bmi:.2f}\nCategory: {category}")
            
            # Refresh history
            self.load_history(user_id)
            
        except ValueError as e:
            show_message_box(self, QMessageBox.Icon.Warning, "Error", str(e))

    def load_history(self, user_id):
        records = self.db_manager.get_records(user_id)
        self.history_widget.update_data(records)

    def clear_history(self):
        user_id = self.input_widget.user_combo.currentData()
        if user_id is None:
            return

        reply = show_question_box(
            self, 'Confirm Delete',
            "Are you sure you want to clear all history for this user?"
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.db_manager.delete_records(user_id)
            self.load_history(user_id)
            show_message_box(self, QMessageBox.Icon.Information, "Success", "History cleared successfully.")
