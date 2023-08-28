from fastapi import FastAPI

from app.core.board import Juggler
from app.core.checker import Checker

app = FastAPI()


@app.get("/")
def index():
    return {"Water Jug Riddle": "Ready"}


@app.get("/riddle/")
async def read_item(x: int, y: int, z: int):
    return Checker(x, y, z, Juggler).report()
