from PySide2 import QtWidgets, QtCore


class ClickedSignalQFrame(QtWidgets.QFrame):
    """Base QFrame with clicked signal. Used to darken out background when dialog is shown."""
    clicked = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.6);")
        self.setFixedSize(parent.size())
        self.move(0, 0)

    def mousePressEvent(self, event):
        super(ClickedSignalQFrame, self).mousePressEvent(event)
        self.clicked.emit()
