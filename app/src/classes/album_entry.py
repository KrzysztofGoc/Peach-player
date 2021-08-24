from PySide6 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player


class AlbumEntry(QtWidgets.QFrame):
    clicked = QtCore.Signal()

    def __init__(self, parent=None, album_name=""):
        super().__init__(parent=parent)
        self.album_name = album_name
        self.setup_layout()

    def setup_layout(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFixedSize(QtCore.QSize(185, 265))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setStyleSheet("#label_31{\n"
                           "   font: 57 10pt \"Heebo Medium\";\n"
                           "}\n"
                           "#label_6{\n"
                           "    font: 87 11pt \"Heebo Black\";\n"
                           "    color: white;\n"
                           "}\n"
                           "#label_5{\n"
                           "    border-radius: 76px;\n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "}\n")
        self.verticalLayout_92 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_92.setContentsMargins(16, 16, 16, 25)
        self.verticalLayout_92.setSpacing(2)
        self.verticalLayout_92.setObjectName("verticalLayout_92")
        self.label_5 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(155, 155))
        self.label_5.setMaximumSize(QtCore.QSize(155, 155))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/peach16bit.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_92.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.frame_127 = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_127.sizePolicy().hasHeightForWidth())
        self.frame_127.setSizePolicy(sizePolicy)
        self.frame_127.setMinimumSize(QtCore.QSize(155, 55))
        self.frame_127.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_127.setObjectName("frame_127")
        self.verticalLayout_93 = QtWidgets.QVBoxLayout(self.frame_127)
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName("verticalLayout_93")
        self.label_6 = QtWidgets.QLabel(self.frame_127)
        self.label_6.setText(self.album_name)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_93.addWidget(self.label_6)
        self.label_31 = QtWidgets.QLabel(self.frame_127)
        self.label_31.setText("Album")
        self.label_31.setObjectName("label_31")
        self.verticalLayout_93.addWidget(self.label_31)
        self.verticalLayout_92.addWidget(self.frame_127)

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super(AlbumEntry, self).mousePressEvent(event)
