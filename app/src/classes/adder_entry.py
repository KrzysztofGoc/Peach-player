from PySide6 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player


class AdderEntry(QtWidgets.QFrame):
    """Adder type ui entry with predefined layout.

    Attributes:
        adder_type : int
            defines the Adder as 1 - CategoryAdder, 2 - AlbumAdder, 3 - AuthorAdder
    """
    clicked = QtCore.Signal()

    def __init__(self, adder_type: int, parent=None):
        super().__init__(parent=parent)
        self.adder_type = adder_type
        self.setup_adder()

    def setup_adder(self):
        """Setup AdderEntry specifics and layout."""
        self.setup_layout()
        if self.adder_type == 1:
            self.label_250.setText("Add category")
        elif self.adder_type == 2:
            self.label_250.setText("Add album")
        elif self.adder_type == 3:
            self.label_250.setText("Add author")
        else:
            raise ValueError("Wrong adder_type value. Use 1, 2, 3.")

    def setup_layout(self):
        self.setStyleSheet("#label_250{\n"
                           "   font: 87 11pt \"Heebo Black\";\n"
                           "   color: white;\n"
                           "}\n")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(185, 265))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_247 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_247.setContentsMargins(16, 16, 16, 25)
        self.verticalLayout_247.setSpacing(2)
        self.verticalLayout_247.setObjectName("verticalLayout_247")
        self.label_249 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_249.sizePolicy().hasHeightForWidth())
        self.label_249.setSizePolicy(sizePolicy)
        self.label_249.setMinimumSize(QtCore.QSize(155, 155))
        self.label_249.setMaximumSize(QtCore.QSize(155, 155))
        self.label_249.setText("")
        self.label_249.setPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_add_gray_48dp.png"))
        self.label_249.setScaledContents(True)
        self.label_249.setAlignment(QtCore.Qt.AlignCenter)
        self.label_249.setObjectName("label_249")
        self.verticalLayout_247.addWidget(self.label_249)
        self.frame_400 = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_400.sizePolicy().hasHeightForWidth())
        self.frame_400.setSizePolicy(sizePolicy)
        self.frame_400.setMinimumSize(QtCore.QSize(155, 55))
        self.frame_400.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_400.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_400.setObjectName("frame_400")
        self.verticalLayout_248 = QtWidgets.QVBoxLayout(self.frame_400)
        self.verticalLayout_248.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_248.setSpacing(0)
        self.verticalLayout_248.setObjectName("verticalLayout_248")
        self.label_250 = QtWidgets.QLabel(self.frame_400)
        self.label_250.setMinimumSize(QtCore.QSize(0, 0))
        self.label_250.setAlignment(QtCore.Qt.AlignCenter)
        self.label_250.setObjectName("label_250")
        self.verticalLayout_248.addWidget(self.label_250)
        spacerItem42 = QtWidgets.QSpacerItem(155, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_248.addItem(spacerItem42)
        self.verticalLayout_247.addWidget(self.frame_400)

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super(AdderEntry, self).mousePressEvent(event)



