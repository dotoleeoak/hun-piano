import sys
from functools import partial
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget
from main_LogIn import LogIn
from main_SignUp import SignUp
from main_InUse import InUse


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Piano Manager")
        self.setFixedSize(800, 480)
        # self.showFullScreen()

        # Create Page Objects Here
        LogInPage = LogIn()
        SignUpPage = SignUp()
        InUsePage = InUse()

        # Connect pages to switch each others
        LogInPage.ui.ButtonRegister.clicked.connect(partial(self.switchPage, 1))
        LogInPage.ui.DButtonYes.clicked.connect(partial(self.switchPage, 2))
        SignUpPage.ui.buttonHome.clicked.connect(partial(self.switchPage, 0))
        InUsePage.ui.ButtonQuit.clicked.connect(partial(self.switchPage, 0))

        # Insert pages into QStackedWidget
        self.centralWidgets = QStackedWidget()
        self.centralWidgets.addWidget(LogInPage)  # index: 0
        self.centralWidgets.addWidget(SignUpPage)  # index: 1
        self.centralWidgets.addWidget(InUsePage)  # index: 2

        self.setCentralWidget(self.centralWidgets)

    def getCurWidget(self):
        return self.centralWidgets.currentWidget()

    def switchPage(self, idx):
        self.getCurWidget().clearPage()
        self.centralWidgets.setCurrentIndex(idx)
        self.getCurWidget().setPage()


class PianoManager(QApplication):

    def __init__(self, argv):
        
        QApplication.__init__(self, argv)

        self.window = MainWindow()
        self.window.show()


if __name__ == '__main__':

    # import os
    # os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

    app = PianoManager(sys.argv)
    sys.exit(app.exec_())
