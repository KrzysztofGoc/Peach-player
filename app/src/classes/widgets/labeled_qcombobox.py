from PySide2 import QtCore, QtGui, QtWidgets
from app.src.classes.widgets.helper_widgets.popup_signals_combo_box import PopupSignalsComboBox


class LabeledQComboBox(QtWidgets.QGroupBox):
    """Base QGroupBox with predefined layout with QComboBox inside.

    Keyword Args:
        input_title (str): Label text that will be shown when QComboBox's popup gets shown.

    """
    def __init__(self, input_title, parent=None):
        super().__init__(parent=parent)
        self.input_title = input_title
        self.setupUi()
        self.comboBox1.popupOpened.connect(self.combo_box_popup_opened_slot)
        self.comboBox1.popupClosed.connect(self.combo_box_popup_closed_slot)
        self.setTitle("")

    def setupUi(self):
        self.setStyleSheet("QComboBox {\n"
                           "    color:  rgb(179, 179, 179);\n"
                           "    border: 1px solid transparent;\n"
                           "    background-color: transparent;\n"
                           "    padding-right: 12px;\n"
                           "    padding-left: 12px;\n"
                           "    padding-top: 12px;\n"
                           "    padding-bottom: 12px;\n"
                           "}\n"
                           "QComboBox:hover{\n"
                           "    color: white;\n"
                           "}\n"
                           "QGroupBox:on{\n"
                           "    background-color: white;\n"
                           "}\n"
                           "QComboBox::drop-down {\n"
                           "    width: 32px;\n"
                           "}\n"
                           "QComboBox::down-arrow {\n"
                           "    image: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_arrow_drop_down_gray_48dp.png);\n"
                           "}\n"
                           "QGroupBox {\n"
                           "    padding: -1px;"
                           "    font: 57 8pt \"Heebo Black\";\n"
                           "    background-color: rgba(179, 179, 179, 0.25);\n"
                           "    border-radius: 4px;\n"
                           "    margin-top: 6px;\n"
                           "}\n"
                           "QGroupBox::title {\n"
                           "    color: rgb(173, 173, 173);\n"
                           "    subcontrol-origin: margin;\n"
                           "    left: 10px;\n"
                           "    padding: 0 3px 0 3px;\n"
                           "}\n"
                           "QComboBox QListView{\n"
                           "    font: 57 10pt \"Heebo Black\";\n"
                           "    border-top: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-left: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-right: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
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
                           "}\n")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Heebo Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.setFont(font)
        self.setTitle("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox1 = PopupSignalsComboBox(self)

        self.comboBox1.setView(QtWidgets.QListView())
        self.comboBox1.view().window().setWindowFlag(QtCore.Qt.Popup)
        self.comboBox1.view().window().setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.comboBox1.view().window().setWindowFlag(QtCore.Qt.NoDropShadowWindowHint)
        self.comboBox1.view().window().setAttribute(QtCore.Qt.WA_TranslucentBackground)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox1.sizePolicy().hasHeightForWidth())
        self.comboBox1.setSizePolicy(sizePolicy)
        self.comboBox1.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        self.comboBox1.setFont(font)
        self.comboBox1.setFrame(True)
        self.comboBox1.setObjectName("comboBox1")
        self.verticalLayout_2.addWidget(self.comboBox1)


    def combo_box_popup_opened_slot(self):
        self.setTitle(self.input_title)
        self.setStyleSheet("QComboBox {\n"
                           "    color:  rgb(179, 179, 179);\n"
                           "    border: none;\n"
                           "    background-color: transparent;\n"
                           "    padding-right: 12px;\n"
                           "    padding-left: 12px;\n"
                           "    padding-top: 12px;\n"
                           "    padding-bottom: 12px;\n"
                           "}\n"
                           "QComboBox:hover{\n"
                           "    color: white;\n"
                           "}\n"
                           "QComboBox::drop-down {\n"
                           "    width: 32px;\n"
                           "}\n"
                           "QComboBox::down-arrow {\n"
                           "    image: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_arrow_drop_down_gray_48dp.png);\n"
                           "}\n"
                           "QGroupBox {\n"
                           "    padding: -1px;"
                           "    font: 57 8pt \"Heebo Black\";\n"
                           "    background-color: rgb(51, 51, 51);\n"
                           "    border: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-top-right-radius: 4px;\n"
                           "    border-top-left-radius: 4px;\n"
                           "    border-bottom-left-radius: 0px;\n"
                           "    border-bottom-right-radius: 0px;\n"
                           "    margin-top: 6px;\n"
                           "}\n"
                           "QGroupBox::title {\n"
                           "    color: rgb(173, 173, 173);\n"
                           "    subcontrol-origin: margin;\n"
                           "    left: 10px;\n"
                           "    padding: 0 3px 0 3px;\n"
                           "}\n"
                           "QComboBox QListView{\n"
                           "    font: 57 10pt \"Heebo Black\";\n"
                           "    margin: 0px;\n"
                           "    border-top: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-left: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-right: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
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
                           "}\n")

    def combo_box_popup_closed_slot(self):
        self.setTitle("")
        self.setStyleSheet("QComboBox {\n"
                           "    color:  rgb(179, 179, 179);\n"
                           "    border: 1px solid transparent;\n"
                           "    background-color: transparent;\n"
                           "    padding-right: 12px;\n"
                           "    padding-left: 12px;\n"
                           "    padding-top: 12px;\n"
                           "    padding-bottom: 12px;\n"
                           "}\n"
                           "QComboBox:hover{\n"
                           "    color: white;\n"
                           "}\n"
                           "QGroupBox:on{\n"
                           "    background-color: white;\n"
                           "}\n"
                           "QComboBox::drop-down {\n"
                           "    width: 32px;\n"
                           "}\n"
                           "QComboBox::down-arrow {\n"
                           "    image: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_arrow_drop_down_gray_48dp.png);\n"
                           "}\n"
                           "QGroupBox {\n"
                           "    padding: -1px;"
                           "    font: 57 8pt \"Heebo Black\";\n"
                           "    background-color: rgba(179, 179, 179, 0.25);\n"
                           "    border-radius: 4px;\n"
                           "    margin-top: 6px;\n"
                           "}\n"
                           "QGroupBox::title {\n"
                           "    color: rgb(173, 173, 173);\n"
                           "    subcontrol-origin: margin;\n"
                           "    left: 10px;\n"
                           "    padding: 0 3px 0 3px;\n"
                           "}\n"
                           "QComboBox QListView{\n"
                           "    font: 57 10pt \"Heebo Black\";\n"
                           "    margin: 0px;\n"
                           "    border-top: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-left: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-right: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
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
                           "}\n")
