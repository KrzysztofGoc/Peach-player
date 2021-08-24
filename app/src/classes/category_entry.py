from PySide6 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player


class CategoryEntry(QtWidgets.QFrame):
    clicked = QtCore.Signal()

    def __init__(self, parent=None, category=""):
        super().__init__(parent=parent)
        self.category = category
        self.setup_layout()

    def setup_layout(self):
        self.setStyleSheet("#label_34{\n"
                           "   font: 57 10pt \"Heebo Medium\";\n"
                           "}\n"
                           "#label_140{\n"
                           "    font: 87 11pt \"Heebo Black\";\n"
                           "    color: white;\n"
                           "}\n"
                           "#label_32{\n"
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
        self.setStyleSheet("")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_94 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_94.setContentsMargins(16, 16, 16, 25)
        self.verticalLayout_94.setSpacing(2)
        self.verticalLayout_94.setObjectName("verticalLayout_94")
        self.label_32 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QtCore.QSize(155, 155))
        self.label_32.setMaximumSize(QtCore.QSize(155, 155))
        self.label_32.setStyleSheet("border-radius: 76px;\n"
                                    "background-color: rgb(0, 0, 0);")
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/peach16bit.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_94.addWidget(self.label_32, 0, QtCore.Qt.AlignHCenter)
        self.frame_143 = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_143.sizePolicy().hasHeightForWidth())
        self.frame_143.setSizePolicy(sizePolicy)
        self.frame_143.setMinimumSize(QtCore.QSize(155, 55))
        self.frame_143.setStyleSheet("background-color: none;")
        self.frame_143.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_143.setObjectName("frame_143")
        self.verticalLayout_95 = QtWidgets.QVBoxLayout(self.frame_143)
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName("verticalLayout_95")
        self.label_140 = QtWidgets.QLabel(self.frame_143)
        self.label_140.setStyleSheet("font: 87 11pt \"Heebo Black\";\n"
                                                           "color: white;\n"
                                                           "")
        self.label_140.setText(self.category)
        self.label_140.setObjectName("label_140")
        self.verticalLayout_95.addWidget(self.label_140)
        self.label_34 = QtWidgets.QLabel(self.frame_143)
        self.label_34.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.label_34.setText("Category")
        self.label_34.setObjectName("label_34")
        self.verticalLayout_95.addWidget(self.label_34)
        self.verticalLayout_94.addWidget(self.frame_143)

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super(CategoryEntry, self).mousePressEvent(event)
