import sys
from PySide2.QtWidgets import *
from ui_SignUp import Ui_SignUp

class SignUp(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_SignUp()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = SignUp()
    view.show()
    sys.exit(app.exec_())