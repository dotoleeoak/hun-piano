import sys
from functools import partial
from PySide2.QtCore import QPropertyAnimation
from PySide2.QtWidgets import *
from PianoManager.Animation import Animation
from PianoManager.UI.ui_NewUser3 import Ui_NewUser3
from PianoManager.writer_for_test import TestDatabaseWriter
from PianoManager.reader_for_test import TestDatabaseReader


class NewUser3(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # UI for the page
        self.ui = Ui_NewUser3()
        self.ui.setupUi(self)

        # animation
        self.animation = Animation()

        # database
        self.dbWriter = TestDatabaseWriter()
        self.dbReader = TestDatabaseReader()

        self.set_page()

    def error_animation(self):
        self.ui.buttonLeft.setDisabled(True)
        self.ui.buttonRight.setDisabled(True)
        self.animation.set_to_vibrate(self.ui.editID, amp=5)
        self.animation.current_anim.start(QPropertyAnimation.DeleteWhenStopped)
        self.animation.current_anim.finished.connect(partial(self.ui.buttonLeft.setEnabled, True))
        self.animation.current_anim.finished.connect(partial(self.ui.buttonRight.setEnabled, True))

    def set_page(self):
        self.ui.buttonLeft.setEnabled(True)
        self.ui.buttonRight.setEnabled(True)
        self.ui.editID.setText(self.dbReader.get_current_data("ID"))
        self.ui.labelError.hide()

    def clear_page(self):
        if self.ui.editID.text() == "":
            self.ui.labelWarning.hide()
            self.ui.labelError.show()
            self.error_animation()
            return "ERR"
        self.dbWriter.write_temporary_data(self.ui.editID.text(), "ID")
        self.ui.editID.clear()
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)

    new_user = NewUser3()

    new_user.show()
    sys.exit(app.exec_())
