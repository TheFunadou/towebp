import sys


BANNER_ASCII = r"""
 ######  ####  ##    ##  ####  ########  ####  ##
 ##      ##  ## ##    ##  ##      ##     ##  ## ##
 ####    ###### ##    ##  ##      ##     ###### ##
 ##      ##  ## ##    ##  ##      ##     ##  ## ##
 ##      ##  ##  ######  ####     ##     ##  ## ##
##       ## ##   ####   ####     ##     ## ## ## ######
"""


def show_banner():
    try:
        from rich.console import Console
        console = Console()
        console.print(BANNER_ASCII, style="bold cyan")
        console.print(
            "[bold green]TOWEBP[/bold green] by theFunadou",
        )
        console.print(
            "Professional image to WEBP converter\n",
            style="white"
        )
    except Exception:
        sys.stdout.write(BANNER_ASCII)
        sys.stdout.write("TOWEBP by theFunadou\n")
        sys.stdout.write("Professional image to WEBP converter\n\n")
