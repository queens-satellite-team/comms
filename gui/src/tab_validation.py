from PyQt5 import QtCore, QtGui, QtWidgets
import qt_widgets as qt
import style_sheets as style
import ui_backend
import os

#Password for tab switch:
ACCEPTED_PASSWORD = 'QSETadmin'

class PasswordDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Tab Switch")
        layout = QtWidgets.QVBoxLayout()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'images/lock.png'))

        # Create widgets
        self.password_label = QtWidgets.QLabel("Password:")
        self.password_edit = QtWidgets.QLineEdit()
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.setDefault(True)
        self.cancel_button = QtWidgets.QPushButton("Cancel")

        # Create layout and add widgets
        self.button_layout = QtWidgets.QHBoxLayout()  # Create horizontal layout for buttons
        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.cancel_button)

        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addLayout(self.button_layout)
        self.setLayout(layout)
        self.setFixedSize(250,100)

        # Connect signals to slots
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        #style window
        self.setStyleSheet(style.TAB_SWITCH_WINDOW)
        self.password_label.setStyleSheet(style.CALL_LABEL)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_edit.setStyleSheet(style.CALL_INPUT)
        self.ok_button.setStyleSheet(style.PASS_SUBMIT)
        self.cancel_button.setStyleSheet(style.PASS_SUBMIT)

    def accept(self):
        #SET ACCEPTED PASSWORD FOR TAB SWITCH HERE
        if self.password_edit.text() == ACCEPTED_PASSWORD:
            super().accept()
        else:
            message_box = QtWidgets.QMessageBox(self)
            message_box.setWindowTitle("Invalid Password")
            message_box.setText("The password you entered is incorrect.")
            message_box.setIcon(QtWidgets.QMessageBox.Critical)
            message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message_box.exec_()

    def reject(self):
        # Overridden reject() function to clear password field on cancel
        self.password_edit.setText("")
        super().reject()

    def close_event(self, event : QtGui.QCloseEvent) -> None:
        event.accept()
        self.close()