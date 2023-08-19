from enums import Status
from exceptions import WaterOverflowException


class BaseJug:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = 0
        self.space = capacity
        self.status = Status.EMPTY

    def __str__(self):
        return f"|{'X|' * self.content}{' |' * self.space} - {self.status.name} - {self.content} of {self.capacity} ({self.space} free)"

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
        self._update_content(self.capacity)

    def empty(self):
        """Sets all capacity to space (empty jar)"""
        self._update_content(-self.content)

    def transfer_in(self, another):
        """Gets water from another jar up to this jar free space (not capacity!)
        Updates self AND ANOTHER this way until I design the orchestrator 'Juggler'
        (one object should not update another, seems like an encapsulation issue).

        Raises FullException if there are not enough space, returning the remaining water as err arg"""
        # TODO: fix negatives bug
        remaining_water = another.content - self.space
        transferable_water = self.content if remaining_water == 0 else self.content - abs(remaining_water)

        self._update_content(transferable_water)
        another._update_content(-transferable_water)

        if remaining_water:
            raise WaterOverflowException(
                f"You got {remaining_water} gallons back.",
                remaining_water=remaining_water
            )

    def transfer_out(self, another):
        """Gives water to another jar up to the other jar free space (not capacity!)
        Updates self AND ANOTHER this way until I design the orchestrator 'Juggler'
        (one object should not update another, seems like an encapsulation issue).

        Handles FullException without losing any water (to keep the measurement)"""

        # TODO: fix negatives bug
        remaining_water = self.content - another.space
        transferable_water = self.content if remaining_water == 0 else self.content - abs(remaining_water)

        another._update_content(transferable_water)
        self._update_content(-transferable_water)

        if remaining_water:
            raise WaterOverflowException(
                f"You got {remaining_water} gallons back.",
                remaining_water=remaining_water
            )


class Juggler:
    def __init__(self, jar_x, jar_y, goal):
        self.jar_x = Jug(jar_x, 'Jar-X')
        self.jar_y = Jug(jar_y, 'Jar-Y')
        self.goal = goal

    def fill(self, jar):
        """Fills jar"""
        jar.fill()

    def empty(self, jar):
        """Empties jar"""
        jar.empty()

    def transfer(self, origin, destination):
        """ Checks remaining space
        and transfers from origin to destination as much as possible"""

        # if destination.space == origin.content:
        #     transferred_water = origin.content
        # elif destination.space < origin.content:
        #     transferred_water = destination.space
        # elif destination.space > origin.content:
        #     transferred_water = destination.space
        transferred_water = min([destination.space, origin.content])

        origin._update_content(-transferred_water)
        destination._update_content(transferred_water)

class Jug(BaseJug):
    def __init__(self, capacity, name):
        self.name = name
        super().__init__(capacity)


if __name__ == '__main__':
    j=Juggler(5, 3, 4)
    print(j.jar_x, j.jar_y)
    j.fill(j.jar_x)  # llenas 5
    print(j.jar_x, j.jar_y)
    j.transfer(j.jar_x, j.jar_y)  # sacas 3 a jarra3
    print(j.jar_x, j.jar_y)
    j.empty(j.jar_y)  # vacias jarra3
    print(j.jar_x, j.jar_y)
    j.transfer(j.jar_x, j.jar_y)  # pasas 2 que  quedaban a j3
    print(j.jar_x, j.jar_y)
    j.fill(j.jar_x)  # llenas 5
    print(j.jar_x, j.jar_y)
    j.transfer(j.jar_x, j.jar_y) # mandas j5 lo que entre a j3
    print(j.jar_x, j.jar_y)
