import typer
from rich import print
from rich.panel import Panel

from core.board import Juggler
from core.checker import Checker
from core.utils.models import OkResult, NokResult


def welcome():
    print(
        Panel(
            """[bold]This is [blue]Water Jug Riddle[/blue] solver app.[/bold]

        You enter the amount of gallons to count, and the size of the buckets.
        We show you the result and the process.
        """,
            title="Hello! :hand:",
            subtitle="Let's play! :partying_face:",
        )
    )


def show_nok(params, solution):
    print(
        Panel(
            f"{solution.reason}",
            title=f"[bold red] Case {params}[/bold red] :confounded_face:",
            subtitle=":boom: [bold red]No solution[/bold red] :boom:"
        )
    )


def show_solution(solution):
    print(
        Panel(
            "Below is the solution for the combination you entered.",
            title=":boom: [bold green]You nailed it![/bold green] :boom:",
        )
    )


def show_solution(params, solution):
    if isinstance(solution, OkResult):
        show_ok(params, solution)
    if isinstance(solution, NokResult):
        show_nok(params, solution)



def request_params():
    x = typer.prompt("Which is the capacity of jar x?")
    y = typer.prompt("Which is the capacity of jar y?")
    z = typer.prompt("Which amount of water do you wanna measure?")
    print(Panel(f"Jar-X: {x} - Jar-Y: {y}. Measuring {z} gallons...", title="Here is our data, then:"))

    return int(x), int(y), int(z)



def main():
    welcome()
    params = request_params()
    solution = Checker(*params, Juggler).report()
    show_solution(params, solution)



if __name__ == "__main__":
    typer.run(main)
