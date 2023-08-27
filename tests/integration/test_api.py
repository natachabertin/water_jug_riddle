from fastapi.testclient import TestClient

from server import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Water Jug Riddle": "Ready"}


def test_riddle_ok():
    response = client.get("/riddle/?x=5&y=3&z=4")
    assert response.status_code == 200
    assert response.json() == {
        "path": [[5, 0], [2, 3], [2, 0], [0, 2], [5, 2], [4, 3]],
        "steps": 6,
    }


def test_riddle_unsolvable():
    response = client.get("/riddle/?x=0&y=1&z=0")
    assert response.status_code == 200
    assert response.json() == {"reason": {"message": "Goal is zero or both jars are."}}
