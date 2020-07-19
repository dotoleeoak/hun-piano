import sys
from functools import partial
from PySide2.QtWidgets import QApplication, QWidget, QStackedWidget
from main_NewUser1 import NewUser1
from main_NewUser2 import NewUser2
from main_NewUser3 import NewUser3
from main_NewUserCheck import NewUserCheck
from writer_for_test import TestDatabaseWriter
from reader_for_test import TestDatabaseReader


class NewUser(QStackedWidget):
    def __init__(self):
        QStackedWidget.__init__(self)

        # # Create Page Objects Here
        new_user_1_page = NewUser1()
        new_user_2_page = NewUser2()
        new_user_3_page = NewUser3()
        new_user_check_page = NewUserCheck()

        # # Writer
        self.dbWriter = TestDatabaseWriter()
        self.dbReader = TestDatabaseReader()
        self.empty_data = {
            "ID": "",
            "name": "",
            "contact": "010--",
            "time_used": "00:00:00",
            "NFC_UID": "",
            "is_temporary": False,
        }

        # # Connect pages to switch each others
        # New User 1
        new_user_1_page.ui.buttonRight.clicked.connect(partial(self.switch_page, 1))
        new_user_1_page.ui.editName.returnPressed.connect(partial(self.switch_page, 1))
        # New User 2
        new_user_2_page.ui.buttonLeft.clicked.connect(partial(self.switch_page, 0))
        new_user_2_page.ui.buttonRight.clicked.connect(partial(self.switch_page, 2))
        new_user_2_page.ui.editContact3.returnPressed.connect(
            partial(self.switch_page, 2)
        )
        # New User 3
        new_user_3_page.ui.buttonLeft.clicked.connect(partial(self.switch_page, 1))
        new_user_3_page.ui.buttonRight.clicked.connect(partial(self.switch_page, 3))
        new_user_3_page.ui.editID.returnPressed.connect(partial(self.switch_page, 3))
        # New User Check
        new_user_check_page.ui.buttonLeft.clicked.connect(partial(self.switch_page, 2))
        new_user_check_page.ui.buttonReturn.clicked.connect(
            partial(self.switch_page, 0)
        )

        # # Insert pages into QStackedWidget
        self.addWidget(new_user_1_page)  # index: 0
        self.addWidget(new_user_2_page)  # index: 1
        self.addWidget(new_user_3_page)  # index: 2
        self.addWidget(new_user_check_page)  # index: 3

    def switch_page(self, idx):
        error = self.currentWidget().clear_page()
        if not error:
            self.setCurrentIndex(idx)
            self.currentWidget().set_page()

    def clear_page(self):
        for i in range(0, 4):
            self.widget(i).clear_page()

    def set_page(self):
        self.dbWriter.write_temporary_data(self.empty_data)
        self.setCurrentIndex(0)
        self.currentWidget().set_page()


if __name__ == "__main__":
    # import os
    # os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

    app = NewUser(sys.argv)
    sys.exit(app.exec_())
