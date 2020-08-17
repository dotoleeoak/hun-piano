import sys
from functools import partial
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget
from model import InUse, LogIn, SignUp


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("음취헌 Piano Manager")
        self.setFixedSize(800, 480)

        # # 라즈베리 파이에서 풀스크린으로 표시하기 위해 아래 코드 필요
        self.showFullScreen()

        page_in_use = InUse()
        page_log_in = LogIn()
        page_sign_up = SignUp()

        self.widget = QStackedWidget()
        self.widget.addWidget(page_log_in)  # index 0
        self.widget.addWidget(page_in_use)  # index 1
        self.widget.addWidget(page_sign_up)  # index 2
        self.setCentralWidget(self.widget)

        page_in_use.ui.button_quit.clicked.connect(partial(self.switch_page, 0))

        page_log_in.ui.button_register.clicked.connect(partial(self.switch_page, 2))
        page_log_in.ui.dialog_true.button_yes.clicked.connect(
            partial(self.switch_page, 1)
        )

        page_sign_up.widget(4).ui.dialog_true.button_ok.clicked.connect(
            partial(self.switch_page, 0)
        )
        for i in range(5):
            page_sign_up.widget(i).ui.button_home.clicked.connect(
                partial(self.switch_page, 0)
            )

    def switch_page(self, idx):
        if idx == 1:
            self.widget.widget(1).set_page(self.widget.widget(0).get_contact())
            self.widget.currentWidget().clear_page()
            self.widget.setCurrentIndex(idx)
        else:
            self.widget.currentWidget().clear_page()
            self.widget.setCurrentIndex(idx)
            self.widget.currentWidget().set_page()


if __name__ == "__main__":
    # # 가상 키보드를 표시하기 위해 아래 코드 필요
    import os
    os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
