from core.utils.enums import Status


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
        self.jar_x = Jug(jar_x, "Jar-X")
        self.jar_y = Jug(jar_y, "Jar-Y")
        self.goal = goal

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

    def solver_xy(self):
        """Always move from x to y"""
        step = 0

        while self.goal not in (self.jar_x.content, self.jar_y.content):
            if self.jar_x.content == 0:
                self.fill(self.jar_x)
                step += 1
                print(f'Step {step} : {self.jar_x.content} - {self.jar_y.content}')
                continue

            if self.jar_y.content == self.jar_y.capacity:
                self.empty(self.jar_y)
                step += 1
                print(f'Step {step} : {self.jar_x.content} - {self.jar_y.content}')
                continue

            self.transfer(self.jar_x, self.jar_y)
            step += 1

            print(f'Step {step} : {self.jar_x.content} - {self.jar_y.content}')


    def solver_yx(self):
        """Always move from y to x"""
        step = 0

        while self.goal not in (self.jar_x.content, self.jar_y.content):
            if self.jar_y.content == 0:
                self.fill(self.jar_y)
                step += 1
                print(f'Step {step} : {self.jar_y.content} - {self.jar_x.content}')
                continue

            if self.jar_x.content == self.jar_x.capacity:
                self.empty(self.jar_x)
                step += 1
                print(f'Step {step} : {self.jar_y.content} - {self.jar_x.content}')
                continue

            self.transfer(self.jar_y, self.jar_x)
            step += 1

            print(f'Step {step} : {self.jar_y.content} - {self.jar_x.content}')






if __name__ == "__main__":
    j = Juggler(5, 3, 4)
    j.solver_xy()
    jj = Juggler(5, 3, 4)
    jj.solver_yx()
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
