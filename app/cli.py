import typer
from rich import print
from rich.panel import Panel


def welcome():
    print(Panel(
        """[bold]This is [blue]Water Jug Riddle[/blue] solver app.[/bold]
        
        You enter the amount of gallons to count, and the size of the buckets. 
        We show you the result and the process."
        """,
        title="Hello! :hand:",
        subtitle="Let's play!"
    ))

def no_solution():
    print(Panel(
        "There is no solution for the combination you entered.",
        title=":boom: [bold red]Wrong![/bold red] :boom:"
    ))


def show_solution():
    print(Panel(
        "Below is the solution for the combination you entered.",
        title=":boom: [bold green]You nailed it![/bold green] :boom:"
    ))


def main():
    welcome()
    no_solution()
    show_solution()


if __name__ == "__main__":
    typer.run(main)