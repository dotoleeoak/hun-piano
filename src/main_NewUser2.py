import sys
from functools import partial
from PySide2.QtCore import QPropertyAnimation, QParallelAnimationGroup
from PySide2.QtWidgets import *
from PianoManager.Animation import Animation
from PianoManager.UI.ui_NewUser2 import Ui_NewUser2
from PianoManager.writer_for_test import TestDatabaseWriter
from PianoManager.reader_for_test import TestDatabaseReader


class NewUser2(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # UI for the page
        self.ui = Ui_NewUser2()
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
        error_animation_group = QParallelAnimationGroup()
        self.animation.set_to_vibrate(self.ui.editContact1, amp=5, direction=90)
        error_animation_group.addAnimation(self.animation.current_anim)
        self.animation.set_to_vibrate(self.ui.editContact2, amp=5, direction=270)
        error_animation_group.addAnimation(self.animation.current_anim)
        self.animation.set_to_vibrate(self.ui.editContact3, amp=5, direction=90)
        error_animation_group.addAnimation(self.animation.current_anim)
        self.animation.current_anim = error_animation_group
        self.animation.current_anim.start(QPropertyAnimation.DeleteWhenStopped)
        self.animation.current_anim.finished.connect(partial(self.ui.buttonLeft.setEnabled, True))
        self.animation.current_anim.finished.connect(partial(self.ui.buttonRight.setEnabled, True))

    def set_page(self):
        self.ui.buttonLeft.setEnabled(True)
        self.ui.buttonRight.setEnabled(True)
        contact = self.dbReader.get_current_data("contact").split('-')
        self.ui.editContact1.setText(contact[0])
        self.ui.editContact2.setText(contact[1])
        self.ui.editContact3.setText(contact[2])
        self.ui.labelError.hide()

    def clear_page(self):
        if self.ui.editContact1.text() == "" \
                or self.ui.editContact2.text() == "" \
                or self.ui.editContact3.text() == "":
            self.ui.labelError.show()
            self.error_animation()
            return "ERR"
        contact = self.ui.editContact1.text() + "-" + self.ui.editContact2.text() + "-" + self.ui.editContact3.text()
        self.dbWriter.write_temporary_data(contact, "contact")
        self.ui.editContact1.clear()
        self.ui.editContact2.clear()
        self.ui.editContact3.clear()
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)

    new_user = NewUser2()

    new_user.show()
    sys.exit(app.exec_())
