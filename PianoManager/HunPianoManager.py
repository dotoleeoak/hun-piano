import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget
from main_LogIn import LogIn
from main_SignUp import SignUp

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Piano Checker")
        self.setFixedSize(800, 480)
        self.showFullScreen()

        # Create Page Objects Here
        LogInPage = LogIn()
        SignUpPage = SignUp()

        # Connect pages to switch each others
        LogInPage.ui.ButtonRegister.clicked.connect(self.showSignUpPage)
        SignUpPage.ui.buttonHome.clicked.connect(self.showLogInPage)

        # Insert pages into QStackedWidget
        self.centralWidgets = QStackedWidget()
        self.centralWidgets.addWidget(LogInPage)    # index: 0
        self.centralWidgets.addWidget(SignUpPage)   # index: 1

        self.setCentralWidget(self.centralWidgets)

    def showSignUpPage(self):
        print("signup")
        self.centralWidgets.setCurrentIndex(1)

    def showLogInPage(self):
        print("login")
        self.centralWidgets.setCurrentIndex(0)
        

class PianoChecker(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self.window = MainWindow()
        self.window.show()
        

if __name__ == '__main__':
    
    app = PianoChecker(sys.argv)
    sys.exit(app.exec_())
