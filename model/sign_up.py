import sys
from functools import partial
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from view.sign_up import *
from model.db import DataBase


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
        page3 = SignUpCheck()

        self.addWidget(page0)  # index: 0
        self.addWidget(page1)  # index: 1
        self.addWidget(page2)  # index: 2
        self.addWidget(page3)  # index: 3

        self.name = "Unknown"
        self.contact = 0
        self.contact1 = "1234"
        self.contact2 = "5678"
        self.id = "2020123456"
        self.db = DataBase()

        f = lambda x: partial(self.switch_page, x)

        page0.ui.button_right.clicked.connect(f(1))
        page0.ui.edit_name.returnPressed.connect(f(1))

        page1.ui.button_left.clicked.connect(f(0))
        page1.ui.button_right.clicked.connect(f(2))
        page1.ui.edit_contact3.returnPressed.connect(f(2))

        page2.ui.button_left.clicked.connect(f(1))
        page2.ui.button_right.clicked.connect(f(3))
        page2.ui.edit_id.returnPressed.connect(f(3))

        page3.ui.button_left.clicked.connect(f(2))
        page3.ui.button_register.clicked.connect(self.sign_up_user)
        page3.ui.dialog_false.button_ok.clicked.connect(page3.ui.dialog_false.hide)

        self.set_page()

    def switch_page(self, idx):
        self.currentWidget().clear_page()

        curr_idx = self.currentIndex()
        if curr_idx == 0:
            self.name = self.currentWidget().ui.edit_name.text()
        elif curr_idx == 1:
            self.contact1 = self.currentWidget().ui.edit_contact2.text()
            self.contact2 = self.currentWidget().ui.edit_contact3.text()
        elif curr_idx == 2:
            self.id = self.currentWidget().ui.edit_id.text()

        self.setCurrentIndex(idx)
        if idx == 3:
            self.currentWidget().set_page(
                self.name, self.contact1, self.contact2, self.id
            )
        else:
            self.currentWidget().set_page()

    def sign_up_user(self):
        self.contact = int(self.contact1) * 10000 + int(self.contact2)
        print(self.contact)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    page = SignUp()
    page.show()
    sys.exit(app.exec_())
