import os

from PIL import Image

from rich.console import Console
from rich.progress import track

from .utils import (
    is_supported_image,
    get_output_path_for_file,
    get_output_path_for_directory
)

console = Console()


def collect_images(
    directory
):

    files_found = []

    for root, _, files in os.walk(directory):

        for file in files:

            if is_supported_image(file):

                files_found.append(
                    (root, file)
                )

    return files_found


def convert_file(
    filepath,
    quality=80,
    output_dir=None,
    overwrite=False,
):

    filename = os.path.basename(filepath)
    root = os.path.dirname(filepath)

    if not is_supported_image(filename):
        console.print(
            f"[red]Error:[/red] Unsupported format: {filename}"
        )
        return

    output_path = get_output_path_for_file(
        root,
        filename,
        output_dir
    )

    if os.path.exists(output_path) and not overwrite:
        console.print(
            f"[yellow]Skipped:[/yellow] {filename} (already exists)"
        )
        return

    try:

        with Image.open(filepath) as img:

            img.save(
                output_path,
                "WEBP",
                quality=quality
            )

        console.print(
            f"[green]Converted:[/green] {filename} -> {os.path.basename(output_path)}"
        )

    except Exception as e:

        console.print(
            f"[red]Error:[/red] {filename} -> {e}"
        )


def convert_directory(
    directory,
    quality=80,
    output_dir=None,
    same_dir=False,
    overwrite=False,
):

    images = collect_images(directory)

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

        output_path = get_output_path_for_directory(
            root,
            file,
            directory,
            output_dir,
            same_dir
        )

        if os.path.exists(output_path) and not overwrite:
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
