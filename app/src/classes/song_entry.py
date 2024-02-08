from PySide2 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player
from app.src.classes.layouts.song_entry_qhboxlayout import VisibilityChangingElementsQHBoxLayout
from typing import Type


class SongEntry(QtWidgets.QFrame):
    """Song type ui entry with predefined layout. Uses frame_structure to define which data elements should be
    visible.

    Args:
            song_id: song identification number.
            song_title: name of the Song, will be displayed in songEntrySongNameQLabel.
            artist_name: name of the Song's author, will be displayed in songEntrySongAuthorQPushButton.
            category_name: name of the Song's category, will be displayed in songEntrySongCategoryQPushButton.
            date_added: date of when Song was added, will be displayed in songEntrySongDateAddedQLabel.
            song_length: length of Song, will be displayed in songEntrySongSongLengthQLabel.
            path: path to the Song's file.
            is_liked: determines if Song is in users liked songs.
            parent: parent of SongEntry.
            frame_structure: determines which data elements should be visible in SongEntry.
            visibility_changing_data_elements: data elements that should be hidden when a certain threshold is reached



    """

    resized = QtCore.Signal()

    def __init__(self, *, song_id: int, song_title: str = "No title", artist_name: str = "No author",
                 category_name: str = "No category", date_added: int = None, song_length: int = None,
                 path=None, is_liked: bool = False, parent: Type[QtWidgets.QWidget] = None,
                 frame_structure: dict[str, bool] = None, visibility_changing_data_elements: list[tuple[str, int]] = None):

        super().__init__(parent=parent)
        if frame_structure is None:
            self.frame_structure = {"song_title": False, "artist_name": False, "category_name": False,
                                    "date_added": False, "song_length": False}
        else:
            self.frame_structure = frame_structure
        self.song_id = song_id
        self.song_title = song_title
        self.artist_name = artist_name
        self.category_name = category_name
        self.date_added = date_added
        self.song_length = song_length
        self.path = path
        self.is_liked = is_liked

        if visibility_changing_data_elements is None:
            self.all_visibility_changing_data_elements = []
        else:
            self.all_visibility_changing_data_elements = visibility_changing_data_elements
        # All elements that can be present inside SongEntry, they are later used to set proper maxWidth of each data
        # element. Every new data element should be added there.
        self.all_data_elements = ["songEntrySongNameQLabel", "songEntrySongDateAddedQLabel",
                                  "songEntrySongCategoryQFrame", "songEntrySongSongLengthQLabel",
                                  "songEntrySongAuthorQFrame"]

        self.setup_layout()
        self.resized.connect(self.adjust_song_entry_data_entries_visibility)

        # Order on which SongEntry data elements are shown when certain width threshold is reached.
        self.visibility_order = [(getattr(self, x[0]), x[1]) for x in self.all_visibility_changing_data_elements if
                                 hasattr(self, x[0])]

    def setup_layout(self):
        self.setStyleSheet("#songEntrySongNameQLabel{\n"
                           "     color: white;\n"
                           "}\n"
                           "#pushButton_30:hover:!checked{\n"
                           "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_favorite_border_white_48dp.png);\n"
                           "}\n"
                           " #pushButton_30:checked{\n"
                           "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_favorite_peach_48dp.png);\n"
                           "}\n"
                           "#songEntrySongDateAddedQLabel{\n"
                           "    padding-left: 25px;\n"
                           "}\n"
                           "#songEntrySongSongLengthQLabel{\n"
                           "    padding-left: 25px;\n"
                           "}\n"
                           "#songEntrySongAuthorQFrame{\n"
                           "    padding-left: 25px;\n"
                           "}\n"
                           "#songEntrySongCategoryQFrame{\n"
                           "    padding-left: 25px;\n"
                           "}\n")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 56))
        self.setMaximumSize(QtCore.QSize(16777215, 56))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout_36 = VisibilityChangingElementsQHBoxLayout(self)
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
        icon.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_pause_white_48dp.png"),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.On)
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_28.addWidget(self.pushButton_13, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.frame_174, 0, 0, 1, 1)
        self.horizontalLayout_36.addWidget(self.frame_78)

        if self.frame_structure["song_title"]:
            self.songEntrySongNameQLabel = QtWidgets.QLabel(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.songEntrySongNameQLabel.sizePolicy().hasHeightForWidth())
            self.songEntrySongNameQLabel.setSizePolicy(sizePolicy)
            self.songEntrySongNameQLabel.setMinimumSize(QtCore.QSize(0, 40))
            self.songEntrySongNameQLabel.setObjectName("songEntrySongNameQLabel")
            self.horizontalLayout_36.addWidget(self.songEntrySongNameQLabel)
            self.songEntrySongNameQLabel.setText(self.song_title)

        if self.frame_structure["artist_name"]:
            self.songEntrySongAuthorQFrame = QtWidgets.QFrame(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.songEntrySongAuthorQFrame.sizePolicy().hasHeightForWidth())
            self.songEntrySongAuthorQFrame.setSizePolicy(sizePolicy)
            self.songEntrySongAuthorQFrame.setMinimumSize(QtCore.QSize(0, 40))
            self.songEntrySongAuthorQFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.songEntrySongAuthorQFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.songEntrySongAuthorQFrame.setObjectName("songEntrySongAuthorQFrame")
            self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.songEntrySongAuthorQFrame)
            self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_53.setSpacing(0)
            self.verticalLayout_53.setObjectName("verticalLayout_53")
            self.songEntrySongAuthorQPushButton = QtWidgets.QPushButton(self.songEntrySongAuthorQFrame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.songEntrySongAuthorQPushButton.sizePolicy().hasHeightForWidth())
            self.songEntrySongAuthorQPushButton.setSizePolicy(sizePolicy)
            self.songEntrySongAuthorQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.songEntrySongAuthorQPushButton.setObjectName("songEntrySongAuthorQPushButton")
            self.verticalLayout_53.addWidget(self.songEntrySongAuthorQPushButton)
            self.horizontalLayout_36.addWidget(self.songEntrySongAuthorQFrame)
            self.songEntrySongAuthorQPushButton.setText(self.artist_name)

        if self.frame_structure["category_name"]:
            self.songEntrySongCategoryQFrame = QtWidgets.QFrame(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.songEntrySongCategoryQFrame.sizePolicy().hasHeightForWidth())
            self.songEntrySongCategoryQFrame.setSizePolicy(sizePolicy)
            self.songEntrySongCategoryQFrame.setMinimumSize(QtCore.QSize(0, 40))
            self.songEntrySongCategoryQFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.songEntrySongCategoryQFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.songEntrySongCategoryQFrame.setObjectName("songEntrySongCategoryQFrame")
            self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.songEntrySongCategoryQFrame)
            self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_54.setSpacing(0)
            self.verticalLayout_54.setObjectName("verticalLayout_54")
            self.songEntrySongCategoryQPushButton = QtWidgets.QPushButton(self.songEntrySongCategoryQFrame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.songEntrySongCategoryQPushButton.sizePolicy().hasHeightForWidth())
            self.songEntrySongCategoryQPushButton.setSizePolicy(sizePolicy)
            self.songEntrySongCategoryQPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.songEntrySongCategoryQPushButton.setObjectName("songEntrySongCategoryQPushButton")
            self.verticalLayout_54.addWidget(self.songEntrySongCategoryQPushButton)
            self.horizontalLayout_36.addWidget(self.songEntrySongCategoryQFrame)
            self.songEntrySongCategoryQPushButton.setText(self.category_name)

        if self.frame_structure["date_added"]:
            self.songEntrySongDateAddedQLabel = QtWidgets.QLabel(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.songEntrySongDateAddedQLabel.sizePolicy().hasHeightForWidth())
            self.songEntrySongDateAddedQLabel.setSizePolicy(sizePolicy)
            self.songEntrySongDateAddedQLabel.setMinimumSize(QtCore.QSize(0, 40))
            self.songEntrySongDateAddedQLabel.setObjectName("songEntrySongDateAddedQLabel")
            self.horizontalLayout_36.addWidget(self.songEntrySongDateAddedQLabel)
            self.songEntrySongDateAddedQLabel.setText("No Date")
            if self.date_added:
                self.songEntrySongDateAddedQLabel.setText(str(self.date_added))

        if self.frame_structure["song_length"]:
            self.songEntrySongSongLengthQLabel = QtWidgets.QLabel(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.songEntrySongSongLengthQLabel.sizePolicy().hasHeightForWidth())
            self.songEntrySongSongLengthQLabel.setSizePolicy(sizePolicy)
            self.songEntrySongSongLengthQLabel.setMinimumSize(QtCore.QSize(0, 40))
            self.songEntrySongSongLengthQLabel.setObjectName("songEntrySongSongLengthQLabel")
            self.horizontalLayout_36.addWidget(self.songEntrySongSongLengthQLabel)
            self.songEntrySongSongLengthQLabel.setText("No Length")
            if self.song_length:
                self.songEntrySongSongLengthQLabel.setText(str(self.song_length))

    def resizeEvent(self, event):
        self.resized.emit()
        return super(SongEntry, self).resizeEvent(event)

    def adjust_song_entry_data_entries_visibility(self):
        """Manage the visibility of data elements that are present in SongEntry. Adjust their visibility when certain
        width thresholds are reached."""
        # check if there are any elements that should be hidden when certain thresholds are reached
        if self.visibility_order:
            # if SongFrame's width is shorter than first element's visibility starting threshold make all elements
            # invisible
            for element, startingThreshold in self.visibility_order:
                if startingThreshold <= self.width():
                    if not element.isVisible():
                        element.setVisible(True)
                else:
                    if element.isVisible():
                        element.setVisible(False)

    def obtain_visible_data_elements(self):
        """Obtain visible elements that are present in SongEntry. Used to calculat each element's proper width."""
        # all elements inside SongEntry that are present and visible
        visible_data_elements = [getattr(self, x) for x in self.all_data_elements if hasattr(self, x)]
        visible_data_elements = [x for x in visible_data_elements if x.isVisible()]

        return visible_data_elements

    def adjust_visible_data_elements_maximum_size(self):
        """Adjust maximum width of SongEntry's data elements to one value. Called by SongEntryQHBoxLayout before setting
        geometry to prevent conflicts."""
        # obtain all data element that are currently present and visible in the SongEntry
        visible_data_elements = self.obtain_visible_data_elements()

        # adjust each element's maximumWidth to one size by dividing SongEntry's current width minus playButton's and
        # likeButton's frame width (110) by number of visible elements
        for element in visible_data_elements:
            element.setMaximumWidth(int((self.width() - 110) / len(visible_data_elements)))
