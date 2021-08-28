from PySide2 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player


class NavbarFrame(QtWidgets.QFrame):
    resized = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._setup_ui(self)
        self.resized.connect(self.navbar_frame_resize_slot)

    def navbar_frame_resize_slot(self):
        if self.rect().width() <= 1020:
            self.navbarUsernameButton.setVisible(False)
            self.navbarUsernameSmallButton.setVisible(True)
        else:
            self.navbarUsernameSmallButton.setVisible(False)
            self.navbarUsernameButton.setVisible(True)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(NavbarFrame, self).resizeEvent(event)

    def _setup_ui(self, Form):
        self.frame_2 = Form
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setStyleSheet("#navbarUsernameButton{\n"
                                   "    background-color: rgb(24, 24, 24);\n"
                                   "    color: white;\n"
                                   "    border-radius: 16px;\n"
                                   "    font: 87 10.5pt \"Heebo Black\";\n"
                                   "}\n"
                                   "#navbarUsernameButton:hover{\n"
                                   "    background-color: rgba(24, 24, 24, 0.75);\n"
                                   "}\n"
                                   "#navbarPlayButton{\n"
                                   "    border-radius: 20px;\n"
                                   "    background-color: rgb(245, 155, 125);\n"
                                   "}\n"
                                   "#navbarPlayButton:checked{\n"
                                   "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_pause_white_48dp.png);\n"
                                   "}\n"
                                   "#navbarPlaylistName{\n"
                                   "    font: 87 17pt \"Heebo Black\";\n"
                                   "    color: white;\n"
                                   "}\n"
                                   "#navbarMaximizeRestoreButton:checked{     \n"
                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_restore_down_48dp.png);\n"
                                   "}\n"
                                   "#navbarMinimizeButton:hover{\n"
                                   "    background-color: rgb(94, 94, 94);\n"
                                   "}\n"
                                   "#navbarMinimizeButton:pressed{\n"
                                   "    background-color: rgb(48, 48, 48);\n"
                                   "}\n"
                                   "#navbarMaximizeRestoreButton:hover{\n"
                                   "    background-color: rgb(94, 94, 94);\n"
                                   "}\n"
                                   "#navbarMaximizeRestoreButton:pressed{\n"
                                   "    background-color: rgb(48, 48, 48);\n"
                                   "}\n"
                                   "#navbarCloseButton:hover{\n"
                                   "    background-color: rgb(232, 17, 35);\n"
                                   "}\n"
                                   "#navbarCloseButton:pressed{\n"
                                   "    background-color: rgb(151, 23, 34);\n"
                                   "}\n"
                                   "#navbarUsernameSmallButton{\n"
                                   "    background-color: rgb(51,  51, 51);\n"
                                   "    border-radius: 16px;\n"
                                   "    border: 2px solid black;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(32, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setContentsMargins(0, 0, 32, 0)
        self.horizontalLayout_3.setSpacing(18)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.navbarPlayButton = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarPlayButton.sizePolicy().hasHeightForWidth())
        self.navbarPlayButton.setSizePolicy(sizePolicy)
        self.navbarPlayButton.setMinimumSize(QtCore.QSize(40, 40))
        self.navbarPlayButton.setMaximumSize(QtCore.QSize(40, 40))
        self.navbarPlayButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_play_arrow_white_48dp.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarPlayButton.setIcon(icon)
        self.navbarPlayButton.setIconSize(QtCore.QSize(20, 20))
        self.navbarPlayButton.setCheckable(True)
        self.navbarPlayButton.setObjectName("navbarPlayButton")
        self.horizontalLayout_3.addWidget(self.navbarPlayButton)
        self.navbarPlaylistName = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarPlaylistName.sizePolicy().hasHeightForWidth())
        self.navbarPlaylistName.setSizePolicy(sizePolicy)
        self.navbarPlaylistName.setMinimumSize(QtCore.QSize(0, 60))
        self.navbarPlaylistName.setText("Integer disnissim")
        self.navbarPlaylistName.setObjectName("navbarPlaylistName")
        self.horizontalLayout_3.addWidget(self.navbarPlaylistName)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 32, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.navbarUsernameButton = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarUsernameButton.sizePolicy().hasHeightForWidth())
        self.navbarUsernameButton.setSizePolicy(sizePolicy)
        self.navbarUsernameButton.setMinimumSize(QtCore.QSize(172, 32))
        self.navbarUsernameButton.setMaximumSize(QtCore.QSize(172, 32))
        self.navbarUsernameButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.navbarUsernameButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.navbarUsernameButton.setText("Logged in as: User    ")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_logout_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarUsernameButton.setIcon(icon1)
        self.navbarUsernameButton.setObjectName("navbarUsernameButton")
        self.verticalLayout_4.addWidget(self.navbarUsernameButton)
        self.navbarUsernameSmallButton = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarUsernameSmallButton.sizePolicy().hasHeightForWidth())
        self.navbarUsernameSmallButton.setSizePolicy(sizePolicy)
        self.navbarUsernameSmallButton.setMinimumSize(QtCore.QSize(32, 32))
        self.navbarUsernameSmallButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_logout_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarUsernameSmallButton.setIcon(icon2)
        self.navbarUsernameSmallButton.setIconSize(QtCore.QSize(16, 16))
        self.navbarUsernameSmallButton.setObjectName("navbarUsernameSmallButton")
        self.verticalLayout_4.addWidget(self.navbarUsernameSmallButton)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(135, 60))
        self.frame_4.setMaximumSize(QtCore.QSize(135, 60))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(135, 30))
        self.frame_5.setMaximumSize(QtCore.QSize(135, 30))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.navbarMinimizeButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarMinimizeButton.sizePolicy().hasHeightForWidth())
        self.navbarMinimizeButton.setSizePolicy(sizePolicy)
        self.navbarMinimizeButton.setMinimumSize(QtCore.QSize(45, 30))
        self.navbarMinimizeButton.setMaximumSize(QtCore.QSize(45, 30))
        self.navbarMinimizeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_minimize_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarMinimizeButton.setIcon(icon3)
        self.navbarMinimizeButton.setIconSize(QtCore.QSize(48, 48))
        self.navbarMinimizeButton.setObjectName("navbarMinimizeButton")
        self.horizontalLayout_2.addWidget(self.navbarMinimizeButton)
        self.navbarMaximizeRestoreButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarMaximizeRestoreButton.sizePolicy().hasHeightForWidth())
        self.navbarMaximizeRestoreButton.setSizePolicy(sizePolicy)
        self.navbarMaximizeRestoreButton.setMinimumSize(QtCore.QSize(45, 30))
        self.navbarMaximizeRestoreButton.setMaximumSize(QtCore.QSize(45, 30))
        self.navbarMaximizeRestoreButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_maximize_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarMaximizeRestoreButton.setIcon(icon4)
        self.navbarMaximizeRestoreButton.setIconSize(QtCore.QSize(48, 48))
        self.navbarMaximizeRestoreButton.setCheckable(True)
        self.navbarMaximizeRestoreButton.setObjectName("navbarMaximizeRestoreButton")
        self.horizontalLayout_2.addWidget(self.navbarMaximizeRestoreButton)
        self.navbarCloseButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarCloseButton.sizePolicy().hasHeightForWidth())
        self.navbarCloseButton.setSizePolicy(sizePolicy)
        self.navbarCloseButton.setMinimumSize(QtCore.QSize(45, 30))
        self.navbarCloseButton.setMaximumSize(QtCore.QSize(45, 30))
        self.navbarCloseButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_close_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarCloseButton.setIcon(icon5)
        self.navbarCloseButton.setIconSize(QtCore.QSize(16, 16))
        self.navbarCloseButton.setObjectName("navbarCloseButton")
        self.horizontalLayout_2.addWidget(self.navbarCloseButton)
        self.verticalLayout_3.addWidget(self.frame_5)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.frame_4)
