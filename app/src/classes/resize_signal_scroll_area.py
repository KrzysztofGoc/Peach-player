from PySide6 import QtWidgets, QtCore


class ResizeSignalScrollArea(QtWidgets.QScrollArea):
    resized = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(ResizeSignalScrollArea, self).resizeEvent(event)
