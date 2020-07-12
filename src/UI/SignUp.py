import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .path import PATH_IMG

# TODO: Better way to get absolute path of directory...?


class UiSignUp:
    def setupUi(self, widget):
        widget.resize(800, 480)

        self.frame_menu = QFrame(widget)
        self.frame_menu.setGeometry(QRect(0, 0, 800, 60))
        self.frame_menu.setStyleSheet(
            "QLabel {"
            "   color: white;"
            "   background-color: rgb(249, 138, 15);"
            "   font: 20pt 배달의민족 주아;"
            "}"
            "QPushButton {"
            "   color: white;"
            "   background-color: rgba(0, 0, 0, 0);"
            "   font: 16pt 배달의민족 주아;"
            "   border: none;"
            "   border-radius: 16px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgb(241, 219, 194);"
            "}"
        )

        self.label_menu = QLabel(self.frame_menu)
        self.label_menu.setGeometry(QRect(0, 0, 800, 60))
        self.label_menu.setText("사용자 등록")
        self.label_menu.setAlignment(Qt.AlignCenter)

        img_home = QPixmap(os.path.join(PATH_IMG, "home.png"))
        self.button_home = QPushButton(self.frame_menu)
        self.button_home.setGeometry(QRect(10, 5, 90, 50))
        self.button_home.setIcon(QIcon(img_home))
        self.button_home.setIconSize(QSize(40, 40))
        self.button_home.setText("홈")

        self.frame_main = QFrame(widget)
        self.frame_main.setGeometry(QRect(0, 60, 800, 420))
        self.frame_main.setStyleSheet(
            "QFrame {"
            "   font: 20pt 배달의민족 주아;"
            "   background-color: white;"
            "}"
            "QLineEdit {"
            "   font: 20pt 배달의민족 주아;"
            "   border: 3px solid black;"
            "   border-radius: 10px;"
            "}"
            "QLineEdit:hover {"
            "   background-color: rgb(200, 200, 200);"
            "}"
            "QLineEdit:focus {"
            "   border-color: rgb(0, 85, 255);"
            "}"
        )

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

        path_left = os.path.join(PATH_IMG, "arrow_left.png")
        path_right = os.path.join(PATH_IMG, "arrow_right.png")
        path_left_hover = os.path.join(PATH_IMG, "arrow_left_hover.png")
        path_right_hover = os.path.join(PATH_IMG, "arrow_right_hover.png")
        path_left = path_left.replace("\\", "/")
        path_right = path_right.replace("\\", "/")
        path_left_hover = path_left_hover.replace("\\", "/")
        path_right_hover = path_right_hover.replace("\\", "/")

        self.button_left = QPushButton(self.frame_main)
        self.button_left.setGeometry(QRect(30, 50, 80, 80))
        self.button_left.setStyleSheet(
            "QPushButton {"
            f"   image: url({path_left});"
            "   border: none;"
            "}"
            "QPushButton:hover {"
            f"   image: url({path_left_hover});"
            "}"
        )

        self.button_right = QPushButton(self.frame_main)
        self.button_right.setGeometry(QRect(690, 50, 80, 80))
        self.button_right.setStyleSheet(
            "QPushButton {"
            f"  image: url({path_right});"
            "   border: none;"
            "}"
            "QPushButton:hover {"
            f"   image: url({path_right_hover});"
            "}"
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


class UiSignUpContact(UiSignUp):
    def setupUi(self, widget):
        super().setupUi(widget)

        self.label_contact = QLabel(self.frame_main)
        self.label_contact.setGeometry(QRect(230, 40, 120, 40))
        self.label_contact.setText("전화번호")

        self.edit_contact1 = QLineEdit(self.frame_main)
        self.edit_contact1.setGeometry(QRect(230, 90, 80, 50))

        self.edit_contact2 = QLineEdit(self.frame_main)
        self.edit_contact2.setGeometry(QRect(350, 90, 100, 50))

        self.edit_contact3 = QLineEdit(self.frame_main)
        self.edit_contact3.setGeometry(QRect(490, 90, 100, 50))


class UiSignUpID(UiSignUp):
    def setupUi(self, widget):
        super().setupUi(widget)

        self.label_id = QLabel(self.frame_main)
        self.label_id.setGeometry(QRect(220, 70, 70, 40))
        self.label_id.setText("학번")

        self.edit_id = QLineEdit(self.frame_main)
        self.edit_id.setGeometry(QRect(310, 60, 255, 60))
