import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap
from UI.ui_NewUserCheck import Ui_NewUserCheck
from writer_for_test import TestDatabaseWriter
from reader_for_test import TestDatabaseReader
from NFC.NFCReaderForTest import NFCReader


class NewUserCheck(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # UI for the page
        self.ui = Ui_NewUserCheck()
        self.ui.setupUi(self)

        # database
        self.dbWriter = TestDatabaseWriter()
        self.dbReader = TestDatabaseReader()

        # NFC
        self.nfcReader = NFCReader()

        # pixmap
        self.checked_pix = QPixmap("../Images/checked.png")
        self.unchecked_pix = QPixmap("../Images/unchecked.png")

        self.ui.buttonRegister.clicked.connect(self.register_nfc)

        self.checked = False
        self.ui.buttonTemp.clicked.connect(self.check_temporary)

        self.set_page()

    def check_temporary(self):
        if self.checked:
            self.ui.buttonTemp.setIcon(self.unchecked_pix)
            self.checked = False
        else:
            self.ui.buttonTemp.setIcon(self.checked_pix)
            self.checked = True

    def register_nfc(self):
        self.nfcReader.nfc_connect.connect(self.save_nfc_uid)
        self.nfcReader.start()
        self.ui.DialogueShadow.show()

    @Slot(str)
    def save_nfc_uid(self, uid):
        self.dbWriter.write_temporary_data(uid, "NFC_UID")
        self.ui.DButtonSkip.click()

    def set_page(self):
        self.ui.DialogueShadow.hide()
        current_data = self.dbReader.get_current_data()
        self.ui.labelUserName.setText(current_data["name"])
        self.ui.labelUserContact.setText(current_data["contact"])
        self.ui.labelUserID.setText(current_data["ID"])
        self.checked = current_data["is_temporary"]
        if self.checked:
            self.ui.buttonTemp.setIcon(self.checked_pix)
        else:
            self.ui.buttonTemp.setIcon(self.unchecked_pix)

    def clear_page(self):
        if not self.nfcReader.isFinished():
            print("thread quit")
            self.nfcReader.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    new_user = NewUserCheck()

    new_user.show()
    sys.exit(app.exec_())
