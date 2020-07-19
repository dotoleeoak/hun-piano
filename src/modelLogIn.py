import sys
from functools import partial
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from UI.LogIn import UiLogIn
from db import DataBase
from Animation import Animation


class LogIn(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiLogIn()
        self.ui.setupUi(self)

        self.db = DataBase()
        self.idx_display = 0
        self.contact = 0
        self.name = ""

        for val, button in enumerate(self.ui.button_keypad):
            button.clicked.connect(partial(self.display_number, val))

        self.ui.dialog_true.button_no.clicked.connect(self.ui.dialog_true.hide)
        self.ui.dialog_true.button_no.clicked.connect(self.clear_page)
        self.ui.dialog_false.button_ok.clicked.connect(self.ui.dialog_false.hide)
        self.ui.dialog_false.button_ok.clicked.connect(self.clear_page)

        self.ui.button_NFC.clicked.connect(self.ui.dialog_nfc.show)
        self.ui.dialog_nfc.button_ok.clicked.connect(self.ui.dialog_nfc.hide)

    def display_number(self, num):
        self.ui.display_number[self.idx_display].setText(str(num))
        self.contact = self.contact * 10 + num
        self.idx_display += 1

        if self.idx_display == 8:
            print(f"contact = {self.contact:08d}")
            if self.db.check_user(self.contact):
                self.name = self.db.get_name(self.contact)
                self.ui.dialog_true_name.setText(self.name + " 님")
                self.ui.dialog_true.show()
                # TODO: swich to in_use page
            else:
                self.ui.dialog_false.show()
                # TODO: error animation

    def set_page(self):
        pass

    def clear_page(self):
        self.contact = 0
        self.idx_display = 0
        self.ui.dialog_true.hide()
        self.ui.dialog_false.hide()
        for label in self.ui.display_number:
            label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    log_in = LogIn()
    log_in.show()
    sys.exit(app.exec_())
