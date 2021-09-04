from PySide2 import QtWidgets, QtCore


class FocusSignalsQLineEdit(QtWidgets.QLineEdit):
    focusIn = QtCore.Signal()
    focusOut = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def focusInEvent(self, event) -> None:
        super(FocusSignalsQLineEdit, self).focusInEvent(event)
        self.focusIn.emit()

    def focusOutEvent(self, event) -> None:
        super(FocusSignalsQLineEdit, self).focusOutEvent(event)
        self.focusOut.emit()
