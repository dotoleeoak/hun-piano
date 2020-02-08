import sys
from functools import partial
from PySide2.QtWidgets import *
from ui_LogIn import Ui_LogIn
from reader_for_login_test import TestDatabaseReader

class Login(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)

        self.dbReader = TestDatabaseReader()
        
        self.ui = Ui_LogIn()
        self.ui.setupUi(self)

        self.ui.DialogueShadow.hide()

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
        self.keyDisplays.addButton(self.ui.roundDisplay_1, 1)
        self.keyDisplays.addButton(self.ui.roundDisplay_2, 2)
        self.keyDisplays.addButton(self.ui.roundDisplay_3, 3)
        self.keyDisplays.addButton(self.ui.roundDisplay_4, 4)
        self.keyDisplays.addButton(self.ui.roundDisplay_5, 5)
        self.keyDisplays.addButton(self.ui.roundDisplay_6, 6)
        self.keyDisplays.addButton(self.ui.roundDisplay_7, 7)
        self.keyDisplays.addButton(self.ui.roundDisplay_8, 8)
            
        self.displayIndex = 1
        self.password = ""

        for i in range(0, 10):
            self.keypadButtons.button(i).clicked.connect(partial(self.writeNumber, i))

        self.ui.DButtonYes.clicked.connect(lambda : print("playing piano!"))
        self.ui.DButtonNo.clicked.connect(lambda: self.hideDialogueCheck())
        

    def writeNumber(self, num):
        
        self.keyDisplays.button(self.displayIndex).setText(str(num))
        self.password += str(num)
        self.displayIndex += 1
        if self.displayIndex > 8 :
            self.checkValidPass(self.password)
            

    def checkValidPass(self, password):
        
        (isInDB, data) = self.dbReader.passInDatabase(password)
        self.password = ""
        self.displayIndex = 1
        if isInDB:
            print("valid")
            self.showDialogueCheck(data["name"])
        else:
            self.password = ""
            self.displayIndex = 1
            print("invalid")
            self.showErrorAnimation()
            
        for i in range(1, 9):
            self.keyDisplays.button(i).setText("")
    

    def showDialogueCheck(self, name):

        self.ui.DLabelName.setText(name + " 님")
        self.ui.DialogueShadow.show()
        

    def hideDialogueCheck(self):

        self.ui.DialogueShadow.hide()
        print("hide!")
        

    def showErrorAnimation(self):
        pass

            

if __name__ == '__main__':
    app = QApplication(sys.argv)

    login = Login()

    login.show()
    sys.exit(app.exec_())
