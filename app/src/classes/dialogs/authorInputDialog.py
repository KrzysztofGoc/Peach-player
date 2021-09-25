from PySide2 import QtCore, QtGui, QtWidgets
from app.src.classes.widgets.labeled_qlineedit import LabeledQLineEdit
from app.src.classes.widgets.helper_widgets.hover_signal_qpushbutton import HoverSignalQToolButton


class authorInputDialog(QtWidgets.QDialog):
    """Base author input dialog with predefined layout, allows user to add new author."""

    def __init__(self, parent=None):
        super().__init__()
        if parent:
            self.setParent(parent)
        self.setupUi(self)
        self.authorInputDialogExitButton.clicked.connect(self.reject)

    def setupUi(self, authorInputDialog):
        """Setup predefined layout."""
        authorInputDialog.setObjectName("authorInputDialog")
        authorInputDialog.resize(524, 330)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(authorInputDialog.sizePolicy().hasHeightForWidth())
        authorInputDialog.setSizePolicy(sizePolicy)
        authorInputDialog.setMinimumSize(QtCore.QSize(524, 330))
        authorInputDialog.setMaximumSize(QtCore.QSize(524, 330))
        authorInputDialog.setStyleSheet("border: none;")
        self.verticalLayout = QtWidgets.QVBoxLayout(authorInputDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(authorInputDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(524, 330))
        self.frame_3.setMaximumSize(QtCore.QSize(524, 330))
        self.frame_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame_3.setStyleSheet("#frame_3{\n"
                                   "    border-radius: 8px;\n"
                                   "    background-color: rgb(40, 40, 40);\n"
                                   "}\n"
                                   "#authorInputDialogExitButton{\n"
                                   "    background-color: none;\n"
                                   "    border-radius: 16px;\n"
                                   "}\n"
                                   "#authorInputDialogExitButton:hover{\n"
                                   "    background-color: rgba(179, 179, 179, 0.25);\n"
                                   "}\n"
                                   "#authorInputDialogExitButton:pressed{\n"
                                   "    background-color: rgba(179, 179, 179, 0.35);\n"
                                   "}\n"
                                   "#label{\n"
                                   "    color: white;\n"
                                   "    font: 87 17pt \"Heebo Black\";\n"
                                   "}\n"
                                   "#authorInputDialogAddButton{\n"
                                   "    border-radius: 16px;\n"
                                   "    background-color: white;\n"
                                   "    color: black;\n"
                                   "    font: 87 9pt \"Heebo Medium\";\n"
                                   "}\n"
                                   "#authorInputDialogMiniatureQLabel{\n"
                                   "    background-color: rgb(40, 40, 40);\n"
                                   "}\n"
                                   "#authorInputDialogMiniatureQToolButton {\n"
                                   "    color: white;\n"
                                   "    font: 57 11pt \"Heebo Medium\";\n"
                                   "    padding-top: 55px;\n"
                                   "    padding-bottom: 26px;\n"
                                   "}\n")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("Add new author")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_4)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.authorInputDialogExitButton = QtWidgets.QPushButton(self.frame_5)
        self.authorInputDialogExitButton.setMinimumSize(QtCore.QSize(32, 32))
        self.authorInputDialogExitButton.setMaximumSize(QtCore.QSize(32, 32))
        self.authorInputDialogExitButton.setStyleSheet("")
        self.authorInputDialogExitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_close_white_48dp.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.authorInputDialogExitButton.setIcon(icon)
        self.authorInputDialogExitButton.setIconSize(QtCore.QSize(20, 20))
        self.authorInputDialogExitButton.setObjectName("authorInputDialogExitButton")
        self.verticalLayout_4.addWidget(self.authorInputDialogExitButton)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 214))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 214))
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setContentsMargins(213, 10, 0, 0)
        self.verticalLayout_15.setSpacing(16)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.groupBox1_3 = LabeledQLineEdit(parent=self.frame_7, input_title="Author Name",
                                            placeholder_text="Author name")
        self.authorInputDialogAuthorNameQLineEdit = self.groupBox1_3.lineEdit_2
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox1_3.sizePolicy().hasHeightForWidth())
        self.groupBox1_3.setSizePolicy(sizePolicy)
        self.groupBox1_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.groupBox1_3.setFont(font)
        self.groupBox1_3.setObjectName("groupBox1_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.groupBox1_3)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.verticalLayout_15.addWidget(self.groupBox1_3)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setContentsMargins(0, 16, 1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.authorInputDialogAddButton = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authorInputDialogAddButton.sizePolicy().hasHeightForWidth())
        self.authorInputDialogAddButton.setSizePolicy(sizePolicy)
        self.authorInputDialogAddButton.setMinimumSize(QtCore.QSize(90, 32))
        self.authorInputDialogAddButton.setMaximumSize(QtCore.QSize(90, 32))
        font = QtGui.QFont()
        font.setFamily("Heebo Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.authorInputDialogAddButton.setFont(font)
        self.authorInputDialogAddButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.authorInputDialogAddButton.setStyleSheet("")
        self.authorInputDialogAddButton.setText("ADD")
        self.authorInputDialogAddButton.setObjectName("authorInputDialogAddButton")
        self.verticalLayout_8.addWidget(self.authorInputDialogAddButton)
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_3)

        self.authorInputDialogMiniatureQLabel = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authorInputDialogMiniatureQLabel.sizePolicy().hasHeightForWidth())
        self.authorInputDialogMiniatureQLabel.setSizePolicy(sizePolicy)
        self.authorInputDialogMiniatureQLabel.setFixedSize(180, 180)
        self.authorInputDialogMiniatureQLabel.setText("")
        self.authorInputDialogMiniatureQLabel.setScaledContents(True)
        self.authorInputDialogMiniatureQLabel.setObjectName("authorInputDialogMiniatureQLabel")
        self.authorInputDialogMiniatureQLabel.move(24, 78)
        # self.authorInputDialogMiniatureQLabel.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/playlistCoverExample1.png"))
        # self._adjust_dialogs_stylesheet()

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(250)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 192))
        self.authorInputDialogMiniatureQLabel.setGraphicsEffect(self.shadow)

        self.authorInputDialogMiniatureQToolButton = HoverSignalQToolButton(self.authorInputDialogMiniatureQLabel)
        self.authorInputDialogMiniatureQToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        # if authorInputDialogMiniatureQLabel doesn't have pixmap set base icon to authorInputDialogMiniatureQToolButton
        if not self.authorInputDialogMiniatureQLabel.pixmap():
            icon11 = QtGui.QIcon()
            icon11.addPixmap(
                QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_music_note_gray_48dp.png"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.authorInputDialogMiniatureQToolButton.setIcon(icon11)

        self.authorInputDialogMiniatureQToolButton.setObjectName("authorInputDialogMiniatureQToolButton")
        self.authorInputDialogMiniatureQToolButton.setFixedSize(180, 180)
        self.authorInputDialogMiniatureQToolButton.setIconSize(QtCore.QSize(52, 52))

        self.authorInputDialogMiniatureQToolButton.mouseIn.connect(self.miniature_qtoolbutton_hover_slot)
        self.authorInputDialogMiniatureQToolButton.mouseOut.connect(self.miniature_qtoolbutton_unhover_slot)

    def miniature_qtoolbutton_hover_slot(self):
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_edit_white_48dp.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.authorInputDialogMiniatureQToolButton.setIcon(icon12)
        self.authorInputDialogMiniatureQToolButton.setText("Choose photo")

    def miniature_qtoolbutton_unhover_slot(self):
        if not self.authorInputDialogMiniatureQLabel.pixmap():
            icon13 = QtGui.QIcon()
            icon13.addPixmap(
                QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_music_note_gray_48dp.png"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.authorInputDialogMiniatureQToolButton.setIcon(icon13)
            self.authorInputDialogMiniatureQToolButton.setText("")
        else:
            self.authorInputDialogMiniatureQToolButton.setIcon(QtGui.QIcon())
            self.authorInputDialogMiniatureQToolButton.setText("")

    def set_dialogs_miniature_preview_pixmap(self, url):
        """Set categoryInputDialogMiniatureQLabel to pixmap from url and call _adjust_dialogs_stylesheet.

        Parameters:
            url (QtCore.QUrl): path to miniature.
        """
        self.authorInputDialogMiniatureQLabel.setPixmap(QtGui.QPixmap(url.toLocalFile()))
        self._adjust_dialogs_stylesheet()
        self.miniature_qtoolbutton_unhover_slot()

    def _adjust_dialogs_stylesheet(self):
        """Adjust dialogs stylesheet. Add black background on hoover to categoryInputDialogMiniatureQToolButton if
         categoryInputDialogMiniatureQLabel has pixmap.

         """
        if self.authorInputDialogMiniatureQLabel.pixmap():
            self.frame_3.setStyleSheet("#frame_3{\n"
                                       "    border-radius: 8px;\n"
                                       "    background-color: rgb(40, 40, 40);\n"
                                       "}\n"
                                       "#authorInputDialogExitButton{\n"
                                       "    background-color: none;\n"
                                       "    border-radius: 16px;\n"
                                       "}\n"
                                       "#authorInputDialogExitButton:hover{\n"
                                       "    background-color: rgba(179, 179, 179, 0.25);\n"
                                       "}\n"
                                       "#authorInputDialogExitButton:pressed{\n"
                                       "    background-color: rgba(179, 179, 179, 0.35);\n"
                                       "}\n"
                                       "#label{\n"
                                       "    color: white;\n"
                                       "    font: 87 17pt \"Heebo Black\";\n"
                                       "}\n"
                                       "#authorInputDialogAddButton{\n"
                                       "    border-radius: 16px;\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    font: 87 9pt \"Heebo Medium\";\n"
                                       "}\n"
                                       "#authorInputDialogMiniatureQLabel{\n"
                                       "    background-color: rgb(40, 40, 40);\n"
                                       "}\n"
                                       "#authorInputDialogMiniatureQToolButton {\n"
                                       "    color: white;\n"
                                       "    font: 57 11pt \"Heebo Medium\";\n"
                                       "    padding-top: 55px;\n"
                                       "    padding-bottom: 26px;\n"
                                       "}\n"
                                       "#authorInputDialogMiniatureQToolButton:hover{\n"
                                       "    background-color: rgba(0, 0, 0, 0.65);\n"
                                       "}\n")
        else:
            self.frame_3.setStyleSheet("#frame_3{\n"
                                       "    border-radius: 8px;\n"
                                       "    background-color: rgb(40, 40, 40);\n"
                                       "}\n"
                                       "#authorInputDialogExitButton{\n"
                                       "    background-color: none;\n"
                                       "    border-radius: 16px;\n"
                                       "}\n"
                                       "#authorInputDialogExitButton:hover{\n"
                                       "    background-color: rgba(179, 179, 179, 0.25);\n"
                                       "}\n"
                                       "#authorInputDialogExitButton:pressed{\n"
                                       "    background-color: rgba(179, 179, 179, 0.35);\n"
                                       "}\n"
                                       "#label{\n"
                                       "    color: white;\n"
                                       "    font: 87 17pt \"Heebo Black\";\n"
                                       "}\n"
                                       "#authorInputDialogAddButton{\n"
                                       "    border-radius: 16px;\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    font: 87 9pt \"Heebo Medium\";\n"
                                       "}\n"
                                       "#authorInputDialogMiniatureQLabel{\n"
                                       "    background-color: rgb(40, 40, 40);\n"
                                       "}\n"
                                       "#authorInputDialogMiniatureQToolButton {\n"
                                       "    color: white;\n"
                                       "    font: 57 11pt \"Heebo Medium\";\n"
                                       "    padding-top: 55px;\n"
                                       "    padding-bottom: 26px;\n"
                                       "}\n")