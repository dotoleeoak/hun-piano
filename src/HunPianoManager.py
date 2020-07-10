import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from functools import partial
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PianoManager.main_LogIn import LogIn
from PianoManager.main_InUse import InUse
from PianoManager.main_NewUser import NewUser


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Piano Manager")
        self.setFixedSize(800, 480)
        # self.showFullScreen()

        # # Create Page Objects Here
        log_in_page = LogIn()
        in_use_page = InUse()
        new_user_page = NewUser()

        # # Connect pages to switch each others
        # Log In
        log_in_page.ui.ButtonRegister.clicked.connect(partial(self.switch_page, 2))
        log_in_page.ui.DButtonYes.clicked.connect(partial(self.switch_page, 1))
        # In Use
        in_use_page.ui.ButtonQuit.clicked.connect(partial(self.switch_page, 0))
        # New User 1
        new_user_page.widget(0).ui.buttonHome.clicked.connect(partial(self.switch_page, 0))
        # New User 2
        new_user_page.widget(1).ui.buttonHome.clicked.connect(partial(self.switch_page, 0))
        # New User 3
        new_user_page.widget(2).ui.buttonHome.clicked.connect(partial(self.switch_page, 0))
        # New User Check
        new_user_page.widget(3).ui.buttonHome.clicked.connect(partial(self.switch_page, 0))
        new_user_page.widget(3).ui.DButtonSkip.clicked.connect(partial(self.switch_page, 1))

        # # Insert pages into QStackedWidget
        self.centralWidgets = QStackedWidget()
        self.centralWidgets.addWidget(log_in_page)  # index: 0
        self.centralWidgets.addWidget(in_use_page)  # index: 1
        self.centralWidgets.addWidget(new_user_page)  # index: 2

        self.setCentralWidget(self.centralWidgets)

    def current_widget(self):
        return self.centralWidgets.currentWidget()

    def switch_page(self, idx):
        self.current_widget().clear_page()
        self.centralWidgets.setCurrentIndex(idx)
        self.current_widget().set_page()


class PianoManager(QApplication):

    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self.window = MainWindow()
        self.window.show()


if __name__ == '__main__':
    # os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

    app = PianoManager(sys.argv)
    sys.exit(app.exec_())
