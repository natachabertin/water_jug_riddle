from main import hello_world


class TestCase:
    def test_hi(self):
        res = hello_world()

        assert res == {"message": "OK"}
