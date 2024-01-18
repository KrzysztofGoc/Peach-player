from PySide2 import QtCore, QtWidgets, QtGui
import random
from PySide2.QtCore import QUrl, QTimer
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from app.src.classes import navbar_frame
from app.src.classes.widgets.sort_buttons_qframe import SortButtonsQFrame
from app_model import *
import requests
import math
from enum import Enum
from functools import partial
from classes.song_entry import SongEntry
from classes.album_entry import AlbumEntry
from classes.category_entry import CategoryEntry
from classes.playlist_entry import PlaylistEntry
from classes.author_entry import AuthorEntry
from classes.adder_entry import AdderEntry
from classes.dialogs.categoryInputDialog import categoryInputDialog
from classes.dialogs.playlistInputDialog import playlistInputDialog
from classes.dialogs.authorInputDialog import authorInputDialog
from classes.dialogs.albumInputDialog import albumInputDialog
from classes.dialogs.synchronizeDialog import synchronizeDialog
from app.src.classes.widgets.helper_widgets.clicked_signal_qframe import ClickedSignalQFrame

from app_model import app as local_database_app

scrollbar_recently_used = False


class PlaylistState(Enum):
    NONE = 0
    SORTED = 1
    SHUFFLED = 2


# TODO Split attributes into logical groups
class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.player = QMediaPlayer()
        self.timer = QTimer()
        self.connect_signals_with_slots()
        self.category_frames = []
        self.loaded_songs = []
        self.loaded_album_page_songs = []
        self.loaded_albums = []
        self.loaded_playlists = []
        self.loaded_selected_author_songs = []
        self.loaded_selected_author_albums = []
        self.loaded_selected_author_playlists = []
        self.loaded_playlist_page_songs = []
        self.now_playing_song = None
        self.user_data = None
        self.get_user_data()
        self.log_in_with_token()
        self.load_playlist_frames()
        self.song_duration = None
        self.current_playing_song_second = None
        self.current_loaded_songs_frames = []
        self.sorted_current_playlist_songs_frames = []
        self.shuffled_current_playlist_songs_frames = []
        self.sorted_playlist_playing_song_index = None
        self.shuffled_playlist_playing_song_index = None
        self.playlist_state = PlaylistState.NONE

    def connect_signals_with_slots(self):
        """Connects Ui's widgets with respective slots"""

        ##########################################################################
        # Now playing page resize events slots
        ##########################################################################
        self.ui.mainPageNowPlaying.resized.connect(self.main_page_now_playing_resize_slot)
        self.ui.mainPageStackedWidget.resized.connect(self.main_page_stacked_widget_resize_slot)

        ##########################################################################
        # Utility buttons slots
        ##########################################################################
        self.ui.nowPlayingButton.clicked.connect(self.now_playing_button_slot)
        self.ui.miniPlayerButton.clicked.connect(self.mini_player_button_slot)
        self.ui.categoriesButton.clicked.connect(self.categories_button_slot)
        self.ui.leftMenuLikedSongsButton.clicked.connect(self.liked_songs_button_slot)
        self.ui.leftMenuLastPlayedButton.clicked.connect(self.last_played_button_slot)
        self.ui.leftMenuAuthorsButton.clicked.connect(self.authors_button_slot)
        self.ui.leftMenuAlbumsButton.clicked.connect(self.albums_button_slot)
        self.ui.bottomPlayerQueueButton.clicked.connect(self.queue_button_slot)
        self.ui.leftMenuAllSongsButton.clicked.connect(self.all_songs_button_slot)

        ##########################################################################
        # Category page utility buttons' slots
        ##########################################################################
        self.ui.mainPageCategorySongsButton.clicked.connect(self.change_widget_category_songs)
        self.ui.mainPageCategoryAlbumsButton.clicked.connect(self.change_widget_category_albums)
        self.ui.mainPageCategoryPlaylistsButton.clicked.connect(self.change_widget_category_playlists)

        ##########################################################################
        # Author page utility buttons' slots
        ##########################################################################
        self.ui.mainPageAuthorSongsButton.clicked.connect(self.change_widget_author_songs)
        self.ui.mainPageAuthorPlaylistsButton.clicked.connect(self.change_widget_author_playlists)
        self.ui.mainPageAuthorAlbumsButton.clicked.connect(self.change_widget_author_albums)

        ##########################################################################
        # Adder buttons slots
        ##########################################################################
        self.ui.mainPageLeftMenuCreatePlaylistQPushButton.clicked.connect(self.create_playlist_button_slot)

        ##########################################################################
        # Slider signals
        ##########################################################################
        self.ui.songTimeSlider.sliderPressed.connect(self.song_time_slider_pressed)
        self.ui.songTimeSlider.sliderReleased.connect(self.song_time_slider_released)
        self.ui.songTimeSlider.valueChanged.connect(self.song_time_slider_value_changed)
        self.ui.volumeSlider.valueChanged.connect(self.volume_slider_value_changed)

        ##########################################################################
        # Authentication backend buttons' slots
        ##########################################################################
        self.ui.centralPageLoginPageLogInButton.clicked.connect(self.log_in_with_credentials)
        self.ui.centralPageLoginPageContinueAsGuestQPushButton.clicked.connect(self.continue_as_guest)
        self.ui.centralPageRegisterPageSignInQPushButton.clicked.connect(self.register)
        self.ui.centralPageRegisterPageButton.clicked.connect(self.load_register_page)
        self.ui.centralPageLoginPageButton.clicked.connect(self.load_login_page)
        self.ui.fixedNavbar.navbarUsernameButton.clicked.connect(self.log_out)

        ##########################################################################
        # Authentication frontend buttons' slots
        ##########################################################################
        self.ui.centralPageLoginPageTogglePasswordQPushButton.clicked.connect(self.toggle_login_page_password_echo_mode)
        self.ui.centralPageRegisterPageTogglePasswordQPushButton.clicked.connect(
            self.toggle_register_page_password_echo_mode)

        ##########################################################################
        # Song adder slots
        ##########################################################################
        self.handle_song_adder_inputs()

        ##########################################################################
        # Sort buttons' slots
        ##########################################################################
        self.ui.mainPageLikedSongsSortButtonsQButtonGroup.buttonClicked.connect(
            self.liked_songs_sort_buttons_qbuttongroup_slot)
        self.ui.mainPagePlaylistSortButtonsQButtonGroup.buttonClicked.connect(
            self.playlist_sort_buttons_qbuttongroup_slot)
        self.ui.mainPageAuthorPageSortButtonsQButtonGroup.buttonClicked.connect(
            self.author_page_sort_buttons_qbuttongroup_slot)
        self.ui.mainPageCategorySortButtonsQButtonGroup.buttonClicked.connect(
            self.category_page_sort_buttons_qbuttongroup_slot)
        self.ui.mainPageAllSongsSortButtonsQButtonGroup.buttonClicked.connect(
            self.all_songs_page_sort_buttons_qbuttongroup_slot)

        ##########################################################################
        # Backend slots
        ##########################################################################
        self.player.stateChanged.connect(self.handle_state_changed)
        self.player.mediaStatusChanged.connect(self.handle_media_status_changed)
        self.ui.playerPausePlayButton.clicked.connect(self.pause_play_button)
        self.ui.bottomPlayerMuteButton.clicked.connect(self.set_muted)
        self.ui.likedSongsPlayPauseButton.clicked.connect(self.start_playlist)
        self.ui.albumPlayPauseButton.clicked.connect(self.start_playlist)
        self.ui.playerPreviousButton.clicked.connect(self.play_previous_playlist_song)
        self.ui.playerNextButton.clicked.connect(self.play_next_playlist_song)
        self.ui.playerShuffleButton.clicked.connect(self.shuffle_now_playing_playlist)
        # self.ui.mainPageCategoriesAlphabeticallySortQPushButton.clicked.connect()
        # self.ui.mainPageCategoriesRecentlyAddedSortQPushButton.clicked.connect()
        # self.ui.mainPageCategoriesMostListenedSortQPushButton.clicked.connect()

        ##########################################################################
        # Scrollbars' slots
        ##########################################################################
        self.ui.mainPageCategoriesScroll.actionTriggered.connect(self.categories_scroll_value_changed_slot)
        self.ui.scrollArea_9.verticalScrollBar().valueChanged.connect(
            self.categories_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_9.verticalScrollBar().rangeChanged.connect(
            self.categories_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_9.resized.connect(self.categories_scroll_area_resize_slot)

        self.ui.mainPageLikedSongsScroll.actionTriggered.connect(self.liked_songs_scroll_value_changed_slot)
        self.ui.scrollArea_4.verticalScrollBar().valueChanged.connect(
            self.liked_songs_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_4.verticalScrollBar().rangeChanged.connect(
            self.liked_songs_scroll_area_scrollbar_range_changed)
        self.ui.scrollArea_4.resized.connect(self.liked_songs_scroll_area_resize_slot)

        self.ui.mainPageLastPlayedScroll.actionTriggered.connect(self.last_played_scroll_value_changed_slot)
        self.ui.scrollArea_10.verticalScrollBar().valueChanged.connect(
            self.last_played_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_10.verticalScrollBar().rangeChanged.connect(
            self.last_played_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_10.resized.connect(self.last_played_scroll_area_resize_slot)

        self.ui.mainPagePlaylistScroll.actionTriggered.connect(self.playlist_scroll_value_changed_slot)
        self.ui.scrollArea_3.verticalScrollBar().valueChanged.connect(
            self.playlist_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_3.verticalScrollBar().rangeChanged.connect(
            self.playlist_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_3.resized.connect(self.playlist_scroll_area_resize_slot)

        self.ui.mainPageAuthorPageScroll.actionTriggered.connect(self.author_page_scroll_value_changed_slot)
        self.ui.scrollArea_8.verticalScrollBar().valueChanged.connect(
            self.author_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_8.verticalScrollBar().rangeChanged.connect(
            self.author_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_8.resized.connect(self.author_page_scroll_area_resize_slot)

        self.ui.mainPageAuthorsScroll.actionTriggered.connect(self.authors_scroll_value_changed_slot)
        self.ui.scrollArea_7.verticalScrollBar().valueChanged.connect(
            self.authors_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_7.verticalScrollBar().rangeChanged.connect(
            self.authors_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_7.resized.connect(self.authors_scroll_area_resize_slot)

        self.ui.mainPageCategoryPageScroll.actionTriggered.connect(self.category_page_scroll_value_changed_slot)
        self.ui.scrollArea_11.verticalScrollBar().valueChanged.connect(
            self.category_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_11.verticalScrollBar().rangeChanged.connect(
            self.category_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_11.resized.connect(self.category_page_scroll_area_resize_slot)

        self.ui.mainPageAlbumPageScroll.actionTriggered.connect(self.album_page_scroll_value_changed_slot)
        self.ui.scrollArea_5.verticalScrollBar().valueChanged.connect(
            self.album_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_5.verticalScrollBar().rangeChanged.connect(
            self.album_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_5.resized.connect(self.album_page_scroll_area_resize_slot)

        self.ui.mainPageSongQueuePageScroll.actionTriggered.connect(self.song_queue_page_scroll_value_changed_slot)
        self.ui.scrollArea_12.verticalScrollBar().valueChanged.connect(
            self.song_queue_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_12.verticalScrollBar().rangeChanged.connect(
            self.song_queue_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_12.resized.connect(self.song_queue_page_scroll_area_resize_slot)

        self.ui.mainPageAlbumsPageScroll.actionTriggered.connect(self.albums_page_scroll_value_changed_slot)
        self.ui.scrollArea_13.verticalScrollBar().valueChanged.connect(
            self.albums_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_13.verticalScrollBar().rangeChanged.connect(
            self.albums_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_13.resized.connect(self.albums_page_scroll_area_resize_slot)

        self.ui.mainPageAllSongsPageScroll.actionTriggered.connect(self.all_songs_page_scroll_value_changed_slot)
        self.ui.scrollArea_14.verticalScrollBar().valueChanged.connect(
            self.all_songs_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_14.verticalScrollBar().rangeChanged.connect(
            self.all_songs_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_14.resized.connect(self.all_songs_page_scroll_area_resize_slot)

        ##########################################################################
        # Navbar's slots
        ##########################################################################
        self.ui.fixedNavbar.navbarSynchronizeButton.clicked.connect(self.synchronize_button_clicked_slot)

    def all_songs_page_scroll_area_resize_slot(self):
        """Resize and move custom scrollbar on all songs' page.

         Calls all_songs_page_scroll_area_scrollbar_range_changed_slot() to toggle custom's scrollbar visibility if needed.
         """
        self.ui.mainPageAllSongsPageScroll.move(self.ui.scrollArea_14.rect().right() - 13, 0)
        self.ui.mainPageAllSongsPageScroll.setFixedSize(self.ui.mainPageAllSongsPageScroll.width(),
                                                        self.ui.scrollArea_14.height())
        self.all_songs_page_scroll_area_scrollbar_range_changed_slot()

    def all_songs_page_scroll_area_scrollbar_range_changed_slot(self):
        """Change visibility of albums' page custom scrollbar when needed, set its maximum and pageStep to suit
         scrollArea's scrollbar.
        """
        if self.ui.scrollArea_14.verticalScrollBar().maximum() > 0:
            self.ui.mainPageAllSongsPageScroll.setVisible(True)
            self.ui.mainPageAllSongsPageScroll.setPageStep(self.ui.scrollArea_14.verticalScrollBar().pageStep())
            self.ui.mainPageAllSongsPageScroll.setMaximum(self.ui.scrollArea_14.verticalScrollBar().maximum())
        else:
            self.ui.mainPageAllSongsPageScroll.setVisible(False)

    def all_songs_page_scroll_area_scrollbar_value_changed_slot(self):
        """Change albums' page custom scrollbar's value to match albums' page scrollArea's scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageAllSongsPageScroll.setValue(self.ui.scrollArea_14.verticalScrollBar().value())
            self.ui.mainPageAllSongsPageScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def all_songs_page_scroll_value_changed_slot(self):
        """Change all songs' page scrollArea's scrollbar's value to match all songs' page custom scrollbar's value.

           Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.

           Adjust fixedNavbar's saturation, navbarPlayButton/navbarPageName visibility and stickySortButtonsFrame
           sort buttons visibility.
        """

        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.label_258.mapTo(self.ui.scrollArea_14, QtCore.QPoint(0, -60)).y(), 215)

        self.ui.fixedNavbar.adjust_elements_visibility(
            self.ui.label_251.mapTo(self.ui.scrollArea_14, QtCore.QPoint(0, -34)).y())

        self.ui.fixedNavbar.adjust_sticky_sort_button_frame_visibility(
            self.ui.allSongsSortButtonsQFrame.mapTo(self.ui.scrollArea_14, QtCore.QPoint(0, -60)).y())

        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_14.verticalScrollBar().setValue(self.ui.mainPageAllSongsPageScroll.value())
            scrollbar_recently_used = False

    def albums_page_scroll_area_resize_slot(self):
        """Resize and move custom scrollbar on albums' page.

         Calls albums_page_scroll_area_scrollbar_range_changed_slot() to toggle custom's scrollbar visibility if needed.
         """
        self.ui.mainPageAlbumsPageScroll.move(self.ui.scrollArea_13.rect().right() - 13, 0)
        self.ui.mainPageAlbumsPageScroll.setFixedSize(self.ui.mainPageAlbumsPageScroll.width(),
                                                      self.ui.scrollArea_13.height())
        self.albums_page_scroll_area_scrollbar_range_changed_slot()

    def albums_page_scroll_area_scrollbar_range_changed_slot(self):
        """Change visibility of albums' page custom scrollbar when needed, set its maximum and pageStep to suit
         scrollArea's scrollbar.
        """
        if self.ui.scrollArea_13.verticalScrollBar().maximum() > 0:
            self.ui.mainPageAlbumsPageScroll.setVisible(True)
            self.ui.mainPageAlbumsPageScroll.setPageStep(self.ui.scrollArea_13.verticalScrollBar().pageStep())
            self.ui.mainPageAlbumsPageScroll.setMaximum(self.ui.scrollArea_13.verticalScrollBar().maximum())
        else:
            self.ui.mainPageAlbumsPageScroll.setVisible(False)

    def albums_page_scroll_area_scrollbar_value_changed_slot(self):
        """Change albums' page custom scrollbar's value to match albums' page scrollArea's scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageAlbumsPageScroll.setValue(self.ui.scrollArea_13.verticalScrollBar().value())
            self.ui.mainPageAlbumsPageScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def albums_page_scroll_value_changed_slot(self):
        """Change albums' page scrollArea's scrollbar's value to match albums' page custom scrollbar's value.

           Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.

           Adjust fixedNavbar's saturation."""

        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.label_146.mapTo(self.ui.scrollArea_13, QtCore.QPoint(0, -34)).y(), 56)

        self.ui.fixedNavbar.adjust_elements_visibility(
            self.ui.label_146.mapTo(self.ui.scrollArea_13, QtCore.QPoint(0, -34)).y(), play_button=False)

        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_13.verticalScrollBar().setValue(self.ui.mainPageAlbumsPageScroll.value())
            scrollbar_recently_used = False

    def song_queue_page_scroll_area_resize_slot(self):
        """Resize and move custom scrollbar on songQueue page.

         Calls song_queue_page_scroll_area_scrollbar_range_changed_slot to toggle custom's scrollbar visibility if needed.
         """
        self.ui.mainPageSongQueuePageScroll.move(self.ui.scrollArea_12.rect().right() - 13, 0)
        self.ui.mainPageSongQueuePageScroll.setFixedSize(self.ui.mainPageSongQueuePageScroll.width(),
                                                         self.ui.scrollArea_12.height())
        self.song_queue_page_scroll_area_scrollbar_range_changed_slot()

    def song_queue_page_scroll_area_scrollbar_range_changed_slot(self):
        """Change visibility of songQueue's page custom scrollbar when needed, set its maximum and pageStep to suit
        scrollArea's scrollbar.
        """
        if self.ui.scrollArea_12.verticalScrollBar().maximum() > 0:
            self.ui.mainPageSongQueuePageScroll.setVisible(True)
            self.ui.mainPageSongQueuePageScroll.setPageStep(self.ui.scrollArea_12.verticalScrollBar().pageStep())
            self.ui.mainPageSongQueuePageScroll.setMaximum(self.ui.scrollArea_12.verticalScrollBar().maximum())
        else:
            self.ui.mainPageSongQueuePageScroll.setVisible(False)

    def song_queue_page_scroll_area_scrollbar_value_changed_slot(self):
        """Change songQueue's page custom scrollbar's value to match songQueue's page scrollArea's scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageSongQueuePageScroll.setValue(self.ui.scrollArea_12.verticalScrollBar().value())
            self.ui.mainPageSongQueuePageScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def song_queue_page_scroll_value_changed_slot(self):
        """Change songQueue's page scrollArea's scrollbar's value to match songQueue's page custom scrollbar's value.

           Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.

           Adjust fixedNavbar's saturation.
        """

        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.label_201.mapTo(self.ui.scrollArea_12, QtCore.QPoint(0, -34)).y(), 65)

        self.ui.fixedNavbar.adjust_elements_visibility(
            self.ui.label_201.mapTo(self.ui.scrollArea_12, QtCore.QPoint(0, -34)).y(), play_button=False)

        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_12.verticalScrollBar().setValue(self.ui.mainPageSongQueuePageScroll.value())
            scrollbar_recently_used = False

    def album_page_scroll_area_resize_slot(self):
        """Resize and move custom scrollbar on album's page.

        Calls album_page_scroll_area_scrollbar_range_changed_slot() to toggle custom's scrollbar visibility if needed.
        """
        self.ui.mainPageAlbumPageScroll.move(self.ui.scrollArea_5.rect().right() - 13, 0)
        self.ui.mainPageAlbumPageScroll.setFixedSize(self.ui.mainPageAlbumPageScroll.width(),
                                                     self.ui.scrollArea_5.height())
        self.album_page_scroll_area_scrollbar_range_changed_slot()

    def album_page_scroll_area_scrollbar_range_changed_slot(self):
        """Change visibility of album's page custom scrollbar when needed, set its maximum and pageStep to suit
        scrollArea's scrollbar.
        """
        if self.ui.scrollArea_5.verticalScrollBar().maximum() > 0:
            self.ui.mainPageAlbumPageScroll.setVisible(True)
            self.ui.mainPageAlbumPageScroll.setPageStep(self.ui.scrollArea_5.verticalScrollBar().pageStep())
            self.ui.mainPageAlbumPageScroll.setMaximum(self.ui.scrollArea_5.verticalScrollBar().maximum())
        else:
            self.ui.mainPageAlbumPageScroll.setVisible(False)

    def album_page_scroll_area_scrollbar_value_changed_slot(self):
        """Change album's page custom scrollbar's value to match album's page scrollArea's scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageAlbumPageScroll.setValue(self.ui.scrollArea_5.verticalScrollBar().value())
            self.ui.mainPageAlbumPageScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def album_page_scroll_value_changed_slot(self):
        """Change album's page scrollArea's scrollbar's value to match album's page custom scrollbar's value.

           Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.

           Adjust fixedNavbar's saturation, navbarPlayButton/navbarPageName visibility and stickySortButtonsFrame
           sort buttons visibility.
        """
        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.frame_261.mapTo(self.ui.scrollArea_5, QtCore.QPoint(0, -60)).y(), 80)

        self.ui.fixedNavbar.adjust_elements_visibility(
            self.ui.albumPlayPauseButton.mapTo(self.ui.scrollArea_5, QtCore.QPoint(0, -32)).y())

        self.ui.fixedNavbar.adjust_sticky_sort_button_frame_visibility(
            self.ui.AlbumSortButtonsQFrame.mapTo(self.ui.scrollArea_5, QtCore.QPoint(0, -60)).y())

        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_5.verticalScrollBar().setValue(self.ui.mainPageAlbumPageScroll.value())
            scrollbar_recently_used = False

    def category_page_scroll_area_resize_slot(self):
        """Resize and move custom scrollbar on category's page.

        Calls category_page_scroll_area_scrollbar_range_changed_slot() to toggle custom's scrollbar visibility if needed.
        """
        self.ui.mainPageCategoryPageScroll.move(self.ui.scrollArea_11.rect().right() - 13, 0)
        self.ui.mainPageCategoryPageScroll.setFixedSize(self.ui.mainPageCategoryPageScroll.width(),
                                                        self.ui.scrollArea_11.height())
        self.category_page_scroll_area_scrollbar_range_changed_slot()

    def category_page_scroll_area_scrollbar_range_changed_slot(self):
        """Change visibility of category's page custom scrollbar when needed, set its maximum and pageStep to suit
        scrollArea's scrollbar.
        """
        if self.ui.scrollArea_11.verticalScrollBar().maximum() > 0:
            self.ui.mainPageCategoryPageScroll.setVisible(True)
            self.ui.mainPageCategoryPageScroll.setPageStep(self.ui.scrollArea_11.verticalScrollBar().pageStep())
            self.ui.mainPageCategoryPageScroll.setMaximum(self.ui.scrollArea_11.verticalScrollBar().maximum())
        else:
            self.ui.mainPageCategoryPageScroll.setVisible(False)

    def category_page_scroll_area_scrollbar_value_changed_slot(self):
        """Change category's page custom scrollbar's value to match category's page scrollArea's scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageCategoryPageScroll.setValue(self.ui.scrollArea_11.verticalScrollBar().value())
            self.ui.mainPageCategoryPageScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def category_page_scroll_value_changed_slot(self):
        """Change category's page scrollArea's scrollbar's value to match category's page custom scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """

        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.mainPageCategoryPageStackedWidget.mapTo(self.ui.scrollArea_11, QtCore.QPoint(0, -60)).y(), 80)

        if self.ui.mainPageCategoryPageStackedWidget.currentIndex() == 0:
            self.ui.fixedNavbar.adjust_sticky_sort_button_frame_visibility(
                self.ui.CategorySortButtonsQFrame.mapTo(self.ui.scrollArea_11, QtCore.QPoint(0, -60)).y())

            self.ui.fixedNavbar.adjust_elements_visibility(
                self.ui.categoryPagePlayPauseQPushButton.mapTo(self.ui.scrollArea_11, QtCore.QPoint(0, -32)).y())
        elif self.ui.mainPageCategoryPageStackedWidget.currentIndex() == 1:
            self.ui.fixedNavbar.adjust_elements_visibility(
                self.ui.mainPageCategoryPageAlbumsCategoryNameLabel.mapTo(self.ui.scrollArea_11,
                                                                          QtCore.QPoint(0, -34)).y(), play_button=False)
        elif self.ui.mainPageCategoryPageStackedWidget.currentIndex() == 2:
            self.ui.fixedNavbar.adjust_elements_visibility(
                self.ui.mainPageCategoryPagePlaylistsCategoryNameLabel.mapTo(self.ui.scrollArea_11,
                                                                             QtCore.QPoint(0, -34)).y(),
                play_button=False)

        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_11.verticalScrollBar().setValue(self.ui.mainPageCategoryPageScroll.value())
            scrollbar_recently_used = False

    def author_page_scroll_area_resize_slot(self):
        """Resize and move custom scrollbar on author's page.

        Calls author_page_scroll_area_scrollbar_range_changed_slot() to toggle custom's scrollbar visibility if needed.
        """
        self.ui.mainPageAuthorPageScroll.move(self.ui.scrollArea_8.rect().right() - 13, 0)
        self.ui.mainPageAuthorPageScroll.setFixedSize(self.ui.mainPageAuthorPageScroll.width(),
                                                      self.ui.scrollArea_8.height())
        self.author_page_scroll_area_scrollbar_range_changed_slot()

    def author_page_scroll_area_scrollbar_range_changed_slot(self):
        """Change visibility of author's page custom scrollbar when needed, set its maximum and pageStep to suit
        scrollArea's scrollbar.
        """
        if self.ui.scrollArea_8.verticalScrollBar().maximum() > 0:
            self.ui.mainPageAuthorPageScroll.setVisible(True)
            self.ui.mainPageAuthorPageScroll.setPageStep(self.ui.scrollArea_8.verticalScrollBar().pageStep())
            self.ui.mainPageAuthorPageScroll.setMaximum(self.ui.scrollArea_8.verticalScrollBar().maximum())
        else:
            self.ui.mainPageAuthorPageScroll.setVisible(False)

    def author_page_scroll_area_scrollbar_value_changed_slot(self):
        """Change author's page custom scrollbar's value to match author's page scrollArea's scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageAuthorPageScroll.setValue(self.ui.scrollArea_8.verticalScrollBar().value())
            self.ui.mainPageAuthorPageScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def author_page_scroll_value_changed_slot(self):
        """Change author's page scrollArea's scrollbar's value to match author's page custom scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.frame_352.mapTo(self.ui.scrollArea_8, QtCore.QPoint(0, -60)).y(), 80)

        if self.ui.mainPageAuthorPageStackedWidget.currentIndex() == 0:
            self.ui.fixedNavbar.adjust_sticky_sort_button_frame_visibility(
                self.ui.AuthorSortButtonsQFrame.mapTo(self.ui.scrollArea_8, QtCore.QPoint(0, -60)).y())

            self.ui.fixedNavbar.adjust_elements_visibility(
                self.ui.authorPagePlayPauseQPushButton.mapTo(self.ui.scrollArea_8, QtCore.QPoint(0, -32)).y())
        elif self.ui.mainPageAuthorPageStackedWidget.currentIndex() == 1:
            self.ui.fixedNavbar.adjust_elements_visibility(
                self.ui.mainPageAuthorPageAlbumsAuthorNameLabel.mapTo(self.ui.scrollArea_8,
                                                                      QtCore.QPoint(0, -34)).y(), play_button=False)
        elif self.ui.mainPageAuthorPageStackedWidget.currentIndex() == 2:
            self.ui.fixedNavbar.adjust_elements_visibility(
                self.ui.mainPageAuthorPagePlaylistsAuthorNameLabel.mapTo(self.ui.scrollArea_8,
                                                                         QtCore.QPoint(0, -34)).y(), play_button=False)
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_8.verticalScrollBar().setValue(self.ui.mainPageAuthorPageScroll.value())
            scrollbar_recently_used = False

    def playlist_scroll_area_resize_slot(self):
        self.ui.mainPagePlaylistScroll.move(self.ui.scrollArea_3.rect().right() - 13, 0)
        self.ui.mainPagePlaylistScroll.setFixedSize(self.ui.mainPagePlaylistScroll.width(),
                                                    self.ui.scrollArea_3.height())
        self.playlist_scroll_area_scrollbar_range_changed_slot()

    def playlist_scroll_area_scrollbar_range_changed_slot(self):
        if self.ui.scrollArea_3.verticalScrollBar().maximum() > 0:
            self.ui.mainPagePlaylistScroll.setVisible(True)
            self.ui.mainPagePlaylistScroll.setPageStep(self.ui.scrollArea_3.verticalScrollBar().pageStep())
            self.ui.mainPagePlaylistScroll.setMaximum(self.ui.scrollArea_3.verticalScrollBar().maximum())
        else:
            self.ui.mainPagePlaylistScroll.setVisible(False)

    def playlist_scroll_area_scrollbar_value_changed_slot(self):
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPagePlaylistScroll.setValue(self.ui.scrollArea_3.verticalScrollBar().value())
            self.ui.mainPagePlaylistScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def playlist_scroll_value_changed_slot(self):
        """Change playlist's page scrollArea's scrollbar's value to match playlist's page custom scrollbar's value.

           Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.

           Adjust fixedNavbar's saturation, navbarPlayButton/navbarPageName visibility and stickySortButtonsFrame
           sort buttons visibility.
        """

        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.frame_17.mapTo(self.ui.scrollArea_3, QtCore.QPoint(0, -60)).y(), 80)

        self.ui.fixedNavbar.adjust_elements_visibility(
            self.ui.playlistPlayPauseButton.mapTo(self.ui.scrollArea_3, QtCore.QPoint(0, -32)).y())

        self.ui.fixedNavbar.adjust_sticky_sort_button_frame_visibility(
            self.ui.PlaylistSortButtonsQFrame.mapTo(self.ui.scrollArea_3, QtCore.QPoint(0, -60)).y())

        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_3.verticalScrollBar().setValue(self.ui.mainPagePlaylistScroll.value())
            scrollbar_recently_used = False

    def authors_scroll_area_resize_slot(self):
        self.ui.mainPageAuthorsScroll.move(self.ui.scrollArea_7.rect().right() - 13, 0)
        self.ui.mainPageAuthorsScroll.setFixedSize(self.ui.mainPageAuthorsScroll.width(), self.ui.scrollArea_7.height())
        self.authors_scroll_area_scrollbar_range_changed_slot()

    def authors_scroll_area_scrollbar_range_changed_slot(self):
        if self.ui.scrollArea_7.verticalScrollBar().maximum() > 0:
            self.ui.mainPageAuthorsScroll.setVisible(True)
            self.ui.mainPageAuthorsScroll.setPageStep(self.ui.scrollArea_7.verticalScrollBar().pageStep())
            self.ui.mainPageAuthorsScroll.setMaximum(self.ui.scrollArea_7.verticalScrollBar().maximum())
        else:
            self.ui.mainPageAuthorsScroll.setVisible(False)

    def authors_scroll_area_scrollbar_value_changed_slot(self):
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageAuthorsScroll.setValue(self.ui.scrollArea_7.verticalScrollBar().value())
            self.ui.mainPageAuthorsScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def authors_scroll_value_changed_slot(self):
        """Change authors' page scrollArea's scrollbar's value to match authors' page custom scrollbar's value.

           Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.

           Adjust fixedNavbar's saturation and navbarPlayButton/navbarPageName visibility.
        """

        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.label_114.mapTo(self.ui.scrollArea_7, QtCore.QPoint(0, -34)).y(), 22)

        self.ui.fixedNavbar.adjust_elements_visibility(
            self.ui.label_114.mapTo(self.ui.scrollArea_7, QtCore.QPoint(0, -34)).y(), play_button=False)

        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_7.verticalScrollBar().setValue(self.ui.mainPageAuthorsScroll.value())
            scrollbar_recently_used = False

    def last_played_scroll_area_resize_slot(self):
        self.ui.mainPageLastPlayedScroll.move(self.ui.scrollArea_10.rect().right() - 13, 0)
        self.ui.mainPageLastPlayedScroll.setFixedSize(self.ui.mainPageLastPlayedScroll.width(),
                                                      self.ui.scrollArea_10.height())
        self.last_played_scroll_area_scrollbar_range_changed_slot()

    def last_played_scroll_area_scrollbar_range_changed_slot(self):
        if self.ui.scrollArea_10.verticalScrollBar().maximum() > 0:
            self.ui.mainPageLastPlayedScroll.setVisible(True)
            self.ui.mainPageLastPlayedScroll.setPageStep(self.ui.scrollArea_10.verticalScrollBar().pageStep())
            self.ui.mainPageLastPlayedScroll.setMaximum(self.ui.scrollArea_10.verticalScrollBar().maximum())
        else:
            self.ui.mainPageLastPlayedScroll.setVisible(False)

    def last_played_scroll_area_scrollbar_value_changed_slot(self):
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageLastPlayedScroll.setValue(self.ui.scrollArea_10.verticalScrollBar().value())
            self.ui.mainPageLastPlayedScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def last_played_scroll_value_changed_slot(self):
        """Change last played's page scrollArea's scrollbar's value to match last played's page custom scrollbar's value.

           Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.

           Adjust fixedNavbar's saturation, navbarPlayButton/navbarPageName visibility and stickySortButtonsFrame
           sort buttons visibility.
        """

        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.mainPageLastPlayedHeaderQLabel.mapTo(self.ui.scrollArea_10, QtCore.QPoint(0, -33)).y(), 70)

        self.ui.fixedNavbar.adjust_elements_visibility(
            self.ui.mainPageLastPlayedHeaderQLabel.mapTo(self.ui.scrollArea_10, QtCore.QPoint(0, -33)).y(),
            play_button=False)

        self.ui.fixedNavbar.adjust_sticky_sort_button_frame_visibility(
            self.ui.LastPlayedSortButtonsQFrame.mapTo(self.ui.scrollArea_10, QtCore.QPoint(0, -60)).y())

        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_10.verticalScrollBar().setValue(self.ui.mainPageLastPlayedScroll.value())
            scrollbar_recently_used = False

    def liked_songs_scroll_area_resize_slot(self):
        self.ui.mainPageLikedSongsScroll.move(self.ui.scrollArea_4.rect().right() - 13, 0)
        self.ui.mainPageLikedSongsScroll.setFixedSize(self.ui.mainPageLikedSongsScroll.width(),
                                                      self.ui.scrollArea_4.height())
        self.liked_songs_scroll_area_scrollbar_range_changed()

    def liked_songs_scroll_area_scrollbar_range_changed(self):
        if self.ui.scrollArea_4.verticalScrollBar().maximum() > 0:
            self.ui.mainPageLikedSongsScroll.setVisible(True)
            self.ui.mainPageLikedSongsScroll.setPageStep(self.ui.scrollArea_4.verticalScrollBar().pageStep())
            self.ui.mainPageLikedSongsScroll.setMaximum(self.ui.scrollArea_4.verticalScrollBar().maximum())
        else:
            self.ui.mainPageLikedSongsScroll.setVisible(False)

    def liked_songs_scroll_area_scrollbar_value_changed_slot(self):
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageLikedSongsScroll.setValue(self.ui.scrollArea_4.verticalScrollBar().value())
            self.ui.mainPageLikedSongsScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def liked_songs_scroll_value_changed_slot(self):
        """Change liked songs' page scrollArea's scrollbar's value to match liked songs' page custom scrollbar's value.

           Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.

           Adjust fixedNavbar's saturation, navbarPlayButton/navbarPageName visibility and stickySortButtonsFrame
           sort buttons visibility."""
        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.frame_22.mapTo(self.ui.scrollArea_4, QtCore.QPoint(0, -60)).y(), 80)

        self.ui.fixedNavbar.adjust_elements_visibility(
            self.ui.likedSongsPlayPauseButton.mapTo(self.ui.scrollArea_4, QtCore.QPoint(0, -32)).y())

        self.ui.fixedNavbar.adjust_sticky_sort_button_frame_visibility(
            self.ui.LikedSongsSortButtonsQFrame.mapTo(self.ui.scrollArea_4, QtCore.QPoint(0, -60)).y())

        # Uses global variable scrollbar_recently_used to prevent from going into a loop
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_4.verticalScrollBar().setValue(self.ui.mainPageLikedSongsScroll.value())

            scrollbar_recently_used = False

    def categories_scroll_area_resize_slot(self):
        self.ui.mainPageCategoriesScroll.move(self.ui.scrollArea_9.rect().right() - 13, 0)
        self.ui.mainPageCategoriesScroll.setFixedSize(self.ui.mainPageCategoriesScroll.width(),
                                                      self.ui.scrollArea_9.height())
        self.categories_scroll_area_scrollbar_range_changed_slot()

    def categories_scroll_area_scrollbar_range_changed_slot(self):
        if self.ui.scrollArea_9.verticalScrollBar().maximum() > 0:
            self.ui.mainPageCategoriesScroll.setVisible(True)
            self.ui.mainPageCategoriesScroll.setPageStep(self.ui.scrollArea_9.verticalScrollBar().pageStep())
            self.ui.mainPageCategoriesScroll.setMaximum(self.ui.scrollArea_9.verticalScrollBar().maximum())
        else:
            self.ui.mainPageCategoriesScroll.setVisible(False)

    def categories_scroll_area_scrollbar_value_changed_slot(self):
        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.mainPageCategoriesScroll.setValue(self.ui.scrollArea_9.verticalScrollBar().value())
            self.ui.mainPageCategoriesScroll.triggerAction(QtWidgets.QAbstractSlider.SliderMove)
            scrollbar_recently_used = False

    def categories_scroll_value_changed_slot(self):
        """Change all songs' page scrollArea's scrollbar's value to match all songs' page custom scrollbar's value.

           Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.

           Adjust fixedNavbar's saturation and navbarPlayButton/navbarPageName.
        """

        self.ui.fixedNavbar.adjust_navbar_saturation(
            self.ui.label_115.mapTo(self.ui.scrollArea_9, QtCore.QPoint(0, -34)).y(), 45)

        self.ui.fixedNavbar.adjust_elements_visibility(
            self.ui.label_115.mapTo(self.ui.scrollArea_9, QtCore.QPoint(0, -34)).y())

        global scrollbar_recently_used
        if not scrollbar_recently_used:
            scrollbar_recently_used = True
            self.ui.scrollArea_9.verticalScrollBar().setValue(self.ui.mainPageCategoriesScroll.value())
            scrollbar_recently_used = False

    def liked_songs_sort_buttons_qbuttongroup_slot(self):
        self.liked_songs_title_sort_button_slot()
        self.liked_songs_artist_sort_button_slot()
        self.liked_songs_category_sort_button_slot()
        self.liked_songs_added_sort_button_slot()
        self.liked_songs_length_sort_button_slot()

    def playlist_sort_buttons_qbuttongroup_slot(self):
        self.playlist_title_sort_button_slot()
        self.playlist_artist_sort_button_slot()
        self.playlist_category_sort_button_slot()
        self.playlist_added_sort_button_slot()
        self.playlist_length_sort_button_slot()

    def author_page_sort_buttons_qbuttongroup_slot(self):
        self.author_page_title_sort_button_slot()
        self.author_page_category_sort_button_slot()
        self.author_page_added_sort_button_slot()
        self.author_page_length_sort_button_slot()

    def category_page_sort_buttons_qbuttongroup_slot(self):
        self.category_title_sort_button_slot()
        self.category_artist_sort_button_slot()
        self.category_added_sort_button_slot()
        self.category_length_sort_button_slot()

    def all_songs_page_sort_buttons_qbuttongroup_slot(self):
        self.all_songs_title_sort_button_slot()
        self.all_songs_artist_sort_button_slot()
        self.all_songs_category_sort_button_slot()
        self.all_songs_added_sort_button_slot()
        self.all_songs_length_sort_button_slot()

    def all_songs_title_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageAllSongsTitleSortQPushButton.isChecked():
            if self.ui.mainPageAllSongsTitleSortQPushButton.wasChecked:
                self.ui.mainPageAllSongsTitleSortQPushButton.wasChecked = False
                self.ui.label_275.setVisible(False)
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageAllSongsTitleSortQPushButton.toggle()
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageAllSongsTitleSortQPushButton.wasChecked = True
                self.ui.label_275.setVisible(True)
                self.sort_songs_by_title()
        else:
            self.ui.mainPageAllSongsTitleSortQPushButton.wasChecked = False
            self.ui.label_275.setVisible(False)

    def all_songs_artist_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageAllSongsArtistSortQPushButton.isChecked():
            if self.ui.mainPageAllSongsArtistSortQPushButton.wasChecked:
                self.ui.mainPageAllSongsArtistSortQPushButton.wasChecked = False
                self.ui.label_276.setVisible(False)
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageAllSongsArtistSortQPushButton.toggle()
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageAllSongsArtistSortQPushButton.wasChecked = True
                self.ui.label_276.setVisible(True)
                self.sort_songs_by_artist()
        else:
            self.ui.mainPageAllSongsArtistSortQPushButton.wasChecked = False
            self.ui.label_276.setVisible(False)

    def all_songs_category_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageAllSongsCategorySortQPushButton.isChecked():
            if self.ui.mainPageAllSongsCategorySortQPushButton.wasChecked:
                self.ui.mainPageAllSongsCategorySortQPushButton.wasChecked = False
                self.ui.label_277.setVisible(False)
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageAllSongsCategorySortQPushButton.toggle()
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageAllSongsCategorySortQPushButton.wasChecked = True
                self.ui.label_277.setVisible(True)
                self.sort_songs_by_category()
        else:
            self.ui.mainPageAllSongsCategorySortQPushButton.wasChecked = False
            self.ui.label_277.setVisible(False)

    def all_songs_added_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageAllSongsAddedSortQPushButton.isChecked():
            if self.ui.mainPageAllSongsAddedSortQPushButton.wasChecked:
                self.ui.mainPageAllSongsAddedSortQPushButton.wasChecked = False
                self.ui.label_278.setVisible(False)
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageAllSongsAddedSortQPushButton.toggle()
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageAllSongsAddedSortQPushButton.wasChecked = True
                self.ui.label_278.setVisible(True)
                self.sort_songs_by_added()
        else:
            self.ui.mainPageAllSongsAddedSortQPushButton.wasChecked = False
            self.ui.label_278.setVisible(False)

    def all_songs_length_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageAllSongsLengthSortQPushButton.isChecked():
            if self.ui.mainPageAllSongsLengthSortQPushButton.wasChecked:
                self.ui.mainPageAllSongsLengthSortQPushButton.wasChecked = False
                self.ui.label_279.setVisible(False)
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageAllSongsLengthSortQPushButton.toggle()
                self.ui.mainPageAllSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageAllSongsLengthSortQPushButton.wasChecked = True
                self.ui.label_279.setVisible(True)
                self.sort_songs_by_length()
        else:
            self.ui.mainPageAllSongsLengthSortQPushButton.wasChecked = False
            self.ui.label_279.setVisible(False)

    def category_length_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageCategoryLengthSortButton.isChecked():
            if self.ui.mainPageCategoryLengthSortButton.wasChecked:
                self.ui.mainPageCategoryLengthSortButton.wasChecked = False
                self.ui.label_231.setVisible(False)
                self.ui.mainPageCategorySortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageCategoryLengthSortButton.toggle()
                self.ui.mainPageCategorySortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageCategoryLengthSortButton.wasChecked = True
                self.ui.label_231.setVisible(True)
                self.sort_songs_by_length()
        else:
            self.ui.mainPageCategoryLengthSortButton.wasChecked = False
            self.ui.label_231.setVisible(False)

    def category_added_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageCategoryAddedSortButton.isChecked():
            if self.ui.mainPageCategoryAddedSortButton.wasChecked:
                self.ui.mainPageCategoryAddedSortButton.wasChecked = False
                self.ui.label_230.setVisible(False)
                self.ui.mainPageCategorySortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageCategoryAddedSortButton.toggle()
                self.ui.mainPageCategorySortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageCategoryAddedSortButton.wasChecked = True
                self.ui.label_230.setVisible(True)
                self.sort_songs_by_added()
        else:
            self.ui.mainPageCategoryAddedSortButton.wasChecked = False
            self.ui.label_230.setVisible(False)

    def category_artist_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageCategoryArtistSortButton.isChecked():
            if self.ui.mainPageCategoryArtistSortButton.wasChecked:
                self.ui.mainPageCategoryArtistSortButton.wasChecked = False
                self.ui.label_229.setVisible(False)
                self.ui.mainPageCategorySortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageCategoryArtistSortButton.toggle()
                self.ui.mainPageCategorySortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageCategoryArtistSortButton.wasChecked = True
                self.ui.label_229.setVisible(True)
                self.sort_songs_by_artist()
        else:
            self.ui.mainPageCategoryArtistSortButton.wasChecked = False
            self.ui.label_229.setVisible(False)

    def category_title_sort_button_slot(self):
        """Toggle likedSong's page title sort button's indicator and sort the songs"""
        if self.ui.mainPageCategoryTitleSortButton.isChecked():
            if self.ui.mainPageCategoryTitleSortButton.wasChecked:
                self.ui.mainPageCategoryTitleSortButton.wasChecked = False
                self.ui.label_228.setVisible(False)
                self.ui.mainPageCategorySortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageCategoryTitleSortButton.toggle()
                self.ui.mainPageCategorySortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageCategoryTitleSortButton.wasChecked = True
                self.ui.label_228.setVisible(True)
                self.sort_songs_by_title()
        else:
            self.ui.mainPageCategoryTitleSortButton.wasChecked = False
            self.ui.label_228.setVisible(False)

    def author_page_length_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageAuthorPageLengthSortButton.isChecked():
            if self.ui.mainPageAuthorPageLengthSortButton.wasChecked:
                self.ui.mainPageAuthorPageLengthSortButton.wasChecked = False
                self.ui.label_227.setVisible(False)
                self.ui.mainPageAuthorPageSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageAuthorPageLengthSortButton.toggle()
                self.ui.mainPageAuthorPageSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageAuthorPageLengthSortButton.wasChecked = True
                self.ui.label_227.setVisible(True)
                self.sort_songs_by_length()
        else:
            self.ui.mainPageAuthorPageLengthSortButton.wasChecked = False
            self.ui.label_227.setVisible(False)

    def author_page_added_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageAuthorPageAddedSortButton.isChecked():
            if self.ui.mainPageAuthorPageAddedSortButton.wasChecked:
                self.ui.mainPageAuthorPageAddedSortButton.wasChecked = False
                self.ui.label_226.setVisible(False)
                self.ui.mainPageAuthorPageSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageAuthorPageAddedSortButton.toggle()
                self.ui.mainPageAuthorPageSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageAuthorPageAddedSortButton.wasChecked = True
                self.ui.label_226.setVisible(True)
                self.sort_songs_by_added()
        else:
            self.ui.mainPageAuthorPageAddedSortButton.wasChecked = False
            self.ui.label_226.setVisible(False)

    def author_page_category_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageAuthorPageCategorySortButton.isChecked():
            if self.ui.mainPageAuthorPageCategorySortButton.wasChecked:
                self.ui.mainPageAuthorPageCategorySortButton.wasChecked = False
                self.ui.label_225.setVisible(False)
                self.ui.mainPageAuthorPageSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageAuthorPageCategorySortButton.toggle()
                self.ui.mainPageAuthorPageSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageAuthorPageCategorySortButton.wasChecked = True
                self.ui.label_225.setVisible(True)
                self.sort_songs_by_category()
        else:
            self.ui.mainPageAuthorPageCategorySortButton.wasChecked = False
            self.ui.label_225.setVisible(False)

    def author_page_title_sort_button_slot(self):
        """Toggle likedSong's page title sort button's indicator and sort the songs"""
        if self.ui.mainPageAuthorPageTitleSortButton.isChecked():
            if self.ui.mainPageAuthorPageTitleSortButton.wasChecked:
                self.ui.mainPageAuthorPageTitleSortButton.wasChecked = False
                self.ui.label_224.setVisible(False)
                self.ui.mainPageAuthorPageSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageAuthorPageTitleSortButton.toggle()
                self.ui.mainPageAuthorPageSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageAuthorPageTitleSortButton.wasChecked = True
                self.ui.label_224.setVisible(True)
                self.sort_songs_by_title()
        else:
            self.ui.mainPageAuthorPageTitleSortButton.wasChecked = False
            self.ui.label_224.setVisible(False)

    def playlist_length_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPagePlaylistLengthSortButton.isChecked():
            if self.ui.mainPagePlaylistLengthSortButton.wasChecked:
                self.ui.mainPagePlaylistLengthSortButton.wasChecked = False
                self.ui.label_223.setVisible(False)
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPagePlaylistLengthSortButton.toggle()
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPagePlaylistLengthSortButton.wasChecked = True
                self.ui.label_223.setVisible(True)
                self.sort_songs_by_length()
        else:
            self.ui.mainPagePlaylistLengthSortButton.wasChecked = False
            self.ui.label_223.setVisible(False)

    def playlist_added_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPagePlaylistAddedSortButton.isChecked():
            if self.ui.mainPagePlaylistAddedSortButton.wasChecked:
                self.ui.mainPagePlaylistAddedSortButton.wasChecked = False
                self.ui.label_221.setVisible(False)
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPagePlaylistAddedSortButton.toggle()
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPagePlaylistAddedSortButton.wasChecked = True
                self.ui.label_221.setVisible(True)
                self.sort_songs_by_added()
        else:
            self.ui.mainPagePlaylistAddedSortButton.wasChecked = False
            self.ui.label_221.setVisible(False)

    def playlist_category_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPagePlaylistCategorySortButton.isChecked():
            if self.ui.mainPagePlaylistCategorySortButton.wasChecked:
                self.ui.mainPagePlaylistCategorySortButton.wasChecked = False
                self.ui.label_220.setVisible(False)
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPagePlaylistCategorySortButton.toggle()
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPagePlaylistCategorySortButton.wasChecked = True
                self.ui.label_220.setVisible(True)
                self.sort_songs_by_category()
        else:
            self.ui.mainPagePlaylistCategorySortButton.wasChecked = False
            self.ui.label_220.setVisible(False)

    def playlist_artist_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPagePlaylistArtistSortButton.isChecked():
            if self.ui.mainPagePlaylistArtistSortButton.wasChecked:
                self.ui.mainPagePlaylistArtistSortButton.wasChecked = False
                self.ui.label_219.setVisible(False)
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPagePlaylistArtistSortButton.toggle()
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPagePlaylistArtistSortButton.wasChecked = True
                self.ui.label_219.setVisible(True)
                self.sort_songs_by_artist()
        else:
            self.ui.mainPagePlaylistArtistSortButton.wasChecked = False
            self.ui.label_219.setVisible(False)

    def playlist_title_sort_button_slot(self):
        """Toggle likedSong's page title sort button's indicator and sort the songs"""
        if self.ui.mainPagePlaylistTitleSortButton.isChecked():
            if self.ui.mainPagePlaylistTitleSortButton.wasChecked:
                self.ui.mainPagePlaylistTitleSortButton.wasChecked = False
                self.ui.label_218.setVisible(False)
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPagePlaylistTitleSortButton.toggle()
                self.ui.mainPagePlaylistSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPagePlaylistTitleSortButton.wasChecked = True
                self.ui.label_218.setVisible(True)
                self.sort_songs_by_title()
        else:
            self.ui.mainPagePlaylistTitleSortButton.wasChecked = False
            self.ui.label_218.setVisible(False)

    def liked_songs_length_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageLikedSongsLengthSortButton.isChecked():
            if self.ui.mainPageLikedSongsLengthSortButton.wasChecked:
                self.ui.mainPageLikedSongsLengthSortButton.wasChecked = False
                self.ui.label_217.setVisible(False)
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageLikedSongsLengthSortButton.toggle()
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageLikedSongsLengthSortButton.wasChecked = True
                self.ui.label_217.setVisible(True)
                self.sort_songs_by_length()
        else:
            self.ui.mainPageLikedSongsLengthSortButton.wasChecked = False
            self.ui.label_217.setVisible(False)

    def liked_songs_added_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageLikedSongsAddedSortButton.isChecked():
            if self.ui.mainPageLikedSongsAddedSortButton.wasChecked:
                self.ui.mainPageLikedSongsAddedSortButton.wasChecked = False
                self.ui.label_216.setVisible(False)
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageLikedSongsAddedSortButton.toggle()
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageLikedSongsAddedSortButton.wasChecked = True
                self.ui.label_216.setVisible(True)
                self.sort_songs_by_added()
        else:
            self.ui.mainPageLikedSongsAddedSortButton.wasChecked = False
            self.ui.label_216.setVisible(False)

    def liked_songs_category_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageLikedSongsCategorySortButton.isChecked():
            if self.ui.mainPageLikedSongsCategorySortButton.wasChecked:
                self.ui.mainPageLikedSongsCategorySortButton.wasChecked = False
                self.ui.label_215.setVisible(False)
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageLikedSongsCategorySortButton.toggle()
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageLikedSongsCategorySortButton.wasChecked = True
                self.ui.label_215.setVisible(True)
                self.sort_songs_by_category()
        else:
            self.ui.mainPageLikedSongsCategorySortButton.wasChecked = False
            self.ui.label_215.setVisible(False)

    def liked_songs_artist_sort_button_slot(self):
        """Toggle likedSong's page artist sort button's indicator and sort the songs"""
        if self.ui.mainPageLikedSongsArtistSortButton.isChecked():
            if self.ui.mainPageLikedSongsArtistSortButton.wasChecked:
                self.ui.mainPageLikedSongsArtistSortButton.wasChecked = False
                self.ui.label_214.setVisible(False)
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageLikedSongsArtistSortButton.toggle()
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageLikedSongsArtistSortButton.wasChecked = True
                self.ui.label_214.setVisible(True)
                self.sort_songs_by_artist()
        else:
            self.ui.mainPageLikedSongsArtistSortButton.wasChecked = False
            self.ui.label_214.setVisible(False)

    def liked_songs_title_sort_button_slot(self):
        """Toggle likedSong's page title sort button's indicator and sort the songs"""
        if self.ui.mainPageLikedSongsTitleSortButton.isChecked():
            if self.ui.mainPageLikedSongsTitleSortButton.wasChecked:
                self.ui.mainPageLikedSongsTitleSortButton.wasChecked = False
                self.ui.label_213.setVisible(False)
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(False)
                self.ui.mainPageLikedSongsTitleSortButton.toggle()
                self.ui.mainPageLikedSongsSortButtonsQButtonGroup.setExclusive(True)
            else:
                self.ui.mainPageLikedSongsTitleSortButton.wasChecked = True
                self.ui.label_213.setVisible(True)
                self.sort_songs_by_title()
        else:
            self.ui.mainPageLikedSongsTitleSortButton.wasChecked = False
            self.ui.label_213.setVisible(False)

    def sort_songs_by_length(self):
        """Sort mainPage's songs by length from shortest to longest"""
        pass

    def sort_songs_by_added(self):
        """Sort mainPage's songs by added from earliest to latest"""
        pass

    def sort_songs_by_title(self):
        """Sorts mainPage's songs by title alphabetically"""
        pass

    def sort_songs_by_category(self):
        """Sort mainPage's songs by category alphabetically"""
        pass

    def sort_songs_by_artist(self):
        """Sort mainPage's songs by artist alphabetically"""
        pass

    def setup_main_page_authors(self):
        """Prepare mainPage's authors page."""
        pass

    def setup_main_page_last_played(self):
        """Prepare mainPage's lastPlayed page."""
        pass

    def setup_main_page_liked_songs(self):
        """Prepare mainPage's likedSongs page."""
        pass

    def setup_main_page_categories(self):
        """ Prepare mainPage's categories page."""
        pass

    def setup_main_page_now_playing(self):
        """Prepare mainPage's nowPlaying page."""
        pass

    def setup_main_page_albums(self):
        """Prepare mainPage's nowPlaying page."""
        pass

    def setup_main_page_queue(self):
        """Prepare mainPage's nowPlaying page."""
        pass

    def albums_button_slot(self):
        """Prepare albums page and change mainPageStackedWidget to album's index"""
        self.setup_main_page_albums()
        self.set_main_page_stacked_widget_index(10)
        with local_database_app.app_context():
            all_albums = Albums.query.all()
        for album in all_albums:
            album_frame = AlbumEntry(self.ui.mainPageAlbumsAlbumsGridFrame, album_name=album.album_name)
            album_frame.clicked.connect(partial(self.load_album_page, album))
            self.ui.mainPageAlbumsAlbumsGridQFlowLayout.addWidget(album_frame)
        album_adder = AdderEntry(adder_type=2, parent=self.ui.mainPageAlbumsAlbumsGridFrame)
        album_adder.clicked.connect(self.album_adder_clicked_slot)
        self.ui.mainPageAlbumsAlbumsGridQFlowLayout.addWidget(album_adder)

    def load_album_page(self, album):
        if len(self.current_loaded_songs_frames) != 0:
            for i in self.current_loaded_songs_frames:
                i.setParent(None)
            self.current_loaded_songs_frames = []
        self.set_main_page_stacked_widget_index(8)
        self.ui.mainPageAlbumNameOfAlbumLabel.setText(album.album_name)
        with local_database_app.app_context():
            songs = AlbumSongs.query.filter_by(album_id=album.id).all()
        for i in songs:
            with local_database_app.app_context():
                song = Songs.query.filter_by(id=i.song_id).first()
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_id=song.id,
                song_title=song.title,
                artist_name=song.author.author_name,
                category_name=song.category.category_name,
                path=song.path,
                is_liked=is_liked,
                frame_structure={"song_title": True, "artist_name": True, "category_name": False, "date_added": False,
                                 "song_length": True},
                visibility_changing_data_elements=[("songEntrySongAuthorQFrame", 552)]
            )
            if self.now_playing_song and song.id == self.now_playing_song.song_id:
                if self.now_playing_song in self.sorted_current_playlist_songs_frames:
                    self.sorted_current_playlist_songs_frames[
                        self.sorted_current_playlist_songs_frames.index(self.now_playing_song)] = song_frame
                self.now_playing_song.setParent(None)
                self.now_playing_song = song_frame
                self.now_playing_song.pushButton_13.setChecked(True)
                self.ui.mainPageAlbumSongsListQVBoxLayout.addWidget(self.now_playing_song)
                self.current_loaded_songs_frames.append(self.now_playing_song)
            else:
                song_frame.pushButton_30.clicked.connect(partial(self.like_song, song_frame))
                song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song_frame))
                song_frame.songEntrySongAuthorQPushButton.clicked.connect(partial(self.load_author_page, song.author))

                self.ui.mainPageAlbumSongsListQVBoxLayout.addWidget(song_frame)

                if len(self.sorted_current_playlist_songs_frames) > 0:
                    for j in self.sorted_current_playlist_songs_frames:
                        if j.song_id == song_frame.song_id:
                            index = self.sorted_current_playlist_songs_frames.index(j)
                            self.sorted_current_playlist_songs_frames[index].setParent(None)
                            self.sorted_current_playlist_songs_frames[index] = song_frame
                    if len(self.shuffled_current_playlist_songs_frames) > 0:
                        for j in self.shuffled_current_playlist_songs_frames:
                            if j.song_id == song_frame.song_id:
                                index = self.shuffled_current_playlist_songs_frames.index(j)
                                self.shuffled_current_playlist_songs_frames[index].setParent(None)
                                self.shuffled_current_playlist_songs_frames[index] = song_frame

                self.current_loaded_songs_frames.append(song_frame)

    # TODO Clear the page before its loaded to not duplicate the author frames
    def authors_button_slot(self):
        """Prepare authors page and change mainPageStackedWidget to authors's index"""
        self.setup_main_page_authors()
        self.set_main_page_stacked_widget_index(4)
        with local_database_app.app_context():
            all_authors = Authors.query.all()
        for author in all_authors:
            author_frame = AuthorEntry(self.ui.mainPageAuthorsGrid, author_name=author.author_name)
            author_frame.clicked.connect(partial(self.load_author_page, author))
            self.ui.mainPageAuthorsAuthorsGridQFlowLayout.addWidget(author_frame)
        author_adder = AdderEntry(adder_type=3, parent=self.ui.mainPageAuthorsGrid)
        author_adder.clicked.connect(self.author_adder_clicked_slot)
        self.ui.mainPageAuthorsAuthorsGridQFlowLayout.addWidget(author_adder)

    # TODO Make author's songs and playlists Frames disappear when changing mainPageAuthorPageStacked widget to author's
    # TODO albums page similarly on other pages to prevent size issues
    def load_author_page(self, author):
        self.set_main_page_stacked_widget_index(6)
        self.ui.mainPageAuthorPageAlbumsAuthorNameLabel.setText(author.author_name + " albums")
        self.ui.mainPageAuthorPagePlaylistsAuthorNameLabel.setText(author.author_name + " playlists")
        self.ui.mainPageAutorNameLabel.setText(author.author_name)
        self.load_selected_author_songs(author)
        self.load_selected_author_albums(author)
        self.load_selected_author_playlists(author)

    def load_selected_author_songs(self, author):
        if len(self.loaded_selected_author_songs) != 0:
            for i in self.loaded_selected_author_songs:
                i.setParent(None)
            self.loaded_selected_author_songs = []
        with local_database_app.app_context():
            songs = Songs.query.filter_by(author_id=author.id).all()
        for song in songs:
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_id=song.id,
                song_title=song.title,
                category_name=song.category.category_name,
                date_added="Placeholder date",
                song_length="Placeholder length",
                path=song.path,
                is_liked=is_liked,
                frame_structure={"song_title": True, "artist_name": False, "category_name": True, "date_added": True,
                                 "song_length": True},
                visibility_changing_data_elements=[("songEntrySongCategoryQFrame", 552),
                                                   ("songEntrySongDateAddedQLabel", 726)]
            )
            self.ui.mainPageAuthorPageSongsListQVBoxLayout.addWidget(song_frame)
            song_frame.pushButton_30.clicked.connect(partial(self.like_song, song_frame))
            song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
            song_frame.songEntrySongCategoryQPushButton.clicked.connect(partial(self.load_selected_category_page,
                                                                                song.category.category_name))
            self.loaded_selected_author_songs.append(song_frame)

    def load_selected_author_albums(self, author):
        if len(self.loaded_selected_author_albums) != 0:
            for i in self.loaded_selected_author_albums:
                i.setParent(None)
            self.loaded_selected_author_albums = []
        with local_database_app.app_context():
            albums = Albums.query.filter_by(author_id=author.id).all()
        for album in albums:
            album_frame = AlbumEntry(album_name=album.album_name)
            album_frame.clicked.connect(partial(self.load_album_page, album))
            self.ui.mainPageAuthorPageAlbumsGridQFlowLayout.addWidget(album_frame)
            self.loaded_selected_author_albums.append(album_frame)

    def load_selected_author_playlists(self, author):
        if len(self.loaded_selected_author_playlists) != 0:
            for i in self.loaded_selected_author_playlists:
                i.setParent(None)
            self.loaded_selected_author_playlists = []
        with local_database_app.app_context():
            author_playlists = AuthorPlaylists.query.filter_by(author_id=author.id).all()
        author_playlists_ids = []
        for i in author_playlists:
            author_playlists_ids.append(i.playlist_id)
        with local_database_app.app_context():
            playlists = Playlist.query.filter(Playlist.id.in_(author_playlists_ids)).all()
        if playlists:
            for playlist in playlists:
                playlist_frame = PlaylistEntry(self.ui.frame_62, playlist_name=playlist.playlist_name)
                playlist_frame.clicked.connect(partial(self.load_playlist_page, playlist))
                self.ui.mainPageAuthorPagePlaylistsGridQFlowLayout.addWidget(playlist_frame)
                self.loaded_selected_author_playlists.append(playlist_frame)

    def last_played_button_slot(self):
        """Prepare lastPlayed page and change mainPageStackedWidget to lastPlayed's index"""
        self.set_main_page_stacked_widget_index(3)

    def liked_songs_button_slot(self):
        """Prepare likedSongs page and change mainPageStackedWidget to likedSongs' index"""
        self.set_main_page_stacked_widget_index(2)
        if len(self.current_loaded_songs_frames) != 0:
            for i in self.current_loaded_songs_frames:
                i.setParent(None)
            self.current_loaded_songs_frames = []
        self.setup_main_page_liked_songs()
        with local_database_app.app_context():
            # TODO Handle error on quest user not subscriptable
            liked_songs = Songs.query.filter_by(liked_by=self.user_data["hashed_name"]).all()
        if liked_songs:
            for song in liked_songs:
                liked_song_frame = SongEntry(
                    song_id=song.id,
                    song_title=song.title,
                    artist_name=song.author.author_name,
                    category_name=song.category.category_name,
                    date_added="Placeholder date",
                    song_length="Placeholder length",
                    path=song.path,
                    is_liked=True,
                    frame_structure={"song_title": True, "artist_name": True, "category_name": True, "date_added": True,
                                     "song_length": True},
                    visibility_changing_data_elements=[("songEntrySongAuthorQFrame", 552),
                                                       ("songEntrySongDateAddedQLabel", 726),
                                                       ("songEntrySongCategoryQFrame", 950)]
                )

                if self.now_playing_song and song.id == self.now_playing_song.song_id:
                    self.ui.mainPageLikedSongsSongListQVBoxLayout.addWidget(self.now_playing_song)
                    self.current_loaded_songs_frames.append(self.now_playing_song)
                else:
                    liked_song_frame.pushButton_30.clicked.connect(partial(self.like_song, liked_song_frame))
                    liked_song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, liked_song_frame))
                    liked_song_frame.songEntrySongAuthorQPushButton.clicked.connect(
                        partial(self.load_author_page, song.author))
                    liked_song_frame.songEntrySongCategoryQPushButton.clicked.connect(
                        partial(self.load_selected_category_page, song.category.category_name))
                    self.ui.mainPageLikedSongsSongListQVBoxLayout.addWidget(liked_song_frame)
                    if len(self.sorted_current_playlist_songs_frames) > 0:
                        for i in self.sorted_current_playlist_songs_frames:
                            if i.song_id == liked_song_frame.song_id:
                                index = self.sorted_current_playlist_songs_frames.index(i)
                                self.sorted_current_playlist_songs_frames[index].setParent(None)
                                self.sorted_current_playlist_songs_frames[index] = liked_song_frame
                        if len(self.shuffled_current_playlist_songs_frames) > 0:
                            for i in self.shuffled_current_playlist_songs_frames:
                                if i.song_id == liked_song_frame.song_id:
                                    index = self.shuffled_current_playlist_songs_frames.index(i)
                                    self.shuffled_current_playlist_songs_frames[index].setParent(None)
                                    self.shuffled_current_playlist_songs_frames[index] = liked_song_frame
                    self.current_loaded_songs_frames.append(liked_song_frame)

    def categories_button_slot(self):
        """Prepare categories page and change mainPageStackedWidget to categories' index"""
        self.setup_main_page_categories()
        self.set_main_page_stacked_widget_index(1)

        music_categories = []
        self.category_frames = []
        with local_database_app.app_context():
            music_categories_query = MusicCategories.query.all()
        for i in music_categories_query:
            music_categories.append(i.category_name)
        for category in music_categories:
            category_frame = CategoryEntry(self.ui.frame_54, category=category)
            category_frame.clicked.connect(partial(self.load_selected_category_page, category))
            self.ui.mainPageCategoriesCategoriesEntriesQFlowLayout.addWidget(category_frame)
            self.category_frames.append(category_frame)
        category_adder = AdderEntry(adder_type=1)
        category_adder.clicked.connect(self.category_adder_clicked_slot)
        self.ui.mainPageCategoriesCategoriesEntriesQFlowLayout.addWidget(category_adder)

    def category_adder_clicked_slot(self):
        """Create new categoryInputDialog and run its show() method, run handle_new_category_creation() to validate
         and create new category.

        """

        # Blacked out semi-transparent frame over whole app, closes dialog when clicked
        app_layer_frame = ClickedSignalQFrame(self.ui.centralwidget)
        category_input_dialog = categoryInputDialog(parent=self.ui.window)

        # Dialog's exit button clicked slot
        category_input_dialog.categoryInputDialogExitButton.clicked.connect(partial(self.handle_dialog_rejection,
                                                                                    app_layer_frame,
                                                                                    category_input_dialog))
        # App layer frame's clicked slot
        app_layer_frame.clicked.connect(partial(self.handle_dialog_rejection, app_layer_frame, category_input_dialog))

        # Show app layer_frame and dialog on the screen
        app_layer_frame.show()
        category_input_dialog.show()

        # Create and handle dialog's miniature selection dialog
        miniature_file_dialog = self.handle_and_connect_new_miniature_file_dialog(
            category_input_dialog.categoryInputDialogMiniatureQToolButton, category_input_dialog)

        # Dialog's add button clicked slot
        category_input_dialog.categoryInputDialogAddButton.clicked.connect(
            partial(self.handle_new_category_creation, category_input_dialog, miniature_file_dialog, app_layer_frame))

    def handle_new_category_creation(self, category_dialog, category_miniature_dialog, app_layer_frame):
        """Handle new category creation. Collect input from category_dialog and miniature_file_dialog then create new
            category.

            Parameters:
                app_layer_frame (QtWidgets.QFrame): blacked-out frame behind dialog that it shown along it.
                category_dialog (categoryInputDialog): categoryInputDialog used to collect data to create category from.
                category_miniature_dialog (QtWidgets.QFileDialog): QFileDialog used to collect miniature for the new
                 category.
        """
        print(f"Handling category creation...\n"
              f"---------------------------------------------------------------------------------------\n"
              f"Category_miniature_dialog files: {category_miniature_dialog.selectedFiles()}\n"
              f"Category name: {category_dialog.categoryInputDialogCategoryNameQLineEdit.text()}\n"
              f"---------------------------------------------------------------------------------------")
        # handle adding new category to database here.
        print("Created new category in database.")
        self.handle_dialog_acceptation(app_layer_frame, category_dialog)

    @staticmethod
    def handle_dialog_acceptation(app_layer_frame, dialog):
        """Call dialog's accept() method and app_layer_frame's deleteLater() to remove both from the screen.

        Parameters:
            app_layer_frame (ClickedSignalQFrame): Frame that gets shown over whole app when dialog is created.
            dialog (QtWidgets.QDialog): Dialog that was shown along app_layer_frame.
        """
        dialog.accept()
        app_layer_frame.deleteLater()

    def now_playing_button_slot(self):
        """Prepare nowPlaying page and change mainPageStackedWidget to nowPlaying's index"""
        self.setup_main_page_now_playing()
        self.set_main_page_stacked_widget_index(0)

    def mini_player_button_slot(self):
        """Close normal size player's window and open minimized version"""
        pass

    def main_page_now_playing_resize_slot(self):
        width = self.ui.mainPageNowPlaying.rect().width()
        heigth = self.ui.mainPageNowPlaying.rect().height()
        self.ui.frame_20.resize(width, heigth)
        self.ui.mainPageNowPlayingBackgroundLabel.resize(width, heigth)
        self.ui.mainPageNowPlayingBackgroundLabel.setPixmap(
            QtGui.QPixmap(":/icons/temporary/icons/playlistCoverExample1.png").scaled(
                self.ui.mainPageNowPlayingBackgroundLabel.size(), QtCore.Qt.KeepAspectRatioByExpanding,
                QtCore.Qt.SmoothTransformation))

    def main_page_stacked_widget_resize_slot(self):
        self.ui.fixedNavbar.setFixedWidth(self.ui.centralPageAppPage.rect().width() - 200)

    # TODO Make category's songs and playlists Frames disappear when changing mainPageCagegoryPageStacked widget to category's
    # TODO albums page similarly on other pages to prevent size issues
    def load_selected_category_page(self, category):
        self.set_main_page_stacked_widget_index(7)
        self.ui.mainPageCategoryNameLabel.setText(category)
        self.ui.mainPageCategoryPageAlbumsCategoryNameLabel.setText(category + " albums")
        self.ui.mainPageCategoryPagePlaylistsCategoryNameLabel.setText(category + " playlists")
        with local_database_app.app_context():
            music_category = MusicCategories.query.filter_by(category_name=category).first()
        self.load_selected_category_songs(music_category)
        self.load_selected_category_albums(music_category)
        self.load_selected_category_playlists(music_category)

    def load_selected_category_songs(self, music_category):
        if len(self.loaded_songs) != 0:
            for i in self.loaded_songs:
                i.setParent(None)
            self.loaded_songs = []
        with local_database_app.app_context():
            songs = Songs.query.filter_by(category=music_category)
        for song in songs:
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_id=song.id,
                song_title=song.title,
                artist_name=song.author.author_name,
                date_added="Placeholder date",
                song_length="Placeholder length",
                path=song.path,
                is_liked=is_liked,
                frame_structure={"song_title": True, "artist_name": True, "category_name": False, "date_added": True,
                                 "song_length": True},
                visibility_changing_data_elements=[("songEntrySongAuthorQFrame", 552),
                                                   ("songEntrySongDateAddedQLabel", 726)]
            )
            self.ui.mainPageCategoryPageSongsListQVBoxLayout.addWidget(song_frame)
            song_frame.pushButton_30.clicked.connect(partial(self.like_song, song_frame))
            song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
            song_frame.songEntrySongAuthorQPushButton.clicked.connect(partial(self.load_author_page, song.author))
            self.loaded_songs.append(song_frame)

    def load_selected_category_albums(self, music_category):
        if len(self.loaded_albums) != 0:
            for i in self.loaded_albums:
                i.setParent(None)
            self.loaded_albums = []
        with local_database_app.app_context():
            albums = Albums.query.filter_by(category=music_category).all()
        for album in albums:
            album_frame = AlbumEntry(album_name=album.album_name)
            album_frame.clicked.connect(partial(self.load_album_page, album))
            self.ui.mainPageCategoryAlbumsGridQFlowLayout.addWidget(album_frame)
            self.loaded_albums.append(album_frame)

    def load_selected_category_playlists(self, music_category):
        if len(self.loaded_playlists) != 0:
            for i in self.loaded_playlists:
                i.setParent(None)
            self.loaded_playlists = []
        with local_database_app.app_context():
            playlists = Playlist.query.filter_by(category=music_category).all()
        row = column = 0
        for playlist in playlists:
            if column % 8 == 0:
                row += 1
                column = 0
            playlist_frame = PlaylistEntry(self.ui.frame_62, playlist_name=playlist.playlist_name)
            playlist_frame.clicked.connect(partial(self.load_playlist_page, playlist))
            self.ui.mainPageCategoryPlaylistsGridQGridLayout.addWidget(playlist_frame, row, column, 1, 1)
            self.loaded_playlists.append(playlist_frame)
            column += 1

    def load_playlist_frames(self):
        with local_database_app.app_context():
            playlists = Playlist.query.all()
        for playlist in playlists:
            playlist_frame = QtWidgets.QPushButton(self.ui.leftMenuBottomPlaylistsFrame)
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(playlist_frame.sizePolicy().hasHeightForWidth())
            playlist_frame.setSizePolicy(size_policy)
            playlist_frame.setMinimumSize(QtCore.QSize(0, 32))
            font = QtGui.QFont()
            font.setFamily("Heebo Medium")
            font.setPointSize(11)
            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(QtGui.QFont.Weight(7))
            font.setStrikeOut(False)
            playlist_frame.setFont(font)
            playlist_frame.setText(playlist.playlist_name)
            playlist_frame.setCheckable(True)
            playlist_frame.setAutoExclusive(False)
            playlist_frame.setObjectName("leftMenuPlaylistDummy1")
            playlist_frame.clicked.connect(partial(self.load_playlist_page, playlist))
            self.ui.verticalLayout_5.addWidget(playlist_frame)
            self.ui.mainPageUtilityButtonsQButtonGroup.addButton(playlist_frame)

    def load_playlist_page(self, playlist):
        self.set_main_page_stacked_widget_index(5)
        self.ui.mainPagePlaylistNameOfPlaylistLabel.setText(playlist.playlist_name)
        self.load_playlist_page_songs(playlist)

    def load_playlist_page_songs(self, playlist):
        with local_database_app.app_context():
            playlist_songs = PlaylistSongs.query.filter_by(playlist_id=playlist.id).all()
        playlist_songs_ids = []
        for i in playlist_songs:
            playlist_songs_ids.append(i.song_id)
        if len(self.loaded_playlist_page_songs) != 0:
            for i in self.loaded_playlist_page_songs:
                i.setParent(None)
            self.loaded_playlist_page_songs = []
        with local_database_app.app_context():
            songs = Songs.query.filter(Songs.id.in_(playlist_songs_ids)).all()
        for song in songs:
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_id=song.id,
                song_title=song.title,
                artist_name=song.author.author_name,
                category_name=song.category.category_name,
                date_added="Placeholder date",
                song_length="Placeholder length",
                path=song.path,
                is_liked=is_liked,
                frame_structure={"song_title": True, "artist_name": True, "category_name": True, "date_added": True,
                                 "song_length": True},
                visibility_changing_data_elements=[("songEntrySongAuthorQFrame", 552),
                                                   ("songEntrySongCategoryQFrame", 726),
                                                   ("songEntrySongDateAddedQLabel", 950)]
            )
            self.loaded_playlist_page_songs.append(song_frame)
            song_frame.pushButton_30.clicked.connect(partial(self.like_song, song_frame))
            # song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
            song_frame.songEntrySongAuthorQPushButton.clicked.connect(partial(self.load_author_page, song.author))
            song_frame.songEntrySongCategoryQPushButton.clicked.connect(partial(self.load_selected_category_page,
                                                                                song.category.category_name))
            self.ui.mainPagePlaylistSongListQVBoxLayout.addWidget(song_frame)

    def like_song(self, song_frame):
        with local_database_app.app_context():
            song_to_like = Songs.query.filter_by(id=song_frame.song_id).first()
        if song_to_like.liked_by == self.user_data["hashed_name"]:
            song_to_like.liked_by = ""
            song_frame.is_liked = False
        else:
            song_to_like.liked_by = self.user_data["hashed_name"]
            song_frame.is_liked = True
        db.session.commit()

    def play_pause_song(self, song_frame):
        if self.now_playing_song:
            if song_frame.song_id == self.now_playing_song.song_id:
                if self.player.state() == self.player.PlayingState:
                    self.player.pause()
                elif self.player.state() == self.player.PausedState:
                    if self.player.position() != 0:
                        self.player.setPosition(self.player.position())
                    self.player.play()
                    self.now_playing_song = song_frame
                else:
                    print("ERROR")
            elif song_frame.song_id != self.now_playing_song.song_id:
                if self.playlist_state == PlaylistState.SORTED:
                    if song_frame in self.sorted_current_playlist_songs_frames:
                        self.sorted_playlist_playing_song_index = self.sorted_current_playlist_songs_frames.index(
                            song_frame) - 1
                        self.player.stop()
                elif self.playlist_state == PlaylistState.SHUFFLED:
                    if song_frame in self.shuffled_current_playlist_songs_frames:
                        self.shuffled_playlist_playing_song_index = self.shuffled_current_playlist_songs_frames.index(
                            song_frame) - 1
                        self.player.stop()
                else:
                    url = QUrl.fromLocalFile(song_frame.path)
                    content = QMediaContent(url)
                    self.ui.playerLoopButton.setChecked(False)
                    self.player.setMedia(content)
                    self.now_playing_song = song_frame
                    self.player.play()

        else:
            self.playlist_state = PlaylistState.NONE
            self.player.setVolume(self.ui.volumeSlider.value())
            self.ui.playerPausePlayButton.setChecked(True)
            url = QUrl.fromLocalFile(song_frame.path)
            content = QMediaContent(url)
            self.player.setMedia(content)
            self.now_playing_song = song_frame
            self.player.play()

    def start_playlist(self):
        for i in self.sorted_current_playlist_songs_frames:
            if i not in self.current_loaded_songs_frames:
                i.setParent(None)
        for i in self.shuffled_current_playlist_songs_frames:
            if i not in self.current_loaded_songs_frames:
                i.setParent(None)
        self.sorted_current_playlist_songs_frames = []
        self.shuffled_current_playlist_songs_frames = []
        self.player.stop()
        self.now_playing_song = None
        if self.current_loaded_songs_frames:
            self.sorted_playlist_playing_song_index = 0
            for i in self.current_loaded_songs_frames:
                self.sorted_current_playlist_songs_frames.append(i)
            new_media = QMediaContent(QUrl.fromLocalFile(self.current_loaded_songs_frames[0].path))
            self.playlist_state = PlaylistState.SORTED
            self.now_playing_song = self.sorted_current_playlist_songs_frames[0]
            self.player.setVolume(self.ui.volumeSlider.value())
            self.player.setMedia(new_media)
            self.player.play()

        if self.ui.playerShuffleButton.isChecked():
            self.shuffle_now_playing_playlist()

    def queue_button_slot(self):
        """Prepare authors page and change mainPageStackedWidget to authors' index"""
        if self.now_playing_song:
            if self.playlist_state == PlaylistState.SORTED:
                song_frame = SongEntry(
                    song_id=self.now_playing_song.song_id,
                    song_title=self.now_playing_song.song_title,
                    artist_name=self.now_playing_song.artist_name,
                    category_name=self.now_playing_song.category_name,
                    path=self.now_playing_song.path,
                    is_liked=True,
                    frame_structure={"song_title": True, "artist_name": True, "category_name": True,
                                     "date_added": True, "song_length": True},
                    visibility_changing_data_elements=[("songEntrySongAuthorQFrame", 552),
                                                       ("songEntrySongCategoryQFrame", 726),
                                                       ("songEntrySongDateAddedQLabel", 950)]
                )
                self.sorted_current_playlist_songs_frames[
                    self.sorted_current_playlist_songs_frames.index(self.now_playing_song)] = song_frame
                self.now_playing_song = song_frame
                self.now_playing_song.pushButton_13.setChecked(True)
                self.ui.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(self.now_playing_song)
                index = self.sorted_current_playlist_songs_frames.index(self.now_playing_song)
                for song in self.sorted_current_playlist_songs_frames[index + 1:]:
                    song_frame = SongEntry(
                        song_id=song.song_id,
                        song_title=song.song_title,
                        artist_name=song.artist_name,
                        category_name=song.category_name,
                        path=song.path,
                        is_liked=True,
                        frame_structure={"song_title": True, "artist_name": True, "category_name": True,
                                         "date_added": True, "song_length": True},
                        visibility_changing_data_elements=[("songEntrySongAuthorQFrame", 552),
                                                           ("songEntrySongCategoryQFrame", 726),
                                                           ("songEntrySongDateAddedQLabel", 950)]
                    )
                    self.sorted_current_playlist_songs_frames[
                        self.sorted_current_playlist_songs_frames.index(song)].setParent(None)
                    self.sorted_current_playlist_songs_frames[
                        self.sorted_current_playlist_songs_frames.index(song)] = song_frame
                    self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(song_frame)
            elif self.playlist_state == PlaylistState.SHUFFLED:
                song_frame = SongEntry(
                    song_id=self.now_playing_song.song_id,
                    song_title=self.now_playing_song.song_title,
                    artist_name=self.now_playing_song.artist_name,
                    category_name=self.now_playing_song.category_name,
                    path=self.now_playing_song.path,
                    is_liked=True,
                    frame_structure={"song_title": True, "artist_name": True, "category_name": True,
                                     "date_added": True, "song_length": True},
                    visibility_changing_data_elements=[("songEntrySongAuthorQFrame", 552),
                                                       ("songEntrySongCategoryQFrame", 726),
                                                       ("songEntrySongDateAddedQLabel", 950)]
                )
                self.shuffled_current_playlist_songs_frames[
                    self.shuffled_current_playlist_songs_frames.index(self.now_playing_song)] = song_frame
                self.now_playing_song = song_frame
                self.now_playing_song.pushButton_13.setChecked(True)
                self.ui.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(self.now_playing_song)
                index = self.shuffled_current_playlist_songs_frames.index(self.now_playing_song)
                for song in self.shuffled_current_playlist_songs_frames[index + 1:]:
                    song_frame = SongEntry(
                        song_id=song.song_id,
                        song_title=song.song_title,
                        artist_name=song.artist_name,
                        category_name=song.category_name,
                        path=song.path,
                        is_liked=True,
                        frame_structure={"song_title": True, "artist_name": True, "category_name": True,
                                         "date_added": True, "song_length": True},
                        visibility_changing_data_elements=[("songEntrySongAuthorQFrame", 552),
                                                           ("songEntrySongCategoryQFrame", 726),
                                                           ("songEntrySongDateAddedQLabel", 950)]
                    )
                    self.shuffled_current_playlist_songs_frames[
                        self.shuffled_current_playlist_songs_frames.index(song)].setParent(None)
                    self.shuffled_current_playlist_songs_frames[
                        self.shuffled_current_playlist_songs_frames.index(song)] = song_frame
                    self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(song_frame)
        self.setup_main_page_queue()
        self.set_main_page_stacked_widget_index(9)

    def play_previous_playlist_song(self):
        widget_index = self.ui.mainPageStackedWidget.currentIndex()
        print(f"PREVIOUS {self.sorted_playlist_playing_song_index}")
        if self.ui.playerLoopButton.checkState() == 2:
            self.ui.playerLoopButton.setCheckState(QtCore.Qt.PartiallyChecked)
        if self.playlist_state == PlaylistState.SORTED:
            if self.sorted_playlist_playing_song_index == 0:
                self.player.setPosition(0)
                self.ui.songCurrentTimestampLabel.setText("00:00")
                self.ui.songTimeSlider.setSliderPosition(0)
            else:
                if widget_index == 9:
                    self.timer.singleShot(0, partial(self.add_sorted_frames_to_queue,
                                                     self.sorted_playlist_playing_song_index))
                self.sorted_playlist_playing_song_index -= 2
                self.player.stop()
        if self.playlist_state == PlaylistState.SHUFFLED:
            if self.shuffled_playlist_playing_song_index == 0:
                self.player.setPosition(0)
                self.ui.songCurrentTimestampLabel.setText("00:00")
                self.ui.songTimeSlider.setSliderPosition(0)
            else:
                if widget_index == 9:
                    self.timer.singleShot(0, partial(self.add_shuffled_frames_to_queue,
                                                     self.shuffled_playlist_playing_song_index))
                self.shuffled_playlist_playing_song_index -= 2
                self.player.stop()

    def add_sorted_frames_to_queue(self, index):
        for i in self.sorted_current_playlist_songs_frames[index:]:
            self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(i)

    def add_shuffled_frames_to_queue(self, index):
        for i in self.shuffled_current_playlist_songs_frames[index:]:
            self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(i)

    def play_next_playlist_song(self):
        if self.ui.playerLoopButton.checkState() == 2:
            self.ui.playerLoopButton.setCheckState(QtCore.Qt.PartiallyChecked)
        self.player.stop()

    def shuffle(self):
        list_to_shuffle = [x for x in self.sorted_current_playlist_songs_frames if x != self.now_playing_song]
        self.shuffled_current_playlist_songs_frames = random.sample(list_to_shuffle, len(list_to_shuffle))
        self.shuffled_current_playlist_songs_frames.insert(0, self.now_playing_song)

    def shuffle_now_playing_playlist(self):
        if len(self.sorted_current_playlist_songs_frames) > 0:
            widget_index = self.ui.mainPageStackedWidget.currentIndex()
            sorted_list_current_song_index = self.sorted_current_playlist_songs_frames.index(self.now_playing_song)
            if self.ui.playerShuffleButton.isChecked():
                self.shuffled_current_playlist_songs_frames = []
                self.playlist_state = PlaylistState.SHUFFLED
                self.shuffle()
                self.shuffled_playlist_playing_song_index = 0
                while self.shuffled_current_playlist_songs_frames == self.sorted_current_playlist_songs_frames:
                    self.shuffle()
                if widget_index == 9:
                    for i in self.sorted_current_playlist_songs_frames[sorted_list_current_song_index + 1:]:
                        i.setParent(None)
                    for i in self.shuffled_current_playlist_songs_frames[1:]:
                        self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(i)
            else:
                shuffled_list_index = self.shuffled_current_playlist_songs_frames.index(self.now_playing_song)
                if widget_index == 9:
                    for i in self.shuffled_current_playlist_songs_frames[shuffled_list_index + 1:]:
                        i.setParent(None)
                    for i in self.sorted_current_playlist_songs_frames[sorted_list_current_song_index + 1:]:
                        self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(i)
                self.playlist_state = PlaylistState.SORTED
                self.sorted_playlist_playing_song_index = sorted_list_current_song_index

    def pause_play_button(self):
        if self.now_playing_song:
            if self.player.state() == self.player.PlayingState:
                self.now_playing_song.pushButton_13.setChecked(False)
                self.player.pause()
            elif self.player.state() == self.player.PausedState:
                self.now_playing_song.pushButton_13.setChecked(True)
                if self.player.position() != 0:
                    self.player.setPosition(self.player.position())
                self.player.play()

    def handle_state_changed(self, state):
        if state == self.player.PlayingState:
            self.now_playing_song.pushButton_13.setChecked(True)
            self.ui.playerPausePlayButton.setCheckable(True)
            self.ui.playerPausePlayButton.setChecked(True)
            if self.player.mediaStatus() == self.player.BufferedMedia:
                self.ui.songTimeSlider.setRepeatAction(
                    self.ui.songTimeSlider.SliderSingleStepAdd,
                    thresholdTime=0,
                    repeatTime=10)
            # print("PLAYING")
        elif state == self.player.StoppedState:
            # print("Finished song")
            self.ui.songTimeSlider.setSliderPosition(0)
            if self.ui.playerLoopButton.checkState() == 2:
                new_media = QMediaContent(QUrl.fromLocalFile(self.now_playing_song.path))
                self.player.setMedia(new_media)
                self.player.play()
            else:
                self.now_playing_song.pushButton_13.setChecked(False)
                widget_index = self.ui.mainPageStackedWidget.currentIndex()
                if widget_index == 9:
                    self.now_playing_song.setParent(None)
                self.now_playing_song = None
                self.ui.songTimeSlider.setRepeatAction(self.ui.songTimeSlider.SliderNoAction)
                self.ui.playerPausePlayButton.setChecked(False)
                self.ui.playerPausePlayButton.setCheckable(False)
                self.ui.songMaximumTimestampLabel.setText("00:00")
                if self.playlist_state == PlaylistState.SORTED and len(
                        self.sorted_current_playlist_songs_frames) > self.sorted_playlist_playing_song_index + 1 >= 0:
                    self.sorted_playlist_playing_song_index += 1
                    new_media = QMediaContent(QUrl.fromLocalFile(
                        self.sorted_current_playlist_songs_frames[self.sorted_playlist_playing_song_index].path))
                    self.now_playing_song = self.sorted_current_playlist_songs_frames[
                        self.sorted_playlist_playing_song_index]
                    if widget_index == 9:
                        self.ui.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(self.now_playing_song)
                    self.player.setVolume(self.ui.volumeSlider.value())
                    self.player.setMedia(new_media)
                    self.player.play()
                elif self.playlist_state == PlaylistState.SHUFFLED and len(
                        self.shuffled_current_playlist_songs_frames) > self.shuffled_playlist_playing_song_index + 1 >= 0:
                    self.shuffled_playlist_playing_song_index += 1
                    new_media = QMediaContent(QUrl.fromLocalFile(self.shuffled_current_playlist_songs_frames[
                                                                     self.shuffled_playlist_playing_song_index].path))
                    self.now_playing_song = self.shuffled_current_playlist_songs_frames[
                        self.shuffled_playlist_playing_song_index]
                    if widget_index == 9:
                        self.ui.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(self.now_playing_song)
                    self.player.setVolume(self.ui.volumeSlider.value())
                    self.player.setMedia(new_media)
                    self.player.play()
                elif self.ui.playerLoopButton.checkState() == 1:
                    if self.playlist_state == PlaylistState.SORTED:
                        self.sorted_playlist_playing_song_index = 0
                        new_media = QMediaContent(
                            QUrl.fromLocalFile(self.sorted_current_playlist_songs_frames[
                                                   self.sorted_playlist_playing_song_index].path))
                        self.now_playing_song = self.sorted_current_playlist_songs_frames[
                            self.sorted_playlist_playing_song_index]
                        if widget_index == 9:
                            self.ui.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(self.now_playing_song)
                            for i in self.sorted_current_playlist_songs_frames[1:]:
                                self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(i)
                        self.player.setVolume(self.ui.volumeSlider.value())
                        self.player.setMedia(new_media)
                        self.player.play()
                    elif self.playlist_state == PlaylistState.SHUFFLED:
                        self.shuffled_playlist_playing_song_index = 0
                        new_media = QMediaContent(
                            QUrl.fromLocalFile(self.shuffled_current_playlist_songs_frames[
                                                   self.shuffled_playlist_playing_song_index].path))
                        self.now_playing_song = self.shuffled_current_playlist_songs_frames[
                            self.shuffled_playlist_playing_song_index]
                        if widget_index == 9:
                            self.ui.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(self.now_playing_song)
                            for i in self.shuffled_current_playlist_songs_frames[1:]:
                                self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(i)
                        self.player.setVolume(self.ui.volumeSlider.value())
                        self.player.setMedia(new_media)
                        self.player.play()
                else:
                    pass
        elif state == self.player.PausedState:
            # print("PAUSED")
            self.now_playing_song.pushButton_13.setChecked(False)
            self.ui.playerPausePlayButton.setChecked(False)
            self.ui.songTimeSlider.setRepeatAction(self.ui.songTimeSlider.SliderNoAction)

    def handle_media_status_changed(self, status):
        # print(self.player.mediaStatus())
        if status == self.player.BufferedMedia:
            self.set_maximum_song_timestamp()

    def set_maximum_song_timestamp(self):
        self.song_duration = round(self.player.duration() / 1000, 2)
        song_duration_in_seconds = math.floor(self.song_duration)
        minutes_amount = int(song_duration_in_seconds / 60)
        seconds_amount = song_duration_in_seconds - minutes_amount * 60
        if song_duration_in_seconds >= 60:
            if minutes_amount >= 10:
                maximum_song_timestamp = f"{minutes_amount}:"
            else:
                maximum_song_timestamp = f"0{minutes_amount}:"
            if seconds_amount >= 10:
                maximum_song_timestamp += str(seconds_amount)
            else:
                maximum_song_timestamp += f"0{seconds_amount}"
        else:
            if seconds_amount >= 10:
                maximum_song_timestamp = f"00:{seconds_amount}"
            else:
                maximum_song_timestamp = f"00:0{seconds_amount}"
        self.ui.songMaximumTimestampLabel.setText(maximum_song_timestamp)
        self.ui.songTimeSlider.setMaximum(self.song_duration * 100)
        self.ui.songTimeSlider.setRepeatAction(
            self.ui.songTimeSlider.SliderSingleStepAdd,
            thresholdTime=0,
            repeatTime=10)

    def song_time_slider_pressed(self):
        self.player.pause()

    def song_time_slider_released(self):
        self.player.setPosition(self.ui.songTimeSlider.value() * 10)

    def song_time_slider_value_changed(self):
        if self.now_playing_song:
            new_value = math.floor(self.ui.songTimeSlider.value() / 100)
            if new_value != self.current_playing_song_second:
                self.current_playing_song_second = new_value
                minutes_amount = int(self.current_playing_song_second / 60)
                seconds_amount = self.current_playing_song_second - minutes_amount * 60
                if self.current_playing_song_second >= 60:
                    if minutes_amount >= 10:
                        current_song_timestamp = f"{minutes_amount}:"
                    else:
                        current_song_timestamp = f"0{minutes_amount}:"
                    if seconds_amount >= 10:
                        current_song_timestamp += str(seconds_amount)
                    else:
                        current_song_timestamp += f"0{seconds_amount}"
                else:
                    if seconds_amount >= 10:
                        current_song_timestamp = f"00:{seconds_amount}"
                    else:
                        current_song_timestamp = f"00:0{seconds_amount}"
                self.ui.songCurrentTimestampLabel.setText(current_song_timestamp)

    def volume_slider_value_changed(self):
        self.player.setVolume(self.ui.volumeSlider.value())

    def set_muted(self):
        if self.player.isMuted():
            self.player.setMuted(False)
        else:
            self.player.setMuted(True)

    """
    def play_pause_song(self, song_id):
        with local_database_app.app_context():
            song = Songs.query.filter_by(id=song_id).first()
        if song.is_playing:
            song.is_playing = False
            if self.now_playing_song and song.id == self.now_playing_song.song_id:
                self.now_playing_song.setParent(None)
                self.now_playing_song = None
                if len(self.songs_in_queue) > 0:
                    self.now_playing_song = self.songs_in_queue[0]
                    self.ui.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(self.songs_in_queue[0])
                    self.songs_in_queue.remove(self.songs_in_queue[0])
            else:
                for i in self.songs_in_queue:
                    if i.song_id == song.id:
                        i.setParent(None)
                        self.songs_in_queue.remove(i)
        else:
            song.is_playing = True
            with local_database_app.app_context():
                last_played_songs = LastPlayedSongs.query.all()
            last_played_songs_ids = []
            record_to_remove = None
            for i in last_played_songs:
                if i.song_id == song_id:
                    record_to_remove = i
                last_played_songs_ids.append(i.song_id)
            if last_played_songs_ids[-1] != song_id:
                song_to_add = LastPlayedSongs(song=song)
                if len(last_played_songs_ids) > 0:
                    if song_id in last_played_songs_ids:
                        db.session.delete(record_to_remove)
                        db.session.add(song_to_add)
                    else:
                        db.session.add(song_to_add)
                else:
                    db.session.add(song_to_add)
            else:
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_id=song.id,
                song_title=song.title,
                date_added=song.date_added,
                song_length=song.length,
                is_liked=is_liked,
                is_playing=song.is_playing
            )
            if not self.now_playing_song:
                self.now_playing_song = song_frame
                self.ui.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(song_frame)
            else:
                self.songs_in_queue.append(song_frame)
                self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(song_frame)
            song_frame.pushButton_30.clicked.connect(partial(self.like_song, song.id))
            song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
        db.session.commit()
"""
    """


            with local_database_app.app_context():
                last_played_songs = LastPlayedSongs.query.all()
            last_played_songs_ids = []
            record_to_remove = None
            for i in last_played_songs:
                if i.song_id == song_id:
                    record_to_remove = i
                last_played_songs_ids.append(i.song_id)
            if last_played_songs_ids[-1] != song_id:
                song_to_add = LastPlayedSongs(song=song)
                if len(last_played_songs_ids) > 0:
                    if song_id in last_played_songs_ids:
                        db.session.delete(record_to_remove)
                        db.session.add(song_to_add)
                    else:
                        db.session.add(song_to_add)
                else:
                    db.session.add(song_to_add)
            else:
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_id=song.id,
                song_title=song.title,
                date_added=song.date_added,
                song_length=song.length,
                is_liked=is_liked,
                is_playing=song.is_playing
            )
            if not self.now_playing_song:
                self.now_playing_song = song_frame
                self.ui.mainPageSongQueueNowPlayingSongQVBoxLayout.addWidget(song_frame)
            else:
                self.songs_in_queue.append(song_frame)
                self.ui.mainPageSongQueueSongListQVBoxLayout.addWidget(song_frame)
            song_frame.pushButton_30.clicked.connect(partial(self.like_song, song.id))
            song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
        db.session.commit()
"""

    def change_widget_category_songs(self):
        self.set_category_page_stacked_widget_index(0)

    def change_widget_category_albums(self):
        self.set_category_page_stacked_widget_index(1)

    def change_widget_category_playlists(self):
        self.set_category_page_stacked_widget_index(2)

    def change_widget_author_songs(self):
        self.set_author_page_stacked_widget_index(0)

    def change_widget_author_albums(self):
        self.set_author_page_stacked_widget_index(1)

    def change_widget_author_playlists(self):
        self.set_author_page_stacked_widget_index(2)

    def handle_dialog_rejection(self, app_layer_frame, dialog):
        """Call dialog's reject() method and app_layer_frame's deleteLater() to remove both from the screen.

        Parameters:
            app_layer_frame (ClickedSignalQFrame): Frame that gets shown over whole app when dialog is created.
            dialog (QtWidgets.QDialog): Dialog that was shown along app_layer_frame.
        """
        dialog.reject()
        app_layer_frame.deleteLater()

    # TODO Refactor this function
    def album_adder_clicked_slot(self):
        """Create new AlbumInputDialog and run its show() method, run handle_new_album_creation() to validate
         and create new album.

        """

        # Create a blacked-out semi-transparent frame over the entire app
        # This frame is set up to close the dialog and itself when clicked
        app_layer_frame = ClickedSignalQFrame(self.ui.centralwidget)
        # Create an instance of the albumInputDialog class
        album_input_dialog = albumInputDialog(parent=self.ui.window)

        # Query local database for all authors
        with local_database_app.app_context():
            all_authors = Authors.query.all()
            all_categories = MusicCategories.query.all()
        # Insert all authors into album's author selection QComboBox
        for author in all_authors:
            album_input_dialog.albumInputDialogAuthorQComboBox.addItem(f"{author.author_name}")
        for category in all_categories:
            album_input_dialog.albumInputDialogCategoryQComboBox.addItem(f"{category.category_name}")

        # Connect buttons
        # Create and handle dialog's miniature selection dialog
        miniature_file_dialog = self.handle_and_connect_new_miniature_file_dialog(album_input_dialog.albumInputDialogMiniatureQToolButton, album_input_dialog)
        # App layer frame's clicked slot
        app_layer_frame.clicked.connect(partial(self.handle_dialog_rejection, app_layer_frame, album_input_dialog))
        # Dialog's exit button clicked slot
        album_input_dialog.albumInputDialogExitButton.clicked.connect(partial(self.handle_dialog_rejection, app_layer_frame, album_input_dialog))
        # Dialog's add button clicked slot
        album_input_dialog.albumInputDialogAddButton.clicked.connect(partial(self.handle_new_album_creation, album_input_dialog, miniature_file_dialog, app_layer_frame, all_authors, all_categories))

        # Show app layer_frame and dialog on the screen
        app_layer_frame.show()
        album_input_dialog.show()

    def handle_new_album_creation(self, album_dialog, album_miniature_dialog, app_layer_frame, all_authors, all_categories):
        """Handle new album creation. Collect input from album_dialog and miniature_file_dialog then create new
            album.

            Parameters:
                app_layer_frame (QtWidgets.QFrame): blacked-out frame behind dialog that it being shown behind it.
                album_dialog (albumInputDialog): albumInputDialog used to collect data to create album from.
                album_miniature_dialog (QtWidgets.QFileDialog): QFileDialog used to collect miniature for the new album.
                all_authors (list): list of all authors contained in the database.
                all_categories (list): list of all categories contained in the database.
        """

        # Obtain name of the new album
        new_album_name = album_dialog.albumInputDialogAlbumNameQLineEdit.text()

        # Select proper category for the new album
        # Subtracting 1 because there is "No category" item at index 0
        new_album_category = all_categories[album_dialog.albumInputDialogCategoryQComboBox.currentIndex() - 1]

        # Select proper author for the new album
        # Subtracting 1 because there is "No author" item at index 0
        new_album_author = all_authors[album_dialog.albumInputDialogAuthorQComboBox.currentIndex() - 1]

        # Create new album item with data provided by user
        new_album = Albums(album_name=new_album_name, category_id=new_album_category.id, author_id=new_album_author.id)
        
        with local_database_app.app_context():
            db.session.add(new_album)
            db.session.commit()
        
        print("Created new album in database.")
        self.handle_dialog_acceptation(app_layer_frame, album_dialog)

    def handle_and_connect_new_miniature_file_dialog(self, clickable_widget, dialog):
        """Create new QFileDialog, connect clickable_widget clicked signal with QFileDialog exec_ method and return it.

        Parameters:
            dialog: Dialog window used to set miniature preview after selection
            clickable_widget: Widget with clicked method to connect with QFileDialog exec method.

        """
        # Create miniature QFileDialog and connect clickable_widget's clicked method to handle_miniature_selection()
        file_dialog = QtWidgets.QFileDialog()
        clickable_widget.clicked.connect(partial(self.handle_miniature_selection, file_dialog, dialog))
        return file_dialog

    def handle_miniature_selection(self, file_dialog, dialog):
        """Wait for file_dialog to exit and set selected file url as dialog's miniature preview."""
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        url = file_dialog.getOpenFileUrl(parent=self.ui.window, filter="*.bmp *.jpg *.jpeg *.png *.ppm *.xbm *.xpm")
        if not url[0].isEmpty():
            dialog.set_dialogs_miniature_preview_pixmap(url[0])

    def author_adder_clicked_slot(self):
        """Create new authorInputDialog and run its show() method, run handle_new_author_creation() to validate
                 and create new author.

        """

        # Blacked out semi-transparent frame over whole app, closes dialog when clicked
        app_layer_frame = ClickedSignalQFrame(self.ui.centralwidget)
        author_input_dialog = authorInputDialog(parent=self.ui.window)

        # Dialog's exit button clicked slot
        author_input_dialog.authorInputDialogExitButton.clicked.connect(partial(self.handle_dialog_rejection,
                                                                                app_layer_frame, author_input_dialog))

        # App layer frame's clicked slot
        app_layer_frame.clicked.connect(partial(self.handle_dialog_rejection, app_layer_frame, author_input_dialog))

        # Show app layer_frame and dialog on the screen
        app_layer_frame.show()
        author_input_dialog.show()

        # Create and handle dialog's miniature selection dialog
        miniature_file_dialog = self.handle_and_connect_new_miniature_file_dialog(
            author_input_dialog.authorInputDialogMiniatureQToolButton, author_input_dialog)

        # Dialog's add button clicked slot
        author_input_dialog.authorInputDialogAddButton.clicked.connect(
            partial(self.handle_new_author_creation, author_input_dialog, miniature_file_dialog, app_layer_frame))

    def handle_new_author_creation(self, author_dialog, author_miniature_dialog, app_layer_frame):
        """Handle new author creation. Collect input from author_dialog and miniature_file_dialog then create new
            author.

            Parameters:
                app_layer_frame (QtWidgets.QFrame): blacked-out QFrame behind dialog that it shown along it.
                author_dialog (authorInputDialog): authorInputDialog used to collect data to create author
                 from.
                author_miniature_dialog (QtWidgets.QFileDialog): QFileDialog used to collect miniature for the new
                 author.
        """
        print(f"Handling author creation...\n"
              f"---------------------------------------------------------------------------------------\n"
              f"Author_miniature_dialog files: {author_miniature_dialog.selectedFiles()}\n"
              f"Author name: {author_dialog.authorInputDialogAuthorNameQLineEdit.text()}\n"
              f"---------------------------------------------------------------------------------------")

        new_author_name = author_dialog.authorInputDialogAuthorNameQLineEdit.text()

        # TODO Add miniature handling to author
        # TODO Add inputs validation and errors
        new_author = Authors(
            author_name=new_author_name,
        )
        with local_database_app.app_context():
            db.session.add(new_author)
            db.session.commit()

        print("Created new author in database.")
        self.handle_dialog_acceptation(app_layer_frame, author_dialog)

    def get_user_data(self):
        with local_database_app.app_context():
            user = User.query.first()
        if user:
            self.user_data = {"token": user.token.strip(), "hashed_name": user.hashed_name}

    def register(self):
        email = self.ui.centralPageRegisterPageEmailQLineEdit.text()
        password = self.ui.centralPageRegisterPagePasswordQLineEdit.text()
        username = self.ui.centralPageRegisterPageNicknameQLineEdit.text()
        data = {'email': email, "username": username, "password": password}
        response = requests.post('http://127.0.0.1:5000/register', data=data).json()
        if response["error"] == "1":
            print(response["message"])
            self.ui.centralStackedWidget.setCurrentIndex(1)
        else:
            print(response["message"])

    def load_register_page(self):
        self.ui.centralStackedWidget.setCurrentIndex(2)

    def load_login_page(self):
        self.ui.centralStackedWidget.setCurrentIndex(1)

    def log_in_with_credentials(self):
        email = self.ui.centralPageLoginPageLoginQLineEdit.text()
        password = self.ui.centralPageLoginPagePasswordQLineEdit.text()
        data = {'email': email, 'password': password}
        response = requests.post('http://127.0.0.1:5000/login', data=data).json()
        if response["error"] == "1":
            token = response["token"]
            user_hashed_name = response["hashed_name"]
            self.user_data = {"token": token.strip(), "hashed_name": user_hashed_name}
            user = User(
                token=token,
                hashed_name=user_hashed_name
            )
            with local_database_app.app_context():
                db.session.add(user)
                db.session.commit()
            print(response["message"])
            self.ui.centralStackedWidget.setCurrentIndex(0)
        else:
            print(response["message"])

    def log_in_with_token(self):
        if self.user_data:
            response = requests.post('http://127.0.0.1:5000/login_t', data=self.user_data).json()
            if response["error"] == "1":
                self.ui.centralStackedWidget.setCurrentIndex(0)
                print(response["message"])
            else:
                with local_database_app.app_context():
                    User.query.delete()
                print(response["message"])
        else:
            self.ui.centralStackedWidget.setCurrentIndex(1)

    def continue_as_guest(self):
        self.ui.centralStackedWidget.setCurrentIndex(0)

    def log_out(self):
        if self.user_data:
            response = requests.post('http://127.0.0.1:5000/logout', data=self.user_data).json()
            print(response["message"])
            with local_database_app.app_context():
                User.query.delete()
            db.session.commit()
            self.user_data = None
            self.ui.centralStackedWidget.setCurrentIndex(1)
        else:
            self.ui.centralStackedWidget.setCurrentIndex(1)

    def create_playlist_button_slot(self):
        """Create new playlistInputDialog and run its show() method, run handle_new_playlist_creation() to validate
         and create new playlist.

        """
        # Blacked out semi-transparent frame over whole app, closes dialog when clicked
        app_layer_frame = ClickedSignalQFrame(self.ui.centralwidget)
        playlist_input_dialog = playlistInputDialog(parent=self.ui.window)

        # Dialog's exit button clicked slot
        playlist_input_dialog.playlistInputDialogExitButton.clicked.connect(partial(self.handle_dialog_rejection,
                                                                                    app_layer_frame,
                                                                                    playlist_input_dialog))

        # App layer frame's clicked slot
        app_layer_frame.clicked.connect(partial(self.handle_dialog_rejection, app_layer_frame, playlist_input_dialog))

        # Show app layer_frame and dialog on the screen
        app_layer_frame.show()
        playlist_input_dialog.show()

        # Create and handle dialog's miniature selection dialog
        miniature_file_dialog = self.handle_and_connect_new_miniature_file_dialog(
            playlist_input_dialog.playlistInputDialogMiniatureQToolButton, playlist_input_dialog)

        # Dialog's add button clicked slot
        playlist_input_dialog.playlistInputDialogAddButton.clicked.connect(
            partial(self.handle_new_playlist_creation, playlist_input_dialog, miniature_file_dialog, app_layer_frame))

    def handle_new_playlist_creation(self, playlist_dialog, playlist_miniature_dialog, app_layer_frame):
        """Handle new playlist creation. Collect input from playlist_dialog and miniature_file_dialog then create new
            playlist.

            Parameters:
                app_layer_frame (QtWidgets.QFrame): blacked-out frame behind dialog that it shown along it.
                playlist_dialog (playlistInputDialog): playlistInputDialog used to collect data to create playlist from.
                playlist_miniature_dialog (QtWidgets.QFileDialog): QFileDialog used to collect miniature for the new
                 playlist.
        """
        print(f"Handling playlist creation...\n"
              f"---------------------------------------------------------------------------------------\n"
              f"Playlist_miniature_dialog files: {playlist_miniature_dialog.selectedFiles()}\n"
              f"Playlist name: {playlist_dialog.playlistInputDialogPlaylistNameQLineEdit.text()}\n"
              f"Playlist category: {playlist_dialog.playlistInputDialogCategoryQComboBox.currentText()}\n"
              f"---------------------------------------------------------------------------------------")
        # handle adding new playlist to database here.
        print("Created new playlist in database.")
        # close dialog
        self.handle_dialog_acceptation(app_layer_frame, playlist_dialog)

    def all_songs_button_slot(self):
        self.set_main_page_stacked_widget_index(11)

    @staticmethod
    def handle_new_file_dialog():
        """Create new QFileDialog and return it."""
        file_dialog = QtWidgets.QFileDialog()
        return file_dialog

    def handle_song_adder_inputs(self):
        """Connect SongAdder's song and miniature QFileDialogs and addSong button."""
        song_file_dialog = self.handle_new_file_dialog()
        self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSelectSongQPushButton.clicked.connect(
            song_file_dialog.exec_)

        miniature_file_dialog = self.handle_new_file_dialog()
        self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSelectSongMiniatureQPushButton.clicked.connect(
            miniature_file_dialog.exec_)

        self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongAddSongQPushButton.clicked.connect(partial(
            self.handle_new_song_creation, song_file_dialog, miniature_file_dialog))

    def handle_new_song_creation(self, song_file_dialog, miniature_file_dialog):
        """Handle new song creation. Collect input from song_file_dialog, miniature_file_dialog and SongAdder's QLineEdits
        and QComboBoxes then create new song.

        Parameters:
            song_file_dialog(QtWidgets.QFileDialog): QFileDialog used to collect song file info from.
            miniature_file_dialog(QtWidgets.QFileDialog): QFileDialog used to collect song miniature info from.

        """
        print(f"Handling song creation...\n"
              f"---------------------------------------------------------------------------------------\n"
              f"Song_file_dialog files: {song_file_dialog.selectedFiles()}\n"
              f"Miniature_file_dialog files: {miniature_file_dialog.selectedFiles()}\n"
              f"Song name: {self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSongTitleQLineEdit.text()}\n"
              f"Song author: {self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSongAuthorQComboBox.currentText()}\n"
              f"Song category: {self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSongCategoryQComboBox.currentText()}\n"
              f"Song album: {self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSongAlbumQComboBox.currentText()}\n"
              f"---------------------------------------------------------------------------------------")
        # handle adding new song to database here

        songTitle = self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSongTitleQLineEdit.text()
        songAuthor = self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSongAuthorQComboBox.currentText()
        songCategory = self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSongCategoryQComboBox.currentText()
        songAlbum = self.ui.mainPageAllSongsSongAdderQFrame.mainPageAllSongsSongAlbumQComboBox.currentText()

        newSong = Songs(
            title=songTitle,
            author_id=songAuthor,
            category_id=songCategory,
            album_id=songAlbum,
        )

        print("Created new song in database.")

    def synchronize_button_clicked_slot(self):
        """Create new synchronizeDialog and run its show() method, create app_layer_frame to darken the background then
         run handle_synchronization() to upload and download data.

        """

        # Blacked out semi-transparent frame over whole app, closes dialog when clicked
        app_layer_frame = ClickedSignalQFrame(self.ui.centralwidget)
        synchronize_dialog = synchronizeDialog(parent=self.ui.window)

        # Dialog's exit button clicked slot
        synchronize_dialog.synchronizeDialogExitButton.clicked.connect(partial(self.handle_dialog_rejection,
                                                                               app_layer_frame, synchronize_dialog))

        # App layer frame's clicked slot
        app_layer_frame.clicked.connect(partial(self.handle_dialog_rejection, app_layer_frame, synchronize_dialog))

        # Show app layer_frame and dialog on the screen
        app_layer_frame.show()
        synchronize_dialog.show()

        # Dialog's add button clicked slot
        synchronize_dialog.synchronizeDialogSynchronizeButton.clicked.connect(
            partial(self.handle_synchronization, synchronize_dialog, app_layer_frame))

    def handle_synchronization(self, synchronize_dialog, app_layer_frame):
        """Handle data synchronization with server. Collect input from synchronize_dialog then download/upload data.
        Use get_selected_synchronization_data to search for data to synchronize.

        Parameters:
            app_layer_frame (QtWidgets.QFrame): blacked-out frame behind dialog that is shown along it.
            synchronize_dialog (synchronizeDialog): synchronizeDialog used to collect info about data to download/upload.
        """
        print(f"Handling data synchronization...\n"
              f"---------------------------------------------------------------------------------------\n"
              f"Songs to download:\n"
              f"{self.get_selected_synchronization_data(synchronize_dialog.synchronizeDialogDownloadSongsQWidget.children())}\n"
              f"Songs to upload:\n"
              f"{self.get_selected_synchronization_data(synchronize_dialog.synchronizeDialogUploadSongsQWidget.children())}\n"
              f"Albums to download:\n"
              f"{self.get_selected_synchronization_data(synchronize_dialog.synchronizeDialogDownloadAlbumsQWidget.children())}\n"
              f"Albums to upload:\n"
              f"{self.get_selected_synchronization_data(synchronize_dialog.synchronizeDialogUploadAlbumsQWidget.children())}\n"
              f"Playlists to download:\n"
              f"{self.get_selected_synchronization_data(synchronize_dialog.synchronizeDialogDownloadPlaylistsQWidget.children())}\n"
              f"Playlists to upload:\n"
              f"{self.get_selected_synchronization_data(synchronize_dialog.synchronizeDialogUploadPlaylistsQWidget.children())}\n"
              f"Authors to download:\n"
              f"{self.get_selected_synchronization_data(synchronize_dialog.synchronizeDialogUploadAuthorsQWidget.children())}\n"
              f"Authors to upload:\n"
              f"{self.get_selected_synchronization_data(synchronize_dialog.synchronizeDialogDownloadAuthorsQWidget.children())}\n"
              f"---------------------------------------------------------------------------------------")
        # handle data synchronization here
        print("Synchronized data.")

        # close dialog
        self.handle_dialog_acceptation(app_layer_frame, synchronize_dialog)

    @staticmethod
    def get_selected_synchronization_data(data_set):
        """Search the data_set for checked buttons. Get the data selected for synchronization.

        Parameters:
            data_set(list): list of data to select items to synchronize from

        Returns:
            list: Data to synchronize selected from data_set
        """
        # Create empty list to store data that should be synchronized
        data_to_synchronize = []
        # Search the data_set for checked QPushButtons and append them to data_to_synchronize
        for data in data_set:
            if isinstance(data, QtWidgets.QPushButton):
                if data.isChecked():
                    data_to_synchronize.append(data)

        return data_to_synchronize

    def toggle_login_page_password_echo_mode(self):
        """Toggle centralPageLoginPage password's echo mode"""
        if self.ui.centralPageLoginPagePasswordQLineEdit.echoMode() == QtWidgets.QLineEdit.Password:
            self.ui.centralPageLoginPagePasswordQLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.centralPageLoginPagePasswordQLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def toggle_register_page_password_echo_mode(self):
        """Toggle centralPageRegisterPage password's echo mode"""
        if self.ui.centralPageRegisterPagePasswordQLineEdit.echoMode() == QtWidgets.QLineEdit.Password:
            self.ui.centralPageRegisterPagePasswordQLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.centralPageRegisterPagePasswordQLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def set_main_page_stacked_widget_index(self, index):
        """Set mainPageStackedWidget's index, adjust stickySortButtonsFrame visibility

           Parameters:
               index(int): index to set mainPageStackedWidget's index to

        """
        # change index immediately to make all elements on page have isVisible set to true to prevent issues such as
        # trying to set visibility of element that is not present on the screen
        self.ui.mainPageStackedWidget.setCurrentIndex(index)

        # set all custom and native scrollbars to value 0 when changing page to prevent issues with navbar saturation
        self.reset_all_custom_and_native_scrollbars()

        # adjust all sortButtonFrames elements visibility when changing page
        self.ui.adjust_all_sort_button_frames_visibility()
        # author page, calls set_author_page_stacked_widget_index to always set mainPageAuthorPageStackedWidget's index
        # to 0 in order to not have to track which Widget is visible and adjusting stickySortButtonFrame visibility
        if index == 6:
            self.ui.mainPageAuthorSongsButton.setChecked(True)
            self.set_author_page_stacked_widget_index(0)
        # category, calls set_author_page_stacked_widget_index to always set mainPageCategoryPageStackedWidget's index
        # to 0 in order to not have to track which Widget is visible and adjusting stickySortButtonFrame visibility
        elif index == 7:
            self.ui.mainPageCategorySongsButton.setChecked(True)
            self.set_category_page_stacked_widget_index(0)
        # adjust fixedNavbar's sticky sort button frame height and visibility accordingly to each page
        self.ui.fixedNavbar.adjust_sticky_sort_button_frame(index)

    def set_author_page_stacked_widget_index(self, index):
        """Set mainPageAuthorsPageStackedWidget's index, adjust stickySortButtonsFrame visibility

                   Parameters:
                       index(int): index to set mainPageAuthorsPageStackedWidget's index to

                """
        self.ui.fixedNavbar.adjust_authors_page_sticky_sort_button_frame(index)
        self.ui.mainPageAuthorPageStackedWidget.setCurrentIndex(index)
        self.reset_all_custom_and_native_scrollbars()

    def set_category_page_stacked_widget_index(self, index):
        """Set mainPageCategoryPageStackedWidget's index, adjust stickySortButtonsFrame visibility

                   Parameters:
                       index(int): index to set mainPageCategoryPageStackedWidget's index to

                """
        self.ui.fixedNavbar.adjust_category_page_sticky_sort_button_frame(index)
        self.ui.mainPageCategoryPageStackedWidget.setCurrentIndex(index)
        self.reset_all_custom_and_native_scrollbars()

    def reset_all_custom_and_native_scrollbars(self):
        """Reset all custom and native vertical scrollbars to value 0."""
        for scrollbar in self.ui.custom_scrollbars_list:
            scrollbar.triggerAction(QtWidgets.QAbstractSlider.SliderToMinimum)
            scrollbar.setValue(0)
        for native_scrollbar in self.ui.native_vertical_scrollbar_list:
            native_scrollbar.setValue(0)
