from PySide2 import QtCore, QtGui, QtWidgets
from app.src import resources_peach_player
from app.src.classes.layouts.song_entry_qhboxlayout import VisibilityChangingElementsQHBoxLayout

from datetime import datetime


# TODO Move Sort Buttons logic to this Class from app_controller and try doing triple state, take care of when
# TODO one sort Button is not present and its state changing fails in app_view
# TODO Add Class' initialization arguments docstring
class SortButtonsQFrame(QtWidgets.QFrame):
    """Sort Button's Frame UI entry with predefined layout. Used in every Page that has SongEntries to indicate what
     SongFrame's Data Element shows and as Sort Buttons Container."""

    resized = QtCore.Signal()

    def __init__(self, *, parent=None, frame_structure=None, visibility_changing_sort_buttons_elements=None):
        super().__init__(parent=parent)
        if frame_structure is None:
            self.frame_structure = {"song_title": False, "artist_name": False, "category_name": False,
                                    "date_added": False, "song_length": False}
        else:
            self.frame_structure = frame_structure
        if visibility_changing_sort_buttons_elements is None:
            self.all_visibility_changing_sort_button_elements = []
        else:
            self.all_visibility_changing_sort_button_elements = visibility_changing_sort_buttons_elements
        # All sort Buttons that can be present inside SortButtonsQFrame, they are later used to set proper maxWidth
        # of each sort Button's Frame. Every new sort Button's QFrame should be added there.
        self.all_sort_button_elements = ["sortButtonsQFrameTitleButtonQFrame", "sortButtonsQFrameAuthorButtonQFrame",
                                         "sortButtonsQFrameCategoryButtonQFrame",
                                         "sortButtonsQFrameDateAddedButtonQFrame",
                                         "sortButtonsQFrameSongLengthButtonQFrame"]

        self.setupLayout()
        self.resized.connect(self.adjust_sort_buttons_qframe_sort_buttons_frames_visibility)

        # Order on which SongEntry data elements are shown when certain width threshold is reached.
        # It is created by using getattr to get handle to data element and encapsulating it with its threshold in tuple
        # in following way (data_element_handle, threshold)
        self.visibility_order = [(getattr(self, x[0]), x[1]) for x in self.all_visibility_changing_sort_button_elements
                                 if hasattr(self, x[0])]
        # QtCore.QTimer.singleShot(20, self.test_fix)

    def setupLayout(self):
        self.setStyleSheet("#sortButtonsQFrameAuthorButtonQFrame{\n"
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
                           "}\n")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 41))
        self.setMaximumSize(QtCore.QSize(16777215, 40))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)

        self.horizontalLayout_32 = VisibilityChangingElementsQHBoxLayout(self)

        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        spacerItem10 = QtWidgets.QSpacerItem(110, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_32.addItem(spacerItem10)

        if self.frame_structure["sortButtonsQFrameTitleButtonQFrame"]:
            self.sortButtonsQFrameTitleButtonQFrame = QtWidgets.QFrame(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.sortButtonsQFrameTitleButtonQFrame.sizePolicy().hasHeightForWidth())
            self.sortButtonsQFrameTitleButtonQFrame.setSizePolicy(sizePolicy)
            self.sortButtonsQFrameTitleButtonQFrame.setMinimumSize(QtCore.QSize(0, 40))
            self.sortButtonsQFrameTitleButtonQFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.sortButtonsQFrameTitleButtonQFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.sortButtonsQFrameTitleButtonQFrame.setObjectName("sortButtonsQFrameTitleButtonQFrame")
            self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.sortButtonsQFrameTitleButtonQFrame)
            self.verticalLayout_32.setContentsMargins(0, 8, 0, 0)
            self.verticalLayout_32.setSpacing(0)
            self.verticalLayout_32.setObjectName("verticalLayout_32")
            self.frame_354 = QtWidgets.QFrame(self.sortButtonsQFrameTitleButtonQFrame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_354.sizePolicy().hasHeightForWidth())
            self.frame_354.setSizePolicy(sizePolicy)
            self.frame_354.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_354.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_354.setObjectName("frame_354")
            self.horizontalLayout_70 = QtWidgets.QHBoxLayout(self.frame_354)
            self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_70.setSpacing(0)
            self.horizontalLayout_70.setObjectName("horizontalLayout_70")
            self.mainPageLikedSongsTitleSortButton = QtWidgets.QPushButton(self.frame_354)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mainPageLikedSongsTitleSortButton.sizePolicy().hasHeightForWidth())
            self.mainPageLikedSongsTitleSortButton.setSizePolicy(sizePolicy)
            self.mainPageLikedSongsTitleSortButton.setText("TITLE")
            self.mainPageLikedSongsTitleSortButton.setCheckable(True)
            self.mainPageLikedSongsTitleSortButton.setAutoExclusive(False)
            self.mainPageLikedSongsTitleSortButton.setObjectName("mainPageLikedSongsTitleSortButton")
            self.horizontalLayout_70.addWidget(self.mainPageLikedSongsTitleSortButton)
            self.frame_355 = QtWidgets.QFrame(self.frame_354)
            self.frame_355.setMinimumSize(QtCore.QSize(20, 19))
            self.frame_355.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_355.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_355.setObjectName("frame_355")
            self.horizontalLayout_69 = QtWidgets.QHBoxLayout(self.frame_355)
            self.horizontalLayout_69.setContentsMargins(13, 0, 0, 0)
            self.horizontalLayout_69.setSpacing(0)
            self.horizontalLayout_69.setObjectName("horizontalLayout_69")
            self.label_213 = QtWidgets.QLabel(self.frame_355)
            self.label_213.setVisible(False)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_213.sizePolicy().hasHeightForWidth())
            self.label_213.setSizePolicy(sizePolicy)
            self.label_213.setMinimumSize(QtCore.QSize(20, 20))
            self.label_213.setMaximumSize(QtCore.QSize(20, 20))
            self.label_213.setText("")
            self.label_213.setPixmap(
                QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_expand_more_peach_48dp.png"))
            self.label_213.setScaledContents(True)
            self.label_213.setObjectName("label_213")
            self.horizontalLayout_69.addWidget(self.label_213)
            self.horizontalLayout_70.addWidget(self.frame_355)
            self.verticalLayout_32.addWidget(self.frame_354)
            self.horizontalLayout_32.addWidget(self.sortButtonsQFrameTitleButtonQFrame)

        if self.frame_structure["sortButtonsQFrameAuthorButtonQFrame"]:
            self.sortButtonsQFrameAuthorButtonQFrame = QtWidgets.QFrame(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.sortButtonsQFrameAuthorButtonQFrame.sizePolicy().hasHeightForWidth())
            self.sortButtonsQFrameAuthorButtonQFrame.setSizePolicy(sizePolicy)
            self.sortButtonsQFrameAuthorButtonQFrame.setMinimumSize(QtCore.QSize(0, 40))
            self.sortButtonsQFrameAuthorButtonQFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.sortButtonsQFrameAuthorButtonQFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.sortButtonsQFrameAuthorButtonQFrame.setObjectName("sortButtonsQFrameAuthorButtonQFrame")
            self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.sortButtonsQFrameAuthorButtonQFrame)
            self.verticalLayout_33.setContentsMargins(0, 8, 0, 0)
            self.verticalLayout_33.setSpacing(0)
            self.verticalLayout_33.setObjectName("verticalLayout_33")
            self.frame_356 = QtWidgets.QFrame(self.sortButtonsQFrameAuthorButtonQFrame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_356.sizePolicy().hasHeightForWidth())
            self.frame_356.setSizePolicy(sizePolicy)
            self.frame_356.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_356.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_356.setObjectName("frame_356")
            self.horizontalLayout_71 = QtWidgets.QHBoxLayout(self.frame_356)
            self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_71.setSpacing(0)
            self.horizontalLayout_71.setObjectName("horizontalLayout_71")
            self.mainPageLikedSongsArtistSortButton = QtWidgets.QPushButton(self.frame_356)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mainPageLikedSongsArtistSortButton.sizePolicy().hasHeightForWidth())
            self.mainPageLikedSongsArtistSortButton.setSizePolicy(sizePolicy)
            self.mainPageLikedSongsArtistSortButton.setText("ARTIST")
            self.mainPageLikedSongsArtistSortButton.setCheckable(True)
            self.mainPageLikedSongsArtistSortButton.setAutoExclusive(False)
            self.mainPageLikedSongsArtistSortButton.setObjectName("mainPageLikedSongsArtistSortButton")
            self.horizontalLayout_71.addWidget(self.mainPageLikedSongsArtistSortButton)
            self.frame_357 = QtWidgets.QFrame(self.frame_356)
            self.frame_357.setMinimumSize(QtCore.QSize(20, 19))
            self.frame_357.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_357.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_357.setObjectName("frame_357")
            self.horizontalLayout_72 = QtWidgets.QHBoxLayout(self.frame_357)
            self.horizontalLayout_72.setContentsMargins(13, 0, 0, 0)
            self.horizontalLayout_72.setSpacing(0)
            self.horizontalLayout_72.setObjectName("horizontalLayout_72")
            self.label_214 = QtWidgets.QLabel(self.frame_357)
            self.label_214.setVisible(False)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_214.sizePolicy().hasHeightForWidth())
            self.label_214.setSizePolicy(sizePolicy)
            self.label_214.setMinimumSize(QtCore.QSize(20, 20))
            self.label_214.setMaximumSize(QtCore.QSize(20, 20))
            self.label_214.setText("")
            self.label_214.setPixmap(
                QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_expand_more_peach_48dp.png"))
            self.label_214.setScaledContents(True)
            self.label_214.setObjectName("label_214")
            self.horizontalLayout_72.addWidget(self.label_214)
            self.horizontalLayout_71.addWidget(self.frame_357)
            self.verticalLayout_33.addWidget(self.frame_356)
            self.horizontalLayout_32.addWidget(self.sortButtonsQFrameAuthorButtonQFrame)

        if self.frame_structure["sortButtonsQFrameCategoryButtonQFrame"]:
            self.sortButtonsQFrameCategoryButtonQFrame = QtWidgets.QFrame(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.sortButtonsQFrameCategoryButtonQFrame.sizePolicy().hasHeightForWidth())
            self.sortButtonsQFrameCategoryButtonQFrame.setSizePolicy(sizePolicy)
            self.sortButtonsQFrameCategoryButtonQFrame.setMinimumSize(QtCore.QSize(0, 40))
            self.sortButtonsQFrameCategoryButtonQFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.sortButtonsQFrameCategoryButtonQFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.sortButtonsQFrameCategoryButtonQFrame.setObjectName("sortButtonsQFrameCategoryButtonQFrame")
            self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.sortButtonsQFrameCategoryButtonQFrame)
            self.verticalLayout_34.setContentsMargins(0, 8, 0, 0)
            self.verticalLayout_34.setSpacing(0)
            self.verticalLayout_34.setObjectName("verticalLayout_34")
            self.frame_358 = QtWidgets.QFrame(self.sortButtonsQFrameCategoryButtonQFrame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_358.sizePolicy().hasHeightForWidth())
            self.frame_358.setSizePolicy(sizePolicy)
            self.frame_358.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_358.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_358.setObjectName("frame_358")
            self.horizontalLayout_73 = QtWidgets.QHBoxLayout(self.frame_358)
            self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_73.setSpacing(0)
            self.horizontalLayout_73.setObjectName("horizontalLayout_73")
            self.mainPageLikedSongsCategorySortButton = QtWidgets.QPushButton(self.frame_358)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mainPageLikedSongsCategorySortButton.sizePolicy().hasHeightForWidth())
            self.mainPageLikedSongsCategorySortButton.setSizePolicy(sizePolicy)
            self.mainPageLikedSongsCategorySortButton.setText("CATEGORY")
            self.mainPageLikedSongsCategorySortButton.setCheckable(True)
            self.mainPageLikedSongsCategorySortButton.setAutoExclusive(False)
            self.mainPageLikedSongsCategorySortButton.setObjectName("mainPageLikedSongsCategorySortButton")
            self.horizontalLayout_73.addWidget(self.mainPageLikedSongsCategorySortButton)
            self.frame_359 = QtWidgets.QFrame(self.frame_358)
            self.frame_359.setMinimumSize(QtCore.QSize(20, 19))
            self.frame_359.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_359.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_359.setObjectName("frame_359")
            self.horizontalLayout_74 = QtWidgets.QHBoxLayout(self.frame_359)
            self.horizontalLayout_74.setContentsMargins(13, 0, 0, 0)
            self.horizontalLayout_74.setSpacing(0)
            self.horizontalLayout_74.setObjectName("horizontalLayout_74")
            self.label_215 = QtWidgets.QLabel(self.frame_359)
            self.label_215.setVisible(False)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_215.sizePolicy().hasHeightForWidth())
            self.label_215.setSizePolicy(sizePolicy)
            self.label_215.setMinimumSize(QtCore.QSize(20, 20))
            self.label_215.setMaximumSize(QtCore.QSize(20, 20))
            self.label_215.setText("")
            self.label_215.setPixmap(
                QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_expand_more_peach_48dp.png"))
            self.label_215.setScaledContents(True)
            self.label_215.setObjectName("label_215")
            self.horizontalLayout_74.addWidget(self.label_215)
            self.horizontalLayout_73.addWidget(self.frame_359)
            self.verticalLayout_34.addWidget(self.frame_358)
            self.horizontalLayout_32.addWidget(self.sortButtonsQFrameCategoryButtonQFrame)

        if self.frame_structure["sortButtonsQFrameDateAddedButtonQFrame"]:
            self.sortButtonsQFrameDateAddedButtonQFrame = QtWidgets.QFrame(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.sortButtonsQFrameDateAddedButtonQFrame.sizePolicy().hasHeightForWidth())
            self.sortButtonsQFrameDateAddedButtonQFrame.setSizePolicy(sizePolicy)
            self.sortButtonsQFrameDateAddedButtonQFrame.setMinimumSize(QtCore.QSize(0, 40))
            self.sortButtonsQFrameDateAddedButtonQFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.sortButtonsQFrameDateAddedButtonQFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.sortButtonsQFrameDateAddedButtonQFrame.setObjectName("sortButtonsQFrameDateAddedButtonQFrame")
            self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.sortButtonsQFrameDateAddedButtonQFrame)
            self.verticalLayout_35.setContentsMargins(0, 8, 0, 0)
            self.verticalLayout_35.setSpacing(0)
            self.verticalLayout_35.setObjectName("verticalLayout_35")
            self.frame_360 = QtWidgets.QFrame(self.sortButtonsQFrameDateAddedButtonQFrame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_360.sizePolicy().hasHeightForWidth())
            self.frame_360.setSizePolicy(sizePolicy)
            self.frame_360.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_360.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_360.setObjectName("frame_360")
            self.horizontalLayout_75 = QtWidgets.QHBoxLayout(self.frame_360)
            self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_75.setSpacing(0)
            self.horizontalLayout_75.setObjectName("horizontalLayout_75")
            self.mainPageLikedSongsAddedSortButton = QtWidgets.QPushButton(self.frame_360)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mainPageLikedSongsAddedSortButton.sizePolicy().hasHeightForWidth())
            self.mainPageLikedSongsAddedSortButton.setSizePolicy(sizePolicy)
            self.mainPageLikedSongsAddedSortButton.setText("ADDED")
            self.mainPageLikedSongsAddedSortButton.setCheckable(True)
            self.mainPageLikedSongsAddedSortButton.setAutoExclusive(False)
            self.mainPageLikedSongsAddedSortButton.setObjectName("mainPageLikedSongsAddedSortButton")
            self.horizontalLayout_75.addWidget(self.mainPageLikedSongsAddedSortButton)
            self.frame_361 = QtWidgets.QFrame(self.frame_360)
            self.frame_361.setMinimumSize(QtCore.QSize(20, 19))
            self.frame_361.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_361.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_361.setObjectName("frame_361")
            self.horizontalLayout_76 = QtWidgets.QHBoxLayout(self.frame_361)
            self.horizontalLayout_76.setContentsMargins(13, 0, 0, 0)
            self.horizontalLayout_76.setSpacing(0)
            self.horizontalLayout_76.setObjectName("horizontalLayout_76")
            self.label_216 = QtWidgets.QLabel(self.frame_361)
            self.label_216.setVisible(False)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_216.sizePolicy().hasHeightForWidth())
            self.label_216.setSizePolicy(sizePolicy)
            self.label_216.setMinimumSize(QtCore.QSize(20, 20))
            self.label_216.setMaximumSize(QtCore.QSize(20, 20))
            self.label_216.setText("")
            self.label_216.setPixmap(
                QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_expand_more_peach_48dp.png"))
            self.label_216.setScaledContents(True)
            self.label_216.setObjectName("label_216")
            self.horizontalLayout_76.addWidget(self.label_216)
            self.horizontalLayout_75.addWidget(self.frame_361)
            self.verticalLayout_35.addWidget(self.frame_360)
            self.horizontalLayout_32.addWidget(self.sortButtonsQFrameDateAddedButtonQFrame)

        if self.frame_structure["sortButtonsQFrameSongLengthButtonQFrame"]:
            self.sortButtonsQFrameSongLengthButtonQFrame = QtWidgets.QFrame(self)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.sortButtonsQFrameSongLengthButtonQFrame.sizePolicy().hasHeightForWidth())
            self.sortButtonsQFrameSongLengthButtonQFrame.setSizePolicy(sizePolicy)
            self.sortButtonsQFrameSongLengthButtonQFrame.setMinimumSize(QtCore.QSize(0, 40))
            self.sortButtonsQFrameSongLengthButtonQFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.sortButtonsQFrameSongLengthButtonQFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.sortButtonsQFrameSongLengthButtonQFrame.setObjectName("sortButtonsQFrameSongLengthButtonQFrame")
            self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.sortButtonsQFrameSongLengthButtonQFrame)
            self.verticalLayout_52.setContentsMargins(0, 8, 0, 0)
            self.verticalLayout_52.setSpacing(0)
            self.verticalLayout_52.setObjectName("verticalLayout_52")
            self.frame_362 = QtWidgets.QFrame(self.sortButtonsQFrameSongLengthButtonQFrame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_362.sizePolicy().hasHeightForWidth())
            self.frame_362.setSizePolicy(sizePolicy)
            self.frame_362.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_362.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_362.setObjectName("frame_362")
            self.horizontalLayout_77 = QtWidgets.QHBoxLayout(self.frame_362)
            self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_77.setSpacing(0)
            self.horizontalLayout_77.setObjectName("horizontalLayout_77")
            self.mainPageLikedSongsLengthSortButton = QtWidgets.QPushButton(self.frame_362)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.mainPageLikedSongsLengthSortButton.sizePolicy().hasHeightForWidth())
            self.mainPageLikedSongsLengthSortButton.setSizePolicy(sizePolicy)
            self.mainPageLikedSongsLengthSortButton.setText("LENGTH")
            self.mainPageLikedSongsLengthSortButton.setCheckable(True)
            self.mainPageLikedSongsLengthSortButton.setAutoExclusive(False)
            self.mainPageLikedSongsLengthSortButton.setObjectName("mainPageLikedSongsLengthSortButton")
            self.horizontalLayout_77.addWidget(self.mainPageLikedSongsLengthSortButton)
            self.frame_363 = QtWidgets.QFrame(self.frame_362)
            self.frame_363.setMinimumSize(QtCore.QSize(20, 19))
            self.frame_363.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_363.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_363.setObjectName("frame_363")
            self.horizontalLayout_78 = QtWidgets.QHBoxLayout(self.frame_363)
            self.horizontalLayout_78.setContentsMargins(13, 0, 0, 0)
            self.horizontalLayout_78.setSpacing(0)
            self.horizontalLayout_78.setObjectName("horizontalLayout_78")
            self.label_217 = QtWidgets.QLabel(self.frame_363)
            self.label_217.setVisible(False)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_217.sizePolicy().hasHeightForWidth())
            self.label_217.setSizePolicy(sizePolicy)
            self.label_217.setMinimumSize(QtCore.QSize(20, 20))
            self.label_217.setMaximumSize(QtCore.QSize(20, 20))
            self.label_217.setText("")
            self.label_217.setPixmap(
                QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_expand_more_peach_48dp.png"))
            self.label_217.setScaledContents(True)
            self.label_217.setObjectName("label_217")
            self.horizontalLayout_78.addWidget(self.label_217)
            self.horizontalLayout_77.addWidget(self.frame_363)
            self.verticalLayout_52.addWidget(self.frame_362)
            self.horizontalLayout_32.addWidget(self.sortButtonsQFrameSongLengthButtonQFrame)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(SortButtonsQFrame, self).resizeEvent(event)

    def adjust_sort_buttons_qframe_sort_buttons_frames_visibility(self):
        """Manage the visibility of sort Buttons' frames. Adjust their visibility when certain
        width thresholds are reached."""
        # check if there are any elements that should be hidden when certain thresholds are reached
        if self.visibility_order:
            # iterate over visibility_order and toggle elements' visibility when certain thresholds are reached
            for element, startingThreshold in self.visibility_order:
                if startingThreshold <= self.width():
                    if not element.isVisible():
                        element.setVisible(True)
                else:
                    if element.isVisible():
                        element.setVisible(False)
        return
        print(f"Adjusting visibility of {self.objectName()}")
        if getattr(self, "sortButtonsQFrameTitleButtonQFrame", 0):
            print(
                f"sortButtonsQFrameTitleButtonQFrame width :| {self.sortButtonsQFrameTitleButtonQFrame.width()} | {self.sortButtonsQFrameTitleButtonQFrame.isVisible()}")

        if getattr(self, "sortButtonsQFrameAuthorButtonQFrame", 0):
            print(
                f"sortButtonsQFrameAuthorButtonQFrame width :| {self.sortButtonsQFrameAuthorButtonQFrame.width()} | {self.sortButtonsQFrameAuthorButtonQFrame.isVisible()}")

        if getattr(self, "sortButtonsQFrameCategoryButtonQFrame", 0):
            print(
                f"sortButtonsQFrameCategoryButtonQFrame width :| {self.sortButtonsQFrameCategoryButtonQFrame.width()} | {self.sortButtonsQFrameCategoryButtonQFrame.isVisible()}")

        if getattr(self, "sortButtonsQFrameDateAddedButtonQFrame", 0):
            print(
                f"sortButtonsQFrameDateAddedButtonQFrame width :| {self.sortButtonsQFrameDateAddedButtonQFrame.width()} | {self.sortButtonsQFrameDateAddedButtonQFrame.isVisible()}")

        if getattr(self, "sortButtonsQFrameSongLengthButtonQFrame", 0):
            print(
                f"sortButtonsQFrameSongLengthButtonQFrame width :| {self.sortButtonsQFrameSongLengthButtonQFrame.width()} | {self.sortButtonsQFrameSongLengthButtonQFrame.isVisible()}\n")

    def obtain_visible_data_elements(self):
        """Obtain visible elements that are present in SortButtonsQFrame. Used to calculate each element's proper
        width. """
        # all elements inside SortButtonsQFrame that are present and visible
        visible_sort_buttons_elements = [getattr(self, x) for x in self.all_sort_button_elements if hasattr(self, x)]
        visible_sort_buttons_elements = [x for x in visible_sort_buttons_elements if x.isVisible()]

        return visible_sort_buttons_elements

    def adjust_visible_data_elements_maximum_size(self):
        """Adjust maximum width of SortButtonsQFrame's sort Button's frames to one value. Called by
         VisibilityChangingElementsQHBoxLayout before setting  geometry to prevent conflicts."""
        # obtain all data element that are currently present and visible in the SortButtonsQFrame
        visible_data_elements = self.obtain_visible_data_elements()
        # adjust each element's maximumWidth to one size by dividing SortButtonsQFrame's current width minus left
        # spacer's width (110) by number of visible elements
        for element in visible_data_elements:
            element.setMaximumWidth(int((self.width() - 110) / len(visible_data_elements)))

    def test_fix(self):
        lista = []
        for x in self.all_sort_button_elements:
            if hasattr(self, x):
                lista.append(getattr(self, x))
        print(self.objectName())
        for x in lista:
            x.setVisible(True)
            print(f"{x.objectName()} : {x.isVisible()}")
        print("\n")
