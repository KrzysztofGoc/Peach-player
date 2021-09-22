from PySide2 import QtWidgets, QtCore


class PopupSignalsComboBox(QtWidgets.QComboBox):
    popupOpened = QtCore.Signal()
    popupClosed = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def showPopup(self) -> None:
        super(PopupSignalsComboBox, self).showPopup()
        self.popupOpened.emit()

    def hidePopup(self) -> None:
        super(PopupSignalsComboBox, self).hidePopup()
        self.popupClosed.emit()



