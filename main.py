from fastapi import FastAPI
from Model import *


app = FastAPI()

@app.get('/')
def home():
    return{"key": "Hello"}

@app.post('/Model')
def DataBase(Users, Games):
    return Users and Games

