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
        parent = None

        for node in reversed(checked_statuses):
            if checking_status == node:
                path.append(node)
                try:
                    parent = list(graph.keys())[list(graph.values()).index([node])]
                except ValueError:
                    parent = [k for k, v in graph.items() if node in v][0]

            if node == (0, 0):
                path.reverse()
                return path

            if parent == node:
                path.append(parent)
                try:
                    parent = list(graph.keys())[list(graph.values()).index([parent])]
                except ValueError:
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
