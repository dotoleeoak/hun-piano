import sys
from functools import partial
from PySide2.QtCore import QElapsedTimer, QTimer, QTime
from PySide2.QtWidgets import *
from ui_InUse import Ui_InUse
from reader_for_login_test import TestDatabaseReader

class InUse(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        # UI for the page
        self.ui = Ui_InUse()
        self.ui.setupUi(self)

        # reader
        reader = TestDatabaseReader()
        self.userData = reader.getCurrentData()
        self.userTime = QTime.fromString(self.userData["time_used"], "hh:mm:ss")

        # Set timer
        self.elapsedTimer = QElapsedTimer()
        self.timer = QTimer(self)
        self.elapsedTimer.start()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(500)

        # Set Page
        self.ui.UserName.setText(self.userData["name"])


    def updateTime(self):
        
        self.ui.UsedTime.setText(
            (self.userTime.addMSecs(self.elapsedTimer.elapsed())).toString("hh:mm:ss")
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)

    inUse = InUse()

    inUse.show()
    sys.exit(app.exec_())
