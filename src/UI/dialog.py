import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Dialog(QFrame):
    def __init__(self, widget):
        QFrame.__init__(self, widget)

        self.setGeometry(QRect(0, 0, 800, 480))
        self.setStyleSheet(
            "font: 24pt 배달의민족 주아;" "background-color: rgba(0, 0, 0, 100);"
        )

        self.dialog = QFrame(self)
        self.dialog.setGeometry(QRect(200, 120, 400, 240))
        self.dialog.setStyleSheet("background-color: white;" "border-radius: 25px;")

        # self.label_notice = QLabel(self.dialog)
        # self.label_notice.setGeometry(QRect(0, 50, 400, 40))
        # self.label_notice.setStyleSheet("color: rgb(71, 71, 71);")


class DialogSelect(Dialog):
    def __init__(self, widget):
        Dialog.__init__(self, widget)

        self.button_no = QPushButton(self.dialog)
        self.button_no.setGeometry(QRect(20, 155, 170, 60))
        self.button_no.setText("취소")
        self.button_no.setStyleSheet(
            "QPushButton {"
            "   font-size: 16pt;"
            "   color: black;"
            "   background-color: rgb(180, 180, 180);"
            "   border-radius: 16px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgb(120, 120, 120);"
            "}"
        )

        self.button_yes = QPushButton(self.dialog)
        self.button_yes.setGeometry(QRect(210, 155, 170, 60))
        self.button_yes.setText("확인")
        self.button_yes.setStyleSheet(
            "QPushButton {"
            "   font-size: 16pt;"
            "   color: white;"
            "   background-color: rgb(0, 124, 255);"
            "   border-radius: 16px;"
            "}"
            "QPushButton:hover {"
            "   color: rgb(200, 200, 200);"
            "   background-color: rgb(0, 64, 195);"
            "}"
        )


class DialogNotify(Dialog):
    def __init__(self, widget):
        Dialog.__init__(self, widget)

        self.button_ok = QPushButton(self.dialog)
        self.button_ok.setGeometry(QRect(100, 155, 200, 60))
        self.button_ok.setText("확인")
        self.button_ok.setStyleSheet(
            "QPushButton {"
            "   font-size: 16pt;"
            "   color: white;"
            "   background-color: rgb(0, 124, 255);"
            "   border-radius: 16px;"
            "}"
            "QPushButton:hover {"
            "   color: rgb(200, 200, 200);"
            "   background-color: rgb(0, 64, 195);"
            "}"
        )


class UiExample:
    def setupUi(self, widget):
        widget.resize(800, 480)

        self.frame_test = QFrame(widget)
        self.frame_test.setGeometry(QRect(0, 0, 800, 480))

        self.button_test = QPushButton(self.frame_test)
        self.button_test.setGeometry(QRect(350, 220, 100, 40))
        self.button_test.setText("Click!")

        self.frame_dialog = DialogSelect(widget)
        self.frame_dialog.hide()


class WidgetExample(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = UiExample()
        self.ui.setupUi(self)

        self.ui.button_test.clicked.connect(self.func)

    def func(self):
        self.ui.frame_dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = WidgetExample()
    widget.show()
    sys.exit(app.exec_())
