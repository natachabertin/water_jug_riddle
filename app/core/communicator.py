from core.checker import Checker


class Communicator:
    """Interacts between core and with API/CLI
    Receives params as integers; and the class Checker,
    which is the enter point to the orchestration logic.
    Returns results object.
    """

    def __init__(self, jar_x, jar_y, goal, checker):
        self.result = checker(jar_x, jar_y, goal).report()

    def report(self):
        return self.result


if __name__ == "__main__":
    print(Communicator(5, 4, 2, Checker).report())
