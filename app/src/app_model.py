from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

SONG_FOLDER = "C:/Users/mrocz/PycharmProjects/Peach-player/app/src/songs"


class User(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    token = Column(String(100))
    hashed_name = Column(String(200))


class Songs(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author_id = Column(Integer, ForeignKey("authors.id"))
    category_id = Column(Integer, ForeignKey("music_categories.id"))
    album_id = Column(Integer, ForeignKey("albums.id"))
    path = Column(String(300))
    date_added = Column(String)
    length = Column(Integer)
    liked_by = Column(String)
    is_playing = Column(Boolean)
    user_hashed_name = Column(String(200))
    album = relationship("Albums", back_populates="song")
    author = relationship("Authors", back_populates="song")
    category = relationship("MusicCategories", back_populates="song")
    playlist = relationship("PlaylistSongs")
    album_songs = relationship("AlbumSongs")


class MusicCategories(db.Model):
    id = Column(Integer, primary_key=True)
    category_name = Column(String(100))
    song = relationship("Songs")
    album = relationship("Albums")
    playlist = relationship("Playlist")


class Albums(db.Model):
    id = Column(Integer, primary_key=True)
    album_name = Column(String(100))
    category_id = Column(Integer, ForeignKey("music_categories.id"))
    author_id = Column(Integer, ForeignKey("authors.id"))
    song = relationship("Songs")
    category = relationship("MusicCategories", back_populates="album")
    author = relationship("Authors", back_populates="album")
    songs = relationship("AlbumSongs")


class AlbumSongs(db.Model):
    id = Column(Integer, primary_key=True)
    album_id = Column(Integer, ForeignKey("albums.id"))
    song_id = Column(Integer, ForeignKey("songs.id"))
    album = relationship("Albums", back_populates="songs")
    song = relationship("Songs", back_populates="album_songs")


class Playlist(db.Model):
    id = Column(Integer, primary_key=True)
    playlist_name = Column(String(100))
    category_id = Column(Integer, ForeignKey("music_categories.id"))
    category = relationship("MusicCategories", back_populates="playlist")
    songs = relationship("PlaylistSongs")
    author = relationship("AuthorPlaylists")


class PlaylistSongs(db.Model):
    id = Column(Integer, primary_key=True)
    playlist_id = Column(Integer, ForeignKey("playlist.id"))
    song_id = Column(Integer, ForeignKey("songs.id"))
    playlist = relationship("Playlist", back_populates="songs")
    songs = relationship("Songs", back_populates="playlist")


class Authors(db.Model):
    id = Column(Integer, primary_key=True)
    author_name = Column(String)
    album = relationship("Albums")
    song = relationship("Songs")
    playlists = relationship("AuthorPlaylists")


class AuthorPlaylists(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    playlist_id = Column(Integer, ForeignKey("playlist.id"))
    author = relationship("Authors", back_populates="playlists")
    playlist = relationship("Playlist", back_populates="author")


class Test(db.Model):
    id = Column(Integer, primary_key=True)
    test_bool = Column(Boolean)

db.create_all()
