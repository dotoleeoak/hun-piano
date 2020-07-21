import sys
from PySide2.QtWidgets import *
from UI.ui_SignUp import Ui_SignUp


class SignUp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_SignUp()
        self.ui.setupUi(self)

    def set_page(self):
        pass

    def clear_page(self):
        self.ui.editName.clear()
        self.ui.editID.clear()
        self.ui.editContact1.clear()
        self.ui.editContact2.clear()
        self.ui.editContact3.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = SignUp()
    view.show()
    sys.exit(app.exec_())
