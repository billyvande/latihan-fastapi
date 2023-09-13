from fastapi import APIRouter, Depends
from .auth import oauth2_scheme

from . import schemas

router = APIRouter()

artist1 = schemas.Artist(name = "David Bayu", age =  46, gender =  "Male")
artist2 = schemas.Artist(name = "Fiersa Besari", age =  38, gender =  "Male")

fakeDB = {
    1 : {
    "Artist" : artist1 ,
    "Title": "Deritaku",
    "Duration" : 150
    },
    2 : {
    "Artist" : artist2,
    "Title" : "Waktu yang salah",
    "Duration" : 326
    }
}

@router.get('/')
async def songs(token : str = Depends(oauth2_scheme)):
    return fakeDB

@router.get('/{id}')
async def song(id:int):
    return fakeDB[id]

@router.post('/')
async def addSong(song : schemas.Song):
    incr = len(fakeDB.keys())+1
    while (incr in fakeDB.keys()):
        incr += 1
    fakeDB[incr] = {
        "Artist" : song.artist,
        "Title": song.title,
        "Duration" : song.duration}
    return fakeDB

@router.put('/{id}')
async def updateSong(id:int, song : schemas.Song):
    fakeDB[id] = {song.artist : song.title}
    return fakeDB[id]

@router.delete('/{id}')
async def deleteSong(id:int):
    before_deleted = fakeDB[id]
    del fakeDB[id]
    return ("deleted", before_deleted)

async def autoDelete():
    return 0