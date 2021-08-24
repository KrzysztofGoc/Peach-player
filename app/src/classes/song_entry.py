from PySide6 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player


class SongEntry(QtWidgets.QFrame):
    """Song type ui entry with predefined layout.

    If any of attributes is not specified it will be hidden in layout.

    """

    def __init__(self, *, song_title="Nam tristique", artist_name=None, category_name="",
                 date_added="24 Dec 2020", song_length="5 : 30", is_liked=False, is_playing=False, parent=None):
        super().__init__(parent=parent)
        self.song_title = song_title
        self.artist_name = artist_name
        self.category_name = category_name
        self.date_added = date_added
        self.song_length = song_length
        self.is_liked = is_liked
        self.is_playing = is_playing
        self.setup_layout()

    def setup_layout(self):
        self.setStyleSheet("#label_19{\n"
                           "     color: white;\n"
                           "}\n"
                           " #pushButton_30:hover:!checked{\n"
                           "     icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_favorite_border_white_48dp.png);\n"
                           "}\n"
                           " #pushButton_30:checked{\n"
                           "     icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_favorite_peach_48dp.png);\n"
                           "}\n")

        """label_to_text = {self.label_19: self.song_title,
                         self.mainPageLikedSongsArtistButton: self.artist_name,
                         self.mainPageLikedSongsCategoryButton: self.category_name,
                         self.label_20: self.date_added,
                         self.label_21: self.song_length}"""

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 56))
        self.setMaximumSize(QtCore.QSize(16777215, 56))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.frame_78 = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_78.sizePolicy().hasHeightForWidth())
        self.frame_78.setSizePolicy(sizePolicy)
        self.frame_78.setMinimumSize(QtCore.QSize(110, 40))
        self.frame_78.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_78.setObjectName("frame_78")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_78)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.frame_79 = QtWidgets.QFrame(self.frame_78)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_79.sizePolicy().hasHeightForWidth())
        self.frame_79.setSizePolicy(sizePolicy)
        self.frame_79.setMinimumSize(QtCore.QSize(55, 40))
        self.frame_79.setMaximumSize(QtCore.QSize(55, 40))
        self.frame_79.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_79.setObjectName("frame_79")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.frame_79)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_79)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)
        self.pushButton_30.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_30.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_30.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_30.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_favorite_border_gray_48dp.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_30.setIcon(icon8)
        self.pushButton_30.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_30.setCheckable(True)
        self.pushButton_30.setChecked(self.is_liked)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_27.addWidget(self.pushButton_30, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.frame_79, 0, 1, 1, 1)
        self.frame_174 = QtWidgets.QFrame(self.frame_78)
        self.frame_174.setMinimumSize(QtCore.QSize(55, 40))
        self.frame_174.setMaximumSize(QtCore.QSize(55, 40))
        self.frame_174.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_174.setObjectName("frame_174")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.frame_174)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_174)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_13.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_13.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_play_arrow_white_48dp.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_pause_white_48dp.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.On)
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(self.is_playing)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_28.addWidget(self.pushButton_13, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.frame_174, 0, 0, 1, 1)
        self.horizontalLayout_36.addWidget(self.frame_78)

        if self.song_title:
            self.label_19 = QtWidgets.QLabel(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
            self.label_19.setSizePolicy(sizePolicy)
            self.label_19.setMinimumSize(QtCore.QSize(250, 40))
            self.label_19.setObjectName("label_19")
            self.horizontalLayout_36.addWidget(self.label_19)
            self.label_19.setText(self.song_title)

        if self.artist_name:
            self.frame_34 = QtWidgets.QFrame(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
            self.frame_34.setSizePolicy(sizePolicy)
            self.frame_34.setMinimumSize(QtCore.QSize(250, 40))
            self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_34.setObjectName("frame_34")
            self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.frame_34)
            self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_53.setSpacing(0)
            self.verticalLayout_53.setObjectName("verticalLayout_53")
            self.mainPageLikedSongsArtistButton = QtWidgets.QPushButton(self.frame_34)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mainPageLikedSongsArtistButton.sizePolicy().hasHeightForWidth())
            self.mainPageLikedSongsArtistButton.setSizePolicy(sizePolicy)
            self.mainPageLikedSongsArtistButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.mainPageLikedSongsArtistButton.setObjectName("mainPageLikedSongsArtistButton")
            self.verticalLayout_53.addWidget(self.mainPageLikedSongsArtistButton)
            self.horizontalLayout_36.addWidget(self.frame_34)
            self.mainPageLikedSongsArtistButton.setText(self.artist_name)

        if self.category_name:
            self.frame_35 = QtWidgets.QFrame(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
            self.frame_35.setSizePolicy(sizePolicy)
            self.frame_35.setMinimumSize(QtCore.QSize(250, 40))
            self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_35.setObjectName("frame_35")
            self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.frame_35)
            self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_54.setSpacing(0)
            self.verticalLayout_54.setObjectName("verticalLayout_54")
            self.mainPageLikedSongsCategoryButton = QtWidgets.QPushButton(self.frame_35)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mainPageLikedSongsCategoryButton.sizePolicy().hasHeightForWidth())
            self.mainPageLikedSongsCategoryButton.setSizePolicy(sizePolicy)
            self.mainPageLikedSongsCategoryButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.mainPageLikedSongsCategoryButton.setObjectName("mainPageLikedSongsCategoryButton")
            self.verticalLayout_54.addWidget(self.mainPageLikedSongsCategoryButton)
            self.horizontalLayout_36.addWidget(self.frame_35)
            self.mainPageLikedSongsCategoryButton.setText(self.category_name)

        if self.date_added:
            self.label_20 = QtWidgets.QLabel(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
            self.label_20.setSizePolicy(sizePolicy)
            self.label_20.setMinimumSize(QtCore.QSize(250, 40))
            self.label_20.setObjectName("label_20")
            self.horizontalLayout_36.addWidget(self.label_20)
            self.label_20.setText(self.date_added)

        if self.song_length:
            self.label_21 = QtWidgets.QLabel(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
            self.label_21.setSizePolicy(sizePolicy)
            self.label_21.setMinimumSize(QtCore.QSize(250, 40))
            self.label_21.setObjectName("label_21")
            self.horizontalLayout_36.addWidget(self.label_21)
            self.label_21.setText(self.song_length)
