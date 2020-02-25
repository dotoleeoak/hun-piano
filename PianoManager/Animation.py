from PySide2.QtCore import QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup, QParallelAnimationGroup
from PySide2.QtWidgets import QGraphicsOpacityEffect


class Animation:
    # for Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Animation, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # for holding the references
        self.current_effect = None
        self.current_anim = None

    def set_fade_in(self, widget):
        fade_in_effect = QGraphicsOpacityEffect()
        self.current_effect = fade_in_effect
        widget.setGraphicsEffect(fade_in_effect)

        fade_in_anim = QPropertyAnimation(fade_in_effect, b"opacity")
        fade_in_anim.setDuration(1000)
        fade_in_anim.setStartValue(0)
        fade_in_anim.setEndValue(1)
        fade_in_anim.setEasingCurve(QEasingCurve.InBack)
        self.current_anim = fade_in_anim

    def set_fade_out(self, widget):
        fade_out_effect = QGraphicsOpacityEffect()
        self.current_effect = fade_out_effect
        widget.setGraphicsEffect(fade_out_effect)

        fade_out_anim = QPropertyAnimation(fade_out_effect, b"opacity")
        fade_out_anim.setDuration(1000)
        fade_out_anim.setStartValue(1)
        fade_out_anim.setEndValue(0)
        fade_out_anim.setEasingCurve(QEasingCurve.InBack)
        self.current_anim = fade_out_anim

