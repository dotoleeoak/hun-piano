import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from UI.InUse import UiInUse


class InUse(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiInUse()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    inUse = InUse()
    inUse.show()
    sys.exit(app.exec_())
