from math import *
from PySide2.QtCore import QPoint, QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup, QParallelAnimationGroup
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

    def set_to_fade_in(self, widget):
        fade_in_effect = QGraphicsOpacityEffect()
        self.current_effect = fade_in_effect
        widget.setGraphicsEffect(fade_in_effect)

        fade_in_anim = QPropertyAnimation(fade_in_effect, b"opacity")
        fade_in_anim.setDuration(1000)
        fade_in_anim.setStartValue(0)
        fade_in_anim.setEndValue(1)
        fade_in_anim.setEasingCurve(QEasingCurve.InBack)
        self.current_anim = fade_in_anim

    def set_to_fade_out(self, widget):
        fade_out_effect = QGraphicsOpacityEffect()
        self.current_effect = fade_out_effect
        widget.setGraphicsEffect(fade_out_effect)

        fade_out_anim = QPropertyAnimation(fade_out_effect, b"opacity")
        fade_out_anim.setDuration(1000)
        fade_out_anim.setStartValue(1)
        fade_out_anim.setEndValue(0)
        fade_out_anim.setEasingCurve(QEasingCurve.InBack)
        self.current_anim = fade_out_anim

    def set_to_vibrate(self, widget, amp=10, period=25, direction=90):
        vibrate_group = QSequentialAnimationGroup()
        origin = widget.pos()
        direction = radians(direction)
        first_pos = QPoint(origin.x() + amp * cos(direction), origin.y() - amp * sin(direction))
        second_pos = QPoint(origin.x() - amp * cos(direction), origin.y() + amp * sin(direction))
        vibrate_anim = QPropertyAnimation(widget, b"pos")
        vibrate_anim.setDuration(period)
        vibrate_anim.setStartValue(origin)
        vibrate_anim.setEndValue(first_pos)
        vibrate_group.addAnimation(vibrate_anim)
        for i in range(0, 3):
            vibrate_anim = QPropertyAnimation(widget, b"pos")
            vibrate_anim.setDuration(2*period)
            vibrate_anim.setStartValue(first_pos)
            vibrate_anim.setEndValue(second_pos)
            vibrate_group.addAnimation(vibrate_anim)
            vibrate_anim = QPropertyAnimation(widget, b"pos")
            vibrate_anim.setDuration(2*period)
            vibrate_anim.setStartValue(second_pos)
            vibrate_anim.setEndValue(first_pos)
            vibrate_group.addAnimation(vibrate_anim)
        vibrate_anim = QPropertyAnimation(widget, b"pos")
        vibrate_anim.setDuration(period)
        vibrate_anim.setStartValue(first_pos)
        vibrate_anim.setEndValue(origin)
        vibrate_group.addAnimation(vibrate_anim)
        self.current_anim = vibrate_group
