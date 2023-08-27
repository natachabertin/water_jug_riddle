from app.api_texts import EXAMPLE
from app.api_texts import RULES
from app.core.board import Juggler
from app.core.checker import Checker
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return dict(rules=RULES, example=EXAMPLE)


@app.get("/riddle/")
async def read_item(x: int, y: int, z: int):
    solution = Checker(x, y, z, Juggler).report()
    return solution
