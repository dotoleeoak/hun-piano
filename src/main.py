import sys
from enum import Enum
from functools import partial
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget
from modelLogIn import LogIn
from modelInUse import InUse
from modelSignUp import SignUp


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("음취헌 Piano Manager")
        self.setFixedSize(800, 480)

        page_in_use = InUse()
        page_log_in = LogIn()
        page_sign_up = SignUp()

        self.widget = QStackedWidget()
        self.widget.addWidget(page_log_in)  # index 0
        self.widget.addWidget(page_in_use)  # index 1
        self.widget.addWidget(page_sign_up)  # index 2
        self.setCentralWidget(self.widget)

        self.idx = {"log_in": 0, "in_use": 1, "sign_up": 2}
        f = lambda x: partial(self.switch_page, x)

        page_in_use.ui.button_quit.clicked.connect(f(self.idx["log_in"]))

        page_log_in.ui.button_register.clicked.connect(f(self.idx["sign_up"]))
        page_log_in.ui.dialog_true.button_yes.clicked.connect(f(self.idx["in_use"]))
        # page_log_in.ui.DButtonYes.clicked.connect(f(self.idx["in_use"]))

        for i in range(4):
            page_sign_up.widget(i).ui.button_home.clicked.connect(f(self.idx["log_in"]))

    def switch_page(self, idx):
        if idx == self.idx["in_use"]:
            self.widget.widget(self.idx["in_use"]).set_page(
                self.widget.widget(self.idx["log_in"]).get_contact()
            )
            self.widget.currentWidget().clear_page()
            self.widget.setCurrentIndex(idx)
        else:
            self.widget.currentWidget().clear_page()
            self.widget.setCurrentIndex(idx)
            self.widget.currentWidget().set_page()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
