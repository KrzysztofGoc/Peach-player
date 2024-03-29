from PySide2 import QtCore, QtGui, QtWidgets

import app.src.classes.widgets.sort_buttons_qframe
from classes.resize_signal_scroll_area import ResizeSignalScrollArea
from classes.resize_signal_widget import ResizeSignalWidget
from classes.resize_signal_stacked_widget import ResizeSignalStackedWidget
from classes.navbar_frame import NavbarFrame
from classes.widgets.song_adder import SongAdder
from classes.widgets.sort_buttons_qframe import SortButtonsQFrame
from classes.layouts.flow_layout import FlowLayout

from classes.song_entry import SongEntry

import resources_peach_player

class Ui_MainWindow:
    def __init__(self, window):
        self.window = window
        self.load_fonts()
        self.setupUi(window)
        QtCore.QTimer.singleShot(10, self.adjust_all_sort_button_frames_visibility)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#leftMenuFrame QPushButton{\n"
                                 "    text-align: left;\n"
                                 "}\n"
                                 "QFrame#playerFrame{\n"
                                 "    background-color: rgb(18, 18, 18);\n"
                                 "    border-top: 1px solid;\n"
                                 "    border-top-color: rgb(40, 40, 40);\n"
                                 "}\n"
                                 "")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 500))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.centralWidgetLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.centralWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.centralWidgetLayout.setSpacing(0)
        self.centralWidgetLayout.setObjectName("centralWidgetLayout")
        self.centralStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.centralStackedWidget.setStyleSheet("border: none;")
        self.centralStackedWidget.setObjectName("centralStackedWidget")
        self.centralPageAppPage = QtWidgets.QWidget()
        self.centralPageAppPage.setStyleSheet("color: rgb(179, 179, 179);")
        self.centralPageAppPage.setObjectName("centralPageAppPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralPageAppPage)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName("mainLayout")
        self.playerFrame = QtWidgets.QFrame(self.centralPageAppPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerFrame.sizePolicy().hasHeightForWidth())
        self.playerFrame.setSizePolicy(sizePolicy)
        self.playerFrame.setMinimumSize(QtCore.QSize(800, 70))
        self.playerFrame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.playerFrame.setStyleSheet("QFrame#playerFrame{\n"
                                       "    border-top: 1px solid;\n"
                                       "    border-top-color: rgb(40, 40, 40);\n"
                                       "}")
        self.playerFrame.setLineWidth(0)
        self.playerFrame.setObjectName("playerFrame")
        self.playerMainLayout = QtWidgets.QHBoxLayout(self.playerFrame)
        self.playerMainLayout.setContentsMargins(0, 0, 0, 0)
        self.playerMainLayout.setSpacing(0)
        self.playerMainLayout.setObjectName("playerMainLayout")
        self.playerLeftPanel = QtWidgets.QFrame(self.playerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLeftPanel.sizePolicy().hasHeightForWidth())
        self.playerLeftPanel.setSizePolicy(sizePolicy)
        self.playerLeftPanel.setMinimumSize(QtCore.QSize(267, 70))
        self.playerLeftPanel.setMaximumSize(QtCore.QSize(480, 70))
        self.playerLeftPanel.setStyleSheet("font: 57 9pt \"Heebo Medium\";\n"
                                           "background-color: rgb(24, 24, 24);")
        self.playerLeftPanel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.playerLeftPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playerLeftPanel.setLineWidth(0)
        self.playerLeftPanel.setObjectName("playerLeftPanel")
        self.playerLeftPanelLayout = QtWidgets.QHBoxLayout(self.playerLeftPanel)
        self.playerLeftPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.playerLeftPanelLayout.setSpacing(0)
        self.playerLeftPanelLayout.setObjectName("playerLeftPanelLayout")
        self.songMiniatureFrame = QtWidgets.QFrame(self.playerLeftPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songMiniatureFrame.sizePolicy().hasHeightForWidth())
        self.songMiniatureFrame.setSizePolicy(sizePolicy)
        self.songMiniatureFrame.setMinimumSize(QtCore.QSize(70, 70))
        self.songMiniatureFrame.setMaximumSize(QtCore.QSize(70, 70))
        self.songMiniatureFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.songMiniatureFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.songMiniatureFrame.setObjectName("songMiniatureFrame")
        self.songMiniatureFrameLayout = QtWidgets.QGridLayout(self.songMiniatureFrame)
        self.songMiniatureFrameLayout.setContentsMargins(12, 12, 12, 12)
        self.songMiniatureFrameLayout.setSpacing(0)
        self.songMiniatureFrameLayout.setObjectName("songMiniatureFrameLayout")
        self.songMiniatureLabel = QtWidgets.QLabel(self.songMiniatureFrame)
        self.songMiniatureLabel.setText("")
        self.songMiniatureLabel.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/playlistCoverExample1.png"))
        self.songMiniatureLabel.setScaledContents(True)
        self.songMiniatureLabel.setObjectName("songMiniatureLabel")
        self.songMiniatureFrameLayout.addWidget(self.songMiniatureLabel, 0, 0, 1, 1)
        self.playerLeftPanelLayout.addWidget(self.songMiniatureFrame)
        self.songInfoLayout = QtWidgets.QVBoxLayout()
        self.songInfoLayout.setSpacing(0)
        self.songInfoLayout.setObjectName("songInfoLayout")
        self.playerLeftPanelsongNameLabel = QtWidgets.QLabel(self.playerLeftPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLeftPanelsongNameLabel.sizePolicy().hasHeightForWidth())
        self.playerLeftPanelsongNameLabel.setSizePolicy(sizePolicy)
        self.playerLeftPanelsongNameLabel.setMinimumSize(QtCore.QSize(211, 34))
        self.playerLeftPanelsongNameLabel.setMaximumSize(QtCore.QSize(16777215, 34))
        self.playerLeftPanelsongNameLabel.setStyleSheet("font: 57 10pt \"Heebo Medium\";\n"
                                                        "color: white;")
        self.playerLeftPanelsongNameLabel.setText("Aliquam maximus")
        self.playerLeftPanelsongNameLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.playerLeftPanelsongNameLabel.setObjectName("playerLeftPanelsongNameLabel")
        self.songInfoLayout.addWidget(self.playerLeftPanelsongNameLabel)
        self.frame_122 = QtWidgets.QFrame(self.playerLeftPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_122.sizePolicy().hasHeightForWidth())
        self.frame_122.setSizePolicy(sizePolicy)
        self.frame_122.setMinimumSize(QtCore.QSize(211, 34))
        self.frame_122.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setFamily("Heebo Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(7))
        self.frame_122.setFont(font)
        self.frame_122.setStyleSheet("QPushButton:hover{\n"
                                     "    text-decoration: underline;\n"
                                     "    color: white;\n"
                                     "}")
        self.frame_122.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_122.setObjectName("frame_122")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_122)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_122)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setText("Sed non,")
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_10.addWidget(self.pushButton_25, 0, QtCore.Qt.AlignTop)
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_122)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_26.setText("Cras interdum,")
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_10.addWidget(self.pushButton_26, 0, QtCore.Qt.AlignTop)
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_122)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setText("Etiam sed,")
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_10.addWidget(self.pushButton_27, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.songInfoLayout.addWidget(self.frame_122)
        self.playerLeftPanelLayout.addLayout(self.songInfoLayout)
        self.playerMainLayout.addWidget(self.playerLeftPanel)
        self.playerCentralPanel = QtWidgets.QFrame(self.playerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerCentralPanel.sizePolicy().hasHeightForWidth())
        self.playerCentralPanel.setSizePolicy(sizePolicy)
        self.playerCentralPanel.setMinimumSize(QtCore.QSize(267, 70))
        self.playerCentralPanel.setStyleSheet("QPushButton#playerShuffleButton:hover:!checked{\n"
                                              "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_shuffle_white_48dp.png);\n"
                                              "}\n"
                                              "QPushButton#playerShuffleButton:checked{ \n"
                                              "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_shuffle_peach_48dp.png);\n"
                                              "}\n"
                                              "QPushButton#playerShuffleButton:checked:hover{ \n"
                                              "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_shuffle_lightpeach_48dp.png);\n"
                                              "}\n"
                                              "\n"
                                              "#playerLoopButton::indicator{\n"
                                              "    width: 18px;\n"
                                              "    height: 18px;\n"
                                              "    image: url(:/icons/48x48/filled/icons/48x48/filled/baseline_loop_gray_48dp.png);\n"
                                              "}\n"
                                              "#playerLoopButton::indicator:hover:!checked:!indeterminate{\n"
                                              "    image: url(:/icons/48x48/filled/icons/48x48/filled/baseline_loop_white_48dp.png);\n"
                                              "}\n"
                                              "#playerLoopButton::indicator:indeterminate{\n"
                                              "    image: url(:/icons/48x48/filled/icons/48x48/filled/baseline_loop_peach_48dp.png);\n"
                                              "}\n"
                                              "#playerLoopButton::indicator:hover:indeterminate{\n"
                                              "    image: url(:/icons/48x48/filled/icons/48x48/filled/baseline_loop_lightpeach_48dp.png);\n"
                                              "}\n"
                                              "#playerLoopButton::indicator:checked{\n"
                                              "    image: url(:/icons/48x48/filled/icons/48x48/filled/baseline_loop_one_peach.PNG);\n"
                                              "}\n"
                                              "#playerLoopButton::indicator::hover:checked{\n"
                                              "    image: url(:/icons/48x48/filled/icons/48x48/filled/baseline_loop_one_light_peach.PNG);\n"
                                              "}\n"
                                              "\n"
                                              "\n"
                                              "QPushButton#playerNextButton:hover{\n"
                                              "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_skip_next_white_48dp.png);\n"
                                              "}\n"
                                              "QPushButton#playerNextButton:pressed{ \n"
                                              "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_skip_next_gray_48dp.png);\n"
                                              "}\n"
                                              "\n"
                                              "\n"
                                              "QPushButton#playerPreviousButton:hover{\n"
                                              "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_skip_previous_white_48dp.png);\n"
                                              "}\n"
                                              "QPushButton#playerPreviousButton:pressed{ \n"
                                              "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_skip_previous_gray_48dp.png);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton#playerPausePlayButton:checked{\n"
                                              "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_pause_circle_white_48dp.png);\n"
                                              "}\n"
                                              "\n"
                                              "\n"
                                              "QSlider#songTimeSlider::groove{\n"
                                              "    border: 1px solid;\n"
                                              "    height: 2px;\n"
                                              "}\n"
                                              "QSlider#songTimeSlider::add-page{\n"
                                              "    background-color: rgb(83, 83, 83);\n"
                                              "    border-radius: 2px;\n"
                                              "}\n"
                                              "QSlider#songTimeSlider::sub-page{\n"
                                              "    background-color: rgb(179, 179, 179);\n"
                                              "    border-radius: 2px;\n"
                                              "}\n"
                                              "\n"
                                              "QSlider#songTimeSlider::handle{\n"
                                              "    width: 12px;\n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              "    margin-top: -5px;\n"
                                              "    margin-bottom: -5px;\n"
                                              "    border-radius: 6px;\n"
                                              "}\n"
                                              "QSlider#songTimeSlider::groove:hover{\n"
                                              "    background-color: rgb(85, 170, 127);\n"
                                              "    border-radius: 2px;\n"
                                              "}\n"
                                              "QFrame#playerCentralPanel{\n"
                                              "    background-color: rgb(24, 24, 24);\n"
                                              "}\n"
                                              "\n"
                                              "")
        self.playerCentralPanel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.playerCentralPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playerCentralPanel.setLineWidth(0)
        self.playerCentralPanel.setObjectName("playerCentralPanel")
        self.playerCentralPanelLayout = QtWidgets.QVBoxLayout(self.playerCentralPanel)
        self.playerCentralPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.playerCentralPanelLayout.setSpacing(0)
        self.playerCentralPanelLayout.setObjectName("playerCentralPanelLayout")
        self.playerCentralButtonsLayout = QtWidgets.QHBoxLayout()
        self.playerCentralButtonsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.playerCentralButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.playerCentralButtonsLayout.setSpacing(0)
        self.playerCentralButtonsLayout.setObjectName("playerCentralButtonsLayout")
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.playerCentralButtonsLayout.addItem(spacerItem1)
        self.playerMiddleCentralButtonsLayout = QtWidgets.QFrame(self.playerCentralPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerMiddleCentralButtonsLayout.sizePolicy().hasHeightForWidth())
        self.playerMiddleCentralButtonsLayout.setSizePolicy(sizePolicy)
        self.playerMiddleCentralButtonsLayout.setMinimumSize(QtCore.QSize(265, 45))
        self.playerMiddleCentralButtonsLayout.setMaximumSize(QtCore.QSize(265, 45))
        self.playerMiddleCentralButtonsLayout.setStyleSheet("")
        self.playerMiddleCentralButtonsLayout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playerMiddleCentralButtonsLayout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playerMiddleCentralButtonsLayout.setObjectName("playerMiddleCentralButtonsLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.playerMiddleCentralButtonsLayout)
        self.horizontalLayout.setContentsMargins(25, 0, 25, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playerShuffleButton = QtWidgets.QPushButton(self.playerMiddleCentralButtonsLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerShuffleButton.sizePolicy().hasHeightForWidth())
        self.playerShuffleButton.setSizePolicy(sizePolicy)
        self.playerShuffleButton.setMinimumSize(QtCore.QSize(18, 18))
        self.playerShuffleButton.setMaximumSize(QtCore.QSize(18, 18))
        self.playerShuffleButton.setStyleSheet("border: None;")
        self.playerShuffleButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/baseline_shuffle_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playerShuffleButton.setIcon(icon)
        self.playerShuffleButton.setIconSize(QtCore.QSize(18, 18))
        self.playerShuffleButton.setCheckable(True)
        self.playerShuffleButton.setObjectName("playerShuffleButton")
        self.horizontalLayout.addWidget(self.playerShuffleButton, 0, QtCore.Qt.AlignLeft)
        self.playerPreviousButton = QtWidgets.QPushButton(self.playerMiddleCentralButtonsLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerPreviousButton.sizePolicy().hasHeightForWidth())
        self.playerPreviousButton.setSizePolicy(sizePolicy)
        self.playerPreviousButton.setMinimumSize(QtCore.QSize(18, 18))
        self.playerPreviousButton.setMaximumSize(QtCore.QSize(18, 18))
        self.playerPreviousButton.setStyleSheet("border: None;")
        self.playerPreviousButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/baseline_skip_previous_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playerPreviousButton.setIcon(icon1)
        self.playerPreviousButton.setIconSize(QtCore.QSize(18, 18))
        self.playerPreviousButton.setObjectName("playerPreviousButton")
        self.horizontalLayout.addWidget(self.playerPreviousButton, 0, QtCore.Qt.AlignLeft)
        self.playerPausePlayButton = QtWidgets.QPushButton(self.playerMiddleCentralButtonsLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerPausePlayButton.sizePolicy().hasHeightForWidth())
        self.playerPausePlayButton.setSizePolicy(sizePolicy)
        self.playerPausePlayButton.setMinimumSize(QtCore.QSize(36, 36))
        self.playerPausePlayButton.setMaximumSize(QtCore.QSize(36, 36))
        self.playerPausePlayButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playerPausePlayButton.setStyleSheet("border: None;\n"
                                                 "")
        self.playerPausePlayButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/baseline_play_circle_white_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playerPausePlayButton.setIcon(icon2)
        self.playerPausePlayButton.setIconSize(QtCore.QSize(36, 36))
        self.playerPausePlayButton.setCheckable(False)
        self.playerPausePlayButton.setObjectName("playerPausePlayButton")
        self.horizontalLayout.addWidget(self.playerPausePlayButton)
        self.playerNextButton = QtWidgets.QPushButton(self.playerMiddleCentralButtonsLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerNextButton.sizePolicy().hasHeightForWidth())
        self.playerNextButton.setSizePolicy(sizePolicy)
        self.playerNextButton.setMinimumSize(QtCore.QSize(18, 18))
        self.playerNextButton.setMaximumSize(QtCore.QSize(18, 18))
        self.playerNextButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.playerNextButton.setStyleSheet("border: None;")
        self.playerNextButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/baseline_skip_next_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playerNextButton.setIcon(icon3)
        self.playerNextButton.setIconSize(QtCore.QSize(18, 18))
        self.playerNextButton.setObjectName("playerNextButton")
        self.horizontalLayout.addWidget(self.playerNextButton, 0, QtCore.Qt.AlignRight)
        self.playerLoopButton = QtWidgets.QCheckBox(self.playerMiddleCentralButtonsLayout)
        self.playerLoopButton.setTristate(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerLoopButton.sizePolicy().hasHeightForWidth())
        self.playerLoopButton.setSizePolicy(sizePolicy)
        self.playerLoopButton.setMinimumSize(QtCore.QSize(18, 18))
        self.playerLoopButton.setMaximumSize(QtCore.QSize(18, 18))
        self.playerLoopButton.setStyleSheet("border: None;")
        self.playerLoopButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/baseline_loop_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playerLoopButton.setIcon(icon4)
        self.playerLoopButton.setIconSize(QtCore.QSize(18, 18))
        self.playerLoopButton.setCheckable(True)
        self.playerLoopButton.setObjectName("playerLoopButton")
        self.horizontalLayout.addWidget(self.playerLoopButton, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 3)
        self.playerCentralButtonsLayout.addWidget(self.playerMiddleCentralButtonsLayout)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.playerCentralButtonsLayout.addItem(spacerItem2)
        self.playerCentralPanelLayout.addLayout(self.playerCentralButtonsLayout)
        self.playerCentralBarLayout = QtWidgets.QHBoxLayout()
        self.playerCentralBarLayout.setContentsMargins(10, -1, 10, -1)
        self.playerCentralBarLayout.setSpacing(5)
        self.playerCentralBarLayout.setObjectName("playerCentralBarLayout")
        self.songCurrentTimestampLabel = QtWidgets.QLabel(self.playerCentralPanel)
        self.songCurrentTimestampLabel.setStyleSheet("font: 57 9pt \"Heebo Medium\";\n"
                                                     "background-color: rgb(24, 24, 24);")
        self.songCurrentTimestampLabel.setText("00:00")
        self.songCurrentTimestampLabel.setObjectName("songCurrentTimestampLabel")
        self.playerCentralBarLayout.addWidget(self.songCurrentTimestampLabel)
        self.songTimeSlider = QtWidgets.QSlider(self.playerCentralPanel)
        self.songTimeSlider.setMaximum(100)
        self.songTimeSlider.setSingleStep(1)
        self.songTimeSlider.setPageStep(1)
        self.songTimeSlider.setProperty("value", 1)
        self.songTimeSlider.setSliderPosition(0)
        self.songTimeSlider.setTracking(True)
        self.songTimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songTimeSlider.setInvertedAppearance(False)
        self.songTimeSlider.setInvertedControls(False)
        self.songTimeSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.songTimeSlider.setTickInterval(25)
        self.songTimeSlider.setObjectName("songTimeSlider")
        self.playerCentralBarLayout.addWidget(self.songTimeSlider)
        self.songMaximumTimestampLabel = QtWidgets.QLabel(self.playerCentralPanel)
        self.songMaximumTimestampLabel.setStyleSheet("font: 57 9pt \"Heebo Medium\";\n"
                                                     "background-color: rgb(24, 24, 24);")
        self.songMaximumTimestampLabel.setText("00:00")
        self.songMaximumTimestampLabel.setObjectName("songMaximumTimestampLabel")
        self.playerCentralBarLayout.addWidget(self.songMaximumTimestampLabel)
        self.playerCentralPanelLayout.addLayout(self.playerCentralBarLayout)
        self.playerCentralPanelLayout.setStretch(0, 2)
        self.playerCentralPanelLayout.setStretch(1, 1)
        self.playerMainLayout.addWidget(self.playerCentralPanel)
        self.playerRightPanel = QtWidgets.QFrame(self.playerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerRightPanel.sizePolicy().hasHeightForWidth())
        self.playerRightPanel.setSizePolicy(sizePolicy)
        self.playerRightPanel.setMinimumSize(QtCore.QSize(267, 70))
        self.playerRightPanel.setMaximumSize(QtCore.QSize(480, 16777215))
        self.playerRightPanel.setStyleSheet("QPushButton#bottomPlayerQueueButton:hover:!checked{\n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_queue_music_white_48dp.png);\n"
                                            "}\n"
                                            "QPushButton#bottomPlayerQueueButton:checked{\n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_queue_music_peach_48dp.png);\n"
                                            "}\n"
                                            "QPushButton#bottomPlayerQueueButton:hover:checked{\n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_queue_music_lightpeach_48dp.png);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "QPushButton#bottomPlayerMuteButton:hover:!checked{\n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_volume_low_white_48dp.png);\n"
                                            "}\n"
                                            "QPushButton#bottomPlayerMuteButton:pressed:!checked{\n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_volume_low_gray_48dp.png);\n"
                                            "}\n"
                                            "QPushButton#bottomPlayerMuteButton:checked{ \n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_volume_off_gray_48dp.png);\n"
                                            "}\n"
                                            "QPushButton#bottomPlayerMuteButton:checked:hover{  \n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_volume_off_white_48dp.png);\n"
                                            "}\n"
                                            "QPushButton#bottomPlayerMuteButton:checked:pressed{ \n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_volume_off_gray_48dp.png);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "QSlider#volumeSlider::groove{\n"
                                            "    border: 1px solid;\n"
                                            "    height: 2px;\n"
                                            "}\n"
                                            "QSlider#volumeSlider::add-page{\n"
                                            "    background-color: rgb(83, 83, 83);\n"
                                            "    border-radius: 2px;\n"
                                            "}\n"
                                            "QSlider#volumeSlider::sub-page{\n"
                                            "    background-color: rgb(179, 179, 179);\n"
                                            "    border-radius: 2px;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider#volumeSlider::handle{\n"
                                            "    width: 12px;\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            "    margin-top: -5px;\n"
                                            "    margin-bottom: -5px;\n"
                                            "    border-radius: 6px;\n"
                                            "}\n"
                                            "QSlider#volumeSlider::sub-page:hover{\n"
                                            "    background-color: rgb(85, 170, 127);\n"
                                            "    border-radius: 2px;\n"
                                            "}\n"
                                            "QFrame#playerRightPanel{\n"
                                            "    background-color: rgb(24, 24, 24);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")
        self.playerRightPanel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.playerRightPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playerRightPanel.setLineWidth(0)
        self.playerRightPanel.setObjectName("playerRightPanel")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.playerRightPanel)
        self.horizontalLayout_2.setContentsMargins(24, 0, 25, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(0, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.bottomPlayerQueueButton = QtWidgets.QPushButton(self.playerRightPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomPlayerQueueButton.sizePolicy().hasHeightForWidth())
        self.bottomPlayerQueueButton.setSizePolicy(sizePolicy)
        self.bottomPlayerQueueButton.setMinimumSize(QtCore.QSize(24, 24))
        self.bottomPlayerQueueButton.setMaximumSize(QtCore.QSize(24, 24))
        self.bottomPlayerQueueButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/baseline_queue_music_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bottomPlayerQueueButton.setIcon(icon5)
        self.bottomPlayerQueueButton.setIconSize(QtCore.QSize(24, 24))
        self.bottomPlayerQueueButton.setCheckable(True)
        self.bottomPlayerQueueButton.setObjectName("bottomPlayerQueueButton")
        self.horizontalLayout_2.addWidget(self.bottomPlayerQueueButton)
        self.bottomPlayerMuteButton = QtWidgets.QPushButton(self.playerRightPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomPlayerMuteButton.sizePolicy().hasHeightForWidth())
        self.bottomPlayerMuteButton.setSizePolicy(sizePolicy)
        self.bottomPlayerMuteButton.setMinimumSize(QtCore.QSize(24, 24))
        self.bottomPlayerMuteButton.setMaximumSize(QtCore.QSize(24, 24))
        self.bottomPlayerMuteButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.bottomPlayerMuteButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/baseline_volume_low_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bottomPlayerMuteButton.setIcon(icon6)
        self.bottomPlayerMuteButton.setIconSize(QtCore.QSize(24, 24))
        self.bottomPlayerMuteButton.setCheckable(True)
        self.bottomPlayerMuteButton.setObjectName("bottomPlayerMuteButton")
        self.horizontalLayout_2.addWidget(self.bottomPlayerMuteButton)
        self.volumeSlider = QtWidgets.QSlider(self.playerRightPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy)
        self.volumeSlider.setMinimumSize(QtCore.QSize(90, 0))
        self.volumeSlider.setProperty("value", 5)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.volumeSlider.setObjectName("volumeSlider")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setSingleStep(1)
        self.horizontalLayout_2.addWidget(self.volumeSlider)
        self.playerMainLayout.addWidget(self.playerRightPanel)
        self.mainLayout.addWidget(self.playerFrame, 1, 0, 1, 3)
        self.mainPageStackedWidget = ResizeSignalStackedWidget(self.centralPageAppPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageStackedWidget.sizePolicy().hasHeightForWidth())
        self.mainPageStackedWidget.setSizePolicy(sizePolicy)
        self.mainPageStackedWidget.setMinimumSize(QtCore.QSize(600, 530))
        self.mainPageStackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPageStackedWidget.setStyleSheet("QScrollBar:vertical {\n"
                                                 "    width: 12px;\n"
                                                 "    margin-top: 42px;\n"
                                                 "    background: transparent;\n"
                                                 "}\n"
                                                 "QComboBox QScrollBar:vertical{\n"
                                                 "    width: 16px;\n"
                                                 "    margin-top: 0px;\n"
                                                 "    background: transparent;\n"
                                                 "}\n"
                                                 "QScrollBar::handle:vertical{\n"
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
                                                 "}\n")
        self.mainPageStackedWidget.setLineWidth(0)
        self.mainPageStackedWidget.setObjectName("mainPageStackedWidget")
        self.mainPageNowPlaying = ResizeSignalWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageNowPlaying.sizePolicy().hasHeightForWidth())
        self.mainPageNowPlaying.setSizePolicy(sizePolicy)
        self.mainPageNowPlaying.setMinimumSize(QtCore.QSize(600, 528))
        self.mainPageNowPlaying.setStyleSheet("QWidget#mainPageNowPlaying{\n"
                                              "    background-color: rgb(18, 18, 18);\n"
                                              "}")
        self.mainPageNowPlaying.setObjectName("mainPageNowPlaying")
        self.mainPageNowPlayingBackgroundLabel = QtWidgets.QLabel(self.mainPageNowPlaying)
        self.blurEffect = QtWidgets.QGraphicsBlurEffect()
        self.blurEffect.setBlurHints(QtWidgets.QGraphicsBlurEffect.QualityHint)
        self.blurEffect.setBlurRadius(60)
        self.mainPageNowPlayingBackgroundLabel.setGraphicsEffect(self.blurEffect)
        self.mainPageNowPlayingBackgroundLabel.setGeometry(QtCore.QRect(0, 0, 600, 530))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.mainPageNowPlaying.setStyleSheet("background-color: red;")
        sizePolicy.setHeightForWidth(self.mainPageNowPlayingBackgroundLabel.sizePolicy().hasHeightForWidth())
        self.mainPageNowPlayingBackgroundLabel.setSizePolicy(sizePolicy)
        self.mainPageNowPlayingBackgroundLabel.setMinimumSize(QtCore.QSize(600, 530))
        self.mainPageNowPlayingBackgroundLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPageNowPlayingBackgroundLabel.setText("")
        self.mainPageNowPlayingBackgroundLabel.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/playlistCoverExample1.png"))
        self.mainPageNowPlayingBackgroundLabel.setObjectName("mainPageNowPlayingBackgroundLabel")
        self.frame_20 = QtWidgets.QFrame(self.mainPageNowPlaying)
        self.frame_20.setGeometry(QtCore.QRect(0, 0, 600, 530))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMinimumSize(QtCore.QSize(600, 530))
        self.frame_20.setStyleSheet("background-color: None;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_21 = QtWidgets.QFrame(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setMinimumSize(QtCore.QSize(450, 250))
        self.frame_21.setStyleSheet("")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.mainPageNowPlayingSongVisualizationFrame = QtWidgets.QFrame(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageNowPlayingSongVisualizationFrame.sizePolicy().hasHeightForWidth())
        self.mainPageNowPlayingSongVisualizationFrame.setSizePolicy(sizePolicy)
        self.mainPageNowPlayingSongVisualizationFrame.setMinimumSize(QtCore.QSize(460, 83))
        self.mainPageNowPlayingSongVisualizationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPageNowPlayingSongVisualizationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPageNowPlayingSongVisualizationFrame.setObjectName("mainPageNowPlayingSongVisualizationFrame")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.mainPageNowPlayingSongVisualizationFrame)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalSlider = QtWidgets.QSlider(self.mainPageNowPlayingSongVisualizationFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_29.addWidget(self.horizontalSlider)
        self.verticalLayout_20.addWidget(self.mainPageNowPlayingSongVisualizationFrame)
        self.frame_25 = QtWidgets.QFrame(self.frame_21)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_30 = QtWidgets.QFrame(self.frame_25)
        self.frame_30.setMinimumSize(QtCore.QSize(167, 167))
        self.frame_30.setMaximumSize(QtCore.QSize(167, 167))
        self.frame_30.setStyleSheet("")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.mainPageNowPlayingSongMiniatureQLabel = QtWidgets.QLabel(self.frame_30)
        self.mainPageNowPlayingSongMiniatureQLabel.setMinimumSize(QtCore.QSize(149, 149))
        self.mainPageNowPlayingSongMiniatureQLabel.setMaximumSize(QtCore.QSize(149, 149))
        self.mainPageNowPlayingSongMiniatureQLabel.setStyleSheet("")
        self.mainPageNowPlayingSongMiniatureQLabel.setText("")
        self.mainPageNowPlayingSongMiniatureQLabel.setPixmap(QtGui.QPixmap("C:/Users/Krzysztof/Desktop/tlo.jpg"))
        self.mainPageNowPlayingSongMiniatureQLabel.setScaledContents(True)
        self.mainPageNowPlayingSongMiniatureQLabel.setObjectName("mainPageNowPlayingSongMiniatureQLabel")
        self.verticalLayout_28.addWidget(self.mainPageNowPlayingSongMiniatureQLabel, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_6.addWidget(self.frame_30)
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QtCore.QSize(142, 167))
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_22.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.mainPageNowPlayingSongNameLabel = QtWidgets.QLabel(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageNowPlayingSongNameLabel.sizePolicy().hasHeightForWidth())
        self.mainPageNowPlayingSongNameLabel.setSizePolicy(sizePolicy)
        self.mainPageNowPlayingSongNameLabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageNowPlayingSongNameLabel.setFont(font)
        self.mainPageNowPlayingSongNameLabel.setStyleSheet("color: white;\n"
                                                           "font: 87 18pt \"Heebo Black\";")
        self.mainPageNowPlayingSongNameLabel.setText("Example Song Name")
        self.mainPageNowPlayingSongNameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mainPageNowPlayingSongNameLabel.setWordWrap(False)
        self.mainPageNowPlayingSongNameLabel.setObjectName("mainPageNowPlayingSongNameLabel")
        self.verticalLayout_22.addWidget(self.mainPageNowPlayingSongNameLabel, 0, QtCore.Qt.AlignBottom)
        self.mainPageNowPlayingAuthorNameLabel = QtWidgets.QPushButton(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageNowPlayingAuthorNameLabel.sizePolicy().hasHeightForWidth())
        self.mainPageNowPlayingAuthorNameLabel.setSizePolicy(sizePolicy)
        self.mainPageNowPlayingAuthorNameLabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Heebo Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(QtGui.QFont.Weight(7))
        font.setStrikeOut(False)
        self.mainPageNowPlayingAuthorNameLabel.setFont(font)
        self.mainPageNowPlayingAuthorNameLabel.setStyleSheet("color: white;\n"
                                                             "font: 57 9pt \"Heebo Medium\";")
        self.mainPageNowPlayingAuthorNameLabel.setText("Example Author Name")
        self.mainPageNowPlayingAuthorNameLabel.setObjectName("mainPageNowPlayingAuthorNameLabel")
        self.verticalLayout_22.addWidget(self.mainPageNowPlayingAuthorNameLabel, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_6.addWidget(self.frame_26)
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_20.addWidget(self.frame_25)
        self.verticalLayout_20.setStretch(0, 1)
        self.verticalLayout_20.setStretch(1, 2)
        self.gridLayout_8.addWidget(self.frame_21, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.mainPageStackedWidget.addWidget(self.mainPageNowPlaying)
        self.mainPageCategories = QtWidgets.QWidget()
        self.mainPageCategories.setStyleSheet("#frame_139{\n"
                                              "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "#scrollAreaWidgetContents_9{\n"
                                              "    background-color: rgb(18, 18, 18);\n"
                                              "}\n"
                                              "CategoryEntry, AdderEntry{\n"
                                              "    background-color: rgb(24, 24, 24);\n"
                                              "    border-radius: 4px;\n"
                                              "}\n"
                                              "CategoryEntry:hover, AdderEntry:hover{\n"
                                              "    background-color: rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "QFrame#frame_139 QPushButton{\n"
                                              "    padding-left: 17px;\n"
                                              "    padding-right: 17px;\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "    border-bottom: 2px solid transparent;\n"
                                              "}\n"
                                              "QFrame#frame_139 QPushButton:hover:!checked{\n"
                                              "    color: white;\n"
                                              "}\n"
                                              "QFrame#frame_139 QPushButton:checked{\n"
                                              "    border-bottom: 2px solid rgb(247, 178, 158);\n"
                                              "    color: white;\n"
                                              "}\n")
        self.mainPageCategories.setObjectName("mainPageCategories")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.mainPageCategories)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_67 = QtWidgets.QFrame(self.mainPageCategories)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_67.sizePolicy().hasHeightForWidth())
        self.frame_67.setSizePolicy(sizePolicy)
        self.frame_67.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.verticalLayout_75 = QtWidgets.QVBoxLayout(self.frame_67)
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName("verticalLayout_75")
        self.scrollArea_9 = ResizeSignalScrollArea(self.frame_67)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_9.sizePolicy().hasHeightForWidth())
        self.scrollArea_9.setSizePolicy(sizePolicy)
        self.scrollArea_9.setMinimumSize(QtCore.QSize(585, 493))
        self.scrollArea_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea_9.setFont(font)
        self.scrollArea_9.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.scrollArea_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 900, 817))
        self.scrollAreaWidgetContents_9.setStyleSheet("")
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.verticalLayout_76 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName("verticalLayout_76")
        self.frame_51 = QtWidgets.QFrame(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy)
        self.frame_51.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_51.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_51.setStyleSheet("")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_77 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_77.setContentsMargins(32, 60, 32, 0)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName("verticalLayout_77")
        self.frame_68 = QtWidgets.QFrame(self.frame_51)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_68.sizePolicy().hasHeightForWidth())
        self.frame_68.setSizePolicy(sizePolicy)
        self.frame_68.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_68.setMaximumSize(QtCore.QSize(16777215, 132))
        self.frame_68.setStyleSheet("")
        self.frame_68.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_68.setObjectName("frame_68")
        self.verticalLayout_78 = QtWidgets.QVBoxLayout(self.frame_68)
        self.verticalLayout_78.setContentsMargins(0, 27, 0, 18)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName("verticalLayout_78")
        self.label_115 = QtWidgets.QLabel(self.frame_68)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy)
        self.label_115.setMinimumSize(QtCore.QSize(0, 52))
        self.label_115.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_115.setFont(font)
        self.label_115.setStyleSheet("color: white;\n"
                                     "font: 87 17pt \"Heebo Black\";")
        self.label_115.setText("Categories")
        self.label_115.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_115.setObjectName("label_115")
        self.verticalLayout_78.addWidget(self.label_115)
        self.verticalLayout_77.addWidget(self.frame_68)
        self.verticalLayout_76.addWidget(self.frame_51)
        self.frame_46 = QtWidgets.QFrame(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy)
        self.frame_46.setStyleSheet("")
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.verticalLayout_79 = QtWidgets.QVBoxLayout(self.frame_46)
        self.verticalLayout_79.setContentsMargins(32, 0, 32, 24)
        self.verticalLayout_79.setSpacing(24)
        self.verticalLayout_79.setObjectName("verticalLayout_79")
        self.frame_139 = QtWidgets.QFrame(self.frame_46)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_139.sizePolicy().hasHeightForWidth())
        self.frame_139.setSizePolicy(sizePolicy)
        self.frame_139.setMinimumSize(QtCore.QSize(0, 33))
        self.frame_139.setStyleSheet("")
        self.frame_139.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_139.setObjectName("frame_139")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_139)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(24)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.mainPageCategoriesRecentlyAddedSortQPushButton = QtWidgets.QPushButton(self.frame_139)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageCategoriesRecentlyAddedSortQPushButton.sizePolicy().hasHeightForWidth())
        self.mainPageCategoriesRecentlyAddedSortQPushButton.setSizePolicy(sizePolicy)
        self.mainPageCategoriesRecentlyAddedSortQPushButton.setMinimumSize(QtCore.QSize(0, 33))
        self.mainPageCategoriesRecentlyAddedSortQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageCategoriesRecentlyAddedSortQPushButton.setText("Recently added")
        self.mainPageCategoriesRecentlyAddedSortQPushButton.setCheckable(True)
        self.mainPageCategoriesRecentlyAddedSortQPushButton.setChecked(True)
        self.mainPageCategoriesRecentlyAddedSortQPushButton.setAutoExclusive(True)
        self.mainPageCategoriesRecentlyAddedSortQPushButton.setObjectName("mainPageCategoriesRecentlyAddedSortQPushButton")
        self.horizontalLayout_13.addWidget(self.mainPageCategoriesRecentlyAddedSortQPushButton)
        self.mainPageCategoriesAlphabeticallySortQPushButton = QtWidgets.QPushButton(self.frame_139)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageCategoriesAlphabeticallySortQPushButton.sizePolicy().hasHeightForWidth())
        self.mainPageCategoriesAlphabeticallySortQPushButton.setSizePolicy(sizePolicy)
        self.mainPageCategoriesAlphabeticallySortQPushButton.setMinimumSize(QtCore.QSize(0, 33))
        self.mainPageCategoriesAlphabeticallySortQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageCategoriesAlphabeticallySortQPushButton.setStyleSheet("")
        self.mainPageCategoriesAlphabeticallySortQPushButton.setText("Alphabetically")
        self.mainPageCategoriesAlphabeticallySortQPushButton.setCheckable(True)
        self.mainPageCategoriesAlphabeticallySortQPushButton.setAutoExclusive(True)
        self.mainPageCategoriesAlphabeticallySortQPushButton.setObjectName("mainPageCategoriesAlphabeticallySortQPushButton")
        self.horizontalLayout_13.addWidget(self.mainPageCategoriesAlphabeticallySortQPushButton)
        self.mainPageCategoriesMostListenedSortQPushButton = QtWidgets.QPushButton(self.frame_139)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageCategoriesMostListenedSortQPushButton.sizePolicy().hasHeightForWidth())
        self.mainPageCategoriesMostListenedSortQPushButton.setSizePolicy(sizePolicy)
        self.mainPageCategoriesMostListenedSortQPushButton.setMinimumSize(QtCore.QSize(0, 33))
        self.mainPageCategoriesMostListenedSortQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageCategoriesMostListenedSortQPushButton.setText("Most listened")
        self.mainPageCategoriesMostListenedSortQPushButton.setCheckable(True)
        self.mainPageCategoriesMostListenedSortQPushButton.setAutoExclusive(True)
        self.mainPageCategoriesMostListenedSortQPushButton.setObjectName("mainPageCategoriesMostListenedSortQPushButton")
        self.horizontalLayout_13.addWidget(self.mainPageCategoriesMostListenedSortQPushButton)
        spacerItem5 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout_79.addWidget(self.frame_139)
        self.frame_54 = QtWidgets.QFrame(self.frame_46)
        self.frame_54.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_54.setStyleSheet("")
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.mainPageCategoriesCategoriesEntriesQFlowLayout = FlowLayout(self.frame_54)
        self.mainPageCategoriesCategoriesEntriesQFlowLayout.setContentsMargins(0, 24, 0, 24)
        self.mainPageCategoriesCategoriesEntriesQFlowLayout.setSpacing(24)
        self.mainPageCategoriesCategoriesEntriesQFlowLayout.setObjectName("mainPageCategoriesCategoriesEntriesQFlowLayout")
        self.verticalLayout_79.addWidget(self.frame_54)
        self.verticalLayout_76.addWidget(self.frame_46)
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayout_75.addWidget(self.scrollArea_9)
        self.verticalLayout_30.addWidget(self.frame_67)
        self.mainPageStackedWidget.addWidget(self.mainPageCategories)
        self.mainPageLikedSongs = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageLikedSongs.sizePolicy().hasHeightForWidth())
        self.mainPageLikedSongs.setSizePolicy(sizePolicy)
        self.mainPageLikedSongs.setMinimumSize(QtCore.QSize(600, 530))
        self.mainPageLikedSongs.setStyleSheet("QWidget#widget_8{\n"
                                              "    background-color: qlineargradient( x1:0 y1:0,\n"
                                              "     x2:0 y2:0.63,\n"
                                              "     stop:0 rgb(255, 176, 85),\n"
                                              "    stop:1 rgb(18, 18, 18));\n"
                                              "}\n"
                                              "QFrame#frame_22{\n"
                                              "    background-color: rgba(18, 18, 18, 0.15);\n"
                                              "}\n"
                                              "SortButtonsQFrame{\n"
                                              "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "SortButtonsQFrame QPushButton:hover{\n"
                                              "    color: white;\n"
                                              "}\n"
                                              "SortButtonsQFrame QPushButton{\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "}\n"
                                              "QFrame#frame_63{\n"
                                              "    background-color: rgba(18, 18, 18, 0.15);\n"
                                              "}\n"
                                              "\n"
                                              "SongEntry{\n"
                                              "    border-radius: 4px;\n"
                                              "}\n"
                                              "SongEntry:hover{\n"
                                              "    background-color: rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "SongEntry QPushButton{\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "SongEntry QLabel{\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "    background-color: none;\n"
                                              "}\n"
                                              "SongEntry QPushButton:hover{\n"
                                              "    text-decoration: underline;\n"
                                              "    color: white;\n"
                                              "}\n")
        self.mainPageLikedSongs.setObjectName("mainPageLikedSongs")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.mainPageLikedSongs)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_11 = QtWidgets.QFrame(self.mainPageLikedSongs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QtCore.QSize(600, 482))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.scrollArea_4 = ResizeSignalScrollArea(self.frame_11)
        self.scrollArea_4.setStyleSheet("")
        self.scrollArea_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.widget_8 = QtWidgets.QWidget()
        self.widget_8.setGeometry(QtCore.QRect(0, -120, 1424, 694))
        self.widget_8.setStyleSheet("")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.mainPageLikedSongsSongHeaderFrame = QtWidgets.QFrame(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageLikedSongsSongHeaderFrame.sizePolicy().hasHeightForWidth())
        self.mainPageLikedSongsSongHeaderFrame.setSizePolicy(sizePolicy)
        self.mainPageLikedSongsSongHeaderFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.mainPageLikedSongsSongHeaderFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPageLikedSongsSongHeaderFrame.setStyleSheet("")
        self.mainPageLikedSongsSongHeaderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPageLikedSongsSongHeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPageLikedSongsSongHeaderFrame.setObjectName("mainPageLikedSongsSongHeaderFrame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.mainPageLikedSongsSongHeaderFrame)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_15 = QtWidgets.QFrame(self.mainPageLikedSongsSongHeaderFrame)
        self.frame_15.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.frame_15.setStyleSheet("")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setContentsMargins(32, 84, 32, 24)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.likedSongsMiniatureLabel = QtWidgets.QLabel(self.frame_15)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(250)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 192))

        self.likedSongsMiniatureLabel.setGraphicsEffect(self.shadow)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.likedSongsMiniatureLabel.sizePolicy().hasHeightForWidth())
        self.likedSongsMiniatureLabel.setSizePolicy(sizePolicy)
        self.likedSongsMiniatureLabel.setMinimumSize(QtCore.QSize(232, 232))
        self.likedSongsMiniatureLabel.setMaximumSize(QtCore.QSize(232, 232))
        self.likedSongsMiniatureLabel.setStyleSheet("")
        self.likedSongsMiniatureLabel.setText("")
        self.likedSongsMiniatureLabel.setPixmap(QtGui.QPixmap(":/minatures/icons/likedSongsMinature.png"))
        self.likedSongsMiniatureLabel.setScaledContents(True)
        self.likedSongsMiniatureLabel.setObjectName("likedSongsMiniatureLabel")
        self.horizontalLayout_16.addWidget(self.likedSongsMiniatureLabel)
        self.frame_18 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_18.setStyleSheet("")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_111 = QtWidgets.QLabel(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy)
        self.label_111.setMinimumSize(QtCore.QSize(0, 0))
        self.label_111.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_111.setFont(font)
        self.label_111.setStyleSheet("font: 87 9pt \"Heebo Black\";\n"
                                     "color: white;\n"
                                     "padding-top: -6px;")
        self.label_111.setText("PLAYLIST")
        self.label_111.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_111.setObjectName("label_111")
        self.verticalLayout_21.addWidget(self.label_111)
        self.label_22 = QtWidgets.QLabel(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(0, 52))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("font: 87 38pt \"Heebo Black\";\n"
                                    "color: white;\n"
                                    "")
        self.label_22.setText("Liked songs")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_22.setWordWrap(False)
        self.label_22.setIndent(-1)
        self.label_22.setOpenExternalLinks(False)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_21.addWidget(self.label_22)
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_19.setStyleSheet("")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setSpacing(4)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.mainPageLikedSongsNumberOfSongsQLabel = QtWidgets.QLabel(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageLikedSongsNumberOfSongsQLabel.sizePolicy().hasHeightForWidth())
        self.mainPageLikedSongsNumberOfSongsQLabel.setSizePolicy(sizePolicy)
        self.mainPageLikedSongsNumberOfSongsQLabel.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.mainPageLikedSongsNumberOfSongsQLabel.setText("3 Songs,")
        self.mainPageLikedSongsNumberOfSongsQLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mainPageLikedSongsNumberOfSongsQLabel.setObjectName("mainPageLikedSongsNumberOfSongsQLabel")
        self.horizontalLayout_31.addWidget(self.mainPageLikedSongsNumberOfSongsQLabel)
        self.mainPageLikedSongsLengthOfPlaylistQLabel = QtWidgets.QLabel(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageLikedSongsLengthOfPlaylistQLabel.sizePolicy().hasHeightForWidth())
        self.mainPageLikedSongsLengthOfPlaylistQLabel.setSizePolicy(sizePolicy)
        self.mainPageLikedSongsLengthOfPlaylistQLabel.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.mainPageLikedSongsLengthOfPlaylistQLabel.setText("0 h. 13 min")
        self.mainPageLikedSongsLengthOfPlaylistQLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mainPageLikedSongsLengthOfPlaylistQLabel.setObjectName("mainPageLikedSongsLengthOfPlaylistQLabel")
        self.horizontalLayout_31.addWidget(self.mainPageLikedSongsLengthOfPlaylistQLabel)
        spacerItem9 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem9)
        self.verticalLayout_21.addWidget(self.frame_19)
        self.horizontalLayout_16.addWidget(self.frame_18, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_19.addWidget(self.frame_15)
        self.frame_22 = QtWidgets.QFrame(self.mainPageLikedSongsSongHeaderFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_22.setStyleSheet("")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_27.setContentsMargins(32, 24, 32, 0)
        self.verticalLayout_27.setSpacing(24)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.likedSongsPlayPauseButton = QtWidgets.QPushButton(self.frame_22)
        self.likedSongsPlayPauseButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.likedSongsPlayPauseButton.sizePolicy().hasHeightForWidth())
        self.likedSongsPlayPauseButton.setSizePolicy(sizePolicy)
        self.likedSongsPlayPauseButton.setMinimumSize(QtCore.QSize(56, 56))
        self.likedSongsPlayPauseButton.setMaximumSize(QtCore.QSize(56, 56))
        self.likedSongsPlayPauseButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                     "border-radius: 28px;\n"
                                                     "text-align: center;\n"
                                                     "font: 87 9pt \"Heebo Black\";\n"
                                                     "background-color: rgb(255, 176, 85);\n"
                                                     "")
        self.likedSongsPlayPauseButton.setText("")

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_play_arrow_white_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.likedSongsPlayPauseButton.setIcon(icon7)
        self.likedSongsPlayPauseButton.setIconSize(QtCore.QSize(24, 24))
        self.likedSongsPlayPauseButton.setCheckable(False)
        self.likedSongsPlayPauseButton.setObjectName("likedSongsPlayPauseButton")
        self.verticalLayout_27.addWidget(self.likedSongsPlayPauseButton)



        self.LikedSongsSortButtonsQFrame = SortButtonsQFrame(parent=self.frame_22,
                                                             frame_structure={"sortButtonsQFrameTitleButtonQFrame": True,
                                                                              "sortButtonsQFrameAuthorButtonQFrame": True,
                                                                              "sortButtonsQFrameCategoryButtonQFrame": True,
                                                                              "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                                              "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                             visibility_changing_sort_buttons_elements=[("sortButtonsQFrameAuthorButtonQFrame", 552),
                                                                                                        ("sortButtonsQFrameCategoryButtonQFrame", 726),
                                                                                                        ("sortButtonsQFrameDateAddedButtonQFrame", 950)]
                                                             )
        self.LikedSongsSortButtonsQFrame.setObjectName("LikedSongsSortButtonsQFrame")
        self.verticalLayout_27.addWidget(self.LikedSongsSortButtonsQFrame)

        self.verticalLayout_19.addWidget(self.frame_22)
        self.verticalLayout_18.addWidget(self.mainPageLikedSongsSongHeaderFrame)
        self.frame_63 = QtWidgets.QFrame(self.widget_8)
        self.frame_63.setStyleSheet("")
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.mainPageLikedSongsSongListQVBoxLayout = QtWidgets.QVBoxLayout(self.frame_63)
        self.mainPageLikedSongsSongListQVBoxLayout.setContentsMargins(32, 9, 32, 32)
        self.mainPageLikedSongsSongListQVBoxLayout.setSpacing(0)
        self.mainPageLikedSongsSongListQVBoxLayout.setObjectName("mainPageLikedSongsSongListQVBoxLayout")
        self.verticalLayout_18.addWidget(self.frame_63)
        self.scrollArea_4.setWidget(self.widget_8)
        self.verticalLayout_17.addWidget(self.scrollArea_4)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.mainPageStackedWidget.addWidget(self.mainPageLikedSongs)
        self.mainPageLastPlayed = QtWidgets.QWidget()
        self.mainPageLastPlayed.setStyleSheet("SongEntry{\n"
                                              "    border-radius: 4px;\n"
                                              "}\n"
                                              "SongEntry:hover{\n"
                                              "    background-color: rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "SongEntry QPushButton{\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "}\n"
                                              "SongEntry QLabel{\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "    background-color: none;\n"
                                              "}\n"
                                              "SongEntry QPushButton:hover{\n"
                                              "    text-decoration: underline;\n"
                                              "    color: white;\n"
                                              "}\n"
                                              "SortButtonsQFrame{\n"
                                              "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "SortButtonsQFrame QPushButton:hover{\n"
                                              "    color: white;\n"
                                              "}\n"
                                              "SortButtonsQFrame QPushButton{\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "}\n"
                                              "#scrollAreaWidgetContents_2{\n"
                                              "    background-color: rgb(18, 18, 18);\n"
                                              "}\n")
        self.mainPageLastPlayed.setObjectName("mainPageLastPlayed")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.mainPageLastPlayed)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.frame_50 = QtWidgets.QFrame(self.mainPageLastPlayed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy)
        self.frame_50.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_50.setStyleSheet("")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_50)
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.scrollArea_10 = ResizeSignalScrollArea(self.frame_50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_10.sizePolicy().hasHeightForWidth())
        self.scrollArea_10.setSizePolicy(sizePolicy)
        self.scrollArea_10.setMinimumSize(QtCore.QSize(600, 530))
        self.scrollArea_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea_10.setFont(font)
        self.scrollArea_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_10.setObjectName("scrollArea_10")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1174, 513))
        self.scrollAreaWidgetContents_2.setStyleSheet("")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_171 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_171.setContentsMargins(0, 105, 0, 0)
        self.verticalLayout_171.setSpacing(0)
        self.verticalLayout_171.setObjectName("verticalLayout_171")
        self.frame_45 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy)
        self.frame_45.setMinimumSize(QtCore.QSize(0, 178))
        self.frame_45.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_45.setStyleSheet("")
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.verticalLayout_229 = QtWidgets.QVBoxLayout(self.frame_45)
        self.verticalLayout_229.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout_229.setSpacing(0)
        self.verticalLayout_229.setObjectName("verticalLayout_229")
        self.frame_81 = QtWidgets.QFrame(self.frame_45)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_81.sizePolicy().hasHeightForWidth())
        self.frame_81.setSizePolicy(sizePolicy)
        self.frame_81.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_81.setMaximumSize(QtCore.QSize(16777215, 132))
        self.frame_81.setStyleSheet("")
        self.frame_81.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_81.setObjectName("frame_81")
        self.verticalLayout_160 = QtWidgets.QVBoxLayout(self.frame_81)
        self.verticalLayout_160.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_160.setSpacing(0)
        self.verticalLayout_160.setObjectName("verticalLayout_160")
        self.mainPageLastPlayedHeaderQLabel = QtWidgets.QLabel(self.frame_81)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageLastPlayedHeaderQLabel.sizePolicy().hasHeightForWidth())
        self.mainPageLastPlayedHeaderQLabel.setSizePolicy(sizePolicy)
        self.mainPageLastPlayedHeaderQLabel.setMinimumSize(QtCore.QSize(0, 52))
        self.mainPageLastPlayedHeaderQLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageLastPlayedHeaderQLabel.setFont(font)
        self.mainPageLastPlayedHeaderQLabel.setStyleSheet("color: white;\n"
                                                          "font: 87 17pt \"Heebo Black\";")
        self.mainPageLastPlayedHeaderQLabel.setText("Last played")
        self.mainPageLastPlayedHeaderQLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mainPageLastPlayedHeaderQLabel.setObjectName("mainPageLastPlayedHeaderQLabel")
        self.verticalLayout_160.addWidget(self.mainPageLastPlayedHeaderQLabel)
        self.verticalLayout_229.addWidget(self.frame_81)


        self.LastPlayedSortButtonsQFrame = SortButtonsQFrame(parent=self.frame_45,
                                           frame_structure={"sortButtonsQFrameTitleButtonQFrame": True,
                                                            "sortButtonsQFrameAuthorButtonQFrame": True,
                                                            "sortButtonsQFrameCategoryButtonQFrame": True,
                                                            "sortButtonsQFrameDateAddedButtonQFrame": False,
                                                            "sortButtonsQFrameSongLengthButtonQFrame": True},
                                           visibility_changing_sort_buttons_elements=[
                                               ("sortButtonsQFrameAuthorButtonQFrame", 552),
                                               ("sortButtonsQFrameCategoryButtonQFrame", 726), ]
                                           )
        self.LastPlayedSortButtonsQFrame.setObjectName("LastPlayedSortButtonsQFrame")
        self.verticalLayout_229.addWidget(self.LastPlayedSortButtonsQFrame)

        self.verticalLayout_171.addWidget(self.frame_45)
        self.frame_292 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_292.setStyleSheet("")
        self.frame_292.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_292.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_292.setObjectName("frame_292")
        self.mainPageLastPlayedSongListQVBoxLayout = QtWidgets.QVBoxLayout(self.frame_292)
        self.mainPageLastPlayedSongListQVBoxLayout.setContentsMargins(32, 14, 32, 32)
        self.mainPageLastPlayedSongListQVBoxLayout.setSpacing(0)
        self.mainPageLastPlayedSongListQVBoxLayout.setObjectName("mainPageLastPlayedSongListQVBoxLayout")
        self.verticalLayout_171.addWidget(self.frame_292)
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_46.addWidget(self.scrollArea_10)
        self.verticalLayout_31.addWidget(self.frame_50)
        self.mainPageStackedWidget.addWidget(self.mainPageLastPlayed)
        self.mainPageAuthors = QtWidgets.QWidget()
        self.mainPageAuthors.setStyleSheet("AuthorEntry, AdderEntry{\n"
                                           "    background-color: rgb(24, 24, 24);\n"
                                           "    border-radius: 4px;\n"
                                           "}\n"
                                           "AuthorEntry:hover, AdderEntry:hover{\n"
                                           "    background-color: rgba(179, 179, 179, 0.25);\n"
                                           "}\n"
                                           "QFrame#frame_114 QPushButton{\n"
                                           "    padding-left: 17px;\n"
                                           "    padding-right: 17px;\n"
                                           "    font: 57 10pt \"Heebo Medium\";\n"
                                           "    border-bottom: 2px solid rgba(255, 255, 255, 0);\n"
                                           "    background-color: none;\n"
                                           "}\n"
                                           "QFrame#frame_114 QPushButton:hover:!checked{\n"
                                           "    color: white;\n"
                                           "}\n"
                                           "QFrame#frame_114 QPushButton:checked{\n"
                                           "    border-bottom: 2px solid rgb(247, 178, 158);\n"
                                           "    color: white;\n"
                                           "}\n"
                                           "#frame_114{\n"
                                           "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                           "}\n"
                                           "#scrollAreaWidgetContents_7{\n"
                                           "    background-color: rgb(18, 18, 18);\n"
                                           "}\n")
        self.mainPageAuthors.setObjectName("mainPageAuthors")
        self.verticalLayout_64 = QtWidgets.QVBoxLayout(self.mainPageAuthors)
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.frame_49 = QtWidgets.QFrame(self.mainPageAuthors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy)
        self.frame_49.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_49)
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.scrollArea_7 = ResizeSignalScrollArea(self.frame_49)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_7.sizePolicy().hasHeightForWidth())
        self.scrollArea_7.setSizePolicy(sizePolicy)
        self.scrollArea_7.setMinimumSize(QtCore.QSize(585, 493))
        self.scrollArea_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea_7.setFont(font)
        self.scrollArea_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 900, 817))
        self.scrollAreaWidgetContents_7.setStyleSheet("")
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.frame_52 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy)
        self.frame_52.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_52.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_52.setStyleSheet("")
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.frame_52)
        self.verticalLayout_61.setContentsMargins(32, 60, 32, 0)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.frame_64 = QtWidgets.QFrame(self.frame_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_64.sizePolicy().hasHeightForWidth())
        self.frame_64.setSizePolicy(sizePolicy)
        self.frame_64.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_64.setMaximumSize(QtCore.QSize(16777215, 132))
        self.frame_64.setStyleSheet("")
        self.frame_64.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout(self.frame_64)
        self.verticalLayout_62.setContentsMargins(0, 27, 0, 18)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.label_114 = QtWidgets.QLabel(self.frame_64)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy)
        self.label_114.setMinimumSize(QtCore.QSize(0, 52))
        self.label_114.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_114.setFont(font)
        self.label_114.setStyleSheet("color: white;\n"
                                     "font: 87 17pt \"Heebo Black\";")
        self.label_114.setText("Authors")
        self.label_114.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_114.setObjectName("label_114")
        self.verticalLayout_62.addWidget(self.label_114)
        self.verticalLayout_61.addWidget(self.frame_64)
        self.verticalLayout_60.addWidget(self.frame_52)
        self.frame_53 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy)
        self.frame_53.setStyleSheet("")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.verticalLayout_63 = QtWidgets.QVBoxLayout(self.frame_53)
        self.verticalLayout_63.setContentsMargins(32, 0, 32, 32)
        self.verticalLayout_63.setSpacing(24)
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.frame_114 = QtWidgets.QFrame(self.frame_53)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_114.sizePolicy().hasHeightForWidth())
        self.frame_114.setSizePolicy(sizePolicy)
        self.frame_114.setMinimumSize(QtCore.QSize(0, 33))
        self.frame_114.setStyleSheet("")
        self.frame_114.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_114.setObjectName("frame_114")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_114)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(24)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.mainPageAuthorsRecentlyAddedSortButton = QtWidgets.QPushButton(self.frame_114)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorsRecentlyAddedSortButton.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorsRecentlyAddedSortButton.setSizePolicy(sizePolicy)
        self.mainPageAuthorsRecentlyAddedSortButton.setMinimumSize(QtCore.QSize(0, 33))
        self.mainPageAuthorsRecentlyAddedSortButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageAuthorsRecentlyAddedSortButton.setText("Recently added")
        self.mainPageAuthorsRecentlyAddedSortButton.setCheckable(True)
        self.mainPageAuthorsRecentlyAddedSortButton.setChecked(True)
        self.mainPageAuthorsRecentlyAddedSortButton.setAutoExclusive(True)
        self.mainPageAuthorsRecentlyAddedSortButton.setObjectName("mainPageAuthorsRecentlyAddedSortButton")
        self.horizontalLayout_12.addWidget(self.mainPageAuthorsRecentlyAddedSortButton)
        self.mainPageAuthorsAlphabeticallySortButton = QtWidgets.QPushButton(self.frame_114)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorsAlphabeticallySortButton.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorsAlphabeticallySortButton.setSizePolicy(sizePolicy)
        self.mainPageAuthorsAlphabeticallySortButton.setMinimumSize(QtCore.QSize(0, 33))
        self.mainPageAuthorsAlphabeticallySortButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageAuthorsAlphabeticallySortButton.setText("Alphabetically")
        self.mainPageAuthorsAlphabeticallySortButton.setCheckable(True)
        self.mainPageAuthorsAlphabeticallySortButton.setAutoExclusive(True)
        self.mainPageAuthorsAlphabeticallySortButton.setObjectName("mainPageAuthorsAlphabeticallySortButton")
        self.horizontalLayout_12.addWidget(self.mainPageAuthorsAlphabeticallySortButton)
        self.mainPageAuthorsMostListenedSortButton = QtWidgets.QPushButton(self.frame_114)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorsMostListenedSortButton.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorsMostListenedSortButton.setSizePolicy(sizePolicy)
        self.mainPageAuthorsMostListenedSortButton.setMinimumSize(QtCore.QSize(0, 33))
        self.mainPageAuthorsMostListenedSortButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageAuthorsMostListenedSortButton.setText("Most listened")
        self.mainPageAuthorsMostListenedSortButton.setCheckable(True)
        self.mainPageAuthorsMostListenedSortButton.setAutoExclusive(True)
        self.mainPageAuthorsMostListenedSortButton.setObjectName("mainPageAuthorsMostListenedSortButton")
        self.horizontalLayout_12.addWidget(self.mainPageAuthorsMostListenedSortButton)
        spacerItem14 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem14)
        self.verticalLayout_63.addWidget(self.frame_114)
        self.mainPageAuthorsGrid = QtWidgets.QFrame(self.frame_53)
        self.mainPageAuthorsGrid.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainPageAuthorsGrid.setStyleSheet("")
        self.mainPageAuthorsGrid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPageAuthorsGrid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPageAuthorsGrid.setObjectName("mainPageAuthorsGrid")
        self.mainPageAuthorsAuthorsGridQFlowLayout = FlowLayout(self.mainPageAuthorsGrid)
        self.mainPageAuthorsAuthorsGridQFlowLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPageAuthorsAuthorsGridQFlowLayout.setSpacing(24)
        self.mainPageAuthorsAuthorsGridQFlowLayout.setObjectName("mainPageAuthorsAuthorsGridQFlowLayout")

        self.verticalLayout_63.addWidget(self.mainPageAuthorsGrid)
        self.verticalLayout_60.addWidget(self.frame_53)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_44.addWidget(self.scrollArea_7)
        self.verticalLayout_64.addWidget(self.frame_49)
        self.mainPageStackedWidget.addWidget(self.mainPageAuthors)
        self.mainPagePlaylist = QtWidgets.QWidget()
        self.mainPagePlaylist.setStyleSheet("SortButtonsQFrame{\n"
                                            "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                            "}\n"
                                            "SortButtonsQFrame QPushButton:hover{\n"
                                            "    color: white;\n"
                                            "}\n"
                                            "SortButtonsQFrame QPushButton{\n"
                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                            "}\n"
                                            "}\n"
                                            "SongEntry{\n"
                                            "    border-radius: 4px;\n"
                                            "}\n"
                                            "SongEntry:hover{\n"
                                            "    background-color: rgba(179, 179, 179, 0.25);\n"
                                            "}\n"
                                            "SongEntry QPushButton{\n"
                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                            "    border: none;\n"
                                            "}\n"
                                            "SongEntry QLabel{\n"
                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                            "    background-color: none;\n"
                                            "}\n"
                                            "SongEntry QPushButton:hover{\n"
                                            "    text-decoration: underline;\n"
                                            "    color: white;\n"
                                            "}\n"
                                            "QFrame#frame_17{\n"
                                            "    background-color: rgba(18, 18, 18, 0.15);\n"
                                            "}\n"
                                            "QFrame#frame_55{\n"
                                            "    background-color: rgba(18, 18, 18, 0.15);\n"
                                            "}\n"
                                            "QWidget#widget_7{\n"
                                            "    background-color: qlineargradient( x1:0 y1:0,\n"
                                            "     x2:0 y2:0.63,\n"
                                            "     stop:0 rgb(137, 153, 153),\n"
                                            "    stop:1 rgb(18, 18, 18));\n"
                                            "}\n"
                                            "")
        self.mainPagePlaylist.setObjectName("mainPagePlaylist")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.mainPagePlaylist)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_5 = QtWidgets.QFrame(self.mainPagePlaylist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(600, 530))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrollArea_3 = ResizeSignalScrollArea(self.frame_5)
        self.scrollArea_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMinimumSize(QtCore.QSize(0, 530))
        self.scrollArea_3.setStyleSheet("")
        self.scrollArea_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.widget_7 = QtWidgets.QWidget()
        self.widget_7.setEnabled(True)
        self.widget_7.setGeometry(QtCore.QRect(0, -164, 1424, 694))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setStyleSheet("")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.mainPagePlaylistSongsHeader = QtWidgets.QFrame(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPagePlaylistSongsHeader.sizePolicy().hasHeightForWidth())
        self.mainPagePlaylistSongsHeader.setSizePolicy(sizePolicy)
        self.mainPagePlaylistSongsHeader.setMinimumSize(QtCore.QSize(0, 0))
        self.mainPagePlaylistSongsHeader.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPagePlaylistSongsHeader.setStyleSheet("")
        self.mainPagePlaylistSongsHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPagePlaylistSongsHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPagePlaylistSongsHeader.setObjectName("mainPagePlaylistSongsHeader")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mainPagePlaylistSongsHeader)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_9 = QtWidgets.QFrame(self.mainPagePlaylistSongsHeader)
        self.frame_9.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.frame_9.setStyleSheet("")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setContentsMargins(32, 84, 32, 24)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.mainPagePlaylistMiniatureQLabel = QtWidgets.QLabel(self.frame_9)

        self.shadow2 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(250)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.shadow2.setColor(QtGui.QColor(0, 0, 0, 192))

        self.mainPagePlaylistMiniatureQLabel.setGraphicsEffect(self.shadow2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPagePlaylistMiniatureQLabel.sizePolicy().hasHeightForWidth())
        self.mainPagePlaylistMiniatureQLabel.setSizePolicy(sizePolicy)
        self.mainPagePlaylistMiniatureQLabel.setMinimumSize(QtCore.QSize(232, 232))
        self.mainPagePlaylistMiniatureQLabel.setMaximumSize(QtCore.QSize(232, 232))
        self.mainPagePlaylistMiniatureQLabel.setStyleSheet("")
        self.mainPagePlaylistMiniatureQLabel.setText("")

        self.mainPagePlaylistMiniatureQLabel.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/playlistCoverExample1.png"))

        self.mainPagePlaylistMiniatureQLabel.setScaledContents(True)
        self.mainPagePlaylistMiniatureQLabel.setObjectName("mainPagePlaylistMiniatureQLabel")
        self.horizontalLayout_15.addWidget(self.mainPagePlaylistMiniatureQLabel)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_15.setContentsMargins(15, 0, 0, 5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_108 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy)
        self.label_108.setMinimumSize(QtCore.QSize(0, 0))
        self.label_108.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_108.setFont(font)
        self.label_108.setStyleSheet("font: 87 9pt \"Heebo Black\";\n"
                                     "color: white;\n"
                                     "padding-top: -6px;")
        self.label_108.setText("PLAYLIST")
        self.label_108.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_108.setObjectName("label_108")
        self.verticalLayout_15.addWidget(self.label_108)
        self.mainPagePlaylistNameOfPlaylistLabel = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPagePlaylistNameOfPlaylistLabel.sizePolicy().hasHeightForWidth())
        self.mainPagePlaylistNameOfPlaylistLabel.setSizePolicy(sizePolicy)
        self.mainPagePlaylistNameOfPlaylistLabel.setMinimumSize(QtCore.QSize(0, 52))
        self.mainPagePlaylistNameOfPlaylistLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(68)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPagePlaylistNameOfPlaylistLabel.setFont(font)
        self.mainPagePlaylistNameOfPlaylistLabel.setStyleSheet("font: 87 28pt \"Heebo Black\";\n"
                                                               "color: white;\n"
                                                               "")
        self.mainPagePlaylistNameOfPlaylistLabel.setText("Lorem ipsum")
        self.mainPagePlaylistNameOfPlaylistLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mainPagePlaylistNameOfPlaylistLabel.setObjectName("mainPagePlaylistNameOfPlaylistLabel")
        self.verticalLayout_15.addWidget(self.mainPagePlaylistNameOfPlaylistLabel)
        self.frame_16 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_16.setStyleSheet("")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setSpacing(4)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.mainPagePlaylistNumberOfSongsLabel = QtWidgets.QLabel(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPagePlaylistNumberOfSongsLabel.sizePolicy().hasHeightForWidth())
        self.mainPagePlaylistNumberOfSongsLabel.setSizePolicy(sizePolicy)
        self.mainPagePlaylistNumberOfSongsLabel.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.mainPagePlaylistNumberOfSongsLabel.setText("3 Songs,")
        self.mainPagePlaylistNumberOfSongsLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mainPagePlaylistNumberOfSongsLabel.setObjectName("mainPagePlaylistNumberOfSongsLabel")
        self.horizontalLayout_30.addWidget(self.mainPagePlaylistNumberOfSongsLabel)
        self.mainPagePlaylistLengthOfPlaylistLabel = QtWidgets.QLabel(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPagePlaylistLengthOfPlaylistLabel.sizePolicy().hasHeightForWidth())
        self.mainPagePlaylistLengthOfPlaylistLabel.setSizePolicy(sizePolicy)
        self.mainPagePlaylistLengthOfPlaylistLabel.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.mainPagePlaylistLengthOfPlaylistLabel.setText("0 h. 13 min")
        self.mainPagePlaylistLengthOfPlaylistLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mainPagePlaylistLengthOfPlaylistLabel.setObjectName("mainPagePlaylistLengthOfPlaylistLabel")
        self.horizontalLayout_30.addWidget(self.mainPagePlaylistLengthOfPlaylistLabel)
        spacerItem18 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem18)
        self.verticalLayout_15.addWidget(self.frame_16)
        self.horizontalLayout_15.addWidget(self.frame_10, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_10.addWidget(self.frame_9)
        self.frame_17 = QtWidgets.QFrame(self.mainPagePlaylistSongsHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_17.setStyleSheet("")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setContentsMargins(32, 24, 32, 0)
        self.verticalLayout_16.setSpacing(24)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.playlistPlayPauseButton = QtWidgets.QPushButton(self.frame_17)
        self.playlistPlayPauseButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistPlayPauseButton.sizePolicy().hasHeightForWidth())
        self.playlistPlayPauseButton.setSizePolicy(sizePolicy)
        self.playlistPlayPauseButton.setMinimumSize(QtCore.QSize(56, 56))
        self.playlistPlayPauseButton.setMaximumSize(QtCore.QSize(56, 56))
        self.playlistPlayPauseButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                   "border-radius: 28px;\n"
                                                   "text-align: center;\n"
                                                   "font: 87 9pt \"Heebo Black\";\n"
                                                   "background-color: rgb(255, 176, 85);\n"
                                                   "")
        self.playlistPlayPauseButton.setText("")
        self.playlistPlayPauseButton.setIcon(icon7)
        self.playlistPlayPauseButton.setIconSize(QtCore.QSize(24, 24))
        self.playlistPlayPauseButton.setCheckable(False)
        self.playlistPlayPauseButton.setObjectName("playlistPlayPauseButton")
        self.verticalLayout_16.addWidget(self.playlistPlayPauseButton)

        self.PlaylistSortButtonsQFrame = SortButtonsQFrame(parent=self.frame_17,
                                                           frame_structure={"sortButtonsQFrameTitleButtonQFrame": True,
                                                                            "sortButtonsQFrameAuthorButtonQFrame": True,
                                                                            "sortButtonsQFrameCategoryButtonQFrame": True,
                                                                            "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                                            "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                           visibility_changing_sort_buttons_elements=[
                                                               ("sortButtonsQFrameAuthorButtonQFrame", 552),
                                                               ("sortButtonsQFrameCategoryButtonQFrame", 726),
                                                               ("sortButtonsQFrameDateAddedButtonQFrame", 950)]
                                                           )
        self.PlaylistSortButtonsQFrame.setObjectName("PlaylistSortButtonsQFrame")
        self.verticalLayout_16.addWidget(self.PlaylistSortButtonsQFrame)


        self.verticalLayout_10.addWidget(self.frame_17)
        self.verticalLayout_12.addWidget(self.mainPagePlaylistSongsHeader)
        self.frame_55 = QtWidgets.QFrame(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy)
        self.frame_55.setStyleSheet("")
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.mainPagePlaylistSongListQVBoxLayout = QtWidgets.QVBoxLayout(self.frame_55)
        self.mainPagePlaylistSongListQVBoxLayout.setContentsMargins(32, 9, 32, 32)
        self.mainPagePlaylistSongListQVBoxLayout.setSpacing(0)
        self.mainPagePlaylistSongListQVBoxLayout.setObjectName("mainPagePlaylistSongListQVBoxLayout")
        self.verticalLayout_12.addWidget(self.frame_55)
        self.scrollArea_3.setWidget(self.widget_7)
        self.verticalLayout_11.addWidget(self.scrollArea_3)
        self.verticalLayout_13.addWidget(self.frame_5)
        self.mainPageStackedWidget.addWidget(self.mainPagePlaylist)
        self.mainPageAuthorPage = QtWidgets.QWidget()
        self.mainPageAuthorPage.setStyleSheet("QFrame#mainPageAuthorHeader{\n"
                                              "    background-color: transparent;\n"
                                              "}\n"
                                              "#scrollAreaWidgetContents_8{\n"
                                              "    background-color: transparent;\n"
                                              "}\n"
                                              "#scrollArea_8{\n"
                                              "    background-color: transparent;\n"
                                              "}\n"
                                              "#mainPageAuthorPage{\n"
                                              "    background-image: url(:/icons/temporary/icons/authorCoverExample.png);\n"
                                              "    background-repeat: no-repeat;\n"
                                              "}\n"
                                              "#frame_352{\n"
                                              "    background-color: rgb(18, 18, 18);\n"
                                              "}\n"
                                              "#authorPagePlayPauseQPushButton{\n"
                                              "    border-radius: 32px;\n"
                                              "    background-color: rgb(247, 178, 158);\n"
                                              "}\n"
                                              "#authorPagePlayPauseQPushButton:checked{\n"
                                              "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_pause_white_48dp.png);\n"
                                              "}\n"
                                              "\n"
                                              "#frame_41 QPushButton{\n"
                                              "    text-align: center;\n"
                                              "    border-bottom: 2px solid rgba(255, 255, 255, 0);\n"
                                              "    background-color: none;\n"
                                              "    color: white;\n"
                                              "    font: 87 12pt \"Heebo Black\";\n"
                                              "    padding-bottom: 5px;\n"
                                              "    padding-left: 17px;\n"
                                              "    padding-right: 17px;\n"
                                              "}\n"
                                              "#frame_41 QPushButton:hover:!checked{\n"
                                              "    color: white;\n"
                                              "    border-bottom: 2px solid rgb(255, 203, 164);\n"
                                              "}\n"
                                              "#frame_41 QPushButton:checked{\n"
                                              "    border-bottom: 2px solid rgb(247, 178, 158);\n"
                                              "    color: white;\n"
                                              "}\n"
                                              "#frame_41{\n"
                                              "    background-color: none;\n"
                                              "}\n"
                                              "SongEntry{\n"
                                              "    border-radius: 4px;\n"
                                              "}\n"
                                              "SongEntry:hover{\n"
                                              "    background-color: rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "SongEntry QPushButton{\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "SongEntry QLabel{\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "    background-color: none;\n"
                                              "}\n"
                                              "SongEntry QPushButton:hover{\n"
                                              "    text-decoration: underline;\n"
                                              "    color: white;\n"
                                              "}\n"
                                              "SortButtonsQFrame{\n"
                                              "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "SortButtonsQFrame QPushButton{\n"
                                              "    font: 57 10pt \"Heebo Medium\";\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "SortButtonsQFrame QPushButton:hover{\n"
                                              "    color: white;\n"
                                              "}\n"
                                              "AlbumEntry{\n"
                                              "    background-color: rgb(24, 24, 24);\n"
                                              "    border-radius: 4px;\n"
                                              "}\n"
                                              "AlbumEntry:hover{\n"
                                              "    background-color: rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "QFrame#mainPageAuthorsHeader_2{\n"
                                              "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "PlaylistEntry{\n"
                                              "    background-color: rgb(24, 24, 24);\n"
                                              "	 border-radius: 4px;\n"
                                              "}\n"
                                              "PlaylistEntry:hover{\n"
                                              "    background-color: rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "QFrame#mainPageAuthorsHeader_3{\n"
                                              "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                              "}"
                                              )
        self.mainPageAuthorPage.setObjectName("mainPageAuthorPage")
        self.verticalLayout_74 = QtWidgets.QVBoxLayout(self.mainPageAuthorPage)
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName("verticalLayout_74")
        self.frame_65 = QtWidgets.QFrame(self.mainPageAuthorPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_65.sizePolicy().hasHeightForWidth())
        self.frame_65.setSizePolicy(sizePolicy)
        self.frame_65.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_65.setStyleSheet("")
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.verticalLayout_65 = QtWidgets.QVBoxLayout(self.frame_65)
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.scrollArea_8 = ResizeSignalScrollArea(self.frame_65)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_8.sizePolicy().hasHeightForWidth())
        self.scrollArea_8.setSizePolicy(sizePolicy)
        self.scrollArea_8.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea_8.setFont(font)
        self.scrollArea_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 1174, 1131))
        self.scrollAreaWidgetContents_8.setStyleSheet("")
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.mainPageAuthorHeader = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorHeader.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorHeader.setSizePolicy(sizePolicy)
        self.mainPageAuthorHeader.setMinimumSize(QtCore.QSize(0, 340))
        self.mainPageAuthorHeader.setMaximumSize(QtCore.QSize(16777215, 415))
        self.mainPageAuthorHeader.setStyleSheet("")
        self.mainPageAuthorHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPageAuthorHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPageAuthorHeader.setObjectName("mainPageAuthorHeader")
        self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.mainPageAuthorHeader)
        self.verticalLayout_67.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout_67.setSpacing(32)
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        spacerItem21 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_67.addItem(spacerItem21)
        self.mainPageAutorNameLabel = QtWidgets.QLabel(self.mainPageAuthorHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAutorNameLabel.sizePolicy().hasHeightForWidth())
        self.mainPageAutorNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageAutorNameLabel.setFont(font)
        self.mainPageAutorNameLabel.setStyleSheet("font: 87 36pt \"Heebo Black\";\n"
                                                  "color: white;\n"
                                                  "background-color: none;")
        self.mainPageAutorNameLabel.setText("Integer dignissim")
        self.mainPageAutorNameLabel.setObjectName("mainPageAutorNameLabel")
        self.verticalLayout_67.addWidget(self.mainPageAutorNameLabel)
        self.frame_41 = QtWidgets.QFrame(self.mainPageAuthorHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy)
        self.frame_41.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(32)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.mainPageAuthorSongsButton = QtWidgets.QPushButton(self.frame_41)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorSongsButton.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorSongsButton.setSizePolicy(sizePolicy)
        self.mainPageAuthorSongsButton.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageAuthorSongsButton.setFont(font)
        self.mainPageAuthorSongsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageAuthorSongsButton.setStyleSheet("")
        self.mainPageAuthorSongsButton.setText("Songs")
        self.mainPageAuthorSongsButton.setCheckable(True)
        self.mainPageAuthorSongsButton.setChecked(True)
        self.mainPageAuthorSongsButton.setAutoExclusive(True)
        self.mainPageAuthorSongsButton.setObjectName("mainPageAuthorSongsButton")
        self.horizontalLayout_9.addWidget(self.mainPageAuthorSongsButton)
        self.mainPageAuthorAlbumsButton = QtWidgets.QPushButton(self.frame_41)
        self.mainPageAuthorAlbumsButton.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageAuthorAlbumsButton.setFont(font)
        self.mainPageAuthorAlbumsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageAuthorAlbumsButton.setStyleSheet("")
        self.mainPageAuthorAlbumsButton.setText("Albums")
        self.mainPageAuthorAlbumsButton.setCheckable(True)
        self.mainPageAuthorAlbumsButton.setAutoExclusive(True)
        self.mainPageAuthorAlbumsButton.setObjectName("mainPageAuthorAlbumsButton")
        self.horizontalLayout_9.addWidget(self.mainPageAuthorAlbumsButton)
        self.mainPageAuthorPlaylistsButton = QtWidgets.QPushButton(self.frame_41)
        self.mainPageAuthorPlaylistsButton.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageAuthorPlaylistsButton.setFont(font)
        self.mainPageAuthorPlaylistsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageAuthorPlaylistsButton.setStyleSheet("")
        self.mainPageAuthorPlaylistsButton.setText("Playlists")
        self.mainPageAuthorPlaylistsButton.setCheckable(True)
        self.mainPageAuthorPlaylistsButton.setAutoExclusive(True)
        self.mainPageAuthorPlaylistsButton.setObjectName("mainPageAuthorPlaylistsButton")
        self.horizontalLayout_9.addWidget(self.mainPageAuthorPlaylistsButton)
        spacerItem22 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem22)
        self.verticalLayout_67.addWidget(self.frame_41, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_66.addWidget(self.mainPageAuthorHeader)
        self.frame_352 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_352.sizePolicy().hasHeightForWidth())
        self.frame_352.setSizePolicy(sizePolicy)
        self.frame_352.setStyleSheet("")
        self.frame_352.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_352.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_352.setObjectName("frame_352")
        self.verticalLayout_69 = QtWidgets.QVBoxLayout(self.frame_352)
        self.verticalLayout_69.setContentsMargins(32, 0, 32, 32)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        self.mainPageAuthorPageStackedWidget = QtWidgets.QStackedWidget(self.frame_352)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorPageStackedWidget.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorPageStackedWidget.setSizePolicy(sizePolicy)
        self.mainPageAuthorPageStackedWidget.setObjectName("mainPageAuthorPageStackedWidget")
        self.widget_4 = QtWidgets.QWidget()
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")

        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_play_arrow_white_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.frame_120 = QtWidgets.QFrame(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_120.sizePolicy().hasHeightForWidth())
        self.frame_120.setSizePolicy(sizePolicy)
        self.frame_120.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_120.setObjectName("frame_120")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.frame_120)
        self.verticalLayout_59.setContentsMargins(0, 24, 0, 11)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.authorPagePlayPauseQPushButton = QtWidgets.QPushButton(self.frame_120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authorPagePlayPauseQPushButton.sizePolicy().hasHeightForWidth())
        self.authorPagePlayPauseQPushButton.setSizePolicy(sizePolicy)
        self.authorPagePlayPauseQPushButton.setMinimumSize(QtCore.QSize(64, 64))
        self.authorPagePlayPauseQPushButton.setMaximumSize(QtCore.QSize(64, 64))
        self.authorPagePlayPauseQPushButton.setText("")
        self.authorPagePlayPauseQPushButton.setIcon(icon8)
        self.authorPagePlayPauseQPushButton.setIconSize(QtCore.QSize(42, 42))
        self.authorPagePlayPauseQPushButton.setCheckable(True)
        self.authorPagePlayPauseQPushButton.setObjectName("authorPagePlayPauseQPushButton")
        self.verticalLayout_59.addWidget(self.authorPagePlayPauseQPushButton)
        self.verticalLayout_40.addWidget(self.frame_120)

        self.AuthorSortButtonsQFrame = SortButtonsQFrame(parent=self.widget_4,
                                                         frame_structure={"sortButtonsQFrameTitleButtonQFrame": True,
                                                                              "sortButtonsQFrameAuthorButtonQFrame": False,
                                                                              "sortButtonsQFrameCategoryButtonQFrame": True,
                                                                              "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                                              "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                         visibility_changing_sort_buttons_elements=[("sortButtonsQFrameCategoryButtonQFrame", 552),
                                                                                     ("sortButtonsQFrameDateAddedButtonQFrame", 726)]
                                                         )
        self.AuthorSortButtonsQFrame.setObjectName("AuthorSortButtonsQFrame")
        self.verticalLayout_40.addWidget(self.AuthorSortButtonsQFrame)

        self.frame_60 = QtWidgets.QFrame(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_60.sizePolicy().hasHeightForWidth())
        self.frame_60.setSizePolicy(sizePolicy)
        self.frame_60.setStyleSheet("")
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.mainPageAuthorPageSongsListQVBoxLayout = QtWidgets.QVBoxLayout(self.frame_60)
        self.mainPageAuthorPageSongsListQVBoxLayout.setContentsMargins(0, 17, 0, 0)
        self.mainPageAuthorPageSongsListQVBoxLayout.setSpacing(0)
        self.mainPageAuthorPageSongsListQVBoxLayout.setObjectName("mainPageAuthorPageSongsListQVBoxLayout")
        self.verticalLayout_40.addWidget(self.frame_60)
        self.mainPageAuthorPageStackedWidget.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget()
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_96 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_96.setSpacing(24)
        self.verticalLayout_96.setObjectName("verticalLayout_96")
        self.mainPageAuthorsHeader_2 = QtWidgets.QFrame(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorsHeader_2.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorsHeader_2.setSizePolicy(sizePolicy)
        self.mainPageAuthorsHeader_2.setMinimumSize(QtCore.QSize(0, 0))
        self.mainPageAuthorsHeader_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPageAuthorsHeader_2.setStyleSheet("")
        self.mainPageAuthorsHeader_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPageAuthorsHeader_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPageAuthorsHeader_2.setObjectName("mainPageAuthorsHeader_2")
        self.verticalLayout_90 = QtWidgets.QVBoxLayout(self.mainPageAuthorsHeader_2)
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName("verticalLayout_90")
        self.frame_123 = QtWidgets.QFrame(self.mainPageAuthorsHeader_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_123.sizePolicy().hasHeightForWidth())
        self.frame_123.setSizePolicy(sizePolicy)
        self.frame_123.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_123.setMaximumSize(QtCore.QSize(16777215, 132))
        self.frame_123.setStyleSheet("")
        self.frame_123.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_123.setObjectName("frame_123")
        self.verticalLayout_91 = QtWidgets.QVBoxLayout(self.frame_123)
        self.verticalLayout_91.setContentsMargins(0, 27, 0, 18)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName("verticalLayout_91")
        self.mainPageAuthorPageAlbumsAuthorNameLabel = QtWidgets.QLabel(self.frame_123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorPageAlbumsAuthorNameLabel.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorPageAlbumsAuthorNameLabel.setSizePolicy(sizePolicy)
        self.mainPageAuthorPageAlbumsAuthorNameLabel.setMinimumSize(QtCore.QSize(0, 52))
        self.mainPageAuthorPageAlbumsAuthorNameLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageAuthorPageAlbumsAuthorNameLabel.setFont(font)
        self.mainPageAuthorPageAlbumsAuthorNameLabel.setStyleSheet("color: white;\n"
                                                                   "font: 87 17pt \"Heebo Black\";")
        self.mainPageAuthorPageAlbumsAuthorNameLabel.setText("Integer dignissim albums")
        self.mainPageAuthorPageAlbumsAuthorNameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mainPageAuthorPageAlbumsAuthorNameLabel.setObjectName("mainPageAuthorPageAlbumsAuthorNameLabel")
        self.verticalLayout_91.addWidget(self.mainPageAuthorPageAlbumsAuthorNameLabel)
        self.verticalLayout_90.addWidget(self.frame_123)
        self.verticalLayout_96.addWidget(self.mainPageAuthorsHeader_2)
        self.frame_293 = QtWidgets.QFrame(self.widget_5)
        self.frame_293.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_293.setStyleSheet("")
        self.frame_293.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_293.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_293.setObjectName("frame_293")
        self.mainPageAuthorPageAlbumsGridQFlowLayout = FlowLayout(self.frame_293)
        self.mainPageAuthorPageAlbumsGridQFlowLayout.setContentsMargins(0, 0, 0, 24)
        self.mainPageAuthorPageAlbumsGridQFlowLayout.setSpacing(24)
        self.mainPageAuthorPageAlbumsGridQFlowLayout.setObjectName("mainPageAuthorPageAlbumsGridQFlowLayout")
        self.verticalLayout_96.addWidget(self.frame_293)
        self.mainPageAuthorPageStackedWidget.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget()
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_157 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_157.setSpacing(24)
        self.verticalLayout_157.setObjectName("verticalLayout_157")
        self.mainPageAuthorsHeader_3 = QtWidgets.QFrame(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorsHeader_3.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorsHeader_3.setSizePolicy(sizePolicy)
        self.mainPageAuthorsHeader_3.setMinimumSize(QtCore.QSize(0, 0))
        self.mainPageAuthorsHeader_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPageAuthorsHeader_3.setStyleSheet("")
        self.mainPageAuthorsHeader_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPageAuthorsHeader_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPageAuthorsHeader_3.setObjectName("mainPageAuthorsHeader_3")
        self.verticalLayout_97 = QtWidgets.QVBoxLayout(self.mainPageAuthorsHeader_3)
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName("verticalLayout_97")
        self.frame_156 = QtWidgets.QFrame(self.mainPageAuthorsHeader_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_156.sizePolicy().hasHeightForWidth())
        self.frame_156.setSizePolicy(sizePolicy)
        self.frame_156.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_156.setMaximumSize(QtCore.QSize(16777215, 132))
        self.frame_156.setStyleSheet("")
        self.frame_156.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_156.setObjectName("frame_156")
        self.verticalLayout_98 = QtWidgets.QVBoxLayout(self.frame_156)
        self.verticalLayout_98.setContentsMargins(0, 27, 0, 18)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName("verticalLayout_98")
        self.mainPageAuthorPagePlaylistsAuthorNameLabel = QtWidgets.QLabel(self.frame_156)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAuthorPagePlaylistsAuthorNameLabel.sizePolicy().hasHeightForWidth())
        self.mainPageAuthorPagePlaylistsAuthorNameLabel.setSizePolicy(sizePolicy)
        self.mainPageAuthorPagePlaylistsAuthorNameLabel.setMinimumSize(QtCore.QSize(0, 52))
        self.mainPageAuthorPagePlaylistsAuthorNameLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageAuthorPagePlaylistsAuthorNameLabel.setFont(font)
        self.mainPageAuthorPagePlaylistsAuthorNameLabel.setStyleSheet("color: white;\n"
                                                                     "font: 87 17pt \"Heebo Black\";")
        self.mainPageAuthorPagePlaylistsAuthorNameLabel.setText("Integer dignissim playlists")
        self.mainPageAuthorPagePlaylistsAuthorNameLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.mainPageAuthorPagePlaylistsAuthorNameLabel.setObjectName("mainPageAuthorPagePlaylistsAuthorNameLabel")
        self.verticalLayout_98.addWidget(self.mainPageAuthorPagePlaylistsAuthorNameLabel)
        self.verticalLayout_97.addWidget(self.frame_156)
        self.verticalLayout_157.addWidget(self.mainPageAuthorsHeader_3)
        self.frame_255 = QtWidgets.QFrame(self.widget_6)
        self.frame_255.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_255.setStyleSheet("")
        self.frame_255.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_255.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_255.setObjectName("frame_255")
        self.mainPageAuthorPagePlaylistsGridQFlowLayout = FlowLayout(self.frame_255)
        self.mainPageAuthorPagePlaylistsGridQFlowLayout.setContentsMargins(0, 0, 0, 24)
        self.mainPageAuthorPagePlaylistsGridQFlowLayout.setSpacing(24)
        self.mainPageAuthorPagePlaylistsGridQFlowLayout.setObjectName("mainPageAuthorPagePlaylistsGridQFlowLayout")
        self.verticalLayout_157.addWidget(self.frame_255)
        self.mainPageAuthorPageStackedWidget.addWidget(self.widget_6)
        self.verticalLayout_69.addWidget(self.mainPageAuthorPageStackedWidget)
        self.verticalLayout_66.addWidget(self.frame_352)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_65.addWidget(self.scrollArea_8)
        self.verticalLayout_74.addWidget(self.frame_65)
        self.mainPageStackedWidget.addWidget(self.mainPageAuthorPage)
        self.mainPageCategoryPage = QtWidgets.QWidget()
        self.mainPageCategoryPage.setStyleSheet("QWidget#widget{\n"
                                                "    background-color: rgba(18, 18, 18, 0.15);\n"
                                                "}\n"
                                                "QWidget#widget_2{\n"
                                                "    background-color: rgba(18, 18, 18, 0.15);\n"
                                                "}\n"
                                                "QWidget#widget_3{\n"
                                                "    background-color: rgba(18, 18, 18, 0.15);\n"
                                                "}\n"
                                                "#scrollAreaWidgetContents_10{\n"
                                                "    background-color: qlineargradient( x1:0 y1:0,\n"
                                                "     x2:0 y2:0.63,\n"
                                                "     stop:0 rgb(228, 34, 53),\n"
                                                "    stop:1 rgb(18, 18, 18));\n"
                                                "}\n"
                                                "SongEntry{\n"
                                                "    border-radius: 4px;\n"
                                                "}\n"
                                                "SongEntry:hover{\n"
                                                "    background-color: rgba(179, 179, 179, 0.25);\n"
                                                "}\n"
                                                "SongEntry QPushButton{\n"
                                                "    font: 57 10pt \"Heebo Medium\";\n"
                                                "    border: none;\n"
                                                "}\n"
                                                "SongEntry QLabel{\n"
                                                "    font: 57 10pt \"Heebo Medium\";\n"
                                                "    background-color: none;\n"
                                                "}\n"
                                                "SongEntry QPushButton:hover{\n"
                                                "    text-decoration: underline;\n"
                                                "    color: white;\n"
                                                "}\n"
                                                "SortButtonsQFrame{\n"
                                                "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                                "}\n"
                                                "SortButtonsQFrame QPushButton{\n"
                                                "    font: 57 10pt \"Heebo Medium\";\n"
                                                "    border: none;\n"
                                                "}\n"
                                                "SortButtonsQFrame QPushButton:hover{\n"
                                                "    color: white;\n"
                                                "}\n"
                                                "AlbumEntry{\n"
                                                "    background-color: rgb(24, 24, 24);\n"
                                                "    border-radius: 4px;\n"
                                                "}\n"
                                                "AlbumEntry:hover{\n"
                                                "    background-color: rgba(179, 179, 179, 0.25);\n"
                                                "}\n"
                                                "QFrame#frame_59{\n"
                                                "    border-bottom: 1px solid rgb(40, 40, 40);\n"
                                                "}\n"
                                                "PlaylistEntry{\n"
                                                "    background-color: rgb(24, 24, 24);\n"
                                                "    border-radius: 4px;\n"
                                                "}\n"
                                                "PlaylistEntry:hover{\n"
                                                "    background-color: rgba(179, 179, 179, 0.25);\n"
                                                "}\n"
                                                "QFrame#frame_62{\n"
                                                "    border-top: 1px solid rgb(40, 40, 40);\n"
                                                "}\n"
                                                "#categoryPagePlayPauseQPushButton{\n"
                                                "    border-radius: 32px;\n"
                                                "    background-color: rgb(247, 178, 158);\n"
                                                "}\n"
                                                "#categoryPagePlayPauseQPushButton:checked{\n"
                                                "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_pause_white_48dp.png);\n"
                                                "}\n"
                                                )
        self.mainPageCategoryPage.setObjectName("mainPageCategoryPage")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.mainPageCategoryPage)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.frame_82 = QtWidgets.QFrame(self.mainPageCategoryPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_82.sizePolicy().hasHeightForWidth())
        self.frame_82.setSizePolicy(sizePolicy)
        self.frame_82.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_82.setStyleSheet("")
        self.frame_82.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_82.setObjectName("frame_82")
        self.verticalLayout_84 = QtWidgets.QVBoxLayout(self.frame_82)
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName("verticalLayout_84")
        self.scrollArea_11 = ResizeSignalScrollArea(self.frame_82)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_11.sizePolicy().hasHeightForWidth())
        self.scrollArea_11.setSizePolicy(sizePolicy)
        self.scrollArea_11.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea_11.setFont(font)
        self.scrollArea_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_11.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_11.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_11.setObjectName("scrollArea_11")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 1174, 1131))
        self.scrollAreaWidgetContents_10.setStyleSheet("")
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.verticalLayout_107 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName("verticalLayout_107")
        self.mainPageCategoryHeader = QtWidgets.QFrame(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageCategoryHeader.sizePolicy().hasHeightForWidth())
        self.mainPageCategoryHeader.setSizePolicy(sizePolicy)
        self.mainPageCategoryHeader.setMinimumSize(QtCore.QSize(0, 340))
        self.mainPageCategoryHeader.setMaximumSize(QtCore.QSize(16777215, 415))
        self.mainPageCategoryHeader.setStyleSheet("")
        self.mainPageCategoryHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPageCategoryHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPageCategoryHeader.setObjectName("mainPageCategoryHeader")
        self.verticalLayout_114 = QtWidgets.QVBoxLayout(self.mainPageCategoryHeader)
        self.verticalLayout_114.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout_114.setSpacing(32)
        self.verticalLayout_114.setObjectName("verticalLayout_114")
        spacerItem29 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_114.addItem(spacerItem29)
        self.mainPageCategoryNameLabel = QtWidgets.QLabel(self.mainPageCategoryHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageCategoryNameLabel.sizePolicy().hasHeightForWidth())
        self.mainPageCategoryNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(68)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageCategoryNameLabel.setFont(font)
        self.mainPageCategoryNameLabel.setStyleSheet("font: 87 68pt \"Heebo Black\";\n"
                                                     "color: white;\n"
                                                     "background-color: none;")
        self.mainPageCategoryNameLabel.setText("Rock")
        self.mainPageCategoryNameLabel.setObjectName("mainPageCategoryNameLabel")
        self.verticalLayout_114.addWidget(self.mainPageCategoryNameLabel)
        self.frame_56 = QtWidgets.QFrame(self.mainPageCategoryHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy)
        self.frame_56.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_56.setStyleSheet("QPushButton{\n"
                                    "    text-align: center;\n"
                                    "    border-bottom: 2px solid rgba(255, 255, 255, 0);\n"
                                    "    background-color: none;\n"
                                    "    color: white;\n"
                                    "    font: 87 12pt \"Heebo Black\";\n"
                                    "    padding-bottom: 5px;\n"
                                    "}\n"
                                    "QPushButton:hover:!checked{\n"
                                    "    color: white;\n"
                                    "    border-bottom: 2px solid rgb(255, 203, 164);\n"
                                    "}\n"
                                    "QPushButton:checked{\n"
                                    "    border-bottom: 2px solid rgb(255, 176, 85);\n"
                                    "    color: white;\n"
                                    "}\n"
                                    "\n"
                                    "QFrame#frame_41{\n"
                                    "    background-color: none;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_56)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(32)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.mainPageCategorySongsButton = QtWidgets.QPushButton(self.frame_56)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageCategorySongsButton.sizePolicy().hasHeightForWidth())
        self.mainPageCategorySongsButton.setSizePolicy(sizePolicy)
        self.mainPageCategorySongsButton.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageCategorySongsButton.setFont(font)
        self.mainPageCategorySongsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageCategorySongsButton.setStyleSheet("")
        self.mainPageCategorySongsButton.setText("Songs")
        self.mainPageCategorySongsButton.setCheckable(True)
        self.mainPageCategorySongsButton.setChecked(True)
        self.mainPageCategorySongsButton.setAutoExclusive(True)
        self.mainPageCategorySongsButton.setObjectName("mainPageCategorySongsButton")
        self.horizontalLayout_11.addWidget(self.mainPageCategorySongsButton)
        self.mainPageCategoryAlbumsButton = QtWidgets.QPushButton(self.frame_56)
        self.mainPageCategoryAlbumsButton.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageCategoryAlbumsButton.setFont(font)
        self.mainPageCategoryAlbumsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageCategoryAlbumsButton.setStyleSheet("")
        self.mainPageCategoryAlbumsButton.setText("Albums")
        self.mainPageCategoryAlbumsButton.setCheckable(True)
        self.mainPageCategoryAlbumsButton.setAutoExclusive(True)
        self.mainPageCategoryAlbumsButton.setObjectName("mainPageCategoryAlbumsButton")
        self.horizontalLayout_11.addWidget(self.mainPageCategoryAlbumsButton)
        self.mainPageCategoryPlaylistsButton = QtWidgets.QPushButton(self.frame_56)
        self.mainPageCategoryPlaylistsButton.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageCategoryPlaylistsButton.setFont(font)
        self.mainPageCategoryPlaylistsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageCategoryPlaylistsButton.setStyleSheet("")
        self.mainPageCategoryPlaylistsButton.setText("Playlists")
        self.mainPageCategoryPlaylistsButton.setCheckable(True)
        self.mainPageCategoryPlaylistsButton.setAutoExclusive(True)
        self.mainPageCategoryPlaylistsButton.setObjectName("mainPageCategoryPlaylistsButton")
        self.horizontalLayout_11.addWidget(self.mainPageCategoryPlaylistsButton)
        spacerItem30 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem30)
        self.verticalLayout_114.addWidget(self.frame_56)
        self.verticalLayout_107.addWidget(self.mainPageCategoryHeader)
        self.frame_58 = QtWidgets.QFrame(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy)
        self.frame_58.setStyleSheet("")
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.verticalLayout_121 = QtWidgets.QVBoxLayout(self.frame_58)
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 32)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName("verticalLayout_121")
        self.mainPageCategoryPageStackedWidget = QtWidgets.QStackedWidget(self.frame_58)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageCategoryPageStackedWidget.sizePolicy().hasHeightForWidth())
        self.mainPageCategoryPageStackedWidget.setSizePolicy(sizePolicy)
        self.mainPageCategoryPageStackedWidget.setObjectName("mainPageCategoryPageStackedWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_41.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")

        self.frame_189 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_189.sizePolicy().hasHeightForWidth())
        self.frame_189.setSizePolicy(sizePolicy)
        self.frame_189.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_189.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_189.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_189.setObjectName("frame_189")
        self.verticalLayout_286 = QtWidgets.QVBoxLayout(self.frame_189)
        self.verticalLayout_286.setContentsMargins(0, 24, 0, 11)
        self.verticalLayout_286.setSpacing(0)
        self.verticalLayout_286.setObjectName("verticalLayout_286")
        self.categoryPagePlayPauseQPushButton = QtWidgets.QPushButton(self.frame_189)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryPagePlayPauseQPushButton.sizePolicy().hasHeightForWidth())
        self.categoryPagePlayPauseQPushButton.setSizePolicy(sizePolicy)
        self.categoryPagePlayPauseQPushButton.setMinimumSize(QtCore.QSize(64, 64))
        self.categoryPagePlayPauseQPushButton.setMaximumSize(QtCore.QSize(64, 64))
        self.categoryPagePlayPauseQPushButton.setText("")
        self.categoryPagePlayPauseQPushButton.setIcon(icon8)
        self.categoryPagePlayPauseQPushButton.setIconSize(QtCore.QSize(42, 42))
        self.categoryPagePlayPauseQPushButton.setCheckable(True)
        self.categoryPagePlayPauseQPushButton.setObjectName("categoryPagePlayPauseQPushButton")
        self.verticalLayout_286.addWidget(self.categoryPagePlayPauseQPushButton)
        self.verticalLayout_41.addWidget(self.frame_189)

        self.CategorySortButtonsQFrame = SortButtonsQFrame(parent=self.widget,
                                                           frame_structure={"sortButtonsQFrameTitleButtonQFrame": True,
                                                           "sortButtonsQFrameAuthorButtonQFrame": True,
                                                           "sortButtonsQFrameCategoryButtonQFrame": False,
                                                           "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                           "sortButtonsQFrameSongLengthButtonQFrame": True},
                                                           visibility_changing_sort_buttons_elements=[
                                              ("sortButtonsQFrameAuthorButtonQFrame", 552),
                                              ("sortButtonsQFrameDateAddedButtonQFrame", 726)]
                                                           )
        self.CategorySortButtonsQFrame.setObjectName("CategorySortButtonsQFrame")
        self.verticalLayout_41.addWidget(self.CategorySortButtonsQFrame)

        self.frame_256 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_256.sizePolicy().hasHeightForWidth())
        self.frame_256.setSizePolicy(sizePolicy)
        self.frame_256.setStyleSheet("")
        self.frame_256.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_256.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_256.setObjectName("frame_256")
        self.mainPageCategoryPageSongsListQVBoxLayout = QtWidgets.QVBoxLayout(self.frame_256)
        self.mainPageCategoryPageSongsListQVBoxLayout.setContentsMargins(0, 17, 0, 0)
        self.mainPageCategoryPageSongsListQVBoxLayout.setSpacing(0)
        self.mainPageCategoryPageSongsListQVBoxLayout.setObjectName("mainPageCategoryPageSongsListQVBoxLayout")
        self.verticalLayout_41.addWidget(self.frame_256)
        self.mainPageCategoryPageStackedWidget.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget()
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_175 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_175.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout_175.setSpacing(24)
        self.verticalLayout_175.setObjectName("verticalLayout_175")
        self.frame_59 = QtWidgets.QFrame(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy)
        self.frame_59.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_59.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_59.setStyleSheet("")
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.verticalLayout_176 = QtWidgets.QVBoxLayout(self.frame_59)
        self.verticalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_176.setSpacing(0)
        self.verticalLayout_176.setObjectName("verticalLayout_176")
        self.frame_225 = QtWidgets.QFrame(self.frame_59)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_225.sizePolicy().hasHeightForWidth())
        self.frame_225.setSizePolicy(sizePolicy)
        self.frame_225.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_225.setMaximumSize(QtCore.QSize(16777215, 132))
        self.frame_225.setStyleSheet("")
        self.frame_225.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_225.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_225.setObjectName("frame_225")
        self.verticalLayout_177 = QtWidgets.QVBoxLayout(self.frame_225)
        self.verticalLayout_177.setContentsMargins(0, 27, 0, 18)
        self.verticalLayout_177.setSpacing(0)
        self.verticalLayout_177.setObjectName("verticalLayout_177")
        self.mainPageCategoryPageAlbumsCategoryNameLabel = QtWidgets.QLabel(self.frame_225)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageCategoryPageAlbumsCategoryNameLabel.sizePolicy().hasHeightForWidth())
        self.mainPageCategoryPageAlbumsCategoryNameLabel.setSizePolicy(sizePolicy)
        self.mainPageCategoryPageAlbumsCategoryNameLabel.setMinimumSize(QtCore.QSize(0, 52))
        self.mainPageCategoryPageAlbumsCategoryNameLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageCategoryPageAlbumsCategoryNameLabel.setFont(font)
        self.mainPageCategoryPageAlbumsCategoryNameLabel.setStyleSheet("color: white;\n"
                                                                     "font: 87 17pt \"Heebo Black\";")
        self.mainPageCategoryPageAlbumsCategoryNameLabel.setText("Rock albums")
        self.mainPageCategoryPageAlbumsCategoryNameLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.mainPageCategoryPageAlbumsCategoryNameLabel.setObjectName("mainPageCategoryPageAlbumsCategoryNameLabel")
        self.verticalLayout_177.addWidget(self.mainPageCategoryPageAlbumsCategoryNameLabel)
        self.verticalLayout_176.addWidget(self.frame_225)
        self.verticalLayout_175.addWidget(self.frame_59)
        self.frame_57 = QtWidgets.QFrame(self.widget_2)
        self.frame_57.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_57.setStyleSheet("")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.mainPageCategoryAlbumsGridQFlowLayout = FlowLayout(self.frame_57)
        self.mainPageCategoryAlbumsGridQFlowLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPageCategoryAlbumsGridQFlowLayout.setSpacing(24)
        self.mainPageCategoryAlbumsGridQFlowLayout.setObjectName("mainPageCategoryAlbumsGridQFlowLayout")
        self.verticalLayout_175.addWidget(self.frame_57)
        self.mainPageCategoryPageStackedWidget.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget()
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_192 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_192.setContentsMargins(32, 0, 32, 32)
        self.verticalLayout_192.setSpacing(0)
        self.verticalLayout_192.setObjectName("verticalLayout_192")
        self.frame_61 = QtWidgets.QFrame(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy)
        self.frame_61.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_61.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_61.setStyleSheet("")
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.verticalLayout_193 = QtWidgets.QVBoxLayout(self.frame_61)
        self.verticalLayout_193.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_193.setSpacing(0)
        self.verticalLayout_193.setObjectName("verticalLayout_193")
        self.frame_240 = QtWidgets.QFrame(self.frame_61)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_240.sizePolicy().hasHeightForWidth())
        self.frame_240.setSizePolicy(sizePolicy)
        self.frame_240.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_240.setMaximumSize(QtCore.QSize(16777215, 132))
        self.frame_240.setStyleSheet("")
        self.frame_240.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_240.setObjectName("frame_240")
        self.verticalLayout_194 = QtWidgets.QVBoxLayout(self.frame_240)
        self.verticalLayout_194.setContentsMargins(0, 27, 0, 18)
        self.verticalLayout_194.setSpacing(0)
        self.verticalLayout_194.setObjectName("verticalLayout_194")
        self.mainPageCategoryPagePlaylistsCategoryNameLabel = QtWidgets.QLabel(self.frame_240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageCategoryPagePlaylistsCategoryNameLabel.sizePolicy().hasHeightForWidth())
        self.mainPageCategoryPagePlaylistsCategoryNameLabel.setSizePolicy(sizePolicy)
        self.mainPageCategoryPagePlaylistsCategoryNameLabel.setMinimumSize(QtCore.QSize(0, 52))
        self.mainPageCategoryPagePlaylistsCategoryNameLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageCategoryPagePlaylistsCategoryNameLabel.setFont(font)
        self.mainPageCategoryPagePlaylistsCategoryNameLabel.setStyleSheet("color: white;\n"
                                                                     "font: 87 17pt \"Heebo Black\";")
        self.mainPageCategoryPagePlaylistsCategoryNameLabel.setText("Rock playlists")
        self.mainPageCategoryPagePlaylistsCategoryNameLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.mainPageCategoryPagePlaylistsCategoryNameLabel.setObjectName("mainPageCategoryPagePlaylistsCategoryNameLabel")
        self.verticalLayout_194.addWidget(self.mainPageCategoryPagePlaylistsCategoryNameLabel)
        self.verticalLayout_193.addWidget(self.frame_240)
        self.verticalLayout_192.addWidget(self.frame_61)
        self.frame_62 = QtWidgets.QFrame(self.widget_3)
        self.frame_62.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_62.setStyleSheet("")
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.mainPageCategoryPlaylistsGridQGridLayout = QtWidgets.QGridLayout(self.frame_62)
        self.mainPageCategoryPlaylistsGridQGridLayout.setContentsMargins(0, 24, 0, 24)
        self.mainPageCategoryPlaylistsGridQGridLayout.setSpacing(24)
        self.mainPageCategoryPlaylistsGridQGridLayout.setObjectName("mainPageCategoryPlaylistsGridQGridLayout")
        self.verticalLayout_192.addWidget(self.frame_62)
        self.mainPageCategoryPageStackedWidget.addWidget(self.widget_3)
        self.verticalLayout_121.addWidget(self.mainPageCategoryPageStackedWidget)
        self.verticalLayout_107.addWidget(self.frame_58)
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_10)
        self.verticalLayout_84.addWidget(self.scrollArea_11)
        self.verticalLayout_55.addWidget(self.frame_82)
        self.mainPageStackedWidget.addWidget(self.mainPageCategoryPage)
        self.mainPageAlbumPage = QtWidgets.QWidget()
        self.mainPageAlbumPage.setStyleSheet("SortButtonsQFrame{\n"
                                             "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                             "}\n"
                                             "SortButtonsQFrame QPushButton{\n"
                                             "    font: 57 10pt \"Heebo Medium\";\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "SortButtonsQFrame QPushButton:hover{\n"
                                             "    color: white;\n"
                                             "}\n"
                                             "SongEntry{\n"
                                             "    border-radius: 4px;\n"
                                             "}\n"
                                             "SongEntry:hover{\n"
                                             "    background-color: rgba(179, 179, 179, 0.25);\n"
                                             "}\n"
                                             "SongEntry QPushButton{\n"
                                             "    font: 57 10pt \"Heebo Medium\";\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "SongEntry QLabel{\n"
                                             "    font: 57 10pt \"Heebo Medium\";\n"
                                             "    background-color: none;\n"
                                             "}\n"
                                             "SongEntry QPushButton:hover{\n"
                                             "    text-decoration: underline;\n"
                                             "    color: white;\n"
                                             "}\n"
                                             "QFrame#frame_268{\n"
                                             "    background-color: rgba(18, 18, 18, 0.15);\n"
                                             "}\n"
                                             "QFrame#frame_261{\n"
                                             "    background-color: rgba(18, 18, 18, 0.15);\n"
                                             "}\n"
                                             "QWidget#widget_9{\n"
                                             "    background-color: qlineargradient( x1:0 y1:0,\n"
                                             "     x2:0 y2:0.63,\n"
                                             "     stop:0 rgb(137, 153, 153),\n"
                                             "    stop:1 rgb(18, 18, 18));\n"
                                             "}")
        self.mainPageAlbumPage.setObjectName("mainPageAlbumPage")
        self.verticalLayout_224 = QtWidgets.QVBoxLayout(self.mainPageAlbumPage)
        self.verticalLayout_224.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_224.setSpacing(0)
        self.verticalLayout_224.setObjectName("verticalLayout_224")
        self.frame_257 = QtWidgets.QFrame(self.mainPageAlbumPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_257.sizePolicy().hasHeightForWidth())
        self.frame_257.setSizePolicy(sizePolicy)
        self.frame_257.setMinimumSize(QtCore.QSize(600, 530))
        self.frame_257.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_257.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_257.setObjectName("frame_257")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.frame_257)
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.scrollArea_5 = ResizeSignalScrollArea(self.frame_257)
        self.scrollArea_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy)
        self.scrollArea_5.setMinimumSize(QtCore.QSize(0, 530))
        self.scrollArea_5.setStyleSheet("")
        self.scrollArea_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.widget_9 = QtWidgets.QWidget()
        self.widget_9.setEnabled(True)
        self.widget_9.setGeometry(QtCore.QRect(0, 0, 924, 702))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setStyleSheet("")
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.mainPagePlaylistSongsHeader_2 = QtWidgets.QFrame(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPagePlaylistSongsHeader_2.sizePolicy().hasHeightForWidth())
        self.mainPagePlaylistSongsHeader_2.setSizePolicy(sizePolicy)
        self.mainPagePlaylistSongsHeader_2.setMinimumSize(QtCore.QSize(0, 0))
        self.mainPagePlaylistSongsHeader_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPagePlaylistSongsHeader_2.setStyleSheet("")
        self.mainPagePlaylistSongsHeader_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPagePlaylistSongsHeader_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPagePlaylistSongsHeader_2.setObjectName("mainPagePlaylistSongsHeader_2")
        self.verticalLayout_209 = QtWidgets.QVBoxLayout(self.mainPagePlaylistSongsHeader_2)
        self.verticalLayout_209.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_209.setSpacing(0)
        self.verticalLayout_209.setObjectName("verticalLayout_209")
        self.frame_258 = QtWidgets.QFrame(self.mainPagePlaylistSongsHeader_2)
        self.frame_258.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.frame_258.setStyleSheet("")
        self.frame_258.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_258.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_258.setObjectName("frame_258")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_258)
        self.horizontalLayout_17.setContentsMargins(32, 84, 32, 24)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.mainPageAlbumMiniatureOfAlbumQLabel = QtWidgets.QLabel(self.frame_258)

        self.shadow3 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow3.setBlurRadius(250)
        self.shadow3.setXOffset(0)
        self.shadow3.setYOffset(0)
        self.shadow3.setColor(QtGui.QColor(0, 0, 0, 192))

        self.mainPageAlbumMiniatureOfAlbumQLabel.setGraphicsEffect(self.shadow3)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAlbumMiniatureOfAlbumQLabel.sizePolicy().hasHeightForWidth())
        self.mainPageAlbumMiniatureOfAlbumQLabel.setSizePolicy(sizePolicy)
        self.mainPageAlbumMiniatureOfAlbumQLabel.setMinimumSize(QtCore.QSize(232, 232))
        self.mainPageAlbumMiniatureOfAlbumQLabel.setMaximumSize(QtCore.QSize(232, 232))
        self.mainPageAlbumMiniatureOfAlbumQLabel.setStyleSheet("")
        self.mainPageAlbumMiniatureOfAlbumQLabel.setText("")
        self.mainPageAlbumMiniatureOfAlbumQLabel.setPixmap(QtGui.QPixmap(":/icons/temporary/icons/playlistCoverExample1.png"))
        self.mainPageAlbumMiniatureOfAlbumQLabel.setScaledContents(True)
        self.mainPageAlbumMiniatureOfAlbumQLabel.setObjectName("mainPageAlbumMiniatureOfAlbumQLabel")
        self.horizontalLayout_17.addWidget(self.mainPageAlbumMiniatureOfAlbumQLabel)
        self.frame_259 = QtWidgets.QFrame(self.frame_258)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_259.sizePolicy().hasHeightForWidth())
        self.frame_259.setSizePolicy(sizePolicy)
        self.frame_259.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_259.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_259.setStyleSheet("")
        self.frame_259.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_259.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_259.setObjectName("frame_259")
        self.verticalLayout_210 = QtWidgets.QVBoxLayout(self.frame_259)
        self.verticalLayout_210.setContentsMargins(15, 0, 0, 5)
        self.verticalLayout_210.setSpacing(0)
        self.verticalLayout_210.setObjectName("verticalLayout_210")
        self.label_175 = QtWidgets.QLabel(self.frame_259)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_175.sizePolicy().hasHeightForWidth())
        self.label_175.setSizePolicy(sizePolicy)
        self.label_175.setMinimumSize(QtCore.QSize(0, 0))
        self.label_175.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_175.setFont(font)
        self.label_175.setStyleSheet("font: 87 9pt \"Heebo Black\";\n"
                                     "color: white;\n"
                                     "padding-top: -6px;")
        self.label_175.setText("ALBUM")
        self.label_175.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_175.setObjectName("label_175")
        self.verticalLayout_210.addWidget(self.label_175)
        self.mainPageAlbumNameOfAlbumLabel = QtWidgets.QLabel(self.frame_259)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAlbumNameOfAlbumLabel.sizePolicy().hasHeightForWidth())
        self.mainPageAlbumNameOfAlbumLabel.setSizePolicy(sizePolicy)
        self.mainPageAlbumNameOfAlbumLabel.setMinimumSize(QtCore.QSize(0, 52))
        self.mainPageAlbumNameOfAlbumLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(68)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.mainPageAlbumNameOfAlbumLabel.setFont(font)
        self.mainPageAlbumNameOfAlbumLabel.setStyleSheet("font: 87 68pt \"Heebo Black\";\n"
                                                         "color: white;\n"
                                                         "")
        self.mainPageAlbumNameOfAlbumLabel.setText("Lorem ipsum")
        self.mainPageAlbumNameOfAlbumLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mainPageAlbumNameOfAlbumLabel.setObjectName("mainPageAlbumNameOfAlbumLabel")
        self.verticalLayout_210.addWidget(self.mainPageAlbumNameOfAlbumLabel)
        self.frame_260 = QtWidgets.QFrame(self.frame_259)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_260.sizePolicy().hasHeightForWidth())
        self.frame_260.setSizePolicy(sizePolicy)
        self.frame_260.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_260.setStyleSheet("")
        self.frame_260.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_260.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_260.setObjectName("frame_260")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.frame_260)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setSpacing(4)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.mainPageAlbumNumberOfSongsLabel = QtWidgets.QLabel(self.frame_260)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAlbumNumberOfSongsLabel.sizePolicy().hasHeightForWidth())
        self.mainPageAlbumNumberOfSongsLabel.setSizePolicy(sizePolicy)
        self.mainPageAlbumNumberOfSongsLabel.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.mainPageAlbumNumberOfSongsLabel.setText("3 Songs,")
        self.mainPageAlbumNumberOfSongsLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mainPageAlbumNumberOfSongsLabel.setObjectName("mainPageAlbumNumberOfSongsLabel")
        self.horizontalLayout_45.addWidget(self.mainPageAlbumNumberOfSongsLabel)
        self.mainPageAlbumsLengthOfAlbumLabel = QtWidgets.QLabel(self.frame_260)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAlbumsLengthOfAlbumLabel.sizePolicy().hasHeightForWidth())
        self.mainPageAlbumsLengthOfAlbumLabel.setSizePolicy(sizePolicy)
        self.mainPageAlbumsLengthOfAlbumLabel.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.mainPageAlbumsLengthOfAlbumLabel.setText("0 h. 13 min")
        self.mainPageAlbumsLengthOfAlbumLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mainPageAlbumsLengthOfAlbumLabel.setObjectName("mainPageAlbumsLengthOfAlbumLabel")
        self.horizontalLayout_45.addWidget(self.mainPageAlbumsLengthOfAlbumLabel)
        spacerItem37 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem37)
        self.verticalLayout_210.addWidget(self.frame_260)
        self.horizontalLayout_17.addWidget(self.frame_259, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_209.addWidget(self.frame_258)
        self.frame_261 = QtWidgets.QFrame(self.mainPagePlaylistSongsHeader_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_261.sizePolicy().hasHeightForWidth())
        self.frame_261.setSizePolicy(sizePolicy)
        self.frame_261.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_261.setStyleSheet("")
        self.frame_261.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_261.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_261.setObjectName("frame_261")
        self.verticalLayout_211 = QtWidgets.QVBoxLayout(self.frame_261)
        self.verticalLayout_211.setContentsMargins(32, 24, 32, 0)
        self.verticalLayout_211.setSpacing(24)
        self.verticalLayout_211.setObjectName("verticalLayout_211")
        self.albumPlayPauseButton = QtWidgets.QPushButton(self.frame_261)
        self.albumPlayPauseButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumPlayPauseButton.sizePolicy().hasHeightForWidth())
        self.albumPlayPauseButton.setSizePolicy(sizePolicy)
        self.albumPlayPauseButton.setMinimumSize(QtCore.QSize(56, 56))
        self.albumPlayPauseButton.setMaximumSize(QtCore.QSize(56, 56))
        self.albumPlayPauseButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                     "border-radius: 28px;\n"
                                                     "text-align: center;\n"
                                                     "font: 87 9pt \"Heebo Black\";\n"
                                                     "background-color: rgb(255, 176, 85);\n"
                                                     "")
        self.albumPlayPauseButton.setText("")
        self.albumPlayPauseButton.setIcon(icon7)
        self.albumPlayPauseButton.setIconSize(QtCore.QSize(24, 24))
        self.albumPlayPauseButton.setCheckable(False)
        self.albumPlayPauseButton.setObjectName("albumPlayPauseButton")
        self.verticalLayout_211.addWidget(self.albumPlayPauseButton)

        self.AlbumSortButtonsQFrame = SortButtonsQFrame(parent=self.frame_261,
                                           frame_structure={"sortButtonsQFrameTitleButtonQFrame": True,
                                                            "sortButtonsQFrameAuthorButtonQFrame": True,
                                                            "sortButtonsQFrameCategoryButtonQFrame": False,
                                                            "sortButtonsQFrameDateAddedButtonQFrame": False,
                                                            "sortButtonsQFrameSongLengthButtonQFrame": True},
                                           visibility_changing_sort_buttons_elements=[
                                               ("sortButtonsQFrameAuthorButtonQFrame", 552)]
                                           )
        self.AlbumSortButtonsQFrame.setObjectName("AlbumSortButtonsQFrame")
        self.verticalLayout_211.addWidget(self.AlbumSortButtonsQFrame)

        self.verticalLayout_209.addWidget(self.frame_261)
        self.verticalLayout_57.addWidget(self.mainPagePlaylistSongsHeader_2)
        self.frame_268 = QtWidgets.QFrame(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_268.sizePolicy().hasHeightForWidth())
        self.frame_268.setSizePolicy(sizePolicy)
        self.frame_268.setStyleSheet("")
        self.frame_268.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_268.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_268.setObjectName("frame_268")
        self.mainPageAlbumSongsListQVBoxLayout = QtWidgets.QVBoxLayout(self.frame_268)
        self.mainPageAlbumSongsListQVBoxLayout.setContentsMargins(32, 17, 32, 32)
        self.mainPageAlbumSongsListQVBoxLayout.setSpacing(0)
        self.mainPageAlbumSongsListQVBoxLayout.setObjectName("mainPageAlbumSongsListQVBoxLayout")
        self.verticalLayout_57.addWidget(self.frame_268)
        self.scrollArea_5.setWidget(self.widget_9)
        self.verticalLayout_56.addWidget(self.scrollArea_5)
        self.verticalLayout_224.addWidget(self.frame_257)
        self.mainPageStackedWidget.addWidget(self.mainPageAlbumPage)
        self.mainPageSongQueue = QtWidgets.QWidget()
        self.mainPageSongQueue.setStyleSheet("SongEntry{\n"
                                             "    border-radius: 4px;\n"
                                             "}\n"
                                             "SongEntry:hover{\n"
                                             "    background-color: rgba(179, 179, 179, 0.25);\n"
                                             "}\n"
                                             "SongEntry QPushButton{\n"
                                             "    font: 57 10pt \"Heebo Medium\";\n"
                                             "}\n"
                                             "SongEntry QLabel{\n"
                                             "    font: 57 10pt \"Heebo Medium\";\n"
                                             "    background-color: none;\n"
                                             "}\n"
                                             "SongEntry QPushButton:hover{\n"
                                             "    text-decoration: underline;\n"
                                             "    color: white;\n"
                                             "}\n"
                                             "#scrollAreaWidgetContents_3{\n"
                                             "    background-color: rgb(18, 18, 18);\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "")
        self.mainPageSongQueue.setObjectName("mainPageSongQueue")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.mainPageSongQueue)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_190 = QtWidgets.QFrame(self.mainPageSongQueue)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_190.sizePolicy().hasHeightForWidth())
        self.frame_190.setSizePolicy(sizePolicy)
        self.frame_190.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_190.setStyleSheet("")
        self.frame_190.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_190.setObjectName("frame_190")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.frame_190)
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.scrollArea_12 = ResizeSignalScrollArea(self.frame_190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_12.sizePolicy().hasHeightForWidth())
        self.scrollArea_12.setSizePolicy(sizePolicy)
        self.scrollArea_12.setMinimumSize(QtCore.QSize(585, 493))
        self.scrollArea_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea_12.setFont(font)
        self.scrollArea_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_12.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_12.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollArea_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_12.setObjectName("scrollArea_12")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1424, 573))
        self.scrollAreaWidgetContents_3.setStyleSheet("")
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_164 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_164.setContentsMargins(0, 105, 0, 0)
        self.verticalLayout_164.setSpacing(0)
        self.verticalLayout_164.setObjectName("verticalLayout_164")
        self.frame_191 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_191.sizePolicy().hasHeightForWidth())
        self.frame_191.setSizePolicy(sizePolicy)
        self.frame_191.setMinimumSize(QtCore.QSize(0, 178))
        self.frame_191.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_191.setStyleSheet("")
        self.frame_191.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_191.setObjectName("frame_191")
        self.verticalLayout_230 = QtWidgets.QVBoxLayout(self.frame_191)
        self.verticalLayout_230.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout_230.setSpacing(0)
        self.verticalLayout_230.setObjectName("verticalLayout_230")
        self.frame_192 = QtWidgets.QFrame(self.frame_191)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_192.sizePolicy().hasHeightForWidth())
        self.frame_192.setSizePolicy(sizePolicy)
        self.frame_192.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_192.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_192.setStyleSheet("")
        self.frame_192.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_192.setObjectName("frame_192")
        self.verticalLayout_72 = QtWidgets.QVBoxLayout(self.frame_192)
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.label_201 = QtWidgets.QLabel(self.frame_192)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_201.sizePolicy().hasHeightForWidth())
        self.label_201.setSizePolicy(sizePolicy)
        self.label_201.setMinimumSize(QtCore.QSize(0, 52))
        self.label_201.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_201.setFont(font)
        self.label_201.setStyleSheet("color: white;\n"
                                     "font: 87 17pt \"Heebo Black\";")
        self.label_201.setText("Song Queue")
        self.label_201.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_201.setObjectName("label_201")
        self.verticalLayout_72.addWidget(self.label_201)
        self.frame_193 = QtWidgets.QFrame(self.frame_192)
        self.frame_193.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_193.setObjectName("frame_193")
        self.mainPageSongQueueNowPlayingSongQVBoxLayout = QtWidgets.QVBoxLayout(self.frame_193)
        self.mainPageSongQueueNowPlayingSongQVBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPageSongQueueNowPlayingSongQVBoxLayout.setSpacing(0)
        self.mainPageSongQueueNowPlayingSongQVBoxLayout.setObjectName("mainPageSongQueueNowPlayingSongQVBoxLayout")
        self.label_197 = QtWidgets.QLabel(self.frame_193)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_197.sizePolicy().hasHeightForWidth())
        self.label_197.setSizePolicy(sizePolicy)
        self.label_197.setStyleSheet("font: 87 11pt \"Heebo Black\";")
        self.label_197.setText("Now Playing")
        self.label_197.setObjectName("label_197")
        self.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(self.label_197)
        self.verticalLayout_72.addWidget(self.frame_193)
        self.verticalLayout_230.addWidget(self.frame_192)
        self.verticalLayout_164.addWidget(self.frame_191)
        self.frame_194 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_194.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_194.setObjectName("frame_194")
        self.verticalLayout_163 = QtWidgets.QVBoxLayout(self.frame_194)
        self.verticalLayout_163.setContentsMargins(32, 48, 32, 0)
        self.verticalLayout_163.setSpacing(0)
        self.verticalLayout_163.setObjectName("verticalLayout_163")
        self.label_202 = QtWidgets.QLabel(self.frame_194)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_202.sizePolicy().hasHeightForWidth())
        self.label_202.setSizePolicy(sizePolicy)
        self.label_202.setStyleSheet("font: 87 11pt \"Heebo Black\";")
        self.label_202.setText("Playing next")
        self.label_202.setObjectName("label_202")
        self.verticalLayout_163.addWidget(self.label_202)
        self.frame_299 = QtWidgets.QFrame(self.frame_194)
        self.frame_299.setStyleSheet("")
        self.frame_299.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_299.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_299.setObjectName("frame_299")
        self.mainPageSongQueueSongListQVBoxLayout = QtWidgets.QVBoxLayout(self.frame_299)
        self.mainPageSongQueueSongListQVBoxLayout.setContentsMargins(0, 20, 0, 32)
        self.mainPageSongQueueSongListQVBoxLayout.setSpacing(0)
        self.mainPageSongQueueSongListQVBoxLayout.setObjectName("mainPageSongQueueSongListQVBoxLayout")
        self.verticalLayout_163.addWidget(self.frame_299)
        self.verticalLayout_164.addWidget(self.frame_194)
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_58.addWidget(self.scrollArea_12)
        self.verticalLayout_7.addWidget(self.frame_190)
        self.mainPageStackedWidget.addWidget(self.mainPageSongQueue)

        self.mainPageAlbumsPage = QtWidgets.QWidget()
        self.mainPageAlbumsPage.setStyleSheet("AlbumEntry, AdderEntry{\n"
                                              "    background-color: rgb(24, 24, 24);\n"
                                              "    border-radius: 4px;\n"
                                              "}\n"
                                              "AlbumEntry:hover, AdderEntry:hover{\n"
                                              "    background-color: rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "QFrame#frame_218{\n"
                                              "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                              "}\n"
                                              "QWidget#scrollAreaWidgetContents_11{\n"
                                              "    background-color: rgb(18, 18, 18);\n"
                                              "}")
        self.mainPageAlbumsPage.setObjectName("mainPageAlbumsPage")
        self.verticalLayout_249 = QtWidgets.QVBoxLayout(self.mainPageAlbumsPage)
        self.verticalLayout_249.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_249.setSpacing(0)
        self.verticalLayout_249.setObjectName("verticalLayout_249")
        self.frame_132 = QtWidgets.QFrame(self.mainPageAlbumsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_132.sizePolicy().hasHeightForWidth())
        self.frame_132.setSizePolicy(sizePolicy)
        self.frame_132.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_132.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_132.setObjectName("frame_132")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.frame_132)
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.scrollArea_13 = ResizeSignalScrollArea(self.frame_132)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_13.sizePolicy().hasHeightForWidth())
        self.scrollArea_13.setSizePolicy(sizePolicy)
        self.scrollArea_13.setMinimumSize(QtCore.QSize(585, 493))
        self.scrollArea_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea_13.setFont(font)
        self.scrollArea_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_13.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_13.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollArea_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_13.setObjectName("scrollArea_13")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 900, 792))
        self.scrollAreaWidgetContents_11.setStyleSheet("")
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.verticalLayout_68 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_68.setContentsMargins(0, 8, 0, 32)
        self.verticalLayout_68.setSpacing(24)
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.frame_188 = QtWidgets.QFrame(self.scrollAreaWidgetContents_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_188.sizePolicy().hasHeightForWidth())
        self.frame_188.setSizePolicy(sizePolicy)
        self.frame_188.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_188.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_188.setStyleSheet("")
        self.frame_188.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_188.setObjectName("frame_188")
        self.verticalLayout_81 = QtWidgets.QVBoxLayout(self.frame_188)
        self.verticalLayout_81.setContentsMargins(32, 60, 32, 0)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName("verticalLayout_81")
        self.frame_218 = QtWidgets.QFrame(self.frame_188)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_218.sizePolicy().hasHeightForWidth())
        self.frame_218.setSizePolicy(sizePolicy)
        self.frame_218.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_218.setMaximumSize(QtCore.QSize(16777215, 132))
        self.frame_218.setStyleSheet("")
        self.frame_218.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_218.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_218.setObjectName("frame_218")
        self.verticalLayout_83 = QtWidgets.QVBoxLayout(self.frame_218)
        self.verticalLayout_83.setContentsMargins(0, 27, 0, 18)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName("verticalLayout_83")
        self.label_146 = QtWidgets.QLabel(self.frame_218)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_146.sizePolicy().hasHeightForWidth())
        self.label_146.setSizePolicy(sizePolicy)
        self.label_146.setMinimumSize(QtCore.QSize(0, 52))
        self.label_146.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_146.setFont(font)
        self.label_146.setStyleSheet("color: white;\n"
                                     "font: 87 17pt \"Heebo Black\";")
        self.label_146.setText("Albums")
        self.label_146.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_146.setObjectName("label_146")
        self.verticalLayout_83.addWidget(self.label_146)
        self.verticalLayout_81.addWidget(self.frame_218)
        self.verticalLayout_68.addWidget(self.frame_188)
        self.frame_224 = QtWidgets.QFrame(self.scrollAreaWidgetContents_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_224.sizePolicy().hasHeightForWidth())
        self.frame_224.setSizePolicy(sizePolicy)
        self.frame_224.setStyleSheet("")
        self.frame_224.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_224.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_224.setObjectName("frame_224")
        self.verticalLayout_149 = QtWidgets.QVBoxLayout(self.frame_224)
        self.verticalLayout_149.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout_149.setSpacing(0)
        self.verticalLayout_149.setObjectName("verticalLayout_149")
        self.mainPageAlbumsAlbumsGridFrame = QtWidgets.QFrame(self.frame_224)
        self.mainPageAlbumsAlbumsGridFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainPageAlbumsAlbumsGridFrame.setStyleSheet("")
        self.mainPageAlbumsAlbumsGridFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPageAlbumsAlbumsGridFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPageAlbumsAlbumsGridFrame.setObjectName("mainPageAlbumsAlbumsGridFrame")
        self.mainPageAlbumsAlbumsGridQFlowLayout = FlowLayout(self.mainPageAlbumsAlbumsGridFrame)
        self.mainPageAlbumsAlbumsGridQFlowLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPageAlbumsAlbumsGridQFlowLayout.setSpacing(24)
        self.mainPageAlbumsAlbumsGridQFlowLayout.setObjectName("mainPageAlbumsAlbumsGridQFlowLayout")
        self.verticalLayout_149.addWidget(self.mainPageAlbumsAlbumsGridFrame)
        self.verticalLayout_68.addWidget(self.frame_224)
        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_11)
        self.verticalLayout_49.addWidget(self.scrollArea_13)
        self.verticalLayout_249.addWidget(self.frame_132)
        self.mainPageStackedWidget.addWidget(self.mainPageAlbumsPage)



        self.mainPageAllSongs = QtWidgets.QWidget()
        self.mainPageAllSongs.setStyleSheet("SongEntry{\n"
                                            "    border-radius: 4px;\n"
                                            "}\n"
                                            "SongAdder{\n"
                                            "    border-radius: 4px;\n"
                                            "}\n"
                                            "SongEntry:hover{\n"
                                            "    background-color: rgba(179, 179, 179, 0.25);\n"
                                            "}\n"
                                            "SongAdder:hover{\n"
                                            "    background-color: rgba(179, 179, 179, 0.25);\n"
                                            "}\n"
                                            "SongEntry QPushButton{\n"
                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                            "}\n"
                                            "SongEntry QLabel{\n"
                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                            "    background-color: none;\n"
                                            "}\n"
                                            "SongEntry QPushButton:hover{\n"
                                            "    text-decoration: underline;\n"
                                            "    color: white;\n"
                                            "}\n"
                                            "QFrame#frame_402 QPushButton{\n"
                                            "    border: none;\n"
                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                            "}\n"
                                            "#scrollAreaWidgetContents_6{\n"
                                            "    background-color: rgb(18, 18, 18);\n"
                                            "}\n"
                                            "#frame_447{\n"
                                            "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                            "}\n"
                                            "SortButtonsQFrame{\n"
                                            "    border-bottom: 1px solid rgba(179, 179, 179, 0.25);\n"
                                            "}\n"
                                            "SortButtonsQFrame QPushButton:hover{\n"
                                                "color: white;\n"
                                            "}\n"
                                            "SortButtonsQFrame QPushButton{\n"
                                                "font: 57 10pt \"Heebo Medium\";\n"
                                            "}\n"
                                            "#mainPageAllSongAddSongQPushButton:hover{\n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_add_white_48dp.png);\n"
                                            "}\n"
                                            "#mainPageAllSongAddSongQPushButton:pressed{\n"
                                            "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_add_gray_48dp.png);\n"
                                            "}\n"
                                            "QComboBox {\n"
                                            "    color: rgb(185, 185, 185);\n"
                                            "    background-color: rgba(179, 179, 179, 0.25);\n"
                                            "    border: 1px solid transparent;\n"
                                            "    padding-right: 12px;\n"
                                            "    padding-left: 12px;\n"
                                            "    padding-top: 12px;\n"
                                            "    padding-bottom: 12px;\n"
                                            "    border-radius: 4px;\n"
                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                            "}\n"
                                            "QComboBox:on{\n"
                                            "    border: 1px solid rgba(179, 179, 179, 0.25);\n"
                                            "    border-bottom-right-radius: 0px;\n"
                                            "    border-bottom-left-radius: 0px;\n"
                                            "    background-color: rgb(51, 51, 51);\n"
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
                                            "\n"
                                            "QLineEdit {\n"
                                            "    font: 57 10pt \"Heebo Medium\";\n"
                                            "    color: white;\n"
                                            "    background-color: rgba(179, 179, 179, 0.25);\n"
                                            "    border: 1px solid transparent;\n"
                                            "    padding-right: 12px;\n"
                                            "    padding-left: 12px;\n"
                                            "    padding-top: 12px;\n"
                                            "    padding-bottom: 12px;\n"
                                            "    border-radius: 4px;\n"
                                            "}\n"
                                            "QLineEdit:focus{\n"
                                            "    border: 1px solid rgba(179, 179, 179, 0.25);\n"
                                            "    background-color: rgb(51, 51, 51);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")
        self.mainPageAllSongs.setObjectName("mainPageAllSongs")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mainPageAllSongs)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_401 = QtWidgets.QFrame(self.mainPageAllSongs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_401.sizePolicy().hasHeightForWidth())
        self.frame_401.setSizePolicy(sizePolicy)
        self.frame_401.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_401.setStyleSheet("")
        self.frame_401.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_401.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_401.setObjectName("frame_401")
        self.verticalLayout_250 = QtWidgets.QVBoxLayout(self.frame_401)
        self.verticalLayout_250.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_250.setSpacing(0)
        self.verticalLayout_250.setObjectName("verticalLayout_250")
        self.scrollArea_14 = ResizeSignalScrollArea(self.frame_401)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_14.sizePolicy().hasHeightForWidth())
        self.scrollArea_14.setSizePolicy(sizePolicy)
        self.scrollArea_14.setMinimumSize(QtCore.QSize(585, 493))
        self.scrollArea_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea_14.setFont(font)
        self.scrollArea_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_14.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_14.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollArea_14.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.scrollArea_14.setObjectName("scrollArea_14")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 1674, 610))
        self.scrollAreaWidgetContents_6.setStyleSheet("")
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_253 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_253.setContentsMargins(0, 105, 0, 0)
        self.verticalLayout_253.setSpacing(0)
        self.verticalLayout_253.setObjectName("verticalLayout_253")
        self.frame_402 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_402.sizePolicy().hasHeightForWidth())
        self.frame_402.setSizePolicy(sizePolicy)
        self.frame_402.setMinimumSize(QtCore.QSize(0, 178))
        self.frame_402.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_402.setStyleSheet("")
        self.frame_402.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_402.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_402.setObjectName("frame_402")
        self.verticalLayout_254 = QtWidgets.QVBoxLayout(self.frame_402)
        self.verticalLayout_254.setContentsMargins(32, 0, 32, 0)
        self.verticalLayout_254.setSpacing(0)
        self.verticalLayout_254.setObjectName("verticalLayout_254")
        self.frame_405 = QtWidgets.QFrame(self.frame_402)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_405.sizePolicy().hasHeightForWidth())
        self.frame_405.setSizePolicy(sizePolicy)
        self.frame_405.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_405.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_405.setStyleSheet("")
        self.frame_405.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_405.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_405.setObjectName("frame_405")
        self.verticalLayout_255 = QtWidgets.QVBoxLayout(self.frame_405)
        self.verticalLayout_255.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_255.setSpacing(0)
        self.verticalLayout_255.setObjectName("verticalLayout_255")
        self.label_251 = QtWidgets.QLabel(self.frame_405)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_251.sizePolicy().hasHeightForWidth())
        self.label_251.setSizePolicy(sizePolicy)
        self.label_251.setMinimumSize(QtCore.QSize(0, 52))
        self.label_251.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_251.setFont(font)
        self.label_251.setStyleSheet("color: white;\n"
                                     "font: 87 17pt \"Heebo Black\";")
        self.label_251.setText("All songs")
        self.label_251.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_251.setObjectName("label_251")
        self.verticalLayout_255.addWidget(self.label_251)
        self.frame_406 = QtWidgets.QFrame(self.frame_405)
        self.frame_406.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_406.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_406.setObjectName("frame_406")
        self.verticalLayout_280 = QtWidgets.QVBoxLayout(self.frame_406)
        self.verticalLayout_280.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_280.setSpacing(9)
        self.verticalLayout_280.setObjectName("verticalLayout_280")
        self.label_252 = QtWidgets.QLabel(self.frame_406)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_252.sizePolicy().hasHeightForWidth())
        self.label_252.setSizePolicy(sizePolicy)
        self.label_252.setStyleSheet("font: 87 11pt \"Heebo Black\";")
        self.label_252.setText("Add new song")
        self.label_252.setObjectName("label_252")
        self.verticalLayout_280.addWidget(self.label_252)
        self.frame_447 = QtWidgets.QFrame(self.frame_406)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_447.sizePolicy().hasHeightForWidth())
        self.frame_447.setSizePolicy(sizePolicy)
        self.frame_447.setMinimumSize(QtCore.QSize(0, 41))
        self.frame_447.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_447.setStyleSheet("")
        self.frame_447.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_447.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_447.setObjectName("frame_447")
        self.horizontalLayout_125 = QtWidgets.QHBoxLayout(self.frame_447)
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName("horizontalLayout_125")
        spacerItem44 = QtWidgets.QSpacerItem(110, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_125.addItem(spacerItem44)
        self.frame_448 = QtWidgets.QFrame(self.frame_447)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_448.sizePolicy().hasHeightForWidth())
        self.frame_448.setSizePolicy(sizePolicy)
        self.frame_448.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_448.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.frame_448.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_448.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_448.setObjectName("frame_448")
        self.verticalLayout_270 = QtWidgets.QVBoxLayout(self.frame_448)
        self.verticalLayout_270.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_270.setSpacing(0)
        self.verticalLayout_270.setObjectName("verticalLayout_270")
        self.label_143 = QtWidgets.QLabel(self.frame_448)
        self.label_143.setText("Song file")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_143.sizePolicy().hasHeightForWidth())
        self.label_143.setSizePolicy(sizePolicy)
        self.label_143.setObjectName("label_143")
        self.verticalLayout_270.addWidget(self.label_143)
        self.horizontalLayout_125.addWidget(self.frame_448)
        self.frame_449 = QtWidgets.QFrame(self.frame_447)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_449.sizePolicy().hasHeightForWidth())
        self.frame_449.setSizePolicy(sizePolicy)
        self.frame_449.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_449.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.frame_449.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_449.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_449.setObjectName("frame_449")
        self.verticalLayout_271 = QtWidgets.QVBoxLayout(self.frame_449)
        self.verticalLayout_271.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_271.setSpacing(0)
        self.verticalLayout_271.setObjectName("verticalLayout_271")
        self.label_255 = QtWidgets.QLabel(self.frame_449)
        self.label_255.setText("Song miniature")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_255.sizePolicy().hasHeightForWidth())
        self.label_255.setSizePolicy(sizePolicy)
        self.label_255.setStyleSheet("")
        self.label_255.setObjectName("label_255")
        self.verticalLayout_271.addWidget(self.label_255)
        self.horizontalLayout_125.addWidget(self.frame_449)
        self.frame_450 = QtWidgets.QFrame(self.frame_447)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_450.sizePolicy().hasHeightForWidth())
        self.frame_450.setSizePolicy(sizePolicy)
        self.frame_450.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_450.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.frame_450.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_450.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_450.setObjectName("frame_450")
        self.verticalLayout_272 = QtWidgets.QVBoxLayout(self.frame_450)
        self.verticalLayout_272.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_272.setSpacing(0)
        self.verticalLayout_272.setObjectName("verticalLayout_272")
        self.label_256 = QtWidgets.QLabel(self.frame_450)
        self.label_256.setText("Song title")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_256.sizePolicy().hasHeightForWidth())
        self.label_256.setSizePolicy(sizePolicy)
        self.label_256.setObjectName("label_256")
        self.verticalLayout_272.addWidget(self.label_256)
        self.horizontalLayout_125.addWidget(self.frame_450)
        self.frame_451 = QtWidgets.QFrame(self.frame_447)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_451.sizePolicy().hasHeightForWidth())
        self.frame_451.setSizePolicy(sizePolicy)
        self.frame_451.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_451.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.frame_451.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_451.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_451.setObjectName("frame_451")
        self.verticalLayout_273 = QtWidgets.QVBoxLayout(self.frame_451)
        self.verticalLayout_273.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_273.setSpacing(0)
        self.verticalLayout_273.setObjectName("verticalLayout_273")
        self.label_257 = QtWidgets.QLabel(self.frame_451)
        self.label_257.setText("Song author")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_257.sizePolicy().hasHeightForWidth())
        self.label_257.setSizePolicy(sizePolicy)
        self.label_257.setObjectName("label_257")
        self.verticalLayout_273.addWidget(self.label_257)
        self.horizontalLayout_125.addWidget(self.frame_451)
        self.frame_452 = QtWidgets.QFrame(self.frame_447)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_452.sizePolicy().hasHeightForWidth())
        self.frame_452.setSizePolicy(sizePolicy)
        self.frame_452.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_452.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.frame_452.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_452.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_452.setObjectName("frame_452")
        self.verticalLayout_274 = QtWidgets.QVBoxLayout(self.frame_452)
        self.verticalLayout_274.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_274.setSpacing(0)
        self.verticalLayout_274.setObjectName("verticalLayout_274")
        self.label_273 = QtWidgets.QLabel(self.frame_452)
        self.label_273.setText("Song category")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_273.sizePolicy().hasHeightForWidth())
        self.label_273.setSizePolicy(sizePolicy)
        self.label_273.setObjectName("label_273")
        self.verticalLayout_274.addWidget(self.label_273)
        self.horizontalLayout_125.addWidget(self.frame_452)
        self.frame_456 = QtWidgets.QFrame(self.frame_447)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_456.sizePolicy().hasHeightForWidth())
        self.frame_456.setSizePolicy(sizePolicy)
        self.frame_456.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_456.setStyleSheet("font: 57 10pt \"Heebo Medium\";")
        self.frame_456.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_456.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_456.setObjectName("frame_456")
        self.verticalLayout_279 = QtWidgets.QVBoxLayout(self.frame_456)
        self.verticalLayout_279.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_279.setSpacing(0)
        self.verticalLayout_279.setObjectName("verticalLayout_279")
        self.label_274 = QtWidgets.QLabel(self.frame_456)
        self.label_274.setText("Song album")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_274.sizePolicy().hasHeightForWidth())
        self.label_274.setSizePolicy(sizePolicy)
        self.label_274.setObjectName("label_274")
        self.verticalLayout_279.addWidget(self.label_274)
        self.horizontalLayout_125.addWidget(self.frame_456)
        self.verticalLayout_280.addWidget(self.frame_447)

        self.mainPageAllSongsSongAdderQFrame = SongAdder(self.frame_406)
        self.verticalLayout_280.addWidget(self.mainPageAllSongsSongAdderQFrame)

        self.verticalLayout_255.addWidget(self.frame_406)
        self.verticalLayout_254.addWidget(self.frame_405)
        self.verticalLayout_253.addWidget(self.frame_402)
        self.frame_413 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_413.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_413.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_413.setObjectName("frame_413")
        self.verticalLayout_285 = QtWidgets.QVBoxLayout(self.frame_413)
        self.verticalLayout_285.setContentsMargins(32, 48, 32, 0)
        self.verticalLayout_285.setSpacing(0)
        self.verticalLayout_285.setObjectName("verticalLayout_285")
        self.label_258 = QtWidgets.QLabel(self.frame_413)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_258.sizePolicy().hasHeightForWidth())
        self.label_258.setSizePolicy(sizePolicy)
        self.label_258.setStyleSheet("font: 87 11pt \"Heebo Black\";")
        self.label_258.setText("Songs list")
        self.label_258.setObjectName("label_258")
        self.verticalLayout_285.addWidget(self.label_258)

        self.allSongsSortButtonsQFrame = SortButtonsQFrame(parent=self.frame_413,
                                           frame_structure={"sortButtonsQFrameTitleButtonQFrame": True,
                                                            "sortButtonsQFrameAuthorButtonQFrame": True,
                                                            "sortButtonsQFrameCategoryButtonQFrame": True,
                                                            "sortButtonsQFrameDateAddedButtonQFrame": True,
                                                            "sortButtonsQFrameSongLengthButtonQFrame": True},
                                           visibility_changing_sort_buttons_elements=[
                                               ("sortButtonsQFrameAuthorButtonQFrame", 552),
                                               ("sortButtonsQFrameCategoryButtonQFrame", 726),
                                               ("sortButtonsQFrameDateAddedButtonQFrame", 950)]
                                           )
        self.allSongsSortButtonsQFrame.setObjectName("allSongsSortButtonsQFrame")
        self.verticalLayout_285.addWidget(self.allSongsSortButtonsQFrame)

        self.frame_414 = QtWidgets.QFrame(self.frame_413)
        self.frame_414.setStyleSheet("")
        self.frame_414.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_414.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_414.setObjectName("frame_414")

        self.mainPageAllSongsSongListQVBoxLayout = QtWidgets.QVBoxLayout(self.frame_414)
        self.mainPageAllSongsSongListQVBoxLayout.setContentsMargins(0, 20, 0, 32)
        self.mainPageAllSongsSongListQVBoxLayout.setSpacing(0)
        self.mainPageAllSongsSongListQVBoxLayout.setObjectName("mainPageAllSongsSongListQVBoxLayout")
        self.verticalLayout_285.addWidget(self.frame_414)
        self.verticalLayout_253.addWidget(self.frame_413)
        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_250.addWidget(self.scrollArea_14)
        self.verticalLayout_4.addWidget(self.frame_401)
        self.mainPageStackedWidget.addWidget(self.mainPageAllSongs)



        self.mainLayout.addWidget(self.mainPageStackedWidget, 0, 1, 1, 1)
        self.leftMenuFrame = QtWidgets.QFrame(self.centralPageAppPage)
        self.leftMenuFrame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuFrame.setSizePolicy(sizePolicy)
        self.leftMenuFrame.setMinimumSize(QtCore.QSize(200, 530))
        self.leftMenuFrame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.leftMenuFrame.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.leftMenuFrame.setFont(font)
        self.leftMenuFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leftMenuFrame.setStyleSheet("font: 87 10pt \"Heebo Black\";\n"
                                         "background-color: rgb(0, 0, 0);\n"
                                         "\n"
                                         "")
        self.leftMenuFrame.setObjectName("leftMenuFrame")
        self.verticalLayout_252 = QtWidgets.QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_252.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_252.setSpacing(0)
        self.verticalLayout_252.setObjectName("verticalLayout_252")
        self.leftMenuNavigationFrame = QtWidgets.QFrame(self.leftMenuFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuNavigationFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuNavigationFrame.setSizePolicy(sizePolicy)
        self.leftMenuNavigationFrame.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.leftMenuNavigationFrame.setFont(font)
        self.leftMenuNavigationFrame.setStyleSheet("QPushButton{\n"
                                                   "    padding-left: 20px;\n"
                                                   "    border-radius: 4px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "\n"
                                                   "QPushButton#nowPlayingButton:hover:!checked{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_album_white_48dp.png);\n"
                                                   "}\n"
                                                   "QPushButton#nowPlayingButton:checked{\n"
                                                   "    background-color: rgba(179, 179, 179, 0.25);\n"
                                                   "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_album_white_48dp.png);\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "}\n"
                                                   "\n"
                                                   "\n"
                                                   "QPushButton#miniPlayerButton:hover:!checked{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_picture_in_picture_white_48dp.png);\n"
                                                   "}\n"
                                                   "QPushButton#miniPlayerButton:checked{\n"
                                                   "    background-color: rgba(179, 179, 179, 0.25);\n"
                                                   "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_picture_in_picture_white_48dp.png);\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton#categoriesButton:hover:!checked{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_list_white_48dp.png);\n"
                                                   "}\n"
                                                   "QPushButton#categoriesButton:checked{\n"
                                                   "    background-color: rgba(179, 179, 179, 0.25);\n"
                                                   "    icon: url(:/icons/48x48/filled/icons/48x48/filled/baseline_list_white_48dp.png);\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "}\n"
                                                   "")
        self.leftMenuNavigationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftMenuNavigationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuNavigationFrame.setObjectName("leftMenuNavigationFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuNavigationFrame)
        self.verticalLayout.setContentsMargins(8, 47, 8, 23)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nowPlayingButton = QtWidgets.QPushButton(self.leftMenuNavigationFrame)
        self.nowPlayingButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nowPlayingButton.sizePolicy().hasHeightForWidth())
        self.nowPlayingButton.setSizePolicy(sizePolicy)
        self.nowPlayingButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        font.setKerning(True)
        self.nowPlayingButton.setFont(font)
        self.nowPlayingButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nowPlayingButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.nowPlayingButton.setStyleSheet("")
        self.nowPlayingButton.setText("   Now playing")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_album_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nowPlayingButton.setIcon(icon10)
        self.nowPlayingButton.setIconSize(QtCore.QSize(26, 26))
        self.nowPlayingButton.setCheckable(True)
        self.nowPlayingButton.setChecked(False)
        self.nowPlayingButton.setAutoRepeat(False)
        self.nowPlayingButton.setAutoExclusive(False)
        self.nowPlayingButton.setObjectName("nowPlayingButton")
        self.verticalLayout.addWidget(self.nowPlayingButton)
        self.miniPlayerButton = QtWidgets.QPushButton(self.leftMenuNavigationFrame)
        self.miniPlayerButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miniPlayerButton.sizePolicy().hasHeightForWidth())
        self.miniPlayerButton.setSizePolicy(sizePolicy)
        self.miniPlayerButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.miniPlayerButton.setFont(font)
        self.miniPlayerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.miniPlayerButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.miniPlayerButton.setText("   Mini player")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_picture_in_picture_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.miniPlayerButton.setIcon(icon11)
        self.miniPlayerButton.setIconSize(QtCore.QSize(26, 26))
        self.miniPlayerButton.setCheckable(True)
        self.miniPlayerButton.setChecked(False)
        self.miniPlayerButton.setAutoRepeat(False)
        self.miniPlayerButton.setAutoExclusive(False)
        self.miniPlayerButton.setObjectName("miniPlayerButton")
        self.verticalLayout.addWidget(self.miniPlayerButton)
        self.categoriesButton = QtWidgets.QPushButton(self.leftMenuNavigationFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoriesButton.sizePolicy().hasHeightForWidth())
        self.categoriesButton.setSizePolicy(sizePolicy)
        self.categoriesButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.categoriesButton.setFont(font)
        self.categoriesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.categoriesButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.categoriesButton.setStyleSheet("")
        self.categoriesButton.setText("   Categories")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_list_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.categoriesButton.setIcon(icon12)
        self.categoriesButton.setIconSize(QtCore.QSize(28, 28))
        self.categoriesButton.setCheckable(True)
        self.categoriesButton.setChecked(False)
        self.categoriesButton.setAutoExclusive(False)
        self.categoriesButton.setObjectName("categoriesButton")
        self.verticalLayout.addWidget(self.categoriesButton)
        self.verticalLayout_252.addWidget(self.leftMenuNavigationFrame)
        self.leftMenuBottomLibraryFrame = QtWidgets.QFrame(self.leftMenuFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuBottomLibraryFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuBottomLibraryFrame.setSizePolicy(sizePolicy)
        self.leftMenuBottomLibraryFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.leftMenuBottomLibraryFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leftMenuBottomLibraryFrame.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.leftMenuBottomLibraryFrame.setFont(font)
        self.leftMenuBottomLibraryFrame.setStyleSheet("QPushButton{\n"
                                                      "    padding-left: 24px;\n"
                                                      "    padding-right: 24px;\n"
                                                      "}\n"
                                                      "QPushButton:hover:!checked{\n"
                                                      "    color:white;\n"
                                                      "}\n"
                                                      "QPushButton:checked{\n"
                                                      "    color: white;\n"
                                                      "}\n"
                                                      "")
        self.leftMenuBottomLibraryFrame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.leftMenuBottomLibraryFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuBottomLibraryFrame.setObjectName("leftMenuBottomLibraryFrame")
        self.verticalLayout_251 = QtWidgets.QVBoxLayout(self.leftMenuBottomLibraryFrame)
        self.verticalLayout_251.setContentsMargins(0, 0, 20, 23)
        self.verticalLayout_251.setSpacing(14)
        self.verticalLayout_251.setObjectName("verticalLayout_251")
        self.frame_403 = QtWidgets.QFrame(self.leftMenuBottomLibraryFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_403.sizePolicy().hasHeightForWidth())
        self.frame_403.setSizePolicy(sizePolicy)
        self.frame_403.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_403.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_403.setObjectName("frame_403")
        self.horizontalLayout_111 = QtWidgets.QHBoxLayout(self.frame_403)
        self.horizontalLayout_111.setContentsMargins(24, 0, 0, 0)
        self.horizontalLayout_111.setSpacing(0)
        self.horizontalLayout_111.setObjectName("horizontalLayout_111")
        self.frame_404 = QtWidgets.QFrame(self.frame_403)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_404.sizePolicy().hasHeightForWidth())
        self.frame_404.setSizePolicy(sizePolicy)
        self.frame_404.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_404.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_404.setObjectName("frame_404")
        self.horizontalLayout_112 = QtWidgets.QHBoxLayout(self.frame_404)
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_112.setSpacing(6)
        self.horizontalLayout_112.setObjectName("horizontalLayout_112")
        self.label_253 = QtWidgets.QLabel(self.frame_404)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_253.sizePolicy().hasHeightForWidth())
        self.label_253.setSizePolicy(sizePolicy)
        self.label_253.setMinimumSize(QtCore.QSize(20, 20))
        self.label_253.setMaximumSize(QtCore.QSize(20, 20))
        self.label_253.setSizeIncrement(QtCore.QSize(0, 1))
        self.label_253.setBaseSize(QtCore.QSize(0, 0))
        self.label_253.setText("")
        self.label_253.setPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/baseline_library_music_white_48dp.png"))
        self.label_253.setScaledContents(True)
        self.label_253.setObjectName("label_253")
        self.horizontalLayout_112.addWidget(self.label_253)
        self.label_254 = QtWidgets.QLabel(self.frame_404)
        self.label_254.setText("Library")
        self.label_254.setObjectName("label_254")
        self.horizontalLayout_112.addWidget(self.label_254)
        self.horizontalLayout_111.addWidget(self.frame_404)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_111.addItem(spacerItem44)
        self.verticalLayout_251.addWidget(self.frame_403)

        self.leftMenuAllSongsButton = QtWidgets.QPushButton(self.leftMenuBottomLibraryFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuAllSongsButton.sizePolicy().hasHeightForWidth())
        self.leftMenuAllSongsButton.setSizePolicy(sizePolicy)
        self.leftMenuAllSongsButton.setMinimumSize(QtCore.QSize(180, 16))
        self.leftMenuAllSongsButton.setMaximumSize(QtCore.QSize(180, 16))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.leftMenuAllSongsButton.setFont(font)
        self.leftMenuAllSongsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leftMenuAllSongsButton.setText("All songs")
        self.leftMenuAllSongsButton.setCheckable(True)
        self.leftMenuAllSongsButton.setObjectName("leftMenuAllSongsButton")
        self.verticalLayout_251.addWidget(self.leftMenuAllSongsButton)

        self.leftMenuLikedSongsButton = QtWidgets.QPushButton(self.leftMenuBottomLibraryFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuLikedSongsButton.sizePolicy().hasHeightForWidth())
        self.leftMenuLikedSongsButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.leftMenuLikedSongsButton.setFont(font)
        self.leftMenuLikedSongsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leftMenuLikedSongsButton.setStyleSheet("")
        self.leftMenuLikedSongsButton.setText("Liked songs")
        self.leftMenuLikedSongsButton.setCheckable(True)
        self.leftMenuLikedSongsButton.setObjectName("leftMenuLikedSongsButton")
        self.verticalLayout_251.addWidget(self.leftMenuLikedSongsButton)

        self.leftMenuLastPlayedButton = QtWidgets.QPushButton(self.leftMenuBottomLibraryFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuLastPlayedButton.sizePolicy().hasHeightForWidth())
        self.leftMenuLastPlayedButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.leftMenuLastPlayedButton.setFont(font)
        self.leftMenuLastPlayedButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leftMenuLastPlayedButton.setText("Last played")
        self.leftMenuLastPlayedButton.setCheckable(True)
        self.leftMenuLastPlayedButton.setObjectName("leftMenuLastPlayedButton")
        self.verticalLayout_251.addWidget(self.leftMenuLastPlayedButton)

        self.leftMenuAuthorsButton = QtWidgets.QPushButton(self.leftMenuBottomLibraryFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuAuthorsButton.sizePolicy().hasHeightForWidth())
        self.leftMenuAuthorsButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.leftMenuAuthorsButton.setFont(font)
        self.leftMenuAuthorsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leftMenuAuthorsButton.setText("Authors")
        self.leftMenuAuthorsButton.setCheckable(True)
        self.leftMenuAuthorsButton.setObjectName("leftMenuAuthorsButton")
        self.verticalLayout_251.addWidget(self.leftMenuAuthorsButton)

        self.leftMenuAlbumsButton = QtWidgets.QPushButton(self.leftMenuBottomLibraryFrame)
        self.leftMenuAlbumsButton.setText("Albums")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuAlbumsButton.sizePolicy().hasHeightForWidth())
        self.leftMenuAlbumsButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.leftMenuAlbumsButton.setFont(font)
        self.leftMenuAlbumsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leftMenuAlbumsButton.setCheckable(True)
        self.leftMenuAlbumsButton.setObjectName("leftMenuAuthorsButton")
        self.verticalLayout_251.addWidget(self.leftMenuAlbumsButton)

        self.verticalLayout_252.addWidget(self.leftMenuBottomLibraryFrame)
        self.line_2 = QtWidgets.QFrame(self.leftMenuFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(0, 1))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setStyleSheet("background-color: rgba(179, 179, 179, 0.25);\n"
                                  "margin-left: 24px;\n"
                                  "margin-right: 24px")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_252.addWidget(self.line_2)
        self.leftMenuBottomFrame = QtWidgets.QFrame(self.leftMenuFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuBottomFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuBottomFrame.setSizePolicy(sizePolicy)
        self.leftMenuBottomFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.leftMenuBottomFrame.setStyleSheet("QPushButton:hover:!checked{\n"
                                               "    color:white;\n"
                                               "}\n"
                                               "QPushButton:checked{\n"
                                               "    color: white;\n"
                                               "}\n"
                                               "QScrollBar:vertical {\n"
                                               "    width: 12px;\n"
                                               "    margin-top: 3px;\n"
                                               "    background: transparent;\n"
                                               "}\n"
                                               "QScrollBar::handle:vertical{\n"
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
                                               "\n"
                                               "")
        self.leftMenuBottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftMenuBottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuBottomFrame.setObjectName("leftMenuBottomFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuBottomFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.leftMenuBottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 198, 256))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.playlistsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistsLabel.sizePolicy().hasHeightForWidth())
        self.playlistsLabel.setSizePolicy(sizePolicy)
        self.playlistsLabel.setMinimumSize(QtCore.QSize(198, 45))
        font = QtGui.QFont()
        font.setFamily("Heebo Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(QtGui.QFont.Weight(10))
        font.setStrikeOut(False)
        font.setKerning(True)
        self.playlistsLabel.setFont(font)
        self.playlistsLabel.setStyleSheet("padding-left: 24px;")
        self.playlistsLabel.setText("Playlists")
        self.playlistsLabel.setObjectName("playlistsLabel")
        self.verticalLayout_3.addWidget(self.playlistsLabel)
        self.leftMenuBottomPlaylistsFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuBottomPlaylistsFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuBottomPlaylistsFrame.setSizePolicy(sizePolicy)
        self.leftMenuBottomPlaylistsFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.leftMenuBottomPlaylistsFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leftMenuBottomPlaylistsFrame.setStyleSheet("font: 57 10.5pt \"Heebo Medium\";\n"
                                                        "")
        self.leftMenuBottomPlaylistsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftMenuBottomPlaylistsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuBottomPlaylistsFrame.setObjectName("leftMenuBottomPlaylistsFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.leftMenuBottomPlaylistsFrame)
        self.verticalLayout_5.setContentsMargins(24, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem45 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem45)
        self.verticalLayout_3.addWidget(self.leftMenuBottomPlaylistsFrame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_252.addWidget(self.leftMenuBottomFrame)
        self.frame_70 = QtWidgets.QFrame(self.leftMenuFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_70.sizePolicy().hasHeightForWidth())
        self.frame_70.setSizePolicy(sizePolicy)
        self.frame_70.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_70.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_70.setStyleSheet("#frame_70{\n"
                                    "    border-top: 1px solid rgb(40, 40, 40);\n"
                                    "    background-color: rgb(24, 24, 24);\n"
                                    "}\n"
                                    "#mainPageLeftMenuCreatePlaylistQPushButton{\n"
                                    "    background-color: rgb(24, 24, 24);\n"
                                    "}\n"
                                    "#mainPageLeftMenuCreatePlaylistQPushButton:hover{\n"
                                    "    color: white; \n"
                                    "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_add_white_48dp.png);\n"
                                    "}")
        self.frame_70.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout(self.frame_70)
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.frame_77 = QtWidgets.QFrame(self.frame_70)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_77.sizePolicy().hasHeightForWidth())
        self.frame_77.setSizePolicy(sizePolicy)
        self.frame_77.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_77.setObjectName("frame_77")
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout(self.frame_77)
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.mainPageLeftMenuCreatePlaylistQPushButton = QtWidgets.QPushButton(self.frame_77)
        self.mainPageLeftMenuCreatePlaylistQPushButton.setText("Create Playlist")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageLeftMenuCreatePlaylistQPushButton.sizePolicy().hasHeightForWidth())
        self.mainPageLeftMenuCreatePlaylistQPushButton.setSizePolicy(sizePolicy)
        self.mainPageLeftMenuCreatePlaylistQPushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.mainPageLeftMenuCreatePlaylistQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainPageLeftMenuCreatePlaylistQPushButton.setStyleSheet("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_add_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainPageLeftMenuCreatePlaylistQPushButton.setIcon(icon13)
        self.mainPageLeftMenuCreatePlaylistQPushButton.setIconSize(QtCore.QSize(24, 24))
        self.mainPageLeftMenuCreatePlaylistQPushButton.setObjectName("mainPageLeftMenuCreatePlaylistQPushButton")
        self.horizontalLayout_87.addWidget(self.mainPageLeftMenuCreatePlaylistQPushButton)
        self.horizontalLayout_88.addWidget(self.frame_77)
        self.verticalLayout_252.addWidget(self.frame_70)
        self.mainLayout.addWidget(self.leftMenuFrame, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.mainLayout, 0, 0, 1, 1)

        self.centralStackedWidget.addWidget(self.centralPageAppPage)
        self.centralPageLoginPage = QtWidgets.QWidget()
        self.centralPageLoginPage.setStyleSheet("#scrollAreaWidgetContents_4{\n"
                                                "    background-color: transparent;\n"
                                                "}\n"
                                                "#scrollArea_2{\n"
                                                "    background-color: transparent;\n"
                                                "}\n"
                                                "#frame_294{\n"
                                                "    background-color: rgb(18, 18, 18);\n"
                                                "}\n"
                                                "#frame_295{\n"
                                                "    border-radius: 8px;\n"
                                                "    background-color: rgb(24, 24, 24);\n"
                                                "}\n"
                                                "#centralPageLoginPageLoginQLineEdit{\n"
                                                "    padding-left: 13px;\n"
                                                "    background-color: rgb(64, 64, 64);\n"
                                                "    font: 57 10pt \"Heebo Medium\";\n"
                                                "}\n"
                                                "#centralPageLoginPagePasswordQLineEdit{\n"
                                                "    padding-left: 13px;\n"
                                                "    background-color: rgb(64, 64, 64);\n"
                                                "    font: 57 10pt \"Heebo Medium\";\n"
                                                "}\n"
                                                "#frame_323{\n"
                                                "    background-color: rgb(64, 64, 64);\n"
                                                "}\n"
                                                "#frame_329{\n"
                                                "    background-color: rgb(64, 64, 64);\n"
                                                "}\n"
                                                "#centralPageLoginPageTogglePasswordQPushButton{\n"
                                                "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_visibility_off_gray_48dp.png);\n"
                                                "}\n"
                                                "#centralPageLoginPageTogglePasswordQPushButton:hover:!checked{\n"
                                                "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_visibility_off_white_48dp.png);\n"
                                                "}\n"
                                                "#centralPageLoginPageTogglePasswordQPushButton:checked{\n"
                                                "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_visibility_gray_48dp.png);\n"
                                                "}\n"
                                                "#centralPageLoginPageTogglePasswordQPushButton:hover:checked{\n"
                                                "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_visibility_white_48dp.png);\n"
                                                "}\n"
                                                "#centralPageLoginPageLogInButton{\n"
                                                "    background-color: rgb(245, 155, 125);\n"
                                                "    color: black;\n"
                                                "    border-radius: 24px;\n"
                                                "    text-align: center;\n"
                                                "    font: 57 10.5pt \"Heebo Medium\";\n"
                                                "}\n"
                                                "#centralPageLoginPageContinueAsGuestQPushButton{\n"
                                                "    border: 1px solid rgb(245, 155, 125);\n"
                                                "    color: white;\n"
                                                "    border-radius: 24px;\n"
                                                "    text-align: center;\n"
                                                "    font: 57 10.5pt \"Heebo Medium\";\n"
                                                "}\n"
                                                "#label_195{\n"
                                                "    font: 87 20pt \"Source Sans Pro Black\";\n"
                                                "    color: white;\n"
                                                "}\n"
                                                "#label_196{\n"
                                                "    font: 87 23pt \"Heebo Black\";\n"
                                                "    color: white;\n"
                                                "}\n"
                                                "#frame_297{\n"
                                                "    border-bottom: 1px solid rgb(245, 155, 125);\n"
                                                "}\n"
                                                "#label_211{\n"
                                                "    font: 57 11pt \"Heebo Medium\";\n"
                                                "    color: rgb(179, 179, 179);\n"
                                                "}\n"
                                                "#centralPageRegisterPageButton{\n"
                                                "    color: white;\n"
                                                "    font: 57 11pt \"Heebo Medium\";\n"
                                                "}\n"
                                                "#centralPageRegisterPageButton:hover{\n"
                                                "    text-decoration: underline;\n"
                                                "}\n"
                                                "#label_212{\n"
                                                "    font: 57 11pt \"Heebo Medium\";\n"
                                                "    color: rgb(179, 179, 179);\n"
                                                "}\n"
                                                "QScrollBar:vertical {\n"
                                                "    width: 12px;\n"
                                                "    background: transparent;\n"
                                                "}\n"
                                                "QScrollBar::handle:vertical{\n"
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
                                                "}\n")
        self.centralPageLoginPage.setObjectName("centralPageLoginPage")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralPageLoginPage)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_294 = QtWidgets.QFrame(self.centralPageLoginPage)
        self.frame_294.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_294.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_294.setObjectName("frame_294")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_294)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_294)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 496, 713))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_63 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_63.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_63.setSpacing(0)
        self.gridLayout_63.setObjectName("gridLayout_63")
        self.frame_295 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_295.sizePolicy().hasHeightForWidth())
        self.frame_295.setSizePolicy(sizePolicy)
        self.frame_295.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_295.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_295.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_295.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_295.setObjectName("frame_295")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.frame_295)
        self.verticalLayout_48.setContentsMargins(80, 50, 80, 50)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.frame_296 = QtWidgets.QFrame(self.frame_295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_296.sizePolicy().hasHeightForWidth())
        self.frame_296.setSizePolicy(sizePolicy)
        self.frame_296.setStyleSheet("")
        self.frame_296.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_296.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_296.setObjectName("frame_296")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_296)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_320 = QtWidgets.QFrame(self.frame_296)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_320.sizePolicy().hasHeightForWidth())
        self.frame_320.setSizePolicy(sizePolicy)
        self.frame_320.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_320.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_320.setObjectName("frame_320")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_320)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_194 = QtWidgets.QLabel(self.frame_320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_194.sizePolicy().hasHeightForWidth())
        self.label_194.setSizePolicy(sizePolicy)
        self.label_194.setMinimumSize(QtCore.QSize(48, 48))
        self.label_194.setMaximumSize(QtCore.QSize(48, 48))
        self.label_194.setText("")
        self.label_194.setPixmap(QtGui.QPixmap(":/icons/logos/icons/logos/peachPlayerLogo.png"))
        self.label_194.setScaledContents(True)
        self.label_194.setObjectName("label_194")
        self.horizontalLayout_14.addWidget(self.label_194)
        self.label_195 = QtWidgets.QLabel(self.frame_320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_195.sizePolicy().hasHeightForWidth())
        self.label_195.setSizePolicy(sizePolicy)
        self.label_195.setMinimumSize(QtCore.QSize(162, 39))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_195.setFont(font)
        self.label_195.setStyleSheet("")
        self.label_195.setText("Peach Player")
        self.label_195.setObjectName("label_195")
        self.horizontalLayout_14.addWidget(self.label_195)
        self.horizontalLayout_20.addWidget(self.frame_320)
        self.verticalLayout_48.addWidget(self.frame_296)
        self.frame_297 = QtWidgets.QFrame(self.frame_295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_297.sizePolicy().hasHeightForWidth())
        self.frame_297.setSizePolicy(sizePolicy)
        self.frame_297.setStyleSheet("")
        self.frame_297.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_297.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_297.setObjectName("frame_297")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_297)
        self.horizontalLayout_18.setContentsMargins(0, 52, 0, 20)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_196 = QtWidgets.QLabel(self.frame_297)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_196.sizePolicy().hasHeightForWidth())
        self.label_196.setSizePolicy(sizePolicy)
        self.label_196.setStyleSheet("")
        self.label_196.setText("Log in to continue.")
        self.label_196.setObjectName("label_196")
        self.horizontalLayout_18.addWidget(self.label_196)
        self.verticalLayout_48.addWidget(self.frame_297)
        self.frame_298 = QtWidgets.QFrame(self.frame_295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_298.sizePolicy().hasHeightForWidth())
        self.frame_298.setSizePolicy(sizePolicy)
        self.frame_298.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_298.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_298.setObjectName("frame_298")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_298)
        self.horizontalLayout_22.setContentsMargins(0, 33, 0, 50)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_319 = QtWidgets.QFrame(self.frame_298)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_319.sizePolicy().hasHeightForWidth())
        self.frame_319.setSizePolicy(sizePolicy)
        self.frame_319.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_319.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_319.setObjectName("frame_319")
        self.verticalLayout_232 = QtWidgets.QVBoxLayout(self.frame_319)
        self.verticalLayout_232.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_232.setSpacing(17)
        self.verticalLayout_232.setObjectName("verticalLayout_232")
        self.frame_321 = QtWidgets.QFrame(self.frame_319)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_321.sizePolicy().hasHeightForWidth())
        self.frame_321.setSizePolicy(sizePolicy)
        self.frame_321.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_321.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_321.setObjectName("frame_321")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_321)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.centralPageLoginPageLoginQLineEdit = QtWidgets.QLineEdit(self.frame_321)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageLoginPageLoginQLineEdit.sizePolicy().hasHeightForWidth())
        self.centralPageLoginPageLoginQLineEdit.setSizePolicy(sizePolicy)
        self.centralPageLoginPageLoginQLineEdit.setMinimumSize(QtCore.QSize(292, 40))
        self.centralPageLoginPageLoginQLineEdit.setMaximumSize(QtCore.QSize(292, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.centralPageLoginPageLoginQLineEdit.setPalette(palette)
        self.centralPageLoginPageLoginQLineEdit.setStyleSheet("")
        self.centralPageLoginPageLoginQLineEdit.setInputMask("")
        self.centralPageLoginPageLoginQLineEdit.setPlaceholderText("Email or username")
        self.centralPageLoginPageLoginQLineEdit.setObjectName("centralPageLoginPageLoginQLineEdit")
        self.horizontalLayout_21.addWidget(self.centralPageLoginPageLoginQLineEdit)
        self.frame_323 = QtWidgets.QFrame(self.frame_321)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_323.sizePolicy().hasHeightForWidth())
        self.frame_323.setSizePolicy(sizePolicy)
        self.frame_323.setMinimumSize(QtCore.QSize(44, 40))
        self.frame_323.setMaximumSize(QtCore.QSize(44, 40))
        self.frame_323.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.frame_323.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_323.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_323.setObjectName("frame_323")
        self.gridLayout_64 = QtWidgets.QGridLayout(self.frame_323)
        self.gridLayout_64.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_64.setSpacing(0)
        self.gridLayout_64.setObjectName("gridLayout_64")
        self.label_203 = QtWidgets.QLabel(self.frame_323)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_203.sizePolicy().hasHeightForWidth())
        self.label_203.setSizePolicy(sizePolicy)
        self.label_203.setMinimumSize(QtCore.QSize(24, 24))
        self.label_203.setMaximumSize(QtCore.QSize(24, 24))
        self.label_203.setText("")
        self.label_203.setPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_email_gray_48dp.png"))
        self.label_203.setScaledContents(True)
        self.label_203.setObjectName("label_203")
        self.gridLayout_64.addWidget(self.label_203, 0, 0, 1, 1)
        self.horizontalLayout_21.addWidget(self.frame_323)
        self.verticalLayout_232.addWidget(self.frame_321)
        self.frame_322 = QtWidgets.QFrame(self.frame_319)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_322.sizePolicy().hasHeightForWidth())
        self.frame_322.setSizePolicy(sizePolicy)
        self.frame_322.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_322.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_322.setObjectName("frame_322")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_322)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.centralPageLoginPagePasswordQLineEdit = QtWidgets.QLineEdit(self.frame_322)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageLoginPagePasswordQLineEdit.sizePolicy().hasHeightForWidth())
        self.centralPageLoginPagePasswordQLineEdit.setSizePolicy(sizePolicy)
        self.centralPageLoginPagePasswordQLineEdit.setMinimumSize(QtCore.QSize(292, 40))
        self.centralPageLoginPagePasswordQLineEdit.setMaximumSize(QtCore.QSize(292, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.centralPageLoginPagePasswordQLineEdit.setPalette(palette)
        self.centralPageLoginPagePasswordQLineEdit.setStyleSheet("")
        self.centralPageLoginPagePasswordQLineEdit.setInputMask("")
        self.centralPageLoginPagePasswordQLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.centralPageLoginPagePasswordQLineEdit.setPlaceholderText("Password")
        self.centralPageLoginPagePasswordQLineEdit.setObjectName("centralPageLoginPagePasswordQLineEdit")
        self.horizontalLayout_19.addWidget(self.centralPageLoginPagePasswordQLineEdit)
        self.frame_329 = QtWidgets.QFrame(self.frame_322)
        self.frame_329.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_329.sizePolicy().hasHeightForWidth())
        self.frame_329.setSizePolicy(sizePolicy)
        self.frame_329.setMinimumSize(QtCore.QSize(44, 40))
        self.frame_329.setMaximumSize(QtCore.QSize(44, 40))
        self.frame_329.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_329.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_329.setObjectName("frame_329")
        self.gridLayout_65 = QtWidgets.QGridLayout(self.frame_329)
        self.gridLayout_65.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_65.setSpacing(0)
        self.gridLayout_65.setObjectName("gridLayout_65")
        self.centralPageLoginPageTogglePasswordQPushButton = QtWidgets.QPushButton(self.frame_329)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageLoginPageTogglePasswordQPushButton.sizePolicy().hasHeightForWidth())
        self.centralPageLoginPageTogglePasswordQPushButton.setSizePolicy(sizePolicy)
        self.centralPageLoginPageTogglePasswordQPushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.centralPageLoginPageTogglePasswordQPushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.centralPageLoginPageTogglePasswordQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralPageLoginPageTogglePasswordQPushButton.setText("")
        self.centralPageLoginPageTogglePasswordQPushButton.setIconSize(QtCore.QSize(24, 24))
        self.centralPageLoginPageTogglePasswordQPushButton.setCheckable(True)
        self.centralPageLoginPageTogglePasswordQPushButton.setObjectName("centralPageLoginPageTogglePasswordQPushButton")
        self.gridLayout_65.addWidget(self.centralPageLoginPageTogglePasswordQPushButton, 0, 0, 1, 1)
        self.horizontalLayout_19.addWidget(self.frame_329)
        self.verticalLayout_232.addWidget(self.frame_322)
        self.horizontalLayout_22.addWidget(self.frame_319)
        self.verticalLayout_48.addWidget(self.frame_298)
        self.frame_330 = QtWidgets.QFrame(self.frame_295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_330.sizePolicy().hasHeightForWidth())
        self.frame_330.setSizePolicy(sizePolicy)
        self.frame_330.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_330.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_330.setObjectName("frame_330")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.frame_330)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.centralPageLoginPageLogInButton = QtWidgets.QPushButton(self.frame_330)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageLoginPageLogInButton.sizePolicy().hasHeightForWidth())
        self.centralPageLoginPageLogInButton.setSizePolicy(sizePolicy)
        self.centralPageLoginPageLogInButton.setMinimumSize(QtCore.QSize(336, 48))
        self.centralPageLoginPageLogInButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralPageLoginPageLogInButton.setText("LOG  IN")
        self.centralPageLoginPageLogInButton.setObjectName("centralPageLoginPageLogInButton")
        self.horizontalLayout_41.addWidget(self.centralPageLoginPageLogInButton)
        self.verticalLayout_48.addWidget(self.frame_330)
        self.frame_348 = QtWidgets.QFrame(self.frame_295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_348.sizePolicy().hasHeightForWidth())
        self.frame_348.setSizePolicy(sizePolicy)
        self.frame_348.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_348.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_348.setObjectName("frame_348")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout(self.frame_348)
        self.horizontalLayout_65.setContentsMargins(0, 27, 0, 27)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.line_4 = QtWidgets.QFrame(self.frame_348)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMinimumSize(QtCore.QSize(0, 1))
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_4.setStyleSheet("background-color: rgb(245, 154, 125);\n"
                                  "")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_65.addWidget(self.line_4)
        self.frame_349 = QtWidgets.QFrame(self.frame_348)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_349.sizePolicy().hasHeightForWidth())
        self.frame_349.setSizePolicy(sizePolicy)
        self.frame_349.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_349.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_349.setObjectName("frame_349")
        self.gridLayout_76 = QtWidgets.QGridLayout(self.frame_349)
        self.gridLayout_76.setContentsMargins(20, 0, 20, 0)
        self.gridLayout_76.setSpacing(0)
        self.gridLayout_76.setObjectName("gridLayout_76")
        self.label_211 = QtWidgets.QLabel(self.frame_349)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_211.sizePolicy().hasHeightForWidth())
        self.label_211.setSizePolicy(sizePolicy)
        self.label_211.setText("OR")
        self.label_211.setAlignment(QtCore.Qt.AlignCenter)
        self.label_211.setObjectName("label_211")
        self.gridLayout_76.addWidget(self.label_211, 0, 0, 1, 1)
        self.horizontalLayout_65.addWidget(self.frame_349)
        self.line_5 = QtWidgets.QFrame(self.frame_348)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setMinimumSize(QtCore.QSize(0, 1))
        self.line_5.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.line_5.setStyleSheet("background-color: rgb(245, 154, 125);\n"
                                  "")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_65.addWidget(self.line_5)
        self.verticalLayout_48.addWidget(self.frame_348)
        self.frame_353 = QtWidgets.QFrame(self.frame_295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_353.sizePolicy().hasHeightForWidth())
        self.frame_353.setSizePolicy(sizePolicy)
        self.frame_353.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_353.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_353.setObjectName("frame_353")
        self.horizontalLayout_68 = QtWidgets.QHBoxLayout(self.frame_353)
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        self.centralPageLoginPageContinueAsGuestQPushButton = QtWidgets.QPushButton(self.frame_353)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageLoginPageContinueAsGuestQPushButton.sizePolicy().hasHeightForWidth())
        self.centralPageLoginPageContinueAsGuestQPushButton.setSizePolicy(sizePolicy)
        self.centralPageLoginPageContinueAsGuestQPushButton.setMinimumSize(QtCore.QSize(336, 48))
        self.centralPageLoginPageContinueAsGuestQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralPageLoginPageContinueAsGuestQPushButton.setText("Continue as guest")
        self.centralPageLoginPageContinueAsGuestQPushButton.setObjectName("centralPageLoginPageContinueAsGuestQPushButton")
        self.horizontalLayout_68.addWidget(self.centralPageLoginPageContinueAsGuestQPushButton)
        self.verticalLayout_48.addWidget(self.frame_353)
        self.frame_350 = QtWidgets.QFrame(self.frame_295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_350.sizePolicy().hasHeightForWidth())
        self.frame_350.setSizePolicy(sizePolicy)
        self.frame_350.setMinimumSize(QtCore.QSize(21, 23))
        self.frame_350.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_350.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_350.setObjectName("frame_350")
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout(self.frame_350)
        self.horizontalLayout_66.setContentsMargins(0, 37, 0, 0)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.frame_351 = QtWidgets.QFrame(self.frame_350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_351.sizePolicy().hasHeightForWidth())
        self.frame_351.setSizePolicy(sizePolicy)
        self.frame_351.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_351.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_351.setObjectName("frame_351")
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout(self.frame_351)
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.label_212 = QtWidgets.QLabel(self.frame_351)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_212.sizePolicy().hasHeightForWidth())
        self.label_212.setSizePolicy(sizePolicy)
        self.label_212.setText("Don\'t have an account?")
        self.label_212.setObjectName("label_212")
        self.horizontalLayout_67.addWidget(self.label_212)
        self.centralPageRegisterPageButton = QtWidgets.QPushButton(self.frame_351)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageRegisterPageButton.sizePolicy().hasHeightForWidth())
        self.centralPageRegisterPageButton.setSizePolicy(sizePolicy)
        self.centralPageRegisterPageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralPageRegisterPageButton.setText("Register for free")
        self.centralPageRegisterPageButton.setObjectName("centralPageRegisterPageButton")
        self.horizontalLayout_67.addWidget(self.centralPageRegisterPageButton)
        self.horizontalLayout_66.addWidget(self.frame_351)
        self.verticalLayout_48.addWidget(self.frame_350)
        self.gridLayout_63.addWidget(self.frame_295, 0, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_13.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.frame_294, 0, 0, 1, 1)
        self.centralStackedWidget.addWidget(self.centralPageLoginPage)
        self.centralPageRegisterPage = QtWidgets.QWidget()
        self.centralPageRegisterPage.setStyleSheet("#scrollAreaWidgetContents_5{\n"
                                                   "     background-color: transparent;\n"
                                                   "}\n"
                                                   "#scrollArea_6{\n"
                                                   "     background-color: transparent;\n"
                                                    "}\n"
                                                    "#frame_331{\n"
                                                    "    background-color: rgb(18, 18, 18);\n"
                                                    "}\n"
                                                   "#frame_332{\n"
                                                   "    background-color: rgb(24, 24, 24);\n"
                                                   "}\n"
                                                   "#centralPageRegisterPageEmailQLineEdit{\n"
                                                   "    padding-left: 13px;\n"
                                                   "    background-color: rgb(64, 64, 64);\n"
                                                   "    font: 57 10pt \"Heebo Medium\";\n"
                                                   "}\n"
                                                   "#centralPageRegisterPagePasswordQLineEdit{\n"
                                                   "    padding-left: 13px;\n"
                                                   "    background-color: rgb(64, 64, 64);\n"
                                                   "    font: 57 10pt \"Heebo Medium\";\n"
                                                   "}\n"
                                                   "#centralPageRegisterPageNicknameQLineEdit{\n"
                                                   "    padding-left: 13px;\n"
                                                   "    background-color: rgb(64, 64, 64);\n"
                                                   "    font: 57 10pt \"Heebo Medium\";\n"
                                                   "}\n"
                                                   "#frame_339{\n"
                                                   "    background-color: rgb(64, 64, 64);\n"
                                                   "}\n"
                                                   "#frame_341{\n"
                                                   "    background-color: rgb(64, 64, 64);\n"
                                                   "}\n"
                                                   "#frame_344{\n"
                                                   "    background-color: rgb(64, 64, 64);\n"
                                                   "}\n"
                                                   "#centralPageRegisterPageTogglePasswordQPushButton{\n"
                                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_visibility_off_gray_48dp.png);\n"
                                                   "}\n"
                                                   "#centralPageRegisterPageTogglePasswordQPushButton:hover:!checked{\n"
                                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_visibility_off_white_48dp.png);\n"
                                                   "}\n"
                                                   "#centralPageRegisterPageTogglePasswordQPushButton:checked{\n"
                                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_visibility_gray_48dp.png);\n"
                                                   "}\n"
                                                   "#centralPageRegisterPageTogglePasswordQPushButton:hover:checked{\n"
                                                   "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_visibility_white_48dp.png);\n"
                                                   "}\n"
                                                   "#centralPageRegisterPageSignInQPushButton{\n"
                                                   "    background-color: rgb(245, 155, 125);\n"
                                                   "    color: black;\n"
                                                   "    border-radius: 24px;\n"
                                                   "    text-align: center;\n"
                                                   "    font: 57 10.5pt \"Heebo Medium\";\n"
                                                   "}\n"
                                                   "#label_205{\n"
                                                   "    color: white;\n"
                                                   "    font: 87 20pt \"Source Sans Pro Black\";\n"
                                                   "}\n"
                                                   "#label_206{\n"
                                                   "    font: 87 23pt \"Heebo Black\";\n"
                                                   "    color: white;\n"
                                                   "}\n"
                                                   "#frame_335{\n"
                                                   "    border-bottom: 1px solid rgb(245, 155, 125);\n"
                                                   "}\n"
                                                   "#label_209{\n"
                                                   "    color: rgb(179, 179, 179);\n"
                                                   "    font: 57 11pt \"Heebo Medium\";\n"
                                                   "}\n"
                                                   "#label_210{\n"
                                                   "    color: rgb(179, 179, 179);\n"
                                                   "    font: 57 11pt \"Heebo Medium\";\n"
                                                   "}\n"
                                                   "#centralPageLoginPageButton{\n"
                                                   "    color: white;\n"
                                                   "    font: 57 11pt \"Heebo Medium\";\n"
                                                   "}\n"
                                                   "#centralPageLoginPageButton:hover{\n"
                                                   "    text-decoration: underline;\n"
                                                   "}\n"
                                                   "QScrollBar:vertical {\n"
                                                   "    width: 12px;\n"
                                                   "    background: transparent;\n"
                                                   "}\n"
                                                   "QScrollBar::handle:vertical{\n"
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
                                                   "}\n")
        self.centralPageRegisterPage.setObjectName("centralPageRegisterPage")
        self.gridLayout_73 = QtWidgets.QGridLayout(self.centralPageRegisterPage)
        self.gridLayout_73.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_73.setSpacing(0)
        self.gridLayout_73.setObjectName("gridLayout_73")
        self.frame_331 = QtWidgets.QFrame(self.centralPageRegisterPage)
        self.frame_331.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_331.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_331.setObjectName("frame_331")
        self.gridLayout_69 = QtWidgets.QGridLayout(self.frame_331)
        self.gridLayout_69.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_69.setSpacing(0)
        self.gridLayout_69.setObjectName("gridLayout_69")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.frame_331)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 783, 650))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_70 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_70.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_70.setSpacing(0)
        self.gridLayout_70.setObjectName("gridLayout_70")
        self.frame_332 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_332.sizePolicy().hasHeightForWidth())
        self.frame_332.setSizePolicy(sizePolicy)
        self.frame_332.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_332.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_332.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_332.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_332.setObjectName("frame_332")
        self.verticalLayout_231 = QtWidgets.QVBoxLayout(self.frame_332)
        self.verticalLayout_231.setContentsMargins(80, 50, 80, 50)
        self.verticalLayout_231.setSpacing(0)
        self.verticalLayout_231.setObjectName("verticalLayout_231")
        self.frame_333 = QtWidgets.QFrame(self.frame_332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_333.sizePolicy().hasHeightForWidth())
        self.frame_333.setSizePolicy(sizePolicy)
        self.frame_333.setStyleSheet("")
        self.frame_333.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_333.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_333.setObjectName("frame_333")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.frame_333)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.frame_334 = QtWidgets.QFrame(self.frame_333)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_334.sizePolicy().hasHeightForWidth())
        self.frame_334.setSizePolicy(sizePolicy)
        self.frame_334.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_334.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_334.setObjectName("frame_334")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.frame_334)
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55.setSpacing(6)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.label_204 = QtWidgets.QLabel(self.frame_334)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_204.sizePolicy().hasHeightForWidth())
        self.label_204.setSizePolicy(sizePolicy)
        self.label_204.setMinimumSize(QtCore.QSize(48, 48))
        self.label_204.setMaximumSize(QtCore.QSize(48, 48))
        self.label_204.setText("")
        self.label_204.setPixmap(QtGui.QPixmap(":/icons/logos/icons/logos/peachPlayerLogo.png"))
        self.label_204.setScaledContents(True)
        self.label_204.setObjectName("label_204")
        self.horizontalLayout_55.addWidget(self.label_204)
        self.label_205 = QtWidgets.QLabel(self.frame_334)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_205.sizePolicy().hasHeightForWidth())
        self.label_205.setSizePolicy(sizePolicy)
        self.label_205.setMinimumSize(QtCore.QSize(162, 39))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QtGui.QFont.Weight(10))
        self.label_205.setFont(font)
        self.label_205.setStyleSheet("")
        self.label_205.setText("Peach Player")
        self.label_205.setObjectName("label_205")
        self.horizontalLayout_55.addWidget(self.label_205)
        self.horizontalLayout_51.addWidget(self.frame_334)
        self.verticalLayout_231.addWidget(self.frame_333)
        self.frame_335 = QtWidgets.QFrame(self.frame_332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_335.sizePolicy().hasHeightForWidth())
        self.frame_335.setSizePolicy(sizePolicy)
        self.frame_335.setStyleSheet("")
        self.frame_335.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_335.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_335.setObjectName("frame_335")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.frame_335)
        self.horizontalLayout_57.setContentsMargins(0, 52, 0, 20)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.label_206 = QtWidgets.QLabel(self.frame_335)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_206.sizePolicy().hasHeightForWidth())
        self.label_206.setSizePolicy(sizePolicy)
        self.label_206.setStyleSheet("")
        self.label_206.setText("Register for free.")
        self.label_206.setObjectName("label_206")
        self.horizontalLayout_57.addWidget(self.label_206)
        self.verticalLayout_231.addWidget(self.frame_335)
        self.frame_336 = QtWidgets.QFrame(self.frame_332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_336.sizePolicy().hasHeightForWidth())
        self.frame_336.setSizePolicy(sizePolicy)
        self.frame_336.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_336.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_336.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_336.setObjectName("frame_336")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.frame_336)
        self.horizontalLayout_58.setContentsMargins(0, 33, 0, 50)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.frame_337 = QtWidgets.QFrame(self.frame_336)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_337.sizePolicy().hasHeightForWidth())
        self.frame_337.setSizePolicy(sizePolicy)
        self.frame_337.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_337.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_337.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_337.setObjectName("frame_337")
        self.verticalLayout_233 = QtWidgets.QVBoxLayout(self.frame_337)
        self.verticalLayout_233.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_233.setSpacing(17)
        self.verticalLayout_233.setObjectName("verticalLayout_233")
        self.frame_338 = QtWidgets.QFrame(self.frame_337)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_338.sizePolicy().hasHeightForWidth())
        self.frame_338.setSizePolicy(sizePolicy)
        self.frame_338.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_338.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_338.setObjectName("frame_338")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout(self.frame_338)
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.centralPageRegisterPageEmailQLineEdit = QtWidgets.QLineEdit(self.frame_338)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageRegisterPageEmailQLineEdit.sizePolicy().hasHeightForWidth())
        self.centralPageRegisterPageEmailQLineEdit.setSizePolicy(sizePolicy)
        self.centralPageRegisterPageEmailQLineEdit.setMinimumSize(QtCore.QSize(292, 40))
        self.centralPageRegisterPageEmailQLineEdit.setMaximumSize(QtCore.QSize(292, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.centralPageRegisterPageEmailQLineEdit.setPalette(palette)
        self.centralPageRegisterPageEmailQLineEdit.setStyleSheet("")
        self.centralPageRegisterPageEmailQLineEdit.setInputMask("")
        self.centralPageRegisterPageEmailQLineEdit.setFrame(True)
        self.centralPageRegisterPageEmailQLineEdit.setPlaceholderText("Email")
        self.centralPageRegisterPageEmailQLineEdit.setObjectName("centralPageRegisterPageEmailQLineEdit")
        self.horizontalLayout_59.addWidget(self.centralPageRegisterPageEmailQLineEdit)
        self.frame_339 = QtWidgets.QFrame(self.frame_338)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_339.sizePolicy().hasHeightForWidth())
        self.frame_339.setSizePolicy(sizePolicy)
        self.frame_339.setMinimumSize(QtCore.QSize(44, 40))
        self.frame_339.setMaximumSize(QtCore.QSize(44, 40))
        self.frame_339.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.frame_339.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_339.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_339.setObjectName("frame_339")
        self.gridLayout_71 = QtWidgets.QGridLayout(self.frame_339)
        self.gridLayout_71.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_71.setSpacing(0)
        self.gridLayout_71.setObjectName("gridLayout_71")
        self.label_207 = QtWidgets.QLabel(self.frame_339)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_207.sizePolicy().hasHeightForWidth())
        self.label_207.setSizePolicy(sizePolicy)
        self.label_207.setMinimumSize(QtCore.QSize(24, 24))
        self.label_207.setMaximumSize(QtCore.QSize(24, 24))
        self.label_207.setText("")
        self.label_207.setPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_email_gray_48dp.png"))
        self.label_207.setScaledContents(True)
        self.label_207.setObjectName("label_207")
        self.gridLayout_71.addWidget(self.label_207, 0, 0, 1, 1)
        self.horizontalLayout_59.addWidget(self.frame_339)
        self.verticalLayout_233.addWidget(self.frame_338)
        self.frame_340 = QtWidgets.QFrame(self.frame_337)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_340.sizePolicy().hasHeightForWidth())
        self.frame_340.setSizePolicy(sizePolicy)
        self.frame_340.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_340.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_340.setObjectName("frame_340")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.frame_340)
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.centralPageRegisterPagePasswordQLineEdit = QtWidgets.QLineEdit(self.frame_340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageRegisterPagePasswordQLineEdit.sizePolicy().hasHeightForWidth())
        self.centralPageRegisterPagePasswordQLineEdit.setSizePolicy(sizePolicy)
        self.centralPageRegisterPagePasswordQLineEdit.setMinimumSize(QtCore.QSize(292, 40))
        self.centralPageRegisterPagePasswordQLineEdit.setMaximumSize(QtCore.QSize(292, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.centralPageRegisterPagePasswordQLineEdit.setPalette(palette)
        self.centralPageRegisterPagePasswordQLineEdit.setStyleSheet("")
        self.centralPageRegisterPagePasswordQLineEdit.setInputMask("")
        self.centralPageRegisterPagePasswordQLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.centralPageRegisterPagePasswordQLineEdit.setPlaceholderText("Password")
        self.centralPageRegisterPagePasswordQLineEdit.setObjectName("centralPageRegisterPagePasswordQLineEdit")
        self.horizontalLayout_60.addWidget(self.centralPageRegisterPagePasswordQLineEdit)
        self.frame_341 = QtWidgets.QFrame(self.frame_340)
        self.frame_341.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_341.sizePolicy().hasHeightForWidth())
        self.frame_341.setSizePolicy(sizePolicy)
        self.frame_341.setMinimumSize(QtCore.QSize(44, 40))
        self.frame_341.setMaximumSize(QtCore.QSize(44, 40))
        self.frame_341.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_341.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_341.setObjectName("frame_341")
        self.gridLayout_72 = QtWidgets.QGridLayout(self.frame_341)
        self.gridLayout_72.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_72.setSpacing(0)
        self.gridLayout_72.setObjectName("gridLayout_72")
        self.centralPageRegisterPageTogglePasswordQPushButton = QtWidgets.QPushButton(self.frame_341)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageRegisterPageTogglePasswordQPushButton.sizePolicy().hasHeightForWidth())
        self.centralPageRegisterPageTogglePasswordQPushButton.setSizePolicy(sizePolicy)
        self.centralPageRegisterPageTogglePasswordQPushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.centralPageRegisterPageTogglePasswordQPushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.centralPageRegisterPageTogglePasswordQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralPageRegisterPageTogglePasswordQPushButton.setText("")
        self.centralPageRegisterPageTogglePasswordQPushButton.setIconSize(QtCore.QSize(24, 24))
        self.centralPageRegisterPageTogglePasswordQPushButton.setCheckable(True)
        self.centralPageRegisterPageTogglePasswordQPushButton.setObjectName("centralPageRegisterPageTogglePasswordQPushButton")
        self.gridLayout_72.addWidget(self.centralPageRegisterPageTogglePasswordQPushButton, 0, 0, 1, 1)
        self.horizontalLayout_60.addWidget(self.frame_341)
        self.verticalLayout_233.addWidget(self.frame_340)
        self.frame_343 = QtWidgets.QFrame(self.frame_337)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_343.sizePolicy().hasHeightForWidth())
        self.frame_343.setSizePolicy(sizePolicy)
        self.frame_343.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_343.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_343.setObjectName("frame_343")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.frame_343)
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.centralPageRegisterPageNicknameQLineEdit = QtWidgets.QLineEdit(self.frame_343)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageRegisterPageNicknameQLineEdit.sizePolicy().hasHeightForWidth())
        self.centralPageRegisterPageNicknameQLineEdit.setSizePolicy(sizePolicy)
        self.centralPageRegisterPageNicknameQLineEdit.setMinimumSize(QtCore.QSize(292, 40))
        self.centralPageRegisterPageNicknameQLineEdit.setMaximumSize(QtCore.QSize(292, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.centralPageRegisterPageNicknameQLineEdit.setPalette(palette)
        self.centralPageRegisterPageNicknameQLineEdit.setStyleSheet("")
        self.centralPageRegisterPageNicknameQLineEdit.setInputMask("")
        self.centralPageRegisterPageNicknameQLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.centralPageRegisterPageNicknameQLineEdit.setPlaceholderText("Nickname")
        self.centralPageRegisterPageNicknameQLineEdit.setObjectName("centralPageRegisterPageNicknameQLineEdit")
        self.horizontalLayout_62.addWidget(self.centralPageRegisterPageNicknameQLineEdit)
        self.frame_344 = QtWidgets.QFrame(self.frame_343)
        self.frame_344.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_344.sizePolicy().hasHeightForWidth())
        self.frame_344.setSizePolicy(sizePolicy)
        self.frame_344.setMinimumSize(QtCore.QSize(44, 40))
        self.frame_344.setMaximumSize(QtCore.QSize(44, 40))
        self.frame_344.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_344.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_344.setObjectName("frame_344")
        self.gridLayout_74 = QtWidgets.QGridLayout(self.frame_344)
        self.gridLayout_74.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_74.setSpacing(0)
        self.gridLayout_74.setObjectName("gridLayout_74")
        self.label_208 = QtWidgets.QLabel(self.frame_344)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_208.sizePolicy().hasHeightForWidth())
        self.label_208.setSizePolicy(sizePolicy)
        self.label_208.setMinimumSize(QtCore.QSize(24, 24))
        self.label_208.setMaximumSize(QtCore.QSize(24, 24))
        self.label_208.setText("")
        self.label_208.setPixmap(QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_account_circle_gray_48dp.png"))
        self.label_208.setScaledContents(True)
        self.label_208.setObjectName("label_208")
        self.gridLayout_74.addWidget(self.label_208, 0, 0, 1, 1)
        self.horizontalLayout_62.addWidget(self.frame_344)
        self.verticalLayout_233.addWidget(self.frame_343)
        self.horizontalLayout_58.addWidget(self.frame_337)
        self.verticalLayout_231.addWidget(self.frame_336)
        self.centralPageRegisterPageSignInQPushButton = QtWidgets.QPushButton(self.frame_332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageRegisterPageSignInQPushButton.sizePolicy().hasHeightForWidth())
        self.centralPageRegisterPageSignInQPushButton.setSizePolicy(sizePolicy)
        self.centralPageRegisterPageSignInQPushButton.setMinimumSize(QtCore.QSize(336, 48))
        self.centralPageRegisterPageSignInQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralPageRegisterPageSignInQPushButton.setText("SIGN UP")
        self.centralPageRegisterPageSignInQPushButton.setObjectName("centralPageRegisterPageSignInQPushButton")
        self.verticalLayout_231.addWidget(self.centralPageRegisterPageSignInQPushButton)
        self.frame_345 = QtWidgets.QFrame(self.frame_332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_345.sizePolicy().hasHeightForWidth())
        self.frame_345.setSizePolicy(sizePolicy)
        self.frame_345.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_345.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_345.setObjectName("frame_345")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.frame_345)
        self.horizontalLayout_63.setContentsMargins(0, 27, 0, 27)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.line = QtWidgets.QFrame(self.frame_345)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 1))
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet("background-color: rgb(245, 154, 125);\n"
                                "")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_63.addWidget(self.line)
        self.frame_346 = QtWidgets.QFrame(self.frame_345)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_346.sizePolicy().hasHeightForWidth())
        self.frame_346.setSizePolicy(sizePolicy)
        self.frame_346.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_346.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_346.setObjectName("frame_346")
        self.gridLayout_75 = QtWidgets.QGridLayout(self.frame_346)
        self.gridLayout_75.setContentsMargins(20, 0, 20, 0)
        self.gridLayout_75.setSpacing(0)
        self.gridLayout_75.setObjectName("gridLayout_75")
        self.label_209 = QtWidgets.QLabel(self.frame_346)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_209.sizePolicy().hasHeightForWidth())
        self.label_209.setSizePolicy(sizePolicy)
        self.label_209.setText("OR")
        self.label_209.setAlignment(QtCore.Qt.AlignCenter)
        self.label_209.setObjectName("label_209")
        self.gridLayout_75.addWidget(self.label_209, 0, 0, 1, 1)
        self.horizontalLayout_63.addWidget(self.frame_346)
        self.line_3 = QtWidgets.QFrame(self.frame_345)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMinimumSize(QtCore.QSize(0, 1))
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.line_3.setStyleSheet("background-color: rgb(245, 154, 125);\n"
                                  "")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_63.addWidget(self.line_3)
        self.verticalLayout_231.addWidget(self.frame_345)
        self.frame_342 = QtWidgets.QFrame(self.frame_332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_342.sizePolicy().hasHeightForWidth())
        self.frame_342.setSizePolicy(sizePolicy)
        self.frame_342.setMinimumSize(QtCore.QSize(21, 23))
        self.frame_342.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_342.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_342.setObjectName("frame_342")
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout(self.frame_342)
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.frame_347 = QtWidgets.QFrame(self.frame_342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_347.sizePolicy().hasHeightForWidth())
        self.frame_347.setSizePolicy(sizePolicy)
        self.frame_347.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_347.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_347.setObjectName("frame_347")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout(self.frame_347)
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.label_210 = QtWidgets.QLabel(self.frame_347)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_210.sizePolicy().hasHeightForWidth())
        self.label_210.setSizePolicy(sizePolicy)
        self.label_210.setText("Already have an account?")
        self.label_210.setObjectName("label_210")
        self.horizontalLayout_61.addWidget(self.label_210)
        self.centralPageLoginPageButton = QtWidgets.QPushButton(self.frame_347)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralPageLoginPageButton.sizePolicy().hasHeightForWidth())
        self.centralPageLoginPageButton.setSizePolicy(sizePolicy)
        self.centralPageLoginPageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralPageLoginPageButton.setText("Log in")
        self.centralPageLoginPageButton.setObjectName("centralPageLoginPageButton")
        self.horizontalLayout_61.addWidget(self.centralPageLoginPageButton)
        self.horizontalLayout_64.addWidget(self.frame_347)
        self.verticalLayout_231.addWidget(self.frame_342)
        self.gridLayout_70.addWidget(self.frame_332, 0, 1, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_69.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.gridLayout_73.addWidget(self.frame_331, 0, 0, 1, 1)
        self.centralStackedWidget.addWidget(self.centralPageRegisterPage)
        self.centralWidgetLayout.addWidget(self.centralStackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.centralStackedWidget.setCurrentIndex(1)
        self.mainPageStackedWidget.setCurrentIndex(0)
        self.mainPageAuthorPageStackedWidget.setCurrentIndex(0)
        self.mainPageCategoryPageStackedWidget.setCurrentIndex(0)

        self.mainPageLikedSongsSortButtonsQButtonGroup = QtWidgets.QButtonGroup()
        self.mainPageLikedSongsSortButtonsQButtonGroup.addButton(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsTitleSortButton)
        setattr(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsTitleSortButton, "wasChecked", False)
        self.mainPageLikedSongsSortButtonsQButtonGroup.addButton(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsArtistSortButton)
        setattr(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsArtistSortButton, "wasChecked", False)
        self.mainPageLikedSongsSortButtonsQButtonGroup.addButton(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsCategorySortButton)
        setattr(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsCategorySortButton, "wasChecked", False)
        self.mainPageLikedSongsSortButtonsQButtonGroup.addButton(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsAddedSortButton)
        setattr(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsAddedSortButton, "wasChecked", False)
        self.mainPageLikedSongsSortButtonsQButtonGroup.addButton(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsLengthSortButton)
        setattr(self.LikedSongsSortButtonsQFrame.mainPageLikedSongsLengthSortButton, "wasChecked", False)

        self.mainPageAuthorPageSortButtonsQButtonGroup = QtWidgets.QButtonGroup()
        """self.mainPageAuthorPageSortButtonsQButtonGroup.addButton(self.mainPageAuthorPageTitleSortButton)
        setattr(self.mainPageAuthorPageTitleSortButton, "wasChecked", False)
        self.mainPageAuthorPageSortButtonsQButtonGroup.addButton(self.mainPageAuthorPageCategorySortButton)
        setattr(self.mainPageAuthorPageCategorySortButton, "wasChecked", False)
        self.mainPageAuthorPageSortButtonsQButtonGroup.addButton(self.mainPageAuthorPageAddedSortButton)
        setattr(self.mainPageAuthorPageAddedSortButton, "wasChecked", False)
        self.mainPageAuthorPageSortButtonsQButtonGroup.addButton(self.mainPageAuthorPageLengthSortButton)
        setattr(self.mainPageAuthorPageLengthSortButton, "wasChecked", False)"""

        self.mainPagePlaylistSortButtonsQButtonGroup = QtWidgets.QButtonGroup()
        """self.mainPagePlaylistSortButtonsQButtonGroup.addButton(self.mainPagePlaylistTitleSortButton)
        setattr(self.mainPagePlaylistTitleSortButton, "wasChecked", False)
        self.mainPagePlaylistSortButtonsQButtonGroup.addButton(self.mainPagePlaylistArtistSortButton)
        setattr(self.mainPagePlaylistArtistSortButton, "wasChecked", False)
        self.mainPagePlaylistSortButtonsQButtonGroup.addButton(self.mainPagePlaylistCategorySortButton)
        setattr(self.mainPagePlaylistCategorySortButton, "wasChecked", False)
        self.mainPagePlaylistSortButtonsQButtonGroup.addButton(self.mainPagePlaylistAddedSortButton)
        setattr(self.mainPagePlaylistAddedSortButton, "wasChecked", False)
        self.mainPagePlaylistSortButtonsQButtonGroup.addButton(self.mainPagePlaylistLengthSortButton)
        setattr(self.mainPagePlaylistLengthSortButton, "wasChecked", False)"""

        self.mainPageCategorySortButtonsQButtonGroup = QtWidgets.QButtonGroup()
        """self.mainPageCategorySortButtonsQButtonGroup.addButton(self.mainPageCategoryTitleSortButton)
        setattr(self.mainPageCategoryTitleSortButton, "wasChecked", False)
        self.mainPageCategorySortButtonsQButtonGroup.addButton(self.mainPageCategoryArtistSortButton)
        setattr(self.mainPageCategoryArtistSortButton, "wasChecked", False)
        self.mainPageCategorySortButtonsQButtonGroup.addButton(self.mainPageCategoryAddedSortButton)
        setattr(self.mainPageCategoryAddedSortButton, "wasChecked", False)
        self.mainPageCategorySortButtonsQButtonGroup.addButton(self.mainPageCategoryLengthSortButton)
        setattr(self.mainPageCategoryLengthSortButton, "wasChecked", False)"""

        self.mainPageAllSongsSortButtonsQButtonGroup = QtWidgets.QButtonGroup()
        """self.mainPageAllSongsSortButtonsQButtonGroup.addButton(self.mainPageAllSongsTitleSortQPushButton)
        setattr(self.mainPageAllSongsTitleSortQPushButton, "wasChecked", False)
        self.mainPageAllSongsSortButtonsQButtonGroup.addButton(self.mainPageAllSongsArtistSortQPushButton)
        setattr(self.mainPageAllSongsArtistSortQPushButton, "wasChecked", False)
        self.mainPageAllSongsSortButtonsQButtonGroup.addButton(self.mainPageAllSongsCategorySortQPushButton)
        setattr(self.mainPageAllSongsCategorySortQPushButton, "wasChecked", False)
        self.mainPageAllSongsSortButtonsQButtonGroup.addButton(self.mainPageAllSongsAddedSortQPushButton)
        setattr(self.mainPageAllSongsAddedSortQPushButton, "wasChecked", False)
        self.mainPageAllSongsSortButtonsQButtonGroup.addButton(self.mainPageAllSongsLengthSortQPushButton)
        setattr(self.mainPageAllSongsLengthSortQPushButton, "wasChecked", False)"""

        #########################################################################
        # Main navigation buttons group
        #########################################################################
        self.mainPageUtilityButtonsQButtonGroup = QtWidgets.QButtonGroup()
        self.mainPageUtilityButtonsQButtonGroup.addButton(self.nowPlayingButton)
        self.mainPageUtilityButtonsQButtonGroup.addButton(self.miniPlayerButton)
        self.mainPageUtilityButtonsQButtonGroup.addButton(self.categoriesButton)
        self.mainPageUtilityButtonsQButtonGroup.addButton(self.bottomPlayerQueueButton)
        self.mainPageUtilityButtonsQButtonGroup.addButton(self.leftMenuLikedSongsButton)
        self.mainPageUtilityButtonsQButtonGroup.addButton(self.leftMenuLastPlayedButton)
        self.mainPageUtilityButtonsQButtonGroup.addButton(self.leftMenuAuthorsButton)
        self.mainPageUtilityButtonsQButtonGroup.addButton(self.leftMenuAlbumsButton)
        self.mainPageUtilityButtonsQButtonGroup.addButton(self.leftMenuAllSongsButton)

        self.mainPageCategoriesScroll = QtWidgets.QScrollBar(self.mainPageCategories)
        self.mainPageCategoriesScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageCategoriesScroll.setFixedWidth(12)
        self.mainPageCategoriesScroll.setMaximum(self.scrollArea_9.verticalScrollBar().maximum())

        self.mainPageLikedSongsScroll = QtWidgets.QScrollBar(self.mainPageLikedSongs)
        self.mainPageLikedSongsScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageLikedSongsScroll.setFixedWidth(12)
        self.mainPageLikedSongsScroll.setMaximum(self.scrollArea_4.verticalScrollBar().maximum())

        self.mainPageLastPlayedScroll = QtWidgets.QScrollBar(self.mainPageLastPlayed)
        self.mainPageLastPlayedScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageLastPlayedScroll.setFixedWidth(12)
        self.mainPageLastPlayedScroll.setMaximum(self.scrollArea_10.verticalScrollBar().maximum())

        self.mainPageAuthorsScroll = QtWidgets.QScrollBar(self.mainPageAuthors)
        self.mainPageAuthorsScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageAuthorsScroll.setFixedWidth(12)
        self.mainPageAuthorsScroll.setMaximum(self.scrollArea_7.verticalScrollBar().maximum())

        self.mainPagePlaylistScroll = QtWidgets.QScrollBar(self.mainPagePlaylist)
        self.mainPagePlaylistScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPagePlaylistScroll.setFixedWidth(12)
        self.mainPagePlaylistScroll.setMaximum(self.scrollArea_3.verticalScrollBar().maximum())

        self.mainPageAuthorPageScroll = QtWidgets.QScrollBar(self.mainPageAuthorPage)
        self.mainPageAuthorPageScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageAuthorPageScroll.setFixedWidth(12)
        self.mainPageAuthorPageScroll.setMaximum(self.scrollArea_8.verticalScrollBar().maximum())

        self.mainPageCategoryPageScroll = QtWidgets.QScrollBar(self.mainPageCategoryPage)
        self.mainPageCategoryPageScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageCategoryPageScroll.setFixedWidth(12)
        self.mainPageCategoryPageScroll.setMaximum(self.scrollArea_11.verticalScrollBar().maximum())

        self.mainPageAlbumPageScroll = QtWidgets.QScrollBar(self.mainPageAlbumPage)
        self.mainPageAlbumPageScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageAlbumPageScroll.setFixedWidth(12)
        self.mainPageAlbumPageScroll.setMaximum(self.scrollArea_5.verticalScrollBar().maximum())

        self.mainPageSongQueuePageScroll = QtWidgets.QScrollBar(self.mainPageSongQueue)
        self.mainPageSongQueuePageScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageSongQueuePageScroll.setFixedWidth(12)
        self.mainPageSongQueuePageScroll.setMaximum(self.scrollArea_12.verticalScrollBar().maximum())

        self.mainPageAlbumsPageScroll = QtWidgets.QScrollBar(self.mainPageAlbumsPage)
        self.mainPageAlbumsPageScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageAlbumsPageScroll.setFixedWidth(12)
        self.mainPageAlbumsPageScroll.setMaximum(self.scrollArea_13.verticalScrollBar().maximum())

        self.mainPageAllSongsPageScroll = QtWidgets.QScrollBar(self.mainPageAllSongs)
        self.mainPageAllSongsPageScroll.setOrientation(QtCore.Qt.Vertical)
        self.mainPageAllSongsPageScroll.setFixedWidth(12)
        self.mainPageAllSongsPageScroll.setMaximum(self.scrollArea_14.verticalScrollBar().maximum())

        self.custom_scrollbars_list = [self.mainPageCategoriesScroll, self.mainPageLikedSongsScroll, self.mainPageLastPlayedScroll,
                                  self.mainPageAuthorsScroll, self.mainPagePlaylistScroll, self.mainPageAuthorPageScroll,
                                  self.mainPageCategoryPageScroll, self.mainPageAlbumPageScroll, self.mainPageSongQueuePageScroll,
                                  self.mainPageAlbumsPageScroll, self.mainPageAllSongsPageScroll]

        self.sort_button_frames = [self.LikedSongsSortButtonsQFrame, self.LastPlayedSortButtonsQFrame,
                                   self.PlaylistSortButtonsQFrame, self.AuthorSortButtonsQFrame,
                                   self.CategorySortButtonsQFrame, self.AlbumSortButtonsQFrame,
                                   self.allSongsSortButtonsQFrame]
        self.native_vertical_scrollbar_list = [self.scrollArea_9.verticalScrollBar(), self.scrollArea_4.verticalScrollBar(),
                                               self.scrollArea_10.verticalScrollBar(), self.scrollArea_7.verticalScrollBar(),
                                               self.scrollArea_7.verticalScrollBar(), self.scrollArea_8.verticalScrollBar(),
                                               self.scrollArea_11.verticalScrollBar(), self.scrollArea_11.verticalScrollBar(),
                                               self.scrollArea_12.verticalScrollBar(), self.scrollArea_13.verticalScrollBar(),
                                               self.scrollArea_14.verticalScrollBar()]

        self.fixedNavbar = NavbarFrame(self.centralPageAppPage)
        self.fixedNavbar.move(200, 0)
        self.fixedNavbar.setFixedHeight(60)

    def set_sliders_page_steps(self):
        pass

    def adjust_all_sort_button_frames_visibility(self):
        """Adjust all sortButtonFrames elements visibility."""
        for sort_button_frame in self.sort_button_frames:
            sort_button_frame.adjust_sort_buttons_qframe_sort_buttons_frames_visibility()


    @staticmethod
    def load_fonts():
        fonts_urls = [':/fonts/fonts/Heebo/static/HeeboBlack.ttf', ':/fonts/fonts/Heebo/static/HeeboBold.ttf',
                      ':/fonts/fonts/Heebo/static/HeeboExtraBold.ttf', ':/fonts/fonts/Heebo/static/HeeboExtraLight.ttf',
                      ':/fonts/fonts/Heebo/static/HeeboLight.ttf', ':/fonts/fonts/Heebo/static/HeeboMedium.ttf',
                      ':/fonts/fonts/Heebo/static/HeeboRegular.ttf', ':/fonts/fonts/Heebo/static/HeeboSemiBold.ttf']
        for url in fonts_urls:
            QtGui.QFontDatabase.addApplicationFont(url)
