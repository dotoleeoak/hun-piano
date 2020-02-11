import sys
from functools import partial
from PySide2.QtWidgets import *
from ui_InUse import Ui_InUse
from reader_for_login_test import TestDatabaseReader

class InUse(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        # UI for the page
        self.ui = Ui_InUse()
        self.ui.setupUi(self)

            

if __name__ == '__main__':
    app = QApplication(sys.argv)

    inUse = InUse()

    inUse.show()
    sys.exit(app.exec_())
