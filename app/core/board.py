from operator import itemgetter

from core.utils.enums import Status
from core.utils.exceptions import UnsolvableException


class BaseJug:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = 0
        self.space = capacity
        self.status = Status.EMPTY

    def __str__(self):
        return f"{self.name} ({self.capacity} gal):{self.content} "

    def __repr__(self):
        return f"<Jug {self.status.name} // {self.content} of {self.capacity} ({self.space} free)>"

    def _update_content(self, amount):
        """Updates content and space consistently.
        Then, calculates and updates status.

        Params:
        -------

        Amount : int
            The amount of water to transfer.
            Positive to add (transfer in); negative to substract (tranfer out).
        """
        self.content += amount
        self.space -= amount

        if self.content == self.capacity:
            self.status = Status.FULL
        elif self.space == self.capacity:
            self.status = Status.EMPTY
        else:
            self.status = Status.PARTIALLY_FULL

    def fill(self):
        """Sets all capacity to content (full jar)"""
        self._update_content(self.space)

    def empty(self):
        """Sets all capacity to space (empty jar)"""
        self._update_content(-self.content)


class Jug(BaseJug):
    def __init__(self, capacity, name):
        self.name = name
        super().__init__(capacity)


class Juggler:
    def __init__(self, jar_x, jar_y, goal):
        # TODO: move this out of juggler (don't call if there is a result or a no result)
        try:
            solution = self._was_solved(jar_x, jar_y, goal)
            if solution:
                self.ok_solution_response(solution)
            self._is_solvable()
        except UnsolvableException:
            self.no_solution_response()

        self.jar_x = Jug(jar_x, "Jar-X")
        self.jar_y = Jug(jar_y, "Jar-Y")
        self.goal = goal

    def __repr__(self):
        return f"<Juggler [{self.jar_x}, {self.jar_y}] - {self.goal}>"


    def no_solution_response(self):
        # TODO: move to some communicator class
        return "No Solution"

    def ok_solution_response(self, solution):
        # TODO: move to some communicator class
        return solution

    def fill(self, jar):
        """Fills jar"""
        jar.fill()

    def empty(self, jar):
        """Empties jar"""
        jar.empty()

    def transfer(self, origin, destination):
        """Checks remaining space
        and transfers from origin to destination as much as possible"""
        transferred_water = min([destination.space, origin.content])

        origin._update_content(-transferred_water)
        destination._update_content(transferred_water)

    def _reset_jars(self):
        """Empties both jars"""
        self.jar_x.empty()
        self.jar_y.empty()

    def _solver_xy(self):
        # TODO: move to solver (divide the movements from the proper algorithm)
        """Always move from x to y"""
        step = 0
        process = list()

        while self.goal not in (self.jar_x.content, self.jar_y.content):
            if self.jar_x.content == 0:
                self.fill(self.jar_x)
                step += 1
                process.append(f'Step {step} : {self.jar_x.content} - {self.jar_y.content}')
                continue

            if self.jar_y.content == self.jar_y.capacity:
                self.empty(self.jar_y)
                step += 1
                process.append(f'Step {step} : {self.jar_x.content} - {self.jar_y.content}')
                continue

            self.transfer(self.jar_x, self.jar_y)
            step += 1
            process.append(f'Step {step} : {self.jar_x.content} - {self.jar_y.content}')
        return dict(steps=step, process=process)

    def _solver_yx(self):
        # TODO: move to solver (divide the movements from the proper algorithm)
        """Always move from y to x"""
        step = 0
        process = list()

        while self.goal not in (self.jar_x.content, self.jar_y.content):
            if self.jar_y.content == 0:
                self.fill(self.jar_y)
                step += 1
                process.append(f'Step {step} : {self.jar_x.content} - {self.jar_y.content}')
                continue

            if self.jar_x.content == self.jar_x.capacity:
                self.empty(self.jar_x)
                step += 1
                process.append(f'Step {step} : {self.jar_x.content} - {self.jar_y.content}')
                continue

            self.transfer(self.jar_y, self.jar_x)
            step += 1
            process.append(f'Step {step} : {self.jar_x.content} - {self.jar_y.content}')
        return dict(steps=step, process=process)

    def solve(self):
        x_to_y = self._solver_xy()
        self._reset_jars()
        y_to_x = self._solver_yx()
        solution = min([x_to_y, y_to_x], key=itemgetter('steps'))
        return solution

    def _is_solvable(self):
        True

    def _was_solved(self, jar_x, jar_y, goal):
        """NOT IMPLEMENTED
        If there is time, implement a cache where it saves the results.
        so you query the DB with the 3 values and if it was solved before,
        retrieve process from cache instead of calculating again.
        If can't be resolved, process is null.
        """
        solved_before = None
        """select process
         from historic
         where goal = ?goal
         and jars = ?(jar_x, jar_y)
         or jars = ?(jar_y, jar_x)
         """
        if solved_before and not solved_before['process']:
            raise UnsolvableException()
        return solved_before


if __name__ == "__main__":
    # j = Juggler(5, 3, 4)
    # j._solver_xy()
    # jj = Juggler(5, 3, 4)
    # jj._solver_yx()
    s = Juggler(5, 3, 4)
    print(s.solve())
    # print(j.jar_x, j.jar_y)
    # j.fill(j.jar_x)  # llenas 5
    # print(j.jar_x, j.jar_y)
    # j.transfer(j.jar_x, j.jar_y)  # sacas 3 a jarra3
    # print(j.jar_x, j.jar_y)
    # j.empty(j.jar_y)  # vacias jarra3
    # print(j.jar_x, j.jar_y)
    # j.transfer(j.jar_x, j.jar_y)  # pasas 2 que  quedaban a j3
    # print(j.jar_x, j.jar_y)
    # j.fill(j.jar_x)  # llenas 5
    # print(j.jar_x, j.jar_y)
    # j.transfer(j.jar_x, j.jar_y)  # mandas j5 lo que entre a j3
    # print(j.jar_x, j.jar_y)
