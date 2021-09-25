from PySide2 import QtCore, QtGui, QtWidgets
from app.src.classes.widgets.labeled_qcombobox import LabeledQComboBox
from app.src.classes.widgets.labeled_qlineedit import LabeledQLineEdit
from app.src.classes.widgets.helper_widgets.hover_signal_qpushbutton import HoverSignalQToolButton


class albumInputDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__()
        if parent:
            self.setParent(parent)
        self.setupUi(self)
        self.albumInputDialogExitButton.clicked.connect(self.reject)

    def setupUi(self, albumInputDialog):
        albumInputDialog.setObjectName("albumInputDialog")
        albumInputDialog.resize(524, 330)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(albumInputDialog.sizePolicy().hasHeightForWidth())
        albumInputDialog.setSizePolicy(sizePolicy)
        albumInputDialog.setFixedSize(QtCore.QSize(524, 330))
        albumInputDialog.setStyleSheet("border: none;")
        self.verticalLayout = QtWidgets.QVBoxLayout(albumInputDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(albumInputDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFixedSize(QtCore.QSize(524, 330))
        self.frame_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame_3.setStyleSheet("#frame_3{\n"
                                   "    border-radius: 8px;\n"
                                   "    background-color: rgb(40, 40, 40);\n"
                                   "}\n"
                                   "#albumInputDialogExitButton{\n"
                                   "    background-color: none;\n"
                                   "    border-radius: 16px;\n"
                                   "}\n"
                                   "#albumInputDialogExitButton:hover{\n"
                                   "    background-color: rgba(179, 179, 179, 0.25);\n"
                                   "}\n"
                                   "#albumInputDialogExitButton:pressed{\n"
                                   "    background-color: rgba(179, 179, 179, 0.35);\n"
                                   "}\n"
                                   "#label{\n"
                                   "    color: white;\n"
                                   "    font: 87 17pt \"Heebo Black\";\n"
                                   "}\n"
                                   "#albumInputDialogAddButton{\n"
                                   "    border-radius: 16px;\n"
                                   "    background-color: white;\n"
                                   "    color: black;\n"
                                   "    font: 87 9pt \"Heebo Medium\";\n"
                                   "}\n"
                                   "QScrollBar:vertical {\n"
                                   "    width: 16px;\n"
                                   "    background: transparent;\n"
                                   "}\n"
                                   "QScrollBar::handle:vertical{\n"
                                   "    margin-right: -10px;\n"
                                   "    background: rgba(179, 179, 179, 0.45);\n"
                                   "}\n"
                                   "QScrollBar::handle:hover:vertical{\n"
                                   "    background: rgba(179, 179, 179, 0.55);\n"
                                   "}\n"
                                   "QScrollBar::sub-page:vertical{\n"
                                   "    background: transparent;\n"
                                   "}\n"
                                   "QScrollBar::add-page:vertical{\n"
                                   "    background: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "QScrollBar::add-line:vertical{\n"
                                   "    widgth: 0px;\n"
                                   "    height: 0px;\n"
                                   "    background: none;\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "QScrollBar::sub-line:vertical{\n"
                                   "    widgth: 0px;\n"
                                   "    height: 0px;\n"
                                   "    border: none;\n"
                                   "    background: none;\n"
                                   "}\n"
                                   "#albumInputDialogAlbumsMiniatureQLabel{\n"
                                   "    background-color: rgb(40, 40, 40);\n"
                                   "}\n"
                                   "#albumInputDialogMiniatureQToolButton{\n"
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
        self.label.setText("Add new album")
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
        self.albumInputDialogExitButton = QtWidgets.QPushButton(self.frame_5)
        self.albumInputDialogExitButton.setMinimumSize(QtCore.QSize(32, 32))
        self.albumInputDialogExitButton.setMaximumSize(QtCore.QSize(32, 32))
        self.albumInputDialogExitButton.setStyleSheet("")
        self.albumInputDialogExitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_close_white_48dp.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.albumInputDialogExitButton.setIcon(icon)
        self.albumInputDialogExitButton.setIconSize(QtCore.QSize(20, 20))
        self.albumInputDialogExitButton.setObjectName("albumInputDialogExitButton")
        self.verticalLayout_4.addWidget(self.albumInputDialogExitButton)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 198))
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setContentsMargins(213, 10, 0, 0)
        self.verticalLayout_15.setSpacing(16)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.groupBox1_3 = LabeledQLineEdit(parent=self.frame_7, input_title="Name", placeholder_text="Album name")
        self.albumInputDialogAlbumNameQLineEdit = self.groupBox1_3.lineEdit_2
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
        self.albumInputDialogAlbumNameQLineEdit.setPalette(palette)
        self.verticalLayout_15.addWidget(self.groupBox1_3)
        self.groupBox1_2 = LabeledQComboBox(parent=self.frame_7, input_title="Category Name")
        self.albumInputDialogCategoryQComboBox = self.groupBox1_2.comboBox1
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox1_2.sizePolicy().hasHeightForWidth())
        self.groupBox1_2.setSizePolicy(sizePolicy)
        self.groupBox1_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.groupBox1_2.setFont(font)
        self.groupBox1_2.setTitle("Category Name")
        self.groupBox1_2.setObjectName("groupBox1_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox1_2)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.albumInputDialogCategoryQComboBox.setMaxVisibleItems(4)
        self.albumInputDialogCategoryQComboBox.addItem("")
        self.albumInputDialogCategoryQComboBox.setItemText(0, "No category")
        self.albumInputDialogCategoryQComboBox.addItem("")
        self.albumInputDialogCategoryQComboBox.setItemText(1, "Category1")
        self.albumInputDialogCategoryQComboBox.addItem("")
        self.albumInputDialogCategoryQComboBox.setItemText(2, "Category2")
        self.albumInputDialogCategoryQComboBox.addItem("")
        self.albumInputDialogCategoryQComboBox.setItemText(3, "Category3")
        self.verticalLayout_15.addWidget(self.groupBox1_2)
        self.groupBox1 = LabeledQComboBox(parent=self.frame_7, input_title="Author Name")
        self.albumInputDialogAuthorQComboBox = self.groupBox1.comboBox1
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox1.sizePolicy().hasHeightForWidth())
        self.groupBox1.setSizePolicy(sizePolicy)
        self.groupBox1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.groupBox1.setFont(font)
        self.groupBox1.setTitle("Author Name")
        self.groupBox1.setObjectName("groupBox1")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox1)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")

        self.albumInputDialogAuthorQComboBox.setMaxVisibleItems(4)
        self.albumInputDialogAuthorQComboBox.addItem("")
        self.albumInputDialogAuthorQComboBox.setItemText(0, "No author")
        self.albumInputDialogAuthorQComboBox.addItem("")
        self.albumInputDialogAuthorQComboBox.setItemText(1, "Author1")
        self.albumInputDialogAuthorQComboBox.addItem("")
        self.albumInputDialogAuthorQComboBox.setItemText(2, "Author2")

        self.verticalLayout_15.addWidget(self.groupBox1)
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
        self.albumInputDialogAddButton = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumInputDialogAddButton.sizePolicy().hasHeightForWidth())
        self.albumInputDialogAddButton.setSizePolicy(sizePolicy)
        self.albumInputDialogAddButton.setMinimumSize(QtCore.QSize(90, 32))
        self.albumInputDialogAddButton.setMaximumSize(QtCore.QSize(90, 32))
        font = QtGui.QFont()
        font.setFamily("Heebo Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.albumInputDialogAddButton.setFont(font)
        self.albumInputDialogAddButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.albumInputDialogAddButton.setStyleSheet("")
        self.albumInputDialogAddButton.setText("ADD")
        self.albumInputDialogAddButton.setObjectName("albumInputDialogAddButton")
        self.verticalLayout_8.addWidget(self.albumInputDialogAddButton)
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_3)

        self.albumInputDialogAlbumsMiniatureQLabel = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumInputDialogAlbumsMiniatureQLabel.sizePolicy().hasHeightForWidth())
        self.albumInputDialogAlbumsMiniatureQLabel.setSizePolicy(sizePolicy)
        self.albumInputDialogAlbumsMiniatureQLabel.setFixedSize(180, 180)
        self.albumInputDialogAlbumsMiniatureQLabel.setText("")
        self.albumInputDialogAlbumsMiniatureQLabel.setScaledContents(True)
        self.albumInputDialogAlbumsMiniatureQLabel.setObjectName("albumInputDialogAlbumsMiniatureQLabel")
        self.albumInputDialogAlbumsMiniatureQLabel.move(24, 78)
        # self.albumInputDialogAlbumsMiniatureQLabel.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/playlistCoverExample1.png"))
        # self._adjust_dialogs_stylesheet()

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(250)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 192))
        self.albumInputDialogAlbumsMiniatureQLabel.setGraphicsEffect(self.shadow)

        self.albumInputDialogMiniatureQToolButton = HoverSignalQToolButton(self.albumInputDialogAlbumsMiniatureQLabel)
        self.albumInputDialogMiniatureQToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        # if albumInputDialogAlbumsMiniatureQLabel doesn't have pixmap set base icon to
        # albumInputDialogMiniatureQToolButton
        if not self.albumInputDialogAlbumsMiniatureQLabel.pixmap():
            icon11 = QtGui.QIcon()
            icon11.addPixmap(
                QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_music_note_gray_48dp.png"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.albumInputDialogMiniatureQToolButton.setIcon(icon11)

        self.albumInputDialogMiniatureQToolButton.setObjectName("albumInputDialogMiniatureQToolButton")
        self.albumInputDialogMiniatureQToolButton.setIconSize(QtCore.QSize(52, 52))
        self.albumInputDialogMiniatureQToolButton.setFixedSize(180, 180)

        self.albumInputDialogMiniatureQToolButton.mouseIn.connect(self.miniature_qtoolbutton_hover_slot)
        self.albumInputDialogMiniatureQToolButton.mouseOut.connect(self.miniature_qtoolbutton_unhover_slot)

    def miniature_qtoolbutton_hover_slot(self):
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_edit_white_48dp.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.albumInputDialogMiniatureQToolButton.setIcon(icon12)
        self.albumInputDialogMiniatureQToolButton.setText("Choose photo")

    def miniature_qtoolbutton_unhover_slot(self):
        if not self.albumInputDialogAlbumsMiniatureQLabel.pixmap():
            icon13 = QtGui.QIcon()
            icon13.addPixmap(
                QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_music_note_gray_48dp.png"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.albumInputDialogMiniatureQToolButton.setIcon(icon13)
            self.albumInputDialogMiniatureQToolButton.setText("")
        else:
            self.albumInputDialogMiniatureQToolButton.setIcon(QtGui.QIcon())
            self.albumInputDialogMiniatureQToolButton.setText("")

    def set_dialogs_miniature_preview_pixmap(self, url):
        """Set albumInputDialogAlbumsMiniatureQLabel to pixmap from url and call _adjust_dialogs_stylesheet.

        Parameters:
            url (QtCore.QUrl): path to miniature.
        """
        self.albumInputDialogAlbumsMiniatureQLabel.setPixmap(QtGui.QPixmap(url.toLocalFile()))
        self._adjust_dialogs_stylesheet()
        self.miniature_qtoolbutton_unhover_slot()

    def _adjust_dialogs_stylesheet(self):
        """Adjust dialogs stylesheet. Add black background on hoover to albumInputDialogMiniatureQToolButton if
         albumInputDialogAlbumsMiniatureQLabel has pixmap.

         """
        if self.albumInputDialogAlbumsMiniatureQLabel.pixmap():
            self.frame_3.setStyleSheet("#frame_3{\n"
                                       "    border-radius: 8px;\n"
                                       "    background-color: rgb(40, 40, 40);\n"
                                       "}\n"
                                       "#albumInputDialogExitButton{\n"
                                       "    background-color: none;\n"
                                       "    border-radius: 16px;\n"
                                       "}\n"
                                       "#albumInputDialogExitButton:hover{\n"
                                       "    background-color: rgba(179, 179, 179, 0.25);\n"
                                       "}\n"
                                       "#albumInputDialogExitButton:pressed{\n"
                                       "    background-color: rgba(179, 179, 179, 0.35);\n"
                                       "}\n"
                                       "#label{\n"
                                       "    color: white;\n"
                                       "    font: 87 17pt \"Heebo Black\";\n"
                                       "}\n"
                                       "#albumInputDialogAddButton{\n"
                                       "    border-radius: 16px;\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    font: 87 9pt \"Heebo Medium\";\n"
                                       "}\n"
                                       "QScrollBar:vertical {\n"
                                       "    width: 16px;\n"
                                       "    background: transparent;\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical{\n"
                                       "    margin-right: -10px;\n"
                                       "    background: rgba(179, 179, 179, 0.45);\n"
                                       "}\n"
                                       "QScrollBar::handle:hover:vertical{\n"
                                       "    background: rgba(179, 179, 179, 0.55);\n"
                                       "}\n"
                                       "QScrollBar::sub-page:vertical{\n"
                                       "    background: transparent;\n"
                                       "}\n"
                                       "QScrollBar::add-page:vertical{\n"
                                       "    background: transparent;\n"
                                       "}\n"
                                       "\n"
                                       "QScrollBar::add-line:vertical{\n"
                                       "    widgth: 0px;\n"
                                       "    height: 0px;\n"
                                       "    background: none;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QScrollBar::sub-line:vertical{\n"
                                       "    widgth: 0px;\n"
                                       "    height: 0px;\n"
                                       "    border: none;\n"
                                       "    background: none;\n"
                                       "}\n"
                                       "#albumInputDialogAlbumsMiniatureQLabel{\n"
                                       "    background-color: rgb(40, 40, 40);\n"
                                       "}\n"
                                       "#albumInputDialogMiniatureQToolButton{\n"
                                       "    color: white;\n"
                                       "    font: 57 11pt \"Heebo Medium\";\n"
                                       "    padding-top: 55px;\n"
                                       "    padding-bottom: 26px;\n"
                                       "}\n"
                                       "#albumInputDialogMiniatureQToolButton:hover{\n"
                                       "    background-color: rgba(0, 0, 0, 0.65);\n"
                                       "}\n")
        else:
            self.frame_3.setStyleSheet("#frame_3{\n"
                                       "    border-radius: 8px;\n"
                                       "    background-color: rgb(40, 40, 40);\n"
                                       "}\n"
                                       "#albumInputDialogExitButton{\n"
                                       "    background-color: none;\n"
                                       "    border-radius: 16px;\n"
                                       "}\n"
                                       "#albumInputDialogExitButton:hover{\n"
                                       "    background-color: rgba(179, 179, 179, 0.25);\n"
                                       "}\n"
                                       "#albumInputDialogExitButton:pressed{\n"
                                       "    background-color: rgba(179, 179, 179, 0.35);\n"
                                       "}\n"
                                       "#label{\n"
                                       "    color: white;\n"
                                       "    font: 87 17pt \"Heebo Black\";\n"
                                       "}\n"
                                       "#albumInputDialogAddButton{\n"
                                       "    border-radius: 16px;\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    font: 87 9pt \"Heebo Medium\";\n"
                                       "}\n"
                                       "QScrollBar:vertical {\n"
                                       "    width: 16px;\n"
                                       "    background: transparent;\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical{\n"
                                       "    margin-right: -10px;\n"
                                       "    background: rgba(179, 179, 179, 0.45);\n"
                                       "}\n"
                                       "QScrollBar::handle:hover:vertical{\n"
                                       "    background: rgba(179, 179, 179, 0.55);\n"
                                       "}\n"
                                       "QScrollBar::sub-page:vertical{\n"
                                       "    background: transparent;\n"
                                       "}\n"
                                       "QScrollBar::add-page:vertical{\n"
                                       "    background: transparent;\n"
                                       "}\n"
                                       "\n"
                                       "QScrollBar::add-line:vertical{\n"
                                       "    widgth: 0px;\n"
                                       "    height: 0px;\n"
                                       "    background: none;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QScrollBar::sub-line:vertical{\n"
                                       "    widgth: 0px;\n"
                                       "    height: 0px;\n"
                                       "    border: none;\n"
                                       "    background: none;\n"
                                       "}\n"
                                       "#albumInputDialogAlbumsMiniatureQLabel{\n"
                                       "    background-color: rgb(40, 40, 40);\n"
                                       "}\n"
                                       "#albumInputDialogMiniatureQToolButton{\n"
                                       "    color: white;\n"
                                       "    font: 57 11pt \"Heebo Medium\";\n"
                                       "    padding-top: 55px;\n"
                                       "    padding-bottom: 26px;\n"
                                       "}\n")
