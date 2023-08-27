from collections import deque

from core.utils.enums import Status
from core.utils.exceptions import UnsolvableException


class Jug:
    def __init__(self, capacity, name):
        self.name = name
        self.capacity = capacity
        self.content = 0
        self.space = capacity
        self.status = Status.EMPTY

    def __str__(self):
        return f"{self.name} ({self.capacity} gal):{self.content} "

    def __repr__(self):
        return f"<Jug {self.status.name} // {self.content} of {self.capacity}>"

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


class Juggler:
    def __init__(self, jar_x, jar_y, goal):
        self.jar_x = Jug(jar_x, "Jar-X")
        self.jar_y = Jug(jar_y, "Jar-Y")
        self.goal = goal

    def __repr__(self):
        return f"<Juggler [{self.jar_x}, {self.jar_y}] - {self.goal}>"

    def solve(self):
        statuses_to_check = deque()
        current_status = self._current_status()
        checked_statuses = list((current_status,))

        graph = {current_status: None}

        next_statuses = self._get_next_statuses(
            self._current_status(), checked_statuses
        )

        graph.update({current_status: next_statuses})

        statuses_to_check.extend(next_statuses)

        while statuses_to_check:
            checking_status = statuses_to_check.popleft()
            checked_statuses.append(checking_status)
            if self.goal_achieved(checking_status):
                path = self.retrieve_path(graph, checking_status, checked_statuses)
                return len(path), path
            else:
                next_statuses = self._get_next_statuses(
                    checking_status, checked_statuses
                )
                graph.update({checking_status: next_statuses})
                statuses_to_check.extend(next_statuses)

    @staticmethod
    def retrieve_path(graph, checking_status, checked_statuses):
        path = list()

        for node in reversed(checked_statuses):
            if checking_status == node:
                path.append(node)
                try:
                    parent = list(graph.keys())[list(graph.values()).index([node])]
                except ValueError as e:
                    parent = [k for k, v in graph.items() if node in v][0]

            if node == (0, 0):
                path.append(node)
                path.reverse()
                return path

            if parent == node:
                path.append(parent)
                try:
                    parent = list(graph.keys())[list(graph.values()).index([parent])]
                except ValueError as e:
                    parent = [k for k, v in graph.items() if parent in v][0]

    def move_water_operations(self, origin_status):
        curr_x, curr_y = origin_status
        next_statuses = list()
        # fill
        if curr_x != self.jar_x.capacity:
            next_statuses.append((self.jar_x.capacity, curr_y))
        if curr_y != self.jar_y.capacity:
            next_statuses.append((curr_x, self.jar_y.capacity))
        # empty
        if curr_x != 0:
            next_statuses.append((0, curr_y))
        if curr_y != 0:
            next_statuses.append((curr_x, 0))
        # transfer
        # x to y
        if curr_x != 0 and curr_y != self.jar_y.capacity:
            amount_to_transfer = min(curr_x, self.jar_y.capacity - curr_y)
            next_statuses.append(
                (curr_x - amount_to_transfer, curr_y + amount_to_transfer)
            )
        # y to x
        if curr_x != self.jar_x.capacity and curr_y != 0:
            amount_to_transfer = min(self.jar_x.capacity - curr_x, curr_y)
            next_statuses.append(
                (curr_x + amount_to_transfer, curr_y - amount_to_transfer)
            )
        return next_statuses

    def _current_status(self):
        return self.jar_x.content, self.jar_y.content

    def _get_next_statuses(self, origin_status, checked):
        next_statuses = self.move_water_operations(origin_status)

        return [status for status in next_statuses if status not in checked]

    def goal_achieved(self, checking_status):
        return self.goal in checking_status


if __name__ == "__main__":
    # s = Juggler(0, 0, 4)
    # s.solve()
    solvable_cases = [
        [5, 3, 4],
        [5, 3, 2],
        [5, 4, 2],
        [5, 3, 1],
        [5, 3, 4],
        [4, 3, 2],
        [7, 5, 6],
        [8, 5, 4],
        [9, 4, 6],
        [10, 7, 9],
        [11, 6, 8],
        [11, 7, 5],
        [11, 9, 8],
        [12, 11, 6],
        [13, 11, 8],
        [7, 3, 2],
    ]
    unsolvable_cases = [
        [1, 2, 3],  # goal eq sum of jars >> unsolvable in one jar but by the sum of two
        [6, 4, 3],  # even both jars and goal odd >> should be covered as unsolvable
        [5, 3, 7],  # even both odd and goal even >> not divisible by gcd
        [0, 0, 0],  # all 0 >> you need a goal, not steps
        [10, 1, 0],  # goal 0, jugs not
        [0, 0, 1],  # jugs 0, goal not
        [0, 0, 4],  # jugs 0, goal not
    ]
    big_num_cases_unsolvable = [
        [
            1000000000,
            2,
            3000000000,
        ],  # goal eq sum of jars >> unsolvable in one jar but by the sum of two
        [
            6,
            4,
            3000000000,
        ],  # even both jars and goal odd >> should be covered as unsolvable
        [10000000000, 10000000000, 10000000],  # Goal is not divisible
        [123456789, 12345678, 1245],  # Goal is not divisible
    ]
    big_num_cases = [
        [50, 30000000, 700],  # filling 50 by 50 up to 700, takes a little but finishes
        [50, 300000000000, 700],  # filling 50 by 50 up to 700, takes a lot
        [50, 3000000000000000000000000, 700],  # filling 50 by 50 up to 700, takes a lot
        [700, 3000000000000000000000000, 50],  # filling 50 by 50 up to 700, takes a lot
        [159, 452, 5],
        [1111112, 2, 45],
    ]
    for case in solvable_cases:
        print(case)
        print(Juggler(*case).solve())

    for case in unsolvable_cases:
        print("unsolvable", case)
        try:
            print(Juggler(*case).solve())
        except UnsolvableException as e:
            print(e.message)

    for case in big_num_cases_unsolvable:
        print("big unsolvable", case)
        try:
            print(Juggler(*case).solve())
        except UnsolvableException as e:
            print(e.message)

    for case in big_num_cases:
        print("big", case)
        try:
            print(Juggler(*case).solve())
        except UnsolvableException as e:
            print(e.message)
