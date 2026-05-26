import os

from PIL import Image

from rich.console import Console
from rich.progress import track

from .utils import (
    is_supported_image,
    create_output_path
)

console = Console()


def collect_images(
    directory,
    recursive
):

    files_found = []

    if recursive:

        for root, _, files in os.walk(directory):

            for file in files:

                if is_supported_image(file):

                    files_found.append(
                        (root, file)
                    )

    else:

        for file in os.listdir(directory):

            if is_supported_image(file):

                files_found.append(
                    (directory, file)
                )

    return files_found


def convert_images(
    directory,
    recursive=False,
    output_dir="webp",
    quality=80,
    overwrite=False,
    skip_existing=True
):

    images = collect_images(
        directory,
        recursive
    )

    if not images:

        console.print(
            "[yellow]No compatible images found[/yellow]"
        )

        return

    console.print(
        f"\n[cyan]Images found:[/cyan] {len(images)}"
    )

    converted = 0
    skipped = 0
    failed = 0

    for root, file in track(
        images,
        description="Converting..."
    ):

        input_path = os.path.join(
            root,
            file
        )

        output_path = create_output_path(
            root,
            file,
            output_dir
        )

        # Saltar si ya existe
        if (
            os.path.exists(output_path)
            and skip_existing
            and not overwrite
        ):

            skipped += 1
            continue

        try:

            with Image.open(input_path) as img:

                img.save(
                    output_path,
                    "WEBP",
                    quality=quality
                )

            converted += 1

        except Exception as e:

            failed += 1

            console.print(
                f"[red]Error:[/red] {file} -> {e}"
            )

    console.print("\n[bold green]Conversion completed[/bold green]")

    console.print(
        f"""
Converted   : {converted}
Skipped     : {skipped}
Errors      : {failed}
"""
    )