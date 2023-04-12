import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QPushButton)
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = CustomDialog()
        # dlg.setWindowTitle("HELLO!")
        dlg.exec_()

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HELLO!")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
