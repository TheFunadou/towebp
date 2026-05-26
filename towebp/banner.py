from rich.console import Console

console = Console()


def show_banner():
    try:
        console.print("""

████████╗ ██████╗ ██╗    ██╗███████╗██████╗ ██████╗
╚══██╔══╝██╔═══██╗██║    ██║██╔════╝██╔══██╗██╔══██╗
   ██║   ██║   ██║██║ █╗ ██║█████╗  ██████╔╝██████╔╝
   ██║   ██║   ██║██║███╗██║██╔══╝  ██╔══██╗██╔═══╝
   ██║   ╚██████╔╝╚███╔███╔╝███████╗██████╔╝██║
   ╚═╝    ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝

""", style="bold cyan")
    except Exception:
        console.print("\n=== TOWEBP ===", style="bold cyan")

    console.print(
        "[bold green]TOWEBP[/bold green] by theFunadou",
    )

    console.print(
        "Professional image to WEBP converter\n",
        style="white"
    )