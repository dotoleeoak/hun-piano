from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiSignUp:
    def setupUi(self, widget):
        widget.resize(800, 480)

        self.frame_menu = QFrame(widget)
        self.frame_menu.setGeometry(QRect(0, 0, 800, 60))

        self.label_menu = QLabel(self.frame_menu)
        self.label_menu.setGeometry(QRect(0, 0, 800, 60))
        self.label_menu.setText("사용자 등록")
        self.label_menu.setAlignment(Qt.AlignCenter)
        self.label_menu.setStyleSheet(
            "color: white; "
            "background-color: rgb(249, 138, 15); "
            "font: 20pt 배달의민족 주아; "
        )

        img_home = QPixmap("../../Images/home.png")
        self.button_home = QPushButton(self.frame_menu)
        self.button_home.setGeometry(QRect(10, 5, 100, 50))
        self.button_home.setIcon(QIcon(img_home))
        self.button_home.setIconSize(QSize(40, 40))
        self.button_home.setText("홈")
        self.button_home.setStyleSheet(
            "QPushButton { "
            "   color: white; "
            "   background-color: rgba(0, 0, 0, 0); "
            "   font: 16pt 배달의민족 주아; "
            "   border: 3px solid white; "
            "   border-radius: 16px; "
            "} "
            "QPushButton:hover { "
            "   background-color: rgb(241, 219, 194); "
            "} "
        )

        self.frame_main = QFrame(widget)
        self.frame_main.setGeometry(QRect(0, 60, 800, 420))
        self.frame_main.setStyleSheet("font: 20pt 배달의민족 주아; background-color: white;")

        self.line_left = QFrame(self.frame_main)
        self.line_left.setGeometry(QRect(130, 50, 2, 80))
        self.line_left.setFrameShape(QFrame.VLine)
        self.line_left.setStyleSheet(
            "background-color: rgb(176, 176, 176); border: none;"
        )

        self.line_right = QFrame(self.frame_main)
        self.line_right.setGeometry(QRect(670, 50, 2, 80))
        self.line_right.setFrameShape(QFrame.VLine)
        self.line_right.setStyleSheet(
            "background-color: rgb(176, 176, 176); border: none;"
        )

        self.button_left = QPushButton(self.frame_main)
        self.button_left.setGeometry(QRect(30, 50, 80, 80))
        self.button_left.setStyleSheet(
            "QPushButton { "
            "   image: url(../../Images/arrow_left.png); "
            "   border: none; "
            "} "
            "QPushButton:hover {"
            "   image: url(../../Images/arrow_left_hover.png); "
            "} "
        )

        self.button_right = QPushButton(self.frame_main)
        self.button_right.setGeometry(QRect(690, 50, 80, 80))
        self.button_right.setStyleSheet(
            "QPushButton { "
            "   image: url(../../Images/arrow_right.png); "
            "   border: none; "
            "} "
            "QPushButton:hover {"
            "   image: url(../../Images/arrow_right_hover.png); "
            "} "
        )


class UiSignUpName(UiSignUp):
    def setupUi(self, widget):
        super().setupUi(widget)

        self.label_name = QLabel(self.frame_main)
        self.label_name.setGeometry(QRect(220, 70, 70, 40))
        self.label_name.setText("이름")

        self.edit_name = QLineEdit(self.frame_main)
        self.edit_name.setGeometry(QRect(310, 60, 250, 60))
        self.edit_name.setMaxLength(20)
        self.edit_name.setStyleSheet(
            "QLineEdit { "
            "   border: 3px solid black; "
            "   border-radius: 10px; "
            "} "
            "QLineEdit:hover { "
            "   background-color: rgb(200, 200, 200); "
            "} "
            "QLineEdit:focus { "
            "   border-color: rgb(0, 85, 255); "
            "} "
        )


class UiSignUpContact(UiSignUp):
    def setupUi(self, widget):
        super().setupUi(widget)

        self.label_contact = QLabel(self.frame_main)
        self.label_contact.setGeometry(QRect(230, 40, 120, 40))
        self.label_contact.setText("전화번호")

        edit_style = (
            "QLineEdit { "
            "   border: 3px solid black; "
            "   border-radius: 10px; "
            "} "
            "QLineEdit:hover { "
            "   background-color: rgb(200, 200, 200); "
            "} "
            "QLineEdit:focus { "
            "   border-color: rgb(0, 85, 255); "
            "} "
        )

        self.edit_contact1 = QLineEdit(self.frame_main)
        self.edit_contact1.setGeometry(QRect(230, 90, 80, 50))
        self.edit_contact1.setStyleSheet(edit_style)

        self.edit_contact2 = QLineEdit(self.frame_main)
        self.edit_contact2.setGeometry(QRect(350, 90, 100, 50))
        self.edit_contact2.setStyleSheet(edit_style)

        self.edit_contact3 = QLineEdit(self.frame_main)
        self.edit_contact3.setGeometry(QRect(490, 90, 100, 50))
        self.edit_contact3.setStyleSheet(edit_style)


class UiSignUpID(UiSignUp):
    def setupUi(self, widget):
        super().setupUi(widget)

        self.label_id = QLabel(self.frame_main)
        self.label_id.setGeometry(QRect(220, 70, 70, 40))
        self.label_id.setText("학번")

        self.edit_id = QLineEdit(self.frame_main)
        self.edit_id.setGeometry(QRect(310, 60, 255, 60))
        self.edit_id.setStyleSheet(
            "QLineEdit { "
            "   border: 3px solid black; "
            "   border-radius: 10px; "
            "} "
            "QLineEdit:hover { "
            "   background-color: rgb(200, 200, 200); "
            "} "
            "QLineEdit:focus { "
            "   border-color: rgb(0, 85, 255); "
            "} "
        )
