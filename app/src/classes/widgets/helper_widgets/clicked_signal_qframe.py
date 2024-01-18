from PySide2 import QtWidgets, QtCore


class ClickedSignalQFrame(QtWidgets.QFrame):
    """QFrame that emits signal when clicked. Appears over the whole window as black, semi-transparent layer behind
    dialogs."""
    clicked = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.6);")
        self.setFixedSize(parent.size())
        self.move(0, 0)

    def mousePressEvent(self, event):
        super(ClickedSignalQFrame, self).mousePressEvent(event)
        self.clicked.emit()
