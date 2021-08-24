from PySide6 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player


class AuthorEntry(QtWidgets.QFrame):
    clicked = QtCore.Signal()

    def __init__(self, parent=None, author_name=""):
        self.author_name = author_name
        super().__init__(parent=parent)
        self.setup_layout()

    def setup_layout(self):
        self.setStyleSheet("#label_4{\n"
                           "   font: 57 10pt \"Heebo Medium\";\n"
                           "}\n"
                           "#label_3{\n"
                           "    font: 87 11pt \"Heebo Black\";\n"
                           "    color: white;\n"
                           "}\n"
                           "#label{\n"
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
        self.verticalLayout_85 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_85.setContentsMargins(16, 16, 16, 25)
        self.verticalLayout_85.setSpacing(2)
        self.verticalLayout_85.setObjectName("verticalLayout_85")
        self.label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(155, 155))
        self.label.setMaximumSize(QtCore.QSize(155, 155))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/peach16bit.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_85.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.frame_99 = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_99.sizePolicy().hasHeightForWidth())
        self.frame_99.setSizePolicy(sizePolicy)
        self.frame_99.setMinimumSize(QtCore.QSize(155, 55))
        self.frame_99.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_99.setObjectName("frame_99")
        self.verticalLayout_86 = QtWidgets.QVBoxLayout(self.frame_99)
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName("verticalLayout_86")
        self.label_3 = QtWidgets.QLabel(self.frame_99)
        self.label_3.setText(self.author_name)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_86.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_99)
        self.label_4.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.label_4.setText("Author")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_86.addWidget(self.label_4)
        self.verticalLayout_85.addWidget(self.frame_99)

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super(AuthorEntry, self).mousePressEvent(event)
