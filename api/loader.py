from fastapi import FastAPI

from database import Database

db = Database()

app = FastAPI()
