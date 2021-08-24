from PySide6 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player


class PlaylistEntry(QtWidgets.QFrame):
    clicked = QtCore.Signal()

    def __init__(self, parent=None, playlist_name=""):
        super().__init__(parent=parent)
        self.playlist_name = playlist_name
        self.setup_layout()

    def setup_layout(self):
        self.setStyleSheet("#label_37{\n"
                           "   font: 57 10pt \"Heebo Medium\";\n"
                           "}\n"
                           "#label_36{\n"
                           "    font: 87 11pt \"Heebo Black\";\n"
                           "    color: white;\n"
                           "}\n"
                           "#label_35{\n"
                           "    border-radius: 76px;\n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "}\n")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(185, 265))
        self.setMaximumSize(QtCore.QSize(185, 265))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_99 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_99.setContentsMargins(16, 16, 16, 25)
        self.verticalLayout_99.setSpacing(2)
        self.verticalLayout_99.setObjectName("verticalLayout_99")
        self.label_35 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setMinimumSize(QtCore.QSize(155, 155))
        self.label_35.setMaximumSize(QtCore.QSize(155, 155))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/peach16bit.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_99.addWidget(self.label_35, 0, QtCore.Qt.AlignHCenter)
        self.frame_160 = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_160.sizePolicy().hasHeightForWidth())
        self.frame_160.setSizePolicy(sizePolicy)
        self.frame_160.setMinimumSize(QtCore.QSize(155, 55))
        self.frame_160.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_160.setObjectName("frame_160")
        self.verticalLayout_100 = QtWidgets.QVBoxLayout(self.frame_160)
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName("verticalLayout_100")
        self.label_36 = QtWidgets.QLabel(self.frame_160)
        self.label_36.setText(self.playlist_name)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_100.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.frame_160)
        self.label_37.setText("Playlist")
        self.label_37.setObjectName("label_37")
        self.verticalLayout_100.addWidget(self.label_37)
        self.verticalLayout_99.addWidget(self.frame_160)

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super(PlaylistEntry, self).mousePressEvent(event)