from PyQt6.QtWidgets import QMessageBox

def show_message_box(parent, icon, title, text):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(icon)
    msg_box.setText(text)
    msg_box.setWindowTitle(title)
    # The stylesheet will be loaded from the main application
    # We just need to ensure the message box is a child of a styled widget
    # or has the style applied directly if needed.
    # In this case, the parent will pass on the style.
    msg_box.exec()

def show_question_box(parent, title, text):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Icon.Question)
    msg_box.setText(text)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msg_box.setDefaultButton(QMessageBox.StandardButton.No)
    return msg_box.exec()
