from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    hashed_name = Column(String)
    token = Column(String)
    songs = relationship("UserSongs", back_populates="user")


class UserSongs(Base):
    __tablename__ = "user_songs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    category_id = Column(Integer, ForeignKey("music_categories.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    song_id = Column(Integer)
    file_path = Column(String)
    user = relationship("User")
    category = relationship("MusicCategories", back_populates="song")


class MusicCategories(Base):
    __tablename__ = "music_categories"
    id = Column(Integer, primary_key=True)
    category_name = Column(String)
    song = relationship("UserSongs")
