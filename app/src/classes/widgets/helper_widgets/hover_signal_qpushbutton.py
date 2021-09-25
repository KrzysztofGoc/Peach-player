from PySide2 import QtWidgets, QtCore


class HoverSignalQToolButton(QtWidgets.QToolButton):
    """Base QPushButton with hover signal."""
    mouseIn = QtCore.Signal()
    mouseOut = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def enterEvent(self, event) -> None:
        super(HoverSignalQToolButton, self).enterEvent(event)
        self.mouseIn.emit()

    def leaveEvent(self, event) -> None:
        super(HoverSignalQToolButton, self).leaveEvent(event)
        self.mouseOut.emit()
