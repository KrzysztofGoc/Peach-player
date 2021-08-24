from functools import partial
from PySide6 import QtCore, QtWidgets, QtGui
from app.src.classes import navbar_frame
from app_model import *
import requests
from classes.category_entry import CategoryEntry
from tkinter.filedialog import askopenfilename
import os
import shutil
import io
import zipfile
from functools import partial
from classes.song_entry import SongEntry
from classes.album_entry import AlbumEntry
from classes.category_entry import CategoryEntry
from classes.playlist_entry import PlaylistEntry
from classes.adder_entry import AdderEntry
from classes.author_entry import AuthorEntry


scrollbar_recently_used = False


class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.connect_signals_with_slots()
        self.category_frames = []
        self.loaded_liked_songs = []
        self.loaded_songs = []
        self.loaded_album_page_songs = []
        self.loaded_albums = []
        self.loaded_playlists = []
        self.loaded_selected_author_songs = []
        self.loaded_selected_author_albums = []
        self.loaded_selected_author_playlists = []
        self.loaded_playlist_page_songs = []
        self.user_data = None
        self.get_user_data()
        self.log_in_with_token()
        self.load_playlist_frames()
        self.turn_off_playing_songs()

    def connect_signals_with_slots(self):
        """Connects Ui's widgets with respective slots"""

        self.ui.mainPageNowPlaying.resized.connect(self.main_page_now_playing_resize_slot)
        self.ui.mainPageStackedWidget.resized.connect(self.main_page_stacked_widget_resize_slot)

        # Buttons' slots
        self.ui.nowPlayingButton.clicked.connect(self.now_playing_button_slot)
        self.ui.miniPlayerButton.clicked.connect(self.mini_player_button_slot)
        self.ui.categoriesButton.clicked.connect(self.categories_button_slot)
        self.ui.leftMenuLikedSongsButton.clicked.connect(self.liked_songs_button_slot)
        self.ui.leftMenuLastPlayedButton.clicked.connect(self.last_played_button_slot)
        self.ui.leftMenuAuthorsButton.clicked.connect(self.authors_button_slot)
        self.ui.leftMenuAlbumsButton.clicked.connect(self.albums_button_slot)
        self.ui.bottomPlayerQueueButton.clicked.connect(self.queue_button_slot)
        self.ui.pushButton_3.clicked.connect(self.log_in_with_credentials)
        self.ui.pushButton_5.clicked.connect(self.continue_as_guest)
        self.ui.pushButton_50.clicked.connect(self.register)
        self.ui.pushButton_53.clicked.connect(self.load_register_page)
        self.ui.fixedNavbar.navbarUsernameButton.clicked.connect(self.log_out)
        self.ui.mainPageCategorySongsButton.clicked.connect(self.change_widget_category_songs)
        self.ui.mainPageCategoryAlbumsButton.clicked.connect(self.change_widget_category_albums)
        self.ui.mainPageCategoryPlaylistsButton.clicked.connect(self.change_widget_category_playlists)
        self.ui.mainPageAuthorSongsButton.clicked.connect(self.change_widget_author_songs)
        self.ui.mainPageAuthorPlaylistsButton.clicked.connect(self.change_widget_author_playlists)
        self.ui.mainPageAuthorAlbumsButton.clicked.connect(self.change_widget_author_albums)
        # Sort buttons' slots
        self.ui.mainPageLikedSongsSortButtonsQButtonGroup.buttonClicked.connect(
            self.liked_songs_sort_buttons_qbuttongroup_slot)
        self.ui.mainPagePlaylistSortButtonsQButtonGroup.buttonClicked.connect(
            self.playlist_sort_buttons_qbuttongroup_slot)
        self.ui.mainPageAuthorPageSortButtonsQButtonGroup.buttonClicked.connect(
            self.author_page_sort_buttons_qbuttongroup_slot)
        self.ui.mainPageCategorySortButtonsQButtonGroup.buttonClicked.connect(
            self.category_page_sort_buttons_qbuttongroup_slot)

        # Sliders' slots
        self.ui.mainPageCategoriesScroll.valueChanged.connect(self.categories_scroll_value_changed_slot)
        self.ui.scrollArea_9.verticalScrollBar().valueChanged.connect(
            self.categories_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_9.verticalScrollBar().rangeChanged.connect(
            self.categories_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_9.resized.connect(self.categories_scroll_area_resize_slot)

        self.ui.mainPageLikedSongsScroll.valueChanged.connect(self.liked_songs_scroll_value_changed_slot)
        self.ui.scrollArea_4.verticalScrollBar().valueChanged.connect(
            self.liked_songs_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_4.verticalScrollBar().rangeChanged.connect(
            self.liked_songs_scroll_area_scrollbar_range_changed)
        self.ui.scrollArea_4.resized.connect(self.liked_songs_scroll_area_resize_slot)

        self.ui.mainPageLastPlayedScroll.valueChanged.connect(self.last_played_scroll_value_changed_slot)
        self.ui.scrollArea_10.verticalScrollBar().valueChanged.connect(
            self.last_played_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_10.verticalScrollBar().rangeChanged.connect(
            self.last_played_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_10.resized.connect(self.last_played_scroll_area_resize_slot)

        self.ui.mainPagePlaylistScroll.valueChanged.connect(self.playlist_scroll_value_changed_slot)
        self.ui.scrollArea_3.verticalScrollBar().valueChanged.connect(
            self.playlist_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_3.verticalScrollBar().rangeChanged.connect(
            self.playlist_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_3.resized.connect(self.playlist_scroll_area_resize_slot)

        self.ui.mainPageAuthorPageScroll.valueChanged.connect(self.author_page_scroll_value_changed_slot)
        self.ui.scrollArea_8.verticalScrollBar().valueChanged.connect(
            self.author_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_8.verticalScrollBar().rangeChanged.connect(
            self.author_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_8.resized.connect(self.author_page_scroll_area_resize_slot)

        self.ui.mainPageAuthorsScroll.valueChanged.connect(self.authors_scroll_value_changed_slot)
        self.ui.scrollArea_7.verticalScrollBar().valueChanged.connect(
            self.authors_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_7.verticalScrollBar().rangeChanged.connect(
            self.authors_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_7.resized.connect(self.authors_scroll_area_resize_slot)

        self.ui.mainPageCategoryPageScroll.valueChanged.connect(self.category_page_scroll_value_changed_slot)
        self.ui.scrollArea_11.verticalScrollBar().valueChanged.connect(
            self.category_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_11.verticalScrollBar().rangeChanged.connect(
            self.category_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_11.resized.connect(self.category_page_scroll_area_resize_slot)

        self.ui.mainPageAlbumPageScroll.valueChanged.connect(self.album_page_scroll_value_changed_slot)
        self.ui.scrollArea_5.verticalScrollBar().valueChanged.connect(
            self.album_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_5.verticalScrollBar().rangeChanged.connect(
            self.album_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_5.resized.connect(self.album_page_scroll_area_resize_slot)

        self.ui.mainPageSongQueuePageScroll.valueChanged.connect(self.song_queue_page_scroll_value_changed_slot)
        self.ui.scrollArea_12.verticalScrollBar().valueChanged.connect(
            self.song_queue_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_12.verticalScrollBar().rangeChanged.connect(
            self.song_queue_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_12.resized.connect(self.song_queue_page_scroll_area_resize_slot)

        self.ui.mainPageAlbumsPageScroll.valueChanged.connect(self.albums_page_scroll_value_changed_slot)
        self.ui.scrollArea_13.verticalScrollBar().valueChanged.connect(
            self.albums_page_scroll_area_scrollbar_value_changed_slot)
        self.ui.scrollArea_13.verticalScrollBar().rangeChanged.connect(
            self.albums_page_scroll_area_scrollbar_range_changed_slot)
        self.ui.scrollArea_13.resized.connect(self.albums_page_scroll_area_resize_slot)

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
            scrollbar_recently_used = False

    def albums_page_scroll_value_changed_slot(self):
        """Change albums' page scrollArea's scrollbar's value to match albums' page custom scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
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
            scrollbar_recently_used = False

    def song_queue_page_scroll_value_changed_slot(self):
        """Change songQueue's page scrollArea's scrollbar's value to match songQueue's page custom scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
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
            scrollbar_recently_used = False

    def album_page_scroll_value_changed_slot(self):
        """Change album's page scrollArea's scrollbar's value to match album's page custom scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
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
            scrollbar_recently_used = False

    def category_page_scroll_value_changed_slot(self):
        """Change category's page scrollArea's scrollbar's value to match category's page custom scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
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
            scrollbar_recently_used = False

    def author_page_scroll_value_changed_slot(self):
        """Change author's page scrollArea's scrollbar's value to match author's page custom scrollbar's value.

        Uses global scrollbar_recently_used to prevent custom and scrollArea's scrollbars going into loop.
        """
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
            scrollbar_recently_used = False

    def playlist_scroll_value_changed_slot(self):
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
            scrollbar_recently_used = False

    def authors_scroll_value_changed_slot(self):
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
            scrollbar_recently_used = False

    def last_played_scroll_value_changed_slot(self):
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
            scrollbar_recently_used = False

    def liked_songs_scroll_value_changed_slot(self):
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
            scrollbar_recently_used = False

    def categories_scroll_value_changed_slot(self):
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

    def queue_button_slot(self):
        """Prepare authors page and change mainPageStackedWidget to authors's index"""
        self.setup_main_page_queue()
        self.ui.set_main_page_stacked_widget_index(9)

    def albums_button_slot(self):
        """Prepare albums page and change mainPageStackedWidget to album's index"""
        self.setup_main_page_albums()
        self.ui.set_main_page_stacked_widget_index(10)
        all_albums = Albums.query.all()
        row = column = 0
        for album in all_albums:
            if column % 8 == 0:
                row += 1
                column = 0
            album_frame = AlbumEntry(self.ui.frame_265, album_name=album.album_name)
            album_frame.clicked.connect(partial(self.load_album_page, album))
            self.ui.mainPageAlbumsAlbumsGridQGridLayout.addWidget(album_frame, row, column, 1, 1)
            column += 1
        if column % 8 == 0:
            row += 1
            column = 0
        album_adder = AdderEntry(adder_type=2, parent=self.ui.frame_265)
        album_adder.clicked.connect(self.add_new_album)
        self.ui.mainPageAlbumsAlbumsGridQGridLayout.addWidget(album_adder, row, column, 1, 1)

    def load_album_page(self, album):
        if len(self.loaded_album_page_songs) != 0:
            for i in self.loaded_album_page_songs:
                i.setParent(None)
            self.loaded_album_page_songs = []
        self.ui.set_main_page_stacked_widget_index(8)
        self.ui.mainPageAlbumNameOfAlbumLabel.setText(album.album_name)
        songs = AlbumSongs.query.filter_by(album_id=album.id).all()
        for i in songs:
            song = Songs.query.filter_by(id=i.song_id).first()
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_title=song.title,
                artist_name=song.author.author_name,
                date_added=None,
                is_liked=is_liked
            )
            self.ui.mainPageAlbumSongsListQVBoxLayout.addWidget(song_frame)
            song_frame.pushButton_30.clicked.connect(partial(self.like_song, song.id))
            song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
            song_frame.mainPageLikedSongsArtistButton.clicked.connect(partial(self.load_author_page, song.author))
            self.loaded_album_page_songs.append(song_frame)

    def authors_button_slot(self):
        """Prepare authors page and change mainPageStackedWidget to authors's index"""
        self.setup_main_page_authors()
        self.ui.set_main_page_stacked_widget_index(4)
        all_authors = Authors.query.all()
        row = column = 0
        for author in all_authors:
            if column % 8 == 0:
                row += 1
                column = 0
            author_frame = AuthorEntry(self.ui.mainPageAuthorsGrid, author_name=author.author_name)
            author_frame.clicked.connect(partial(self.load_author_page, author))
            self.ui.mainPageAuthorsAuthorsGridQGridLayout.addWidget(author_frame, row, column, 1, 1)
            column += 1
        if column % 8 == 0:
            row += 1
            column = 0
        author_adder = AdderEntry(adder_type=3, parent=self.ui.mainPageAuthorsGrid)
        author_adder.clicked.connect(self.add_new_author)
        self.ui.mainPageAuthorsAuthorsGridQGridLayout.addWidget(author_adder, row, column, 1, 1)

    def load_author_page(self, author):
        self.ui.set_main_page_stacked_widget_index(6)
        self.ui.mainPageAuthorPageAlbumsAuthorNameLabel.setText(author.author_name + " albums")
        self.ui.mainPageAuthorPageAlbumsAuthorNameLabel_2.setText(author.author_name + " playlists")
        self.ui.mainPageAutorNameLabel.setText(author.author_name)
        self.load_selected_author_songs(author)
        self.load_selected_author_albums(author)
        self.load_selected_author_playlists(author)

    def load_selected_author_songs(self, author):
        if len(self.loaded_selected_author_songs) != 0:
            for i in self.loaded_selected_author_songs:
                i.setParent(None)
            self.loaded_selected_author_songs = []
        songs = Songs.query.filter_by(author_id=author.id).all()
        for song in songs:
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_title=song.title,
                category_name=song.category.category_name,
                is_liked=is_liked
            )
            self.ui.mainPageAuthorPageSongsListQVBoxLayout.addWidget(song_frame)
            song_frame.pushButton_30.clicked.connect(partial(self.like_song, song.id))
            song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
            song_frame.mainPageLikedSongsCategoryButton.clicked.connect(partial(self.load_selected_category_page,
                                                                        song.category.category_name))
            self.loaded_selected_author_songs.append(song_frame)

    def load_selected_author_albums(self, author):
        if len(self.loaded_selected_author_albums) != 0:
            for i in self.loaded_selected_author_albums:
                i.setParent(None)
            self.loaded_selected_author_albums = []
        albums = Albums.query.filter_by(author_id=author.id).all()
        row = column = 0
        for album in albums:
            if column % 8 == 0:
                row += 1
                column = 0
            album_frame = AlbumEntry(album_name=album.album_name)
            album_frame.clicked.connect(partial(self.load_album_page, album))
            self.ui.mainPageAuthorPageAlbumsGridQGridLayout.addWidget(album_frame, row, column, 1, 1)
            self.loaded_selected_author_albums.append(album_frame)
            column += 1

    def load_selected_author_playlists(self, author):
        if len(self.loaded_selected_author_playlists) != 0:
            for i in self.loaded_selected_author_playlists:
                i.setParent(None)
            self.loaded_selected_author_playlists = []
        author_playlists = AuthorPlaylists.query.filter_by(author_id=author.id).all()
        author_playlists_ids = []
        for i in author_playlists:
            author_playlists_ids.append(i.playlist_id)
        playlists = Playlist.query.filter(Playlist.id.in_(author_playlists_ids)).all()
        row = column = 0
        for playlist in playlists:
            if column % 8 == 0:
                row += 1
                column = 0
            playlist_frame = PlaylistEntry(self.ui.frame_62, playlist_name=playlist.playlist_name)
            playlist_frame.clicked.connect(partial(self.load_playlist_page, playlist))
            self.ui.mainPageAuthorPagePlaylistsGridQGridLayout.addWidget(playlist_frame, row, column, 1, 1)
            self.loaded_selected_author_playlists.append(playlist_frame)
            column += 1

    def last_played_button_slot(self):
        """Prepare lastPlayed page and change mainPageStackedWidget to lastPlayed's index"""
        self.setup_main_page_authors()
        self.ui.set_main_page_stacked_widget_index(3)

    def liked_songs_button_slot(self):
        """Prepare likedSongs page and change mainPageStackedWidget to likedSongs' index"""
        if len(self.loaded_liked_songs) != 0:
            for i in self.loaded_liked_songs:
                i.setParent(None)
            self.loaded_liked_songs = []
        self.setup_main_page_liked_songs()
        self.ui.set_main_page_stacked_widget_index(2)
        liked_songs = Songs.query.filter_by(liked_by=self.user_data["hashed_name"]).all()
        for song in liked_songs:
            liked_song_frame = SongEntry(song_title=song.title, artist_name=song.author.author_name,
                                         category_name=song.category.category_name, is_liked=True)
            self.ui.mainPageLikedSongsSongListQVBoxLayout.addWidget(liked_song_frame)
            liked_song_frame.pushButton_30.clicked.connect(partial(self.like_song, song.id))
            liked_song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
            liked_song_frame.mainPageLikedSongsArtistButton.clicked.connect(
                partial(self.load_author_page, song.author))
            liked_song_frame.mainPageLikedSongsCategoryButton.clicked.connect(
                partial(self.load_selected_category_page, song.category.category_name))
            self.loaded_liked_songs.append(liked_song_frame)

    def categories_button_slot(self):
        """Prepare categories page and change mainPageStackedWidget to categories' index"""
        self.setup_main_page_categories()
        self.ui.set_main_page_stacked_widget_index(1)
        music_categories = []
        self.category_frames = []
        row = column = 0
        music_categories_query = MusicCategories.query.all()
        for i in music_categories_query:
            music_categories.append(i.category_name)
        for category in music_categories:
            if column % 8 == 0:
                row += 1
                column = 0
            category_frame = CategoryEntry(self.ui.frame_54, category=category)
            category_frame.clicked.connect(partial(self.load_selected_category_page, category))
            self.ui.mainPageCategoriesCategoriesEntriesQGridLayout.addWidget(
                category_frame,
                row, column, 1, 1
            )
            self.category_frames.append(category_frame)
            column += 1

    def now_playing_button_slot(self):
        """Prepare nowPlaying page and change mainPageStackedWidget to nowPlaying's index"""
        self.setup_main_page_now_playing()
        self.ui.set_main_page_stacked_widget_index(0)

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

    def load_selected_category_page(self, category):
        self.ui.mainPageStackedWidget.setCurrentIndex(7)
        self.ui.mainPageCategoryNameLabel.setText(category)
        self.ui.mainPageAuthorPageAlbumsAuthorNameLabel_3.setText(category + " albums")
        self.ui.mainPageAuthorPageAlbumsAuthorNameLabel_4.setText(category + " playlists")
        music_category = MusicCategories.query.filter_by(category_name=category).first()
        self.load_selected_category_songs(music_category)
        self.load_selected_category_albums(music_category)
        self.load_selected_category_playlists(music_category)

    def load_selected_category_songs(self, music_category):
        if len(self.loaded_songs) != 0:
            for i in self.loaded_songs:
                i.setParent(None)
            self.loaded_songs = []
        songs = Songs.query.filter_by(category=music_category)
        for song in songs:
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_title=song.title,
                artist_name=song.author.author_name,
                is_liked=is_liked
            )
            self.ui.mainPageCategoryPageSongsListQVBoxLayout.addWidget(song_frame)
            song_frame.pushButton_30.clicked.connect(partial(self.like_song, song.id))
            song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
            song_frame.mainPageLikedSongsArtistButton.clicked.connect(partial(self.load_author_page, song.author))
            self.loaded_songs.append(song_frame)

    def load_selected_category_albums(self, music_category):
        if len(self.loaded_albums) != 0:
            for i in self.loaded_albums:
                i.setParent(None)
            self.loaded_albums = []
        albums = Albums.query.filter_by(category=music_category).all()
        row = column = 0
        for album in albums:
            if column % 8 == 0:
                row += 1
                column = 0
            album_frame = AlbumEntry(album_name=album.album_name)
            album_frame.clicked.connect(partial(self.load_album_page, album))
            self.ui.mainPageCategoryAlbumsGridQGridLayout.addWidget(album_frame, row, column, 1, 1)
            self.loaded_albums.append(album_frame)
            column += 1

    def load_selected_category_playlists(self, music_category):
        if len(self.loaded_playlists) != 0:
            for i in self.loaded_playlists:
                i.setParent(None)
            self.loaded_playlists = []
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
        self.ui.set_main_page_stacked_widget_index(5)
        self.ui.mainPagePlaylistNameOfPlaylistLabel.setText(playlist.playlist_name)
        self.load_playlist_page_songs(playlist)

    def load_playlist_page_songs(self, playlist):
        playlist_songs = PlaylistSongs.query.filter_by(playlist_id=playlist.id).all()
        playlist_songs_ids = []
        for i in playlist_songs:
            playlist_songs_ids.append(i.song_id)
        if len(self.loaded_playlist_page_songs) != 0:
            for i in self.loaded_playlist_page_songs:
                i.setParent(None)
            self.loaded_playlist_page_songs = []
        songs = Songs.query.filter(Songs.id.in_(playlist_songs_ids)).all()
        for song in songs:
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_title=song.title,
                artist_name=song.author.author_name,
                category_name=song.category.category_name,
                is_liked=is_liked
            )
            self.loaded_playlist_page_songs.append(song_frame)
            song_frame.pushButton_30.clicked.connect(partial(self.like_song, song.id))
            song_frame.pushButton_13.clicked.connect(partial(self.play_pause_song, song.id))
            song_frame.mainPageLikedSongsArtistButton.clicked.connect(partial(self.load_author_page, song.author))
            song_frame.mainPageLikedSongsCategoryButton.clicked.connect(partial(self.load_selected_category_page,
                                                                                song.category.category_name))
            self.ui.mainPagePlaylistSongListQVBoxLayout.addWidget(song_frame)

    def like_song(self, song_id):
        song_to_like = Songs.query.filter_by(id=song_id).first()
        if song_to_like.liked_by == self.user_data["hashed_name"]:
            song_to_like.liked_by = ""
        else:
            song_to_like.liked_by = self.user_data["hashed_name"]
        db.session.commit()

    def play_pause_song(self, song_id):
        song = Songs.query.filter_by(id=song_id).first()
        if song.is_playing:
            song.is_playing = False
        else:
            song.is_playing = True
            is_liked = False
            if song.liked_by == self.user_data["hashed_name"]:
                is_liked = True
            song_frame = SongEntry(
                song_title=song.title,
                date_added=song.date_added,
                song_length=song.length,
                is_liked=is_liked,
                is_playing=song.is_playing
            )
            print("ADDING")
            self.ui.verticalLayout_59.addWidget(song_frame)
        db.session.commit()

    def change_widget_category_songs(self):
        self.ui.mainPageCategoryPageStackedWidget.setCurrentIndex(0)

    def change_widget_category_albums(self):
        self.ui.mainPageCategoryPageStackedWidget.setCurrentIndex(1)

    def change_widget_category_playlists(self):
        self.ui.mainPageCategoryPageStackedWidget.setCurrentIndex(2)

    def change_widget_author_songs(self):
        self.ui.mainPageAuthorPageStackedWidget.setCurrentIndex(0)

    def change_widget_author_albums(self):
        self.ui.mainPageAuthorPageStackedWidget.setCurrentIndex(1)

    def change_widget_author_playlists(self):
        self.ui.mainPageAuthorPageStackedWidget.setCurrentIndex(2)

    def add_new_album(self):
        print("ADD NEW ALBUM")

    def add_new_author(self):
        print("ADD NEW AUTHOR")

    def get_user_data(self):
        user = User.query.first()
        if user:
            self.user_data = {"token": user.token.strip(), "hashed_name": user.hashed_name}
        return False

    def register(self):
        email = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_4.text()
        username = self.ui.lineEdit_5.text()
        data = {'email': email, "username": username, "password": password}
        response = requests.post('http://127.0.0.1:5000/register', data=data).json()
        if response["error"] == "1":
            print(response["message"])
            self.ui.centralStackedWidget.setCurrentIndex(1)
        else:
            print(response["message"])

    def load_register_page(self):
        self.ui.centralStackedWidget.setCurrentIndex(2)

    def log_in_with_credentials(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
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
            db.session.add(user)
            print(response["message"])
            self.ui.centralStackedWidget.setCurrentIndex(0)
        else:
            print(response["message"])
        db.session.commit()

    def log_in_with_token(self):
        if self.user_data:
            response = requests.post('http://127.0.0.1:5000/login_t', data=self.user_data).json()
            if response["error"] == "1":
                self.ui.centralStackedWidget.setCurrentIndex(0)
                print(response["message"])
            else:
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
            User.query.delete()
            db.session.commit()
            self.user_data = None
            self.ui.centralStackedWidget.setCurrentIndex(1)
        else:
            self.ui.centralStackedWidget.setCurrentIndex(1)

    def turn_off_playing_songs(self):
        Songs.query.update({"is_playing": False})
        db.session.commit()
