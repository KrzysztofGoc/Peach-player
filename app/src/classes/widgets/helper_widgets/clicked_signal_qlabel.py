from PySide2 import QtWidgets, QtCore


class ClickedSignalQLabel(QtWidgets.QLabel):
    clicked = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super(ClickedSignalQLabel, self).mousePressEvent(event)
