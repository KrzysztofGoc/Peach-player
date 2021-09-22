from PySide2 import QtCore, QtGui, QtWidgets
from app.src.classes.widgets.helper_widgets.focus_signals_qlineedit import FocusSignalsQLineEdit


class LabeledQLineEdit(QtWidgets.QGroupBox):
    def __init__(self, input_title, placeholder_text, parent=None):
        super().__init__(parent=parent)
        self.placeholder_text = placeholder_text
        self.input_title = input_title
        self.setupUi()
        self.lineEdit_2.focusIn.connect(self.line_edit_focus_in_event)
        self.lineEdit_2.focusOut.connect(self.lineEdit_focus_out_event)

    def setupUi(self):
        self.setStyleSheet("QLineEdit {\n"
                           "    font: 57 10pt \"Heebo Black\";\n"
                           "    color: white;\n"
                           "    background-color: transparent;\n"
                           "    border: none;\n"
                           "    padding-right: 12px;\n"
                           "    padding-left: 12px;\n"
                           "    padding-top: 12px;\n"
                           "    padding-bottom: 12px;\n"
                           "}\n"
                           "QGroupBox {\n"
                           "    font: 57 8pt \"Heebo Black\";\n"
                           "    background-color: rgba(179, 179, 179, 0.25);\n"
                           "    border: 1px solid transparent;\n"
                           "    border-radius: 4px;\n"
                           "    margin-top: 6px;\n"
                           "}\n"
                           "QGroupBox::title {\n"
                           "    color: rgb(173, 173, 173);\n"
                           "    subcontrol-origin: margin;\n"
                           "    left: 10px;\n"
                           "    padding: 0 3px 0 3px;\n"
                           "}\n")
        self.setGeometry(QtCore.QRect(60, 90, 280, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(280, 40))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.setFont(font)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lineEdit_2 = FocusSignalsQLineEdit(self)
        self.lineEdit_2.setPlaceholderText(self.placeholder_text)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_15.addWidget(self.lineEdit_2)

    def line_edit_focus_in_event(self):
        self.setTitle(self.input_title)
        self.setStyleSheet("QLineEdit {\n"
                           "    font: 57 10pt \"Heebo Black\";\n"
                           "    color: white;\n"
                           "    background-color: transparent;\n"
                           "    border: none;\n"
                           "    padding-right: 12px;\n"
                           "    padding-left: 12px;\n"
                           "    padding-top: 12px;\n"
                           "    padding-bottom: 12px;\n"
                           "}\n"
                           "QGroupBox {\n"
                           "    font: 57 8pt \"Heebo Black\";\n"
                           "    background-color: rgb(51, 51, 51);\n"
                           "    border: 1px solid rgba(179, 179, 179, 0.25);\n"
                           "    border-radius: 4px;\n"
                           "    margin-top: 6px;\n"
                           "}\n"
                           "QGroupBox::title {\n"
                           "    color: rgb(173, 173, 173);\n"
                           "    subcontrol-origin: margin;\n"
                           "    left: 10px;\n"
                           "    padding: 0 3px 0 3px;\n"
                           "}\n")

    def lineEdit_focus_out_event(self):
        self.setTitle("")
        self.setStyleSheet("QLineEdit {\n"
                           "    font: 57 10pt \"Heebo Black\";\n"
                           "    color: white;\n"
                           "    background-color: transparent;\n"
                           "    border: none;\n"
                           "    padding-right: 12px;\n"
                           "    padding-left: 12px;\n"
                           "    padding-top: 12px;\n"
                           "    padding-bottom: 12px;\n"
                           "}\n"
                           "QGroupBox {\n"
                           "    font: 57 8pt \"Heebo Black\";\n"
                           "    background-color: rgba(179, 179, 179, 0.25);\n"
                           "    border: 1px solid transparent;\n"
                           "    border-radius: 4px;\n"
                           "    margin-top: 6px;\n"
                           "}\n"
                           "QGroupBox::title {\n"
                           "    color: rgb(173, 173, 173);\n"
                           "    subcontrol-origin: margin;\n"
                           "    left: 10px;\n"
                           "    padding: 0 3px 0 3px;\n"
                           "}\n")
