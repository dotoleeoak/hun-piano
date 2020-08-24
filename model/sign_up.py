import sys
from functools import partial

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QStackedWidget, QWidget

from model.db import DataBase
from nfc import NFCReader
from view import UiSignUpCheck, UiSignUpContact, UiSignUpID, UiSignUpName, UiSignUpNFC


class SignUpName(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiSignUpName()
        self.ui.setupUi(self)
        self.set_page()

    def set_page(self):
        pass

    def clear_page(self):
        print("name =", self.ui.edit_name.text())


class SignUpContact(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiSignUpContact()
        self.ui.setupUi(self)
        self.set_page()

    def set_page(self):
        pass

    def clear_page(self):
        print("contact2 =", self.ui.edit_contact2.text())
        print("contact3 =", self.ui.edit_contact3.text())


class SignUpID(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiSignUpID()
        self.ui.setupUi(self)
        self.set_page()

    def set_page(self):
        pass

    def clear_page(self):
        print("id =", self.ui.edit_id.text())


class SignUpNFC(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiSignUpNFC()
        self.ui.setupUi(self)

        self.nfc_reader = NFCReader()
        self.nfc_uid = ""

    @Slot(str)
    def get_uid_from_tag(self, uid):
        print(uid)
        self.nfc_uid = uid
        self.check_nfc_tagged()

    def set_page(self):
        self.check_nfc_tagged()
        self.nfc_reader.start()
        self.nfc_reader.nfc_connect.connect(self.get_uid_from_tag)

    def check_nfc_tagged(self):
        if self.nfc_uid == "":
            self.ui.label_nfc_status.setText("Not Tagged Yet")
        else:
            self.ui.label_nfc_status.setText("Tagged!")

    def clear_page(self):
        print("nfc_uid =", self.nfc_uid)
        if not self.nfc_reader.isFinished():
            self.nfc_reader.quit()


class SignUpCheck(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiSignUpCheck()
        self.ui.setupUi(self)
        self.set_page()

    def set_page(self, name="홍길동", contact1="1234", contact2="5678", id="2020123456"):
        self.ui.label_name_user.setText(name)
        self.ui.label_contact_user.setText(f"010-{contact1}-{contact2}")
        self.ui.label_id_user.setText(id)

    def clear_page(self):
        pass


class SignUp(QStackedWidget):
    def __init__(self):
        QStackedWidget.__init__(self)

        self.setFixedSize(800, 480)

        page0 = SignUpName()
        page1 = SignUpContact()
        page2 = SignUpID()
        page3 = SignUpNFC()
        page4 = SignUpCheck()

        self.addWidget(page0)  # index: 0
        self.addWidget(page1)  # index: 1
        self.addWidget(page2)  # index: 2
        self.addWidget(page3)  # index: 3
        self.addWidget(page4)  # index: 4

        self.name = "Unknown"
        self.contact = 0
        self.contact1 = "1234"
        self.contact2 = "5678"
        self.id = "2020123456"
        self.nfc_uid = ""
        self.db = DataBase()

        page0.ui.button_right.clicked.connect(self.save_name)
        page0.ui.button_right.clicked.connect(partial(self.switch_page, 1))
        page0.ui.edit_name.returnPressed.connect(self.save_name)
        page0.ui.edit_name.returnPressed.connect(partial(self.switch_page, 1))

        page1.ui.button_left.clicked.connect(partial(self.switch_page, 0))
        page1.ui.button_right.clicked.connect(self.save_contact)
        page1.ui.button_right.clicked.connect(partial(self.switch_page, 2))
        page1.ui.edit_contact3.returnPressed.connect(self.save_contact)
        page1.ui.edit_contact3.returnPressed.connect(partial(self.switch_page, 2))

        page2.ui.button_left.clicked.connect(partial(self.switch_page, 1))
        page2.ui.button_right.clicked.connect(self.save_id)
        page2.ui.button_right.clicked.connect(partial(self.switch_page, 3))
        page2.ui.edit_id.returnPressed.connect(self.save_id)
        page2.ui.edit_id.returnPressed.connect(partial(self.switch_page, 3))

        page3.ui.button_left.clicked.connect(partial(self.switch_page, 2))
        page3.ui.button_right.clicked.connect(self.save_nfc_uid)
        page3.ui.button_right.clicked.connect(partial(self.switch_page, 4))

        page4.ui.button_left.clicked.connect(partial(self.switch_page, 3))
        page4.ui.button_register.clicked.connect(self.sign_up_user)
        page4.ui.dialog_false.button_ok.clicked.connect(page4.ui.dialog_false.hide)

        self.set_page()

    def save_name(self):
        self.name = self.widget(0).ui.edit_name.text()

    def save_contact(self):
        self.contact1 = self.widget(1).ui.edit_contact2.text()
        self.contact2 = self.widget(1).ui.edit_contact3.text()

    def save_id(self):
        self.id = self.widget(2).ui.edit_id.text()

    def save_nfc_uid(self):
        self.nfc_uid = self.widget(3).nfc_uid

    def switch_page(self, idx):
        self.currentWidget().clear_page()
        self.setCurrentIndex(idx)
        if idx == 4:
            self.currentWidget().set_page(
                self.name, self.contact1, self.contact2, self.id
            )
        else:
            self.currentWidget().set_page()

    def sign_up_user(self):
        self.contact = int(self.contact1) * 10000 + int(self.contact2)
        print(self.contact)
        # TODO: Add an user to DB with nfc uid
        if self.db.add_user(self.name, self.id, self.contact):
            self.currentWidget().ui.dialog_true_name.setText(self.name + " 님")
            self.currentWidget().ui.dialog_true.show()
        else:
            self.currentWidget().ui.dialog_false.show()

    def set_page(self):
        self.setCurrentIndex(0)
        self.currentWidget().set_page()

    def clear_page(self):
        self.widget(0).ui.edit_name.setText("")
        self.widget(1).ui.edit_contact1.setText("")
        self.widget(1).ui.edit_contact2.setText("")
        self.widget(1).ui.edit_contact3.setText("")
        self.widget(2).ui.edit_id.setText("")
        self.widget(3).nfc_uid = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    page = SignUp()
    page.show()
    sys.exit(app.exec_())
