import sys
from functools import partial
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QWidget
from view import UiLogIn
from model.db import DataBase
from nfc.nfc_reader_for_test import NFCReader  # from nfc.nfc_reader import NFCReader


class LogIn(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiLogIn()
        self.ui.setupUi(self)

        self.nfc_reader = NFCReader()
        self.nfc_reader.start()
        self.nfc_reader.nfc_connect.connect(self.check_valid_uid)

        self.db = DataBase()
        self.idx_display = 0
        self.contact = 0
        self.info = {}

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
                self.info = self.db.get_info(self.contact)
                self.ui.dialog_true_name.setText(self.info["name"] + " 님")
                self.ui.dialog_true.show()
                # TODO: swich to in_use page
            else:
                self.ui.dialog_false.show()
                # TODO: error animation

    @Slot(str)
    def check_valid_uid(self, uid):
        print(uid)
        # TODO: check uid from database

    def get_contact(self):
        return self.contact

    def set_page(self):
        if not self.nfc_reader.isRunning():
            print("Thread start")
            self.nfc_reader.start()
        self.nfc_reader.nfc_connect.connect(self.check_valid_uid)

    def clear_page(self):
        self.contact = 0
        self.idx_display = 0
        self.ui.dialog_true.hide()
        self.ui.dialog_false.hide()
        for label in self.ui.display_number:
            label.setText("")

        if not self.nfc_reader.isFinished():
            self.nfc_reader.quit()

    def __del__(self):
        self.nfc_reader.quit()
        self.nfc_reader.terminate()
        self.nfc_reader.wait()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    log_in = LogIn()
    log_in.show()
    sys.exit(app.exec_())
