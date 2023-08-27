class Result:
    pass


class OkResult(Result):
    def __init__(self, steps, path):
        self.steps = steps
        self.path = path

    def __str__(self):
        return f"OK in the following {self.steps} moves: {self.path}"


class NokResult(Result):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return f"No solution: {self.reason}"
