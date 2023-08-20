import typer
from rich import print
from rich.panel import Panel

from core.board import Juggler


def welcome():
    print(
        Panel(
            """[bold]This is [blue]Water Jug Riddle[/blue] solver app.[/bold]

        You enter the amount of gallons to count, and the size of the buckets.
        We show you the result and the process."
        """,
            title="Hello! :hand:",
            subtitle="Let's play!",
        )
    )


def no_solution():
    print(
        Panel(
            "There is no solution for the combination you entered.",
            title=":boom: [bold red]Wrong![/bold red] :boom:",
        )
    )


def show_solution():
    print(
        Panel(
            "Below is the solution for the combination you entered.",
            title=":boom: [bold green]You nailed it![/bold green] :boom:",
        )
    )


def request_params():
    print(Panel("Which are x y z values", title="PRETTY THIS AND MAKE IT PROMPT"))
    return (5, 3, 4)


def mock_process():
    """ implement jsonified status as data for the output and prettify it in cli with rich"""
    j = Juggler(5, 3, 4)
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
    j.transfer(j.jar_x, j.jar_y)  # mandas j5 lo que entre a j3
    print(j.jar_x, j.jar_y)


class NoSolutionException:
    # TODO. move to excs module
    pass


def main():
    welcome()
    x, y, z = request_params()

    try:
        board = Juggler(x, y, z)
        # board.solve()  # There should be another entity ('solver') that aplies the algorithm and return the list of statuses
        show_solution()
        # this is the mock replacing the printing until solver returns the status list
        process = mock_process()
    except NoSolutionException:
        no_solution()


if __name__ == "__main__":
    typer.run(main)
