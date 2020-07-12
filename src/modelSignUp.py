import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from UI.SignUp import *


class SignUpName(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiSignUpName()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sign_up_name = SignUpName()
    sign_up_name.show()
    sys.exit(app.exec_())
