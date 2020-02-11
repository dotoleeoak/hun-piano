import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget
from main_LogIn import LogIn
from main_SignUp import SignUp
from main_InUse import InUse

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Piano Checker")
        self.setFixedSize(800, 480)
        #self.showFullScreen()

        # Create Page Objects Here
        LogInPage = LogIn()
        SignUpPage = SignUp()
        InUsePage = InUse()

        # Connect pages to switch each others
        LogInPage.ui.ButtonRegister.clicked.connect(self.showSignUpPage)
        LogInPage.ui.DButtonYes.clicked.connect(self.showInUsePage)
        SignUpPage.ui.buttonHome.clicked.connect(self.showLogInPage)
        InUsePage.ui.pushButton.clicked.connect(self.showLogInPage)

        # Insert pages into QStackedWidget
        self.centralWidgets = QStackedWidget()
        self.centralWidgets.addWidget(LogInPage)    # index: 0
        self.centralWidgets.addWidget(SignUpPage)   # index: 1
        self.centralWidgets.addWidget(InUsePage)    # index: 2

        self.setCentralWidget(self.centralWidgets)

    def getCurWidget(self):
        return self.centralWidgets.currentWidget()

    def showLogInPage(self):
        print("login")
        self.centralWidgets.setCurrentIndex(0)
        self.getCurWidget().ui.DialogueShadow.hide()
        

    def showSignUpPage(self):
        print("signup")
        self.centralWidgets.setCurrentIndex(1)
        

    def showInUsePage(self):
        print("inuse")
        self.centralWidgets.setCurrentIndex(2)

        

class PianoManager(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self.window = MainWindow()
        self.window.show()
        

if __name__ == '__main__':
    
    app = PianoManager(sys.argv)
    sys.exit(app.exec_())
