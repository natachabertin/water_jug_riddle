from fastapi import FastAPI

# from api_texts import RULES, EXAMPLE
from core.board import Juggler
from core.checker import Checker

app = FastAPI()


@app.get("/")
def index():
    return dict(rules=RULES, example=EXAMPLE)


@app.get("/riddle/")
async def read_item(x: int, y: int, z: int):
    solution = Checker(x, y, z, Juggler).report()
    return solution

RULES = """You have an X-gallon and a Y-gallon jug that you can fill from a lake. (You should assume the
lake has unlimited amounts of water.) Measure Z gallons of water using only an X-gallon and
Y-gallon jug (no third jug)."""

EXAMPLE = """A GET to http://localhost:8000/riddle/?x=5&y=3&z=4 returns the path to calculate 4 gallons with two jars of 5 and 3 gallons."""
