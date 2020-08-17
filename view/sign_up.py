from pathlib import Path

from PySide2.QtCore import QRect, QSize, Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton

from view.dialog import DialogNotify

PATH_IMG = Path(__file__).absolute().parents[1] / "image"


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

        img_home = QPixmap(str(PATH_IMG / "home.png"))
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

        path_left = PATH_IMG / "arrow_left.png"
        path_right = PATH_IMG / "arrow_right.png"
        path_left_hover = PATH_IMG / "arrow_left_hover.png"
        path_right_hover = PATH_IMG / "arrow_right_hover.png"

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

        self.button_left.hide()
        self.line_left.hide()

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
        self.edit_contact1.setMaxLength(3)

        self.edit_contact2 = QLineEdit(self.frame_main)
        self.edit_contact2.setGeometry(QRect(350, 90, 100, 50))
        self.edit_contact2.setMaxLength(4)

        self.edit_contact3 = QLineEdit(self.frame_main)
        self.edit_contact3.setGeometry(QRect(490, 90, 100, 50))
        self.edit_contact3.setMaxLength(4)


class UiSignUpID(UiSignUp):
    def setupUi(self, widget):
        super().setupUi(widget)

        self.label_id = QLabel(self.frame_main)
        self.label_id.setGeometry(QRect(220, 70, 70, 40))
        self.label_id.setText("학번")

        self.edit_id = QLineEdit(self.frame_main)
        self.edit_id.setGeometry(QRect(310, 60, 255, 60))

class UiSignUpNFC(UiSignUp):
    def setupUi(self, widget):
        super().setupUi(widget)

        self.label_nfc = QLabel(self.frame_main)
        self.label_nfc.setGeometry(QRect(120, 70, 560, 40))
        self.label_nfc.setText("등록할 NFC가 있다면 지금 태그헤주세요")

        self.label_nfc_status = QLabel(self.frame_main)
        self.label_nfc_status.setGeometry(QRect(200, 250, 400, 40))
        self.label_nfc_status.setText("Not Tagged Yet")

class UiSignUpCheck(UiSignUp):
    def setupUi(self, widget):
        super().setupUi(widget)

        self.button_right.hide()
        self.line_right.hide()

        self.frame_main.setStyleSheet("background-color: white;" "font: 16pt 배달의민족 주아;")

        self.label_guide = QLabel(self.frame_main)
        self.label_guide.setGeometry(QRect(150, 52, 500, 30))
        self.label_guide.setText("아래 사용자로 등록하시겠습니까?")
        self.label_guide.setAlignment(Qt.AlignCenter)
        self.label_guide.setStyleSheet("color: red;")

        self.label_name = QLabel(self.frame_main)
        self.label_name.setGeometry(200, 100, 150, 40)
        self.label_name.setText("이름: ")
        self.label_name.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_name_user = QLabel(self.frame_main)
        self.label_name_user.setGeometry(QRect(360, 100, 200, 40))
        self.label_name_user.setText("홍길동")
        self.label_name_user.setAlignment(Qt.AlignVCenter)

        self.label_contact = QLabel(self.frame_main)
        self.label_contact.setGeometry(200, 150, 150, 40)
        self.label_contact.setText("전화번호: ")
        self.label_contact.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_contact_user = QLabel(self.frame_main)
        self.label_contact_user.setGeometry(QRect(360, 150, 200, 40))
        self.label_contact_user.setText("010-1234-5678")
        self.label_contact_user.setAlignment(Qt.AlignVCenter)

        self.label_id = QLabel(self.frame_main)
        self.label_id.setGeometry(200, 200, 150, 40)
        self.label_id.setText("학번: ")
        self.label_id.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.label_id_user = QLabel(self.frame_main)
        self.label_id_user.setGeometry(QRect(360, 200, 200, 40))
        self.label_id_user.setText("2020123456")
        self.label_id_user.setAlignment(Qt.AlignVCenter)

        # TODO: Button with hover image looks better
        img_temp = QPixmap(str(PATH_IMG / "unchecked.png"))
        self.button_temp = QPushButton(self.frame_main)
        self.button_temp.setGeometry(QRect(270, 255, 40, 40))
        self.button_temp.setIcon(QIcon(img_temp))
        self.button_temp.setStyleSheet("border: none;")

        self.label_temp = QLabel(self.frame_main)
        self.label_temp.setGeometry(QRect(320, 255, 280, 40))
        self.label_temp.setText("이 정보를 이번만 사용합니다.")
        self.label_temp.setStyleSheet("font-size: 12pt;")

        self.button_register = QPushButton(self.frame_main)
        self.button_register.setGeometry(QRect(340, 320, 120, 60))
        self.button_register.setText("등록")
        self.button_register.setStyleSheet(
            "QPushButton {"
            "   font-size: 20pt;"
            "   color: white;"
            "   background-color: rgb(0, 124, 255);"
            "   border-radius: 16px;"
            "}"
            "QPushButton:hover {"
            "   color: rgb(150, 150, 150);"
            "   background-color: rgb(0, 64, 195);"
            "}"
        )

        self.dialog_true = DialogNotify(widget)
        self.dialog_true.setFrameStyle(QFrame.Raised)
        self.dialog_true.hide()

        self.dialog_true_name = QLabel(self.dialog_true.dialog)
        self.dialog_true_name.setGeometry(QRect(50, 60, 300, 40))
        self.dialog_true_name.setAlignment(Qt.AlignCenter)
        self.dialog_true_name.setText("홍길동 님")
        self.dialog_true_name.setStyleSheet(
            "font-size: 24pt;" "color: rgb(71, 71, 71);"
        )

        self.dialog_true_guide = QLabel(self.dialog_true.dialog)
        self.dialog_true_guide.setGeometry(QRect(50, 100, 300, 40))
        self.dialog_true_guide.setAlignment(Qt.AlignCenter)
        self.dialog_true_guide.setText("등록되었습니다!")
        self.dialog_true_guide.setStyleSheet(
            "font-size: 16pt;" "color: rgb(71, 71, 71);"
        )

        self.dialog_false = DialogNotify(widget)
        self.dialog_false.setFrameStyle(QFrame.Raised)
        self.dialog_false.hide()

        self.dialog_false_guide = QLabel(self.dialog_false.dialog)
        self.dialog_false_guide.setGeometry(QRect(20, 45, 360, 100))
        self.dialog_false_guide.setAlignment(Qt.AlignCenter)
        self.dialog_false_guide.setText("이미 가입된 정보입니다.")
        self.dialog_false_guide.setStyleSheet(
            "font-size: 18pt;" "color: rgb(71, 71, 71);"
        )
