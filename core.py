from enums import Status
from exceptions import WaterOverflowException


class Jug:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = 0
        self.space = capacity
        self.status = Status.EMPTY

    def __repr__(self):
        return f"|{'X|' * self.content}{' |' * self.space} - {self.status.name} - {self.content} of {self.capacity} ({self.space} free)"

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
        self._update_content(-self.capacity)

    def transfer_in(self, another):
        """Gets water from another jar up to this jar free space (not capacity!)
        Updates self AND ANOTHER this way until I design the orchestrator 'Juggler'
        (one object should not update another, seems like an encapsulation issue).

        Raises FullException if there are not enough space, returning the remaining water as err arg"""
        remaining_water = another.content - self.space
        transferable_water = another.content if not remaining_water else another.content - remaining_water

        self._update_content(transferable_water)
        another._update_content(-transferable_water)

        if remaining_water:
            raise WaterOverflowException(
                f"Only {self.space} gallons free. You got the rest back.",
                remaining_water=remaining_water
            )

    def transfer_out(self, another):
        """Gives water to another jar up to the other jar free space (not capacity!)
        Updates self AND ANOTHER this way until I design the orchestrator 'Juggler'
        (one object should not update another, seems like an encapsulation issue).

        Handles FullException without losing any water (to keep the measurement)"""
        remaining_water = self.content - another.space
        transferable_water = self.content if not remaining_water else self.content - remaining_water

        another._update_content(transferable_water)
        self._update_content(-transferable_water)

        if remaining_water:
            raise WaterOverflowException(
                f"Only {another.space} gallons free. You got the rest back.",
                remaining_water=remaining_water
            )


class Juggler:
    def __init__(self, jar_a, jar_b, goal):
        self.big_jar, self.little_jar = self._tag_jars(jar_a, jar_b)
        self.goal = goal

    def _tag_jars(self, jar_a, jar_b):
        return sorted([jar_a, jar_b], reverse=True)

    def fill(self, jar):
        """Saca agua infinita y lo llena"""
        pass

    def empty(self, jar):
        """Tira el agua y lo deja en cero"""
        pass

    def transfer(origin, destination):
        """Saca agua infinita y lo llena"""




def brute_force(ja, jb, goal):
    juggler = Juggler(ja, jb, goal)




if __name__ == '__main__':
    # print(brute_force(5,3,4))
    big_jar = Jug(5)

    print(big_jar)