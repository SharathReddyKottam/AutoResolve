from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt

load_dotenv()

from autoresolve.observability.logger import get_logger

console = Console()
logger = get_logger(__name__)


def run():
    logger.info("Starting AutoResolve")
    console.print("\n[bold blue]AutoResolve[/bold blue] - incident auto-resolution agent")
    console.print("Type [bold]/ticket <description>[/bold] to submit a ticket, or [bold]/exit[/bold] to quit\n")

    while True:
        user_input = Prompt.ask("[bold green]>[/bold green]")
        if not user_input.strip():
            continue
        if user_input.lower() in ("/exit", "/quit"):
            console.print("[dim]Goodbye![/dim]")
            break
        elif user_input.startswith("/ticket"):
            description = user_input.removeprefix("/ticket").strip()
            if not description:
                console.print("[yellow]Please describe the problem after /ticket[/yellow]")
                continue
            logger.info(f"Ticket received: {description}")
            console.print(f"[dim]Received ticket: {description}[/dim]")
            # TODO: classify, diagnose, resolve
        else:
            logger.warning(f"Unknown command received: {user_input}")
            console.print("[yellow]Unknown command. Try:[/yellow]")
            console.print("  [bold]/ticket <description>[/bold]  - submit a ticket")
            console.print("  [bold]/exit[/bold]  - quit")


if __name__ == "__main__":
    run()