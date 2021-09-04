from PySide2 import QtWidgets, QtCore, QtGui
from app.src import resources_peach_player
from app.src.classes.widgets.styled_qcombobox import StyledQComboBox


class SongAdder(QtWidgets.QFrame):
    """Adder type ui entry with predefined layout."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.mainPageAllSongsSongAdderQFrame = self
        self.setup_layout()

    def setup_layout(self):
        self.icon8 = QtGui.QIcon()
        self.icon8.addPixmap(
            QtGui.QPixmap(":/icons/48x48/outlined/icons/48x48/outlined/outline_favorite_border_gray_48dp.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAllSongsSongAdderQFrame.sizePolicy().hasHeightForWidth())
        self.mainPageAllSongsSongAdderQFrame.setSizePolicy(sizePolicy)
        self.mainPageAllSongsSongAdderQFrame.setMinimumSize(QtCore.QSize(0, 56))
        self.mainPageAllSongsSongAdderQFrame.setMaximumSize(QtCore.QSize(16777215, 56))
        self.mainPageAllSongsSongAdderQFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPageAllSongsSongAdderQFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPageAllSongsSongAdderQFrame.setObjectName("mainPageAllSongsSongAdderQFrame")
        self.horizontalLayout_107 = QtWidgets.QHBoxLayout(self.mainPageAllSongsSongAdderQFrame)
        self.horizontalLayout_107.setContentsMargins(0, 8, 0, 8)
        self.horizontalLayout_107.setSpacing(0)
        self.horizontalLayout_107.setObjectName("horizontalLayout_107")
        self.frame_408 = QtWidgets.QFrame(self.mainPageAllSongsSongAdderQFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_408.sizePolicy().hasHeightForWidth())
        self.frame_408.setSizePolicy(sizePolicy)
        self.frame_408.setMinimumSize(QtCore.QSize(110, 40))
        self.frame_408.setStyleSheet("background-color: none;")
        self.frame_408.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_408.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_408.setObjectName("frame_408")
        self.gridLayout_77 = QtWidgets.QGridLayout(self.frame_408)
        self.gridLayout_77.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_77.setSpacing(0)
        self.gridLayout_77.setObjectName("gridLayout_77")
        self.frame_409 = QtWidgets.QFrame(self.frame_408)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_409.sizePolicy().hasHeightForWidth())
        self.frame_409.setSizePolicy(sizePolicy)
        self.frame_409.setMinimumSize(QtCore.QSize(55, 40))
        self.frame_409.setMaximumSize(QtCore.QSize(55, 40))
        self.frame_409.setStyleSheet("QPushButton:hover:!checked{\n"
                                     "    icon: url(:/icons/48x48/outlined/icons/48x48/outlined/outline_favorite_border_white_48dp.png);\n"
                                     "}\n"
                                     "QPushButton:checked{\n"
                                     "    icon: url(:/icons/48x48/filled/icons/48x48/filled/filled_favorite_peach_48dp.png);\n"
                                     "}")
        self.frame_409.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_409.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_409.setObjectName("frame_409")
        self.gridLayout_78 = QtWidgets.QGridLayout(self.frame_409)
        self.gridLayout_78.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_78.setSpacing(0)
        self.gridLayout_78.setObjectName("gridLayout_78")
        self.mainPageAllSongsFavouriteQPushButton = QtWidgets.QPushButton(self.frame_409)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAllSongsFavouriteQPushButton.sizePolicy().hasHeightForWidth())
        self.mainPageAllSongsFavouriteQPushButton.setSizePolicy(sizePolicy)
        self.mainPageAllSongsFavouriteQPushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.mainPageAllSongsFavouriteQPushButton.setMaximumSize(QtCore.QSize(16, 16))
        self.mainPageAllSongsFavouriteQPushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.mainPageAllSongsFavouriteQPushButton.setStyleSheet("border: None;")
        self.mainPageAllSongsFavouriteQPushButton.setText("")
        self.mainPageAllSongsFavouriteQPushButton.setIcon(self.icon8)
        self.mainPageAllSongsFavouriteQPushButton.setIconSize(QtCore.QSize(16, 16))
        self.mainPageAllSongsFavouriteQPushButton.setCheckable(True)
        self.mainPageAllSongsFavouriteQPushButton.setChecked(False)
        self.mainPageAllSongsFavouriteQPushButton.setObjectName("mainPageAllSongsFavouriteQPushButton")
        self.gridLayout_78.addWidget(self.mainPageAllSongsFavouriteQPushButton, 0, 0, 1, 1)
        self.gridLayout_77.addWidget(self.frame_409, 0, 1, 1, 1)
        self.frame_410 = QtWidgets.QFrame(self.frame_408)
        self.frame_410.setMinimumSize(QtCore.QSize(55, 40))
        self.frame_410.setMaximumSize(QtCore.QSize(55, 40))
        self.frame_410.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_410.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_410.setObjectName("frame_410")
        self.gridLayout_79 = QtWidgets.QGridLayout(self.frame_410)
        self.gridLayout_79.setObjectName("gridLayout_79")
        self.mainPageAllSongAddSongQPushButton = QtWidgets.QPushButton(self.frame_410)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAllSongAddSongQPushButton.sizePolicy().hasHeightForWidth())
        self.mainPageAllSongAddSongQPushButton.setSizePolicy(sizePolicy)
        self.mainPageAllSongAddSongQPushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.mainPageAllSongAddSongQPushButton.setMaximumSize(QtCore.QSize(16, 16))
        self.mainPageAllSongAddSongQPushButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/48x48/filled/icons/48x48/filled/filled_add_gray_48dp.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainPageAllSongAddSongQPushButton.setIcon(icon10)
        self.mainPageAllSongAddSongQPushButton.setIconSize(QtCore.QSize(24, 24))
        self.mainPageAllSongAddSongQPushButton.setObjectName("mainPageAllSongAddSongQPushButton")
        self.gridLayout_79.addWidget(self.mainPageAllSongAddSongQPushButton, 0, 0, 1, 1)
        self.gridLayout_77.addWidget(self.frame_410, 0, 0, 1, 1)
        self.horizontalLayout_107.addWidget(self.frame_408)
        self.frame_88 = QtWidgets.QFrame(self.mainPageAllSongsSongAdderQFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_88.sizePolicy().hasHeightForWidth())
        self.frame_88.setSizePolicy(sizePolicy)
        self.frame_88.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_88.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_88.setObjectName("frame_88")
        self.verticalLayout_256 = QtWidgets.QVBoxLayout(self.frame_88)
        self.verticalLayout_256.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_256.setSpacing(0)
        self.verticalLayout_256.setObjectName("verticalLayout_256")
        self.mainPageAllSongsSelectSongQPushButton = QtWidgets.QPushButton(self.frame_88)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAllSongsSelectSongQPushButton.sizePolicy().hasHeightForWidth())
        self.mainPageAllSongsSelectSongQPushButton.setSizePolicy(sizePolicy)
        self.mainPageAllSongsSelectSongQPushButton.setText("Choose song file")
        self.mainPageAllSongsSelectSongQPushButton.setObjectName("mainPageAllSongsSelectSongQPushButton")
        self.verticalLayout_256.addWidget(self.mainPageAllSongsSelectSongQPushButton)
        self.horizontalLayout_107.addWidget(self.frame_88)
        self.frame_411 = QtWidgets.QFrame(self.mainPageAllSongsSongAdderQFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_411.sizePolicy().hasHeightForWidth())
        self.frame_411.setSizePolicy(sizePolicy)
        self.frame_411.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_411.setStyleSheet("")
        self.frame_411.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_411.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_411.setObjectName("frame_411")
        self.verticalLayout_257 = QtWidgets.QVBoxLayout(self.frame_411)
        self.verticalLayout_257.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_257.setSpacing(0)
        self.verticalLayout_257.setObjectName("verticalLayout_257")
        self.mainPageAllSongsSelectSongMiniatureQPushButton = QtWidgets.QPushButton(self.frame_411)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainPageAllSongsSelectSongMiniatureQPushButton.sizePolicy().hasHeightForWidth())
        self.mainPageAllSongsSelectSongMiniatureQPushButton.setSizePolicy(sizePolicy)
        self.mainPageAllSongsSelectSongMiniatureQPushButton.setText("Choose song miniature")
        self.mainPageAllSongsSelectSongMiniatureQPushButton.setObjectName(
            "mainPageAllSongsSelectSongMiniatureQPushButton")
        self.verticalLayout_257.addWidget(self.mainPageAllSongsSelectSongMiniatureQPushButton)
        self.horizontalLayout_107.addWidget(self.frame_411)
        self.frame_454 = QtWidgets.QFrame(self.mainPageAllSongsSongAdderQFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_454.sizePolicy().hasHeightForWidth())
        self.frame_454.setSizePolicy(sizePolicy)
        self.frame_454.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_454.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_454.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_454.setObjectName("frame_454")
        self.verticalLayout_277 = QtWidgets.QVBoxLayout(self.frame_454)
        self.verticalLayout_277.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_277.setSpacing(0)
        self.verticalLayout_277.setObjectName("verticalLayout_277")
        self.mainPageAllSongsSongTitleQLineEdit = QtWidgets.QLineEdit(self.frame_454)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAllSongsSongTitleQLineEdit.sizePolicy().hasHeightForWidth())
        self.mainPageAllSongsSongTitleQLineEdit.setSizePolicy(sizePolicy)
        self.mainPageAllSongsSongTitleQLineEdit.setMinimumSize(QtCore.QSize(175, 40))
        self.mainPageAllSongsSongTitleQLineEdit.setInputMask("")
        self.mainPageAllSongsSongTitleQLineEdit.setPlaceholderText("Song title")
        self.mainPageAllSongsSongTitleQLineEdit.setObjectName("mainPageAllSongsSongTitleQLineEdit")
        self.verticalLayout_277.addWidget(self.mainPageAllSongsSongTitleQLineEdit)
        self.horizontalLayout_107.addWidget(self.frame_454)
        self.frame_412 = QtWidgets.QFrame(self.mainPageAllSongsSongAdderQFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_412.sizePolicy().hasHeightForWidth())
        self.frame_412.setSizePolicy(sizePolicy)
        self.frame_412.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_412.setStyleSheet("")
        self.frame_412.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_412.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_412.setObjectName("frame_412")
        self.verticalLayout_258 = QtWidgets.QVBoxLayout(self.frame_412)
        self.verticalLayout_258.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_258.setSpacing(0)
        self.verticalLayout_258.setObjectName("verticalLayout_258")

        self.mainPageAllSongsSongAuthorQComboBox = StyledQComboBox(self.frame_412)
        self.mainPageAllSongsSongAuthorQComboBox.setMaxVisibleItems(10)
        self.mainPageAllSongsSongAuthorQComboBox.setFixedSize(175, 40)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAllSongsSongAuthorQComboBox.sizePolicy().hasHeightForWidth())
        self.mainPageAllSongsSongAuthorQComboBox.setSizePolicy(sizePolicy)
        self.mainPageAllSongsSongAuthorQComboBox.setMinimumSize(QtCore.QSize(125, 0))
        self.mainPageAllSongsSongAuthorQComboBox.setObjectName("mainPageAllSongsSongAuthorQComboBox")
        self.mainPageAllSongsSongAuthorQComboBox.addItem("")
        self.mainPageAllSongsSongAuthorQComboBox.setItemText(0, "noAuthor")
        self.mainPageAllSongsSongAuthorQComboBox.addItem("")
        self.mainPageAllSongsSongAuthorQComboBox.setItemText(1, "Author1")
        self.mainPageAllSongsSongAuthorQComboBox.addItem("")
        self.mainPageAllSongsSongAuthorQComboBox.setItemText(2, "Author2")
        self.verticalLayout_258.addWidget(self.mainPageAllSongsSongAuthorQComboBox)

        self.horizontalLayout_107.addWidget(self.frame_412)
        self.frame_453 = QtWidgets.QFrame(self.mainPageAllSongsSongAdderQFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_453.sizePolicy().hasHeightForWidth())
        self.frame_453.setSizePolicy(sizePolicy)
        self.frame_453.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_453.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_453.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_453.setObjectName("frame_453")
        self.verticalLayout_276 = QtWidgets.QVBoxLayout(self.frame_453)
        self.verticalLayout_276.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_276.setSpacing(0)
        self.verticalLayout_276.setObjectName("verticalLayout_276")
        self.mainPageAllSongsSongCategoryQComboBox = StyledQComboBox(self.frame_453)
        self.mainPageAllSongsSongCategoryQComboBox.setMaxVisibleItems(10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAllSongsSongCategoryQComboBox.sizePolicy().hasHeightForWidth())
        self.mainPageAllSongsSongCategoryQComboBox.setSizePolicy(sizePolicy)
        self.mainPageAllSongsSongCategoryQComboBox.setMinimumSize(QtCore.QSize(175, 0))
        self.mainPageAllSongsSongCategoryQComboBox.setObjectName("mainPageAllSongsSongCategoryQComboBox")
        self.mainPageAllSongsSongCategoryQComboBox.addItem("")
        self.mainPageAllSongsSongCategoryQComboBox.setItemText(0, "noCategory")
        self.mainPageAllSongsSongCategoryQComboBox.addItem("")
        self.mainPageAllSongsSongCategoryQComboBox.setItemText(1, "Category1")
        self.mainPageAllSongsSongCategoryQComboBox.addItem("")
        self.mainPageAllSongsSongCategoryQComboBox.setItemText(2, "Category2")
        self.verticalLayout_276.addWidget(self.mainPageAllSongsSongCategoryQComboBox)
        self.horizontalLayout_107.addWidget(self.frame_453)
        self.frame_455 = QtWidgets.QFrame(self.mainPageAllSongsSongAdderQFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_455.sizePolicy().hasHeightForWidth())
        self.frame_455.setSizePolicy(sizePolicy)
        self.frame_455.setMinimumSize(QtCore.QSize(250, 40))
        self.frame_455.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_455.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_455.setObjectName("frame_455")
        self.verticalLayout_278 = QtWidgets.QVBoxLayout(self.frame_455)
        self.verticalLayout_278.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_278.setSpacing(0)
        self.verticalLayout_278.setObjectName("verticalLayout_278")
        self.mainPageAllSongsSongAlbumQComboBox = StyledQComboBox(self.frame_455)
        self.mainPageAllSongsSongAlbumQComboBox.setMaxVisibleItems(10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageAllSongsSongAlbumQComboBox.sizePolicy().hasHeightForWidth())
        self.mainPageAllSongsSongAlbumQComboBox.setSizePolicy(sizePolicy)
        self.mainPageAllSongsSongAlbumQComboBox.setMinimumSize(QtCore.QSize(175, 0))
        self.mainPageAllSongsSongAlbumQComboBox.setObjectName("mainPageAllSongsSongAlbumQComboBox")
        self.mainPageAllSongsSongAlbumQComboBox.addItem("")
        self.mainPageAllSongsSongAlbumQComboBox.setItemText(0, "noAlbum")
        self.mainPageAllSongsSongAlbumQComboBox.addItem("")
        self.mainPageAllSongsSongAlbumQComboBox.setItemText(1, "Album1")
        self.mainPageAllSongsSongAlbumQComboBox.addItem("")
        self.mainPageAllSongsSongAlbumQComboBox.setItemText(2, "Album2")
        self.verticalLayout_278.addWidget(self.mainPageAllSongsSongAlbumQComboBox)
        self.horizontalLayout_107.addWidget(self.frame_455)
