import sys
from functools import partial
<<<<<<< HEAD
<<<<<<< HEAD
=======
from PySide2.QtCore import QTime
>>>>>>> LinkingPages
=======
from PySide2.QtCore import QElapsedTimer, QTimer, QTime
>>>>>>> LinkingPages
from PySide2.QtWidgets import *
from ui_InUse import Ui_InUse
from reader_for_login_test import TestDatabaseReader

class InUse(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        # UI for the page
        self.ui = Ui_InUse()
        self.ui.setupUi(self)
<<<<<<< HEAD
<<<<<<< HEAD

            
=======
        
        # Set start_time to current time
        self.start_time = QTime()
        self.start_time.start()
=======
>>>>>>> LinkingPages

        # Set timer
        self.elapsedTimer = QElapsedTimer()
        self.timer = QTimer(self)

        # Set Page
        self.setPage()


    def updateTime(self):

        self.ui.UsedTime.setText(
            (QTime(0, 0).addMSecs(self.elapsedTimer.elapsed())).toString("hh:mm:ss")
            )

    def setPage(self):
        self.elapsedTimer.start()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(500)
        

    def clearPage(self):
        self.

        
>>>>>>> LinkingPages

if __name__ == '__main__':
    app = QApplication(sys.argv)

    inUse = InUse()

    inUse.show()
    sys.exit(app.exec_())
