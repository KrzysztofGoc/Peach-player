from PySide6 import QtCore, QtWidgets


class AspectRatioLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)