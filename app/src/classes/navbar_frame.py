from PySide2 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player
from app.src.classes.widgets.sort_buttons_qframe import SortButtonsQFrame


# TODO Comment this class
class NavbarFrame(QtWidgets.QFrame):
    resized = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._setup_ui(self)
        self.resized.connect(self.navbar_frame_resize_slot)

    def navbar_frame_resize_slot(self):
        self.layer_frame.setFixedSize(self.width(), self.height())
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
        self.frame = Form
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 101))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 101))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
                                   "    font: 87 10.5pt Heebo Black;\n"
                                   "}\n"
                                   "#navbarUsernameButton:hover{\n"
                                   "    background-color: rgba(24, 24, 24, 0.75);\n"
                                   "}#navbarPlayButton{\n"
                                   "    border-radius: 20px;\n"
                                   "    background-color: rgb(245, 155, 125);\n"
                                   "}\n"
                                   "#navbarPlayButton:checked{\n"
                                   "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_pause_white_48dp.png);\n"
                                   "}\n"
                                   "#navbarPageName{\n"
                                   "    font: 87 17pt Heebo Black;\n"
                                   "    color: white;\n"
                                   "}\n"
                                   "#navbarMaximizeRestoreButton:checked{\n"
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
                                   "#navbarUsernameSmallButton:hover{\n"
                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_logout_white_48dp.png);\n"
                                   "}\n"
                                   "#navbarSynchronizeButton{\n"
                                   "    background-color: rgb(51,  51, 51);\n"
                                   "    border-radius: 16px;\n"
                                   "    border: 2px solid black;\n"
                                   "}\n"
                                   "#navbarSynchronizeButton:hover{\n"
                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_sync_alt_white_48dp.png);\n"
                                   "}\n")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(32, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # Blacked-out semi-transparent frame over Navbar
        self.layer_frame = QtWidgets.QFrame(self.frame_2)
        self.layer_frame.move(0, 0)
        self.layer_frame.setStyleSheet("background-color: rgba(18, 18, 18, 0)")

        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(0, 0, 18, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.navbarPlayButton = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarPlayButton.sizePolicy().hasHeightForWidth())
        self.navbarPlayButton.setSizePolicy(sizePolicy)
        self.navbarPlayButton.setMinimumSize(QtCore.QSize(40, 40))
        self.navbarPlayButton.setMaximumSize(QtCore.QSize(40, 40))
        self.navbarPlayButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.navbarPlayButton.setStyleSheet("")
        self.navbarPlayButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_play_arrow_white_48dp.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarPlayButton.setIcon(icon)
        self.navbarPlayButton.setIconSize(QtCore.QSize(20, 20))
        self.navbarPlayButton.setCheckable(True)
        self.navbarPlayButton.setObjectName("navbarPlayButton")
        self.horizontalLayout.addWidget(self.navbarPlayButton)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.navbarPageName = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarPageName.sizePolicy().hasHeightForWidth())
        self.navbarPageName.setSizePolicy(sizePolicy)
        self.navbarPageName.setText("Integer dignissim")
        self.navbarPageName.setObjectName("navbarPageName")
        self.horizontalLayout_2.addWidget(self.navbarPageName)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_4.addWidget(self.frame_3)
        spacerItem = QtWidgets.QSpacerItem(274, 57, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(16)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.navbarSynchronizeButton = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarSynchronizeButton.sizePolicy().hasHeightForWidth())
        self.navbarSynchronizeButton.setSizePolicy(sizePolicy)
        self.navbarSynchronizeButton.setMinimumSize(QtCore.QSize(32, 32))
        self.navbarSynchronizeButton.setMaximumSize(QtCore.QSize(32, 32))
        self.navbarSynchronizeButton.setToolTip("Synchronize songs")
        self.navbarSynchronizeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_sync_alt_gray_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarSynchronizeButton.setIcon(icon1)
        self.navbarSynchronizeButton.setIconSize(QtCore.QSize(18, 18))
        self.navbarSynchronizeButton.setObjectName("navbarSynchronizeButton")
        self.horizontalLayout_5.addWidget(self.navbarSynchronizeButton)
        self.navbarUsernameSmallButton = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarUsernameSmallButton.sizePolicy().hasHeightForWidth())
        self.navbarUsernameSmallButton.setSizePolicy(sizePolicy)
        self.navbarUsernameSmallButton.setMinimumSize(QtCore.QSize(32, 32))
        self.navbarUsernameSmallButton.setMaximumSize(QtCore.QSize(32, 32))
        self.navbarUsernameSmallButton.setToolTip("")
        self.navbarUsernameSmallButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_logout_gray_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarUsernameSmallButton.setIcon(icon2)
        self.navbarUsernameSmallButton.setObjectName("navbarUsernameSmallButton")
        self.horizontalLayout_5.addWidget(self.navbarUsernameSmallButton)
        self.navbarUsernameButton = QtWidgets.QPushButton(self.frame_6)
        self.navbarUsernameButton.setMinimumSize(QtCore.QSize(172, 32))
        self.navbarUsernameButton.setMaximumSize(QtCore.QSize(172, 32))
        self.navbarUsernameButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.navbarUsernameButton.setStyleSheet("")
        self.navbarUsernameButton.setText("Logged in as: User    ")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_logout_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarUsernameButton.setIcon(icon3)
        self.navbarUsernameButton.setObjectName("navbarUsernameButton")
        self.horizontalLayout_5.addWidget(self.navbarUsernameButton)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("PlaylistSortButtonsQFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.navbarMinimizeButton = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarMinimizeButton.sizePolicy().hasHeightForWidth())
        self.navbarMinimizeButton.setSizePolicy(sizePolicy)
        self.navbarMinimizeButton.setMinimumSize(QtCore.QSize(45, 30))
        self.navbarMinimizeButton.setMaximumSize(QtCore.QSize(45, 30))
        self.navbarMinimizeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_minimize_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarMinimizeButton.setIcon(icon4)
        self.navbarMinimizeButton.setIconSize(QtCore.QSize(48, 48))
        self.navbarMinimizeButton.setObjectName("navbarMinimizeButton")
        self.horizontalLayout_6.addWidget(self.navbarMinimizeButton)
        self.navbarMaximizeRestoreButton = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarMaximizeRestoreButton.sizePolicy().hasHeightForWidth())
        self.navbarMaximizeRestoreButton.setSizePolicy(sizePolicy)
        self.navbarMaximizeRestoreButton.setMinimumSize(QtCore.QSize(45, 30))
        self.navbarMaximizeRestoreButton.setMaximumSize(QtCore.QSize(45, 30))
        self.navbarMaximizeRestoreButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_maximize_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarMaximizeRestoreButton.setIcon(icon5)
        self.navbarMaximizeRestoreButton.setIconSize(QtCore.QSize(48, 48))
        self.navbarMaximizeRestoreButton.setCheckable(True)
        self.navbarMaximizeRestoreButton.setObjectName("navbarMaximizeRestoreButton")
        self.horizontalLayout_6.addWidget(self.navbarMaximizeRestoreButton)
        self.navbarCloseButton = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbarCloseButton.sizePolicy().hasHeightForWidth())
        self.navbarCloseButton.setSizePolicy(sizePolicy)
        self.navbarCloseButton.setMinimumSize(QtCore.QSize(45, 30))
        self.navbarCloseButton.setMaximumSize(QtCore.QSize(45, 30))
        self.navbarCloseButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_close_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navbarCloseButton.setIcon(icon6)
        self.navbarCloseButton.setObjectName("navbarCloseButton")
        self.horizontalLayout_6.addWidget(self.navbarCloseButton)
        self.verticalLayout_2.addWidget(self.frame_8)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.navbarPlayButton.setVisible(False)
        self.navbarPageName.setVisible(False)

        self.frame_13 = QtWidgets.QFrame(self.frame)
        self.frame_13.setVisible(False)
        self.frame_13.setStyleSheet("#frame_13{\n"
                                    f"    background-color: rgb(24, 24, 24);\n"
                                    f"    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                    "}\n")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 41))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 41))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.likedSongsStickySortButtonsFrame = SortButtonsQFrame(parent=self.frame_13,
                                                                  frame_structure={
                                                                      "sortButtonsQFrameTitleButtonQFrame": True,
                                                                      "sortButtonsQFrameAuthorButtonQFrame": True,
                                                                      "sortButtonsQFrameCategoryButtonQFrame": True,
                                                                      "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                                      "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                                  visibility_changing_sort_buttons_elements=[
                                                                      ("sortButtonsQFrameAuthorButtonQFrame", 552),
                                                                      ("sortButtonsQFrameCategoryButtonQFrame", 726),
                                                                      ("sortButtonsQFrameDateAddedButtonQFrame", 950)]
                                                                  )
        self.likedSongsStickySortButtonsFrame.setStyleSheet("#sortButtonsQFrameAuthorButtonQFrame{\n"
                                                            "    padding-left: 25px;\n"
                                                            "}\n"
                                                            "#sortButtonsQFrameCategoryButtonQFrame{\n"
                                                            "    padding-left: 25px;\n"
                                                            "}\n"
                                                            "#sortButtonsQFrameDateAddedButtonQFrame{\n"
                                                            "    padding-left: 25px;\n"
                                                            "}\n"
                                                            "#sortButtonsQFrameSongLengthButtonQFrame{\n"
                                                            "    padding-left: 25px;\n"
                                                            "}\n"
                                                            "SortButtonsQFrame QPushButton:hover{\n"
                                                            "    color: white;\n"
                                                            "}\n"
                                                            "SortButtonsQFrame QPushButton{\n"
                                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                                            "}\n")
        self.verticalLayout.addWidget(self.likedSongsStickySortButtonsFrame)

        self.lastPlayedStickySortButtonsFrame = SortButtonsQFrame(parent=self.frame_13,
                                                                  frame_structure={
                                                                      "sortButtonsQFrameTitleButtonQFrame": True,
                                                                      "sortButtonsQFrameAuthorButtonQFrame": True,
                                                                      "sortButtonsQFrameCategoryButtonQFrame": True,
                                                                      "sortButtonsQFrameDateAddedButtonQFrame": False,
                                                                      "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                                  visibility_changing_sort_buttons_elements=[
                                                                      ("sortButtonsQFrameAuthorButtonQFrame", 552),
                                                                      ("sortButtonsQFrameCategoryButtonQFrame", 726), ]
                                                                  )
        self.lastPlayedStickySortButtonsFrame.setStyleSheet("#sortButtonsQFrameAuthorButtonQFrame{\n"
                                                            "    padding-left: 25px;\n"
                                                            "}\n"
                                                            "#sortButtonsQFrameCategoryButtonQFrame{\n"
                                                            "    padding-left: 25px;\n"
                                                            "}\n"
                                                            "#sortButtonsQFrameDateAddedButtonQFrame{\n"
                                                            "    padding-left: 25px;\n"
                                                            "}\n"
                                                            "#sortButtonsQFrameSongLengthButtonQFrame{\n"
                                                            "    padding-left: 25px;\n"
                                                            "}\n"
                                                            "SortButtonsQFrame QPushButton:hover{\n"
                                                            "    color: white;\n"
                                                            "}\n"
                                                            "SortButtonsQFrame QPushButton{\n"
                                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                                            "}\n")
        self.verticalLayout.addWidget(self.lastPlayedStickySortButtonsFrame)

        self.playlistStickySortButtonsFrame = SortButtonsQFrame(parent=self.frame_13,
                                                                frame_structure={
                                                                    "sortButtonsQFrameTitleButtonQFrame": True,
                                                                    "sortButtonsQFrameAuthorButtonQFrame": True,
                                                                    "sortButtonsQFrameCategoryButtonQFrame": True,
                                                                    "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                                    "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                                visibility_changing_sort_buttons_elements=[
                                                                    ("sortButtonsQFrameAuthorButtonQFrame", 552),
                                                                    ("sortButtonsQFrameCategoryButtonQFrame", 726),
                                                                    (
                                                                        "sortButtonsQFrameDateAddedButtonQFrame", 950)]
                                                                )
        self.playlistStickySortButtonsFrame.setStyleSheet("#sortButtonsQFrameAuthorButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "#sortButtonsQFrameCategoryButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "#sortButtonsQFrameDateAddedButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "#sortButtonsQFrameSongLengthButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "SortButtonsQFrame QPushButton:hover{\n"
                                                          "    color: white;\n"
                                                          "}\n"
                                                          "SortButtonsQFrame QPushButton{\n"
                                                          "    font: 57 10pt \"Heebo Medium\";\n"
                                                          "}\n")
        self.verticalLayout.addWidget(self.playlistStickySortButtonsFrame)

        self.authorStickySortButtonsFrame = SortButtonsQFrame(parent=self.frame_13,
                                                              frame_structure={
                                                                  "sortButtonsQFrameTitleButtonQFrame": True,
                                                                  "sortButtonsQFrameAuthorButtonQFrame": False,
                                                                  "sortButtonsQFrameCategoryButtonQFrame": True,
                                                                  "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                                  "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                              visibility_changing_sort_buttons_elements=[
                                                                  ("sortButtonsQFrameCategoryButtonQFrame", 552),
                                                                  ("sortButtonsQFrameDateAddedButtonQFrame", 726)]
                                                              )
        self.authorStickySortButtonsFrame.setStyleSheet("#sortButtonsQFrameAuthorButtonQFrame{\n"
                                                        "    padding-left: 25px;\n"
                                                        "}\n"
                                                        "#sortButtonsQFrameCategoryButtonQFrame{\n"
                                                        "    padding-left: 25px;\n"
                                                        "}\n"
                                                        "#sortButtonsQFrameDateAddedButtonQFrame{\n"
                                                        "    padding-left: 25px;\n"
                                                        "}\n"
                                                        "#sortButtonsQFrameSongLengthButtonQFrame{\n"
                                                        "    padding-left: 25px;\n"
                                                        "}\n"
                                                        "SortButtonsQFrame QPushButton:hover{\n"
                                                        "    color: white;\n"
                                                        "}\n"
                                                        "SortButtonsQFrame QPushButton{\n"
                                                        "    font: 57 10pt \"Heebo Medium\";\n"
                                                        "}\n")
        self.verticalLayout.addWidget(self.authorStickySortButtonsFrame)

        self.categoryStickySortButtonsFrame = SortButtonsQFrame(parent=self.frame_13,
                                                                frame_structure={
                                                                    "sortButtonsQFrameTitleButtonQFrame": True,
                                                                    "sortButtonsQFrameAuthorButtonQFrame": True,
                                                                    "sortButtonsQFrameCategoryButtonQFrame": False,
                                                                    "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                                    "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                                visibility_changing_sort_buttons_elements=[
                                                                    ("sortButtonsQFrameAuthorButtonQFrame", 552),
                                                                    ("sortButtonsQFrameDateAddedButtonQFrame", 726)]
                                                                )
        self.categoryStickySortButtonsFrame.setStyleSheet("#sortButtonsQFrameAuthorButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "#sortButtonsQFrameCategoryButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "#sortButtonsQFrameDateAddedButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "#sortButtonsQFrameSongLengthButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "SortButtonsQFrame QPushButton:hover{\n"
                                                          "    color: white;\n"
                                                          "}\n"
                                                          "SortButtonsQFrame QPushButton{\n"
                                                          "    font: 57 10pt \"Heebo Medium\";\n"
                                                          "}\n")
        self.verticalLayout.addWidget(self.categoryStickySortButtonsFrame)

        self.albumStickySortButtonsFrame = SortButtonsQFrame(parent=self.frame_13,
                                                             frame_structure={
                                                                 "sortButtonsQFrameTitleButtonQFrame": True,
                                                                 "sortButtonsQFrameAuthorButtonQFrame": True,
                                                                 "sortButtonsQFrameCategoryButtonQFrame": False,
                                                                 "sortButtonsQFrameDateAddedButtonQFrame": False,
                                                                 "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                             visibility_changing_sort_buttons_elements=[
                                                                 ("sortButtonsQFrameAuthorButtonQFrame", 552)]
                                                             )
        self.albumStickySortButtonsFrame.setStyleSheet("#sortButtonsQFrameAuthorButtonQFrame{\n"
                                                       "    padding-left: 25px;\n"
                                                       "}\n"
                                                       "#sortButtonsQFrameCategoryButtonQFrame{\n"
                                                       "    padding-left: 25px;\n"
                                                       "}\n"
                                                       "#sortButtonsQFrameDateAddedButtonQFrame{\n"
                                                       "    padding-left: 25px;\n"
                                                       "}\n"
                                                       "#sortButtonsQFrameSongLengthButtonQFrame{\n"
                                                       "    padding-left: 25px;\n"
                                                       "}\n"
                                                       "SortButtonsQFrame QPushButton:hover{\n"
                                                       "    color: white;\n"
                                                       "}\n"
                                                       "SortButtonsQFrame QPushButton{\n"
                                                       "    font: 57 10pt \"Heebo Medium\";\n"
                                                       "}\n")
        self.verticalLayout.addWidget(self.albumStickySortButtonsFrame)

        self.allSongsStickySortButtonsFrame = SortButtonsQFrame(parent=self.frame_13,
                                                                frame_structure={
                                                                    "sortButtonsQFrameTitleButtonQFrame": True,
                                                                    "sortButtonsQFrameAuthorButtonQFrame": True,
                                                                    "sortButtonsQFrameCategoryButtonQFrame": True,
                                                                    "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                                    "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                                visibility_changing_sort_buttons_elements=[
                                                                    ("sortButtonsQFrameAuthorButtonQFrame", 552),
                                                                    ("sortButtonsQFrameCategoryButtonQFrame", 726),
                                                                    ("sortButtonsQFrameDateAddedButtonQFrame", 950)]
                                                                )
        self.allSongsStickySortButtonsFrame.setStyleSheet("#sortButtonsQFrameAuthorButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "#sortButtonsQFrameCategoryButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "#sortButtonsQFrameDateAddedButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "#sortButtonsQFrameSongLengthButtonQFrame{\n"
                                                          "    padding-left: 25px;\n"
                                                          "}\n"
                                                          "SortButtonsQFrame QPushButton:hover{\n"
                                                          "    color: white;\n"
                                                          "}\n"
                                                          "SortButtonsQFrame QPushButton{\n"
                                                          "    font: 57 10pt \"Heebo Medium\";\n"
                                                          "}\n")
        self.verticalLayout.addWidget(self.allSongsStickySortButtonsFrame)
        self.verticalLayout_4.addWidget(self.frame_13)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)

        # list with all StickySortButtonsFrames inside frame_13's verticalLayout
        self.stickySortButtonsFrames = [self.likedSongsStickySortButtonsFrame, self.lastPlayedStickySortButtonsFrame,
                                        self.playlistStickySortButtonsFrame, self.authorStickySortButtonsFrame,
                                        self.categoryStickySortButtonsFrame, self.albumStickySortButtonsFrame,
                                        self.allSongsStickySortButtonsFrame]

        self.set_sticky_sort_button_frames_invisible()

    def set_sticky_sort_button_frames_invisible(self):
        """Set all frames inside frame_13's verticalLayout to invisible."""
        for frame in self.stickySortButtonsFrames:
            frame.setVisible(False)

    def adjust_elements_visibility(self, distance, play_button=True, page_name=True):
        """Make navbarPageName and navbarPlayButton visible when certain scroll threshold is reached.

        Parameters:
            distance(int): distance between navbar and certain point on the page
            play_button(bool): determines if navbarPlayButton should be made visible when certain point on the page is reached
            page_name(bool): determines if navbarPageName should be made visible when certain point on the page is reached
        """
        if distance > 0:
            self.navbarPlayButton.setVisible(False)
            self.navbarPageName.setVisible(False)
        else:
            if play_button:
                self.navbarPlayButton.setVisible(True)
            if page_name:
                self.navbarPageName.setVisible(True)

    def calculate_navbar_saturation(self, distance, offset):
        """Calculate the saturation of the Navbar depending on distance from certain point respective for each page.

        Parameters:
            distance(int): distance between navbar and certain point on the page
            offset(int): distance at which navbar should start to gain saturation
        """
        return (offset - distance) / offset * 255

    # TODO Fix Navbar not saturating properly when scrollbar gets clicked at bottom - use QOneShot
    def adjust_navbar_saturation(self, distance, offset):
        """Adjust the Navbar's saturation depending on distance from certain point respective for each page.

        Parameters:
            distance(int): distance between navbar and certain point on the page.
            offset(int): distance at which navbar should start to gain saturation
        """
        if offset >= distance >= 0:
            saturation = self.calculate_navbar_saturation(distance, offset)
            # workaround for issue when saturation is in range 1-1.5 the color turns black
            if 1.5 > saturation > 0:
                self.set_navbar_saturation(1.5)
                self.layer_frame.setStyleSheet(f"background-color: rgba(18, 18, 18, {1.5})")
            else:
                self.set_navbar_saturation(saturation)
                self.layer_frame.setStyleSheet(f"background-color: rgba(18, 18, 18, {saturation*0.45})")
        elif distance > offset:
            self.layer_frame.setStyleSheet("background-color: rgba(18, 18, 18, 0)")
            self.set_navbar_saturation(0)
        else:
            self.layer_frame.setStyleSheet("background-color: rgba(18, 18, 18, 0.45)")
            self.set_navbar_saturation(255)

    def set_navbar_saturation(self, saturation):
        """Set Navbar's background color saturation.

        Parameters:
            saturation(float): value to set Navbar's background color saturation to.
        """
        self.frame_2.setStyleSheet("#frame_2{\n"
                                   f"    background-color: rgba(255, 176, 85, {saturation});\n"
                                   "}\n"
                                   "#navbarUsernameButton{\n"
                                   "    background-color: rgb(24, 24, 24);\n"
                                   "    color: white;\n"
                                   "    border-radius: 16px;\n"
                                   "    font: 87 10.5pt Heebo Black;\n"
                                   "}\n"
                                   "#navbarUsernameButton:hover{\n"
                                   "    background-color: rgba(24, 24, 24, 0.75);\n"
                                   "}#navbarPlayButton{\n"
                                   "    border-radius: 20px;\n"
                                   "    background-color: rgb(245, 155, 125);\n"
                                   "}\n"
                                   "#navbarPlayButton:checked{\n"
                                   "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_pause_white_48dp.png);\n"
                                   "}\n"
                                   "#navbarPageName{\n"
                                   "    font: 87 17pt Heebo Black;\n"
                                   "    color: white;\n"
                                   "}\n"
                                   "#navbarMaximizeRestoreButton:checked{\n"
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
                                   "#navbarUsernameSmallButton:hover{\n"
                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_logout_white_48dp.png);\n"
                                   "}\n"
                                   "#navbarSynchronizeButton{\n"
                                   "    background-color: rgb(51,  51, 51);\n"
                                   "    border-radius: 16px;\n"
                                   "    border: 2px solid black;\n"
                                   "}\n"
                                   "#navbarSynchronizeButton:hover{\n"
                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_sync_alt_white_48dp.png);\n"
                                   "}\n")

    def adjust_sticky_sort_button_frame_visibility(self, distance):
        """Adjust the Navbar's sticky SortButtonFrame depending on distance from certain point respective for each page.

               Parameters:
                   distance(int): distance between navbar and certain point on the page.
               """
        if distance <= 0:
            self.frame_13.setVisible(True)
            self.setFixedHeight(101)
            # Call adjust_sort_buttons_qframe_sort_buttons_frames_visibility to prevent sort button frames having
            # wrong visibility when making frame_13 visible and before resizing window
            for frame in self.stickySortButtonsFrames:
                frame.adjust_sort_buttons_qframe_sort_buttons_frames_visibility()
        else:
            self.frame_13.setVisible(False)
            self.setFixedHeight(60)

    def adjust_sticky_sort_button_frame(self, index):
        """Select and make visible sortButtonFrame proper for mainPageStackedWidget's currently visible QWidget"""
        # now playing
        if index == 0:
            self.frame_13.setVisible(False)
            self.setFixedHeight(60)
        # categories
        elif index == 1:
            self.frame_13.setVisible(False)
            self.setFixedHeight(60)
        # liked songs
        elif index == 2:
            # set other sticky sort button visibility to false
            self.set_sticky_sort_button_frames_invisible()
            self.setFixedHeight(101)
            self.likedSongsStickySortButtonsFrame.setVisible(True)
        # last played
        elif index == 3:
            # set other sticky sort button visibility to false
            self.set_sticky_sort_button_frames_invisible()
            self.setFixedHeight(101)
            self.lastPlayedStickySortButtonsFrame.setVisible(True)
        # authors
        elif index == 4:
            self.frame_13.setVisible(False)
            self.setFixedHeight(60)
        # playlist
        elif index == 5:
            # set other sticky sort button visibility to false
            self.set_sticky_sort_button_frames_invisible()
            self.setFixedHeight(101)
            self.playlistStickySortButtonsFrame.setVisible(True)
        # author
        elif index == 6:
            # handled by adjust_authors_page_sticky_sort_button_frame
            pass
        # category
        elif index == 7:
            # handled by adjust_category_page_sticky_sort_button_frame
            pass
        # album
        elif index == 8:
            # set other sticky sort button visibility to false
            self.set_sticky_sort_button_frames_invisible()
            self.setFixedHeight(101)
            self.albumStickySortButtonsFrame.setVisible(True)
        # song queue
        elif index == 9:
            self.frame_13.setVisible(False)
            self.setFixedHeight(60)
        # albums
        elif index == 10:
            self.frame_13.setVisible(False)
            self.setFixedHeight(60)
        # all songs
        elif index == 11:
            # set other sticky sort button visibility to false
            self.set_sticky_sort_button_frames_invisible()
            self.setFixedHeight(101)
            self.allSongsStickySortButtonsFrame.setVisible(True)

    def adjust_authors_page_sticky_sort_button_frame(self, index):
        """Select and make visible sortButtonFrame proper for mainPageAuthorPageStackedWidget's currently visible
         QWidget
         """
        # songs
        if index == 0:
            # set other sticky sort button visibility to false
            self.set_sticky_sort_button_frames_invisible()
            self.setFixedHeight(101)
            self.authorStickySortButtonsFrame.setVisible(True)
        # albums, playlists
        else:
            self.frame_13.setVisible(False)
            self.setFixedHeight(60)

    def adjust_category_page_sticky_sort_button_frame(self, index):
        """Select and make visible sortButtonFrame proper for mainPageCategoryPageStackedWidget's currently visible
         QWidget
         """
        # songs
        if index == 0:
            # set other sticky sort button visibility to false
            self.set_sticky_sort_button_frames_invisible()
            self.setFixedHeight(101)
            self.categoryStickySortButtonsFrame.setVisible(True)
        # albums, playlists
        else:
            self.frame_13.setVisible(False)
            self.setFixedHeight(60)

