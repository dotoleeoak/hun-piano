import sys
from functools import partial
from PySide2.QtCore import Slot, QPropertyAnimation, QParallelAnimationGroup
from PySide2.QtWidgets import *
from PianoManager.UI.ui_LogIn import Ui_LogIn
from PianoManager.reader_for_test import TestDatabaseReader
from PianoManager.NFC.NFCReaderForTest import NFCReader
from PianoManager.Animation import Animation


class LogIn(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # Database Reader Module
        self.dbReader = TestDatabaseReader()
        # NFC Reader Thread
        self.nfcReader = NFCReader()
        # Animation
        self.animation = Animation()

        # UI for the page
        self.ui = Ui_LogIn()
        self.ui.setupUi(self)

        # hide dialogue
        self.ui.DialogueShadow.hide()

        # Insert buttons into QButtonGroup
        self.keypadButtons = QButtonGroup()
        self.keypadButtons.addButton(self.ui.KeypadButton_0, 0)
        self.keypadButtons.addButton(self.ui.KeypadButton_1, 1)
        self.keypadButtons.addButton(self.ui.KeypadButton_2, 2)
        self.keypadButtons.addButton(self.ui.KeypadButton_3, 3)
        self.keypadButtons.addButton(self.ui.KeypadButton_4, 4)
        self.keypadButtons.addButton(self.ui.KeypadButton_5, 5)
        self.keypadButtons.addButton(self.ui.KeypadButton_6, 6)
        self.keypadButtons.addButton(self.ui.KeypadButton_7, 7)
        self.keypadButtons.addButton(self.ui.KeypadButton_8, 8)
        self.keypadButtons.addButton(self.ui.KeypadButton_9, 9)

        self.keyDisplays = QButtonGroup()
        self.keyDisplays.addButton(self.ui.NumberDisplay_1, 1)
        self.keyDisplays.addButton(self.ui.NumberDisplay_2, 2)
        self.keyDisplays.addButton(self.ui.NumberDisplay_3, 3)
        self.keyDisplays.addButton(self.ui.NumberDisplay_4, 4)
        self.keyDisplays.addButton(self.ui.NumberDisplay_5, 5)
        self.keyDisplays.addButton(self.ui.NumberDisplay_6, 6)
        self.keyDisplays.addButton(self.ui.NumberDisplay_7, 7)
        self.keyDisplays.addButton(self.ui.NumberDisplay_8, 8)

        self.displayIndex = 1
        self.password = ""

        for i in range(0, 10):
            self.keypadButtons.button(i).clicked.connect(partial(self.write_number, i))

        self.ui.DButtonYes.clicked.connect(lambda: print("playing piano!"))
        self.ui.DButtonNo.clicked.connect(lambda: self.hide_dialogue_check())

        self.set_page()

    # Input a password and display it
    def write_number(self, num):

        if self.displayIndex > 8:
            return
        self.keyDisplays.button(self.displayIndex).setText(str(num))
        self.password += str(num)
        self.displayIndex += 1
        if self.displayIndex > 8:
            self.check_valid_pass(self.password)

    # Check whether the password is valid
    def check_valid_pass(self, password):

        (isInDB, data) = self.dbReader.is_pass_in_database(password)  # (bool, data)

        if isInDB:
            print("valid")
            self.show_dialogue_check(data["name"])
            self.clear_password()
        else:
            print("invalid")
            self.show_error_animation()

    # When NFC signal detected
    @Slot(str)
    def check_valid_uid(self, uid):

        (isInDB, data) = self.dbReader.is_uid_in_database(uid)  # (bool, data)

        if isInDB:
            print("valid")
            self.show_dialogue_check(data["name"])
        else:
            print("invalid")
        self.clear_password()

    def show_dialogue_check(self, name):

        self.ui.DLabelName.setText(name + " 님")
        self.ui.DialogueShadow.show()

        # # example: how to use Animation (fade in)
        # self.animation.set_to_fade_in(self.ui.DialogueShadow)
        # self.animation.current_anim.start(QPropertyAnimation.DeleteWhenStopped)

    def hide_dialogue_check(self):

        # # example: how to use Animation (fade out)
        # self.animation.set_to_fade_out(self.ui.DialogueShadow)
        # self.animation.current_anim.start(QPropertyAnimation.DeleteWhenStopped)
        # # make sure to hide a widget after the animation is finished
        # self.animation.current_anim.finished.connect(self.ui.DialogueShadow.hide)
        self.ui.DialogueShadow.hide()
        print("hide!")

    def clear_password(self):

        self.password = ""
        self.displayIndex = 1
        for i in range(1, 9):
            self.keyDisplays.button(i).setText("")

    def show_error_animation(self):
        error_group = QParallelAnimationGroup()
        for i in range(1, 9):
            self.animation.set_to_vibrate(self.keyDisplays.button(i), amp=10, direction=90 + 180 * (i % 2))
            error_group.addAnimation(self.animation.current_anim)
        self.animation.current_anim = error_group
        self.animation.current_anim.start(QPropertyAnimation.DeleteWhenStopped)
        self.animation.current_anim.finished.connect(self.clear_password)

    def set_page(self):

        if not self.nfcReader.isRunning():
            print("thread run")
            self.nfcReader.start()
        self.nfcReader.nfc_connect.connect(self.check_valid_uid)

    def clear_page(self):

        if not self.nfcReader.isFinished():
            print("thread quit")
            self.nfcReader.quit()
        self.hide_dialogue_check()
        self.clear_password()

    def __del__(self):

        self.nfcReader.quit()
        self.nfcReader.terminate()
        self.nfcReader.wait()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    login = LogIn()

    login.show()
    sys.exit(app.exec_())
