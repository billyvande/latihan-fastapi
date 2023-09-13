import uvicorn
from . import song,  auth

from imp import reload
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from .model import User

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'token')

app.include_router(song.router, prefix="/song", tags=['song'])
app.include_router(auth.router, prefix="" , tags=['auth'])

# if __name__ == "__main__":
#     uvicorn.run( 'main:app', host = '127.0.0.1', port=8080, reload = True)