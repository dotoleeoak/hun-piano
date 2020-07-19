import sys
from PySide2.QtCore import QElapsedTimer, QTime, QTimer
from PySide2.QtWidgets import QApplication, QWidget
from UI.InUse import UiInUse
from db import DataBase


class InUse(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiInUse()
        self.ui.setupUi(self)

        self.db = DataBase()
        self.time = QTime(0, 0)
        self.elapsed_timer = QElapsedTimer()
        self.timer = QTimer(self)
        self.info = {}

    def update_time(self):
        self.ui.used_time.setText(
            (self.time.addMSecs(self.elapsed_timer.elapsed())).toString("hh:mm:ss")
        )

    def set_page(self, contact):
        self.info = self.db.get_info(contact)

        self.elapsed_timer.start()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(500)
        self.ui.used_time.setText(self.time.toString("hh:mm:ss"))
        self.ui.username.setText(self.info["name"] + " 님")

    def clear_page(self):
        self.timer.stop()
        self.ui.used_time.setText("00:00:00")
        self.ui.username.setText("???")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    inUse = InUse()
    inUse.show()
    sys.exit(app.exec_())
