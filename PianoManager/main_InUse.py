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
        self.reader = TestDatabaseReader()
        self.userData = dict()
        self.userTime = QTime(0, 0)

        # Set timer
        self.elapsedTimer = QElapsedTimer()
        self.timer = QTimer(self)

        self.ui.UsedTime.setText("00:00:00")
        self.ui.UserName.setText("")


    def updateTime(self):
        
        self.ui.UsedTime.setText(
            (self.userTime.addMSecs(self.elapsedTimer.elapsed())).toString("hh:mm:ss")
            )

    def setPage(self):
        
        self.elapsedTimer.start()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(500)
        self.userData = self.reader.getCurrentData()
        self.userTime = QTime.fromString(self.userData["time_used"], "hh:mm:ss")
        self.ui.UsedTime.setText(self.userTime.toString("hh:mm:ss"))
        self.ui.UserName.setText(self.userData["name"] + " 님")

    def clearPage(self):

        self.timer.stop()
        self.ui.UsedTime.setText("00:00:00")
        self.ui.UserName.setText("")
        
        """TODO: ADD CODES FOR WRITING CURRENT USERTIME TO DB HERE"""

        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)

    inUse = InUse()

    inUse.show()
    sys.exit(app.exec_())
