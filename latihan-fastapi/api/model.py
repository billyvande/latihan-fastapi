from turtle import title
from typing import Collection
from sqlalchemy import Column, Integer, String
from .database import Base
from pydantic import BaseModel


class Song(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    artist = Column(String)
    title = Column(String)
    duration = Column(Integer)

class User(BaseModel):
    __tablename__ = 'user'

    username: str
    email: str
    full_name: str
    disabled: bool
    password : str
