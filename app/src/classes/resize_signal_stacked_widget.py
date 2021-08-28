from PySide2 import QtWidgets, QtCore


class ResizeSignalStackedWidget(QtWidgets.QStackedWidget):
    resized = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(ResizeSignalStackedWidget, self).resizeEvent(event)