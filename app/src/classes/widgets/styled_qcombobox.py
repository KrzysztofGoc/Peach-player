from PySide2 import QtCore, QtGui, QtWidgets


class StyledQComboBox(QtWidgets.QComboBox):
    """Base QComboBox with predefined layout.

    Keyword Args
        parent: Parent widget of QComboBox.

    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setView(QtWidgets.QListView())
        self.view().window().setWindowFlag(QtCore.Qt.Popup)
        self.view().window().setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.view().window().setWindowFlag(QtCore.Qt.NoDropShadowWindowHint)
        self.view().window().setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("QComboBox {\n"
                           "    color: rgb(185, 185, 185);\n"
                           "    background-color: rgba(179, 179, 179, 0.25);\n"
                           "    border: 1px solid transparent;\n"
                           "    padding-right: 12px;\n"
                           "    padding-left: 12px;\n"
                           "    padding-top: 12px;\n"
                           "    padding-bottom: 12px;\n"
                           "    border-radius: 4px;\n"
                           "}\n"
                           "QComboBox:hover{\n"
                           "    color: white;\n"
                           "}\n"
                           "QComboBox::drop-down {\n"
                           "    border: none;\n"
                           "}\n"
                           "QComboBox:down-arrow {\n"
                           "    image: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_arrow_drop_down_gray_48dp.png);\n"
                           "    width: 26px;\n"
                           "    height: 26px;\n"
                           "    right: 10px;\n"
                           "}\n"
                           "QComboBox QListView{\n"
                           "    font: 57 10pt \"Heebo Black\";\n"
                           "    margin: 0px;\n"
                           "    border: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-bottom-left-radius: 4px;\n"
                           "    border-bottom-right-radius: 4px;\n"
                           "    background-color: rgb(51, 51, 51);\n"
                           "    outline: none;\n"
                           "    padding: 4px;\n"
                           "}\n"
                           "QComboBox QListView::item{\n"
                           "    color: white;\n"
                           "    height: 40px;\n"
                           "    border-radius: 2px;\n"
                           "    padding-left: 15px;\n"
                           "}\n"
                           "QComboBox QListView::item:selected{\n"
                           "    background-color: rgba(179, 179, 179, 0.25);\n"
                           "}\n"
                           "QComboBox:on{\n"
                           "    border: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    background-color: rgb(51, 51, 51);\n"
                           "    border-bottom-left-radius: 0px;\n"
                           "    border-bottom-right-radius: 0px;\n"
                           "}\n")
        self.setGeometry(QtCore.QRect(140, 120, 278, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setCurrentText("bozo")
        self.setIconSize(QtCore.QSize(17, 16))
        self.setPlaceholderText("")
        self.setFrame(True)
