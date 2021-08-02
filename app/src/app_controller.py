from functools import partial
from PySide6 import QtCore, QtWidgets, QtGui

scrollbar_recently_used = False


class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.connect_signals_with_slots()

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
        """Prepare authors page and change mainPageStackedWidget to authors's index"""
        self.setup_main_page_albums()
        self.ui.set_main_page_stacked_widget_index(10)

    def authors_button_slot(self):
        """Prepare authors page and change mainPageStackedWidget to authors's index"""
        self.setup_main_page_authors()
        self.ui.set_main_page_stacked_widget_index(4)

    def last_played_button_slot(self):
        """Prepare lastPlayed page and change mainPageStackedWidget to lastPlayed's index"""
        self.setup_main_page_authors()
        self.ui.set_main_page_stacked_widget_index(3)

    def liked_songs_button_slot(self):
        """Prepare likedSongs page and change mainPageStackedWidget to likedSongs' index"""
        self.setup_main_page_liked_songs()
        self.ui.set_main_page_stacked_widget_index(2)

    def categories_button_slot(self):
        """Prepare categories page and change mainPageStackedWidget to categories' index"""
        self.setup_main_page_categories()
        self.ui.set_main_page_stacked_widget_index(1)

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
