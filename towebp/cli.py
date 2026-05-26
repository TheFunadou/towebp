import argparse
import os
import sys

from rich.console import Console
from rich_argparse import RichHelpFormatter

from .banner import show_banner
from .converter import convert_images

console = Console()


# ==========================================================
# ENGLISH HELP
# ==========================================================

def build_english_parser():
    parser = argparse.ArgumentParser(
        prog="towebp",
        formatter_class=RichHelpFormatter,
        usage="towebp [OPTIONS]",
        description="""
Professional image to WEBP converter.

BASIC USAGE:
  Convert images in the current directory:
    towebp

  Convert images in another directory:
    towebp -d ./images

  Convert images recursively:
    towebp -d ./assets -r

  Save WEBP images in the same folder:
    towebp -o .

  Change WEBP quality:
    towebp -q 90

FLAG COMBINATIONS:
  Convert recursively and save in the same folder:
    towebp -d ./assets -r -o .

  Convert recursively with custom quality:
    towebp -d ./assets -r -q 95

  Convert recursively, save in the same folder, and overwrite existing WEBP files:
    towebp -d ./assets -r -o . --overwrite

DEFAULT VALUES:
  Directory:              . (Current directory)
  Output directory:       webp (Subdirectory)
  WEBP quality:           80 (0-100)
  Recursive search:       Disabled
  Overwrite existing:     Disabled
""",
        epilog="""
SUPPORTED FORMATS:
  • PNG, JPG, JPEG

NOTES:
  • By default, WEBP files are saved in a 'webp' folder.
  • Use '-o .' to save WEBP files next to the original images.
  • Existing WEBP files are skipped unless '--overwrite' is used.

TOWEBP by theFunadou
"""
    )

    # DIRECTORY OPTIONS
    directory_group = parser.add_argument_group("DIRECTORY OPTIONS")
    
    directory_group.add_argument(
        "-d", "--directory",
        default=".",
        metavar="PATH",
        help="Root directory to search for images (default: '.')."
    )
    
    directory_group.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Search images recursively through all subdirectories."
    )
    
    directory_group.add_argument(
        "-o", "--output-dir",
        default="webp",
        metavar="DIR",
        help="Output directory name (default: 'webp'). Use '.' to save next to original images."
    )

    # CONVERSION OPTIONS
    conversion_group = parser.add_argument_group("CONVERSION OPTIONS")
    
    conversion_group.add_argument(
        "-q", "--quality",
        type=int,
        default=80,
        metavar="0-100",
        help="WEBP image quality (default: 80)."
    )
    
    conversion_group.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing WEBP files."
    )
    
    conversion_group.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="Skip already converted images (default: True)."
    )

    return parser


# ==========================================================
# SPANISH HELP
# ==========================================================

def build_spanish_parser():
    parser = argparse.ArgumentParser(
        prog="towebp",
        formatter_class=RichHelpFormatter,
        usage="towebp [OPCIONES]",
        description="""
Conversor profesional de imágenes a WEBP.

USO BÁSICO:
  Convertir imágenes en el directorio actual:
    towebp

  Convertir imágenes en otro directorio:
    towebp -d ./imagenes

  Convertir imágenes recursivamente:
    towebp -d ./assets -r

  Guardar imágenes WEBP en la misma carpeta:
    towebp -o .

  Cambiar calidad WEBP:
    towebp -q 90

COMBINACIÓN DE FLAGS:
  Convertir recursivamente y guardar en la misma carpeta:
    towebp -d ./assets -r -o .

  Convertir recursivamente con calidad personalizada:
    towebp -d ./assets -r -q 95

  Convertir recursivamente, guardar en la misma carpeta y sobrescribir WEBP existentes:
    towebp -d ./assets -r -o . --overwrite

VALORES PREDETERMINADOS:
  Directorio:             . (Directorio actual)
  Directorio de salida:   webp (Subdirectorio)
  Calidad WEBP:           80 (0-100)
  Búsqueda recursiva:     Deshabilitada
  Sobrescribir existente: Deshabilitado
""",
        epilog="""
FORMATOS SOPORTADOS:
  • PNG, JPG, JPEG

NOTAS:
  • Por defecto, las imágenes WEBP se guardan en la carpeta 'webp'.
  • Usa '-o .' para guardar las imágenes WEBP junto a las originales.
  • Las imágenes WEBP existentes se omiten a menos que uses '--overwrite'.

TOWEBP por theFunadou
"""
    )

    # OPCIONES DE DIRECTORIO
    directory_group = parser.add_argument_group("OPCIONES DE DIRECTORIO")
    
    directory_group.add_argument(
        "-d", "--directory",
        default=".",
        metavar="RUTA",
        help="Directorio raíz para buscar imágenes (por defecto: '.')."
    )
    
    directory_group.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Buscar imágenes recursivamente en todos los subdirectorios."
    )
    
    directory_group.add_argument(
        "-o", "--output-dir",
        default="webp",
        metavar="DIR",
        help="Nombre del directorio de salida (por defecto: 'webp'). Usa '.' para guardar junto a las originales."
    )

    # OPCIONES DE CONVERSIÓN
    conversion_group = parser.add_argument_group("OPCIONES DE CONVERSIÓN")
    
    conversion_group.add_argument(
        "-q", "--quality",
        type=int,
        default=80,
        metavar="0-100",
        help="Calidad de la imagen WEBP (por defecto: 80)."
    )
    
    conversion_group.add_argument(
        "--overwrite",
        action="store_true",
        help="Sobrescribir los archivos WEBP existentes."
    )
    
    conversion_group.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="Omitir imágenes ya convertidas (por defecto: True)."
    )

    return parser


# ==========================================================
# MAIN
# ==========================================================

def main():
    # ==========================================================
    # WELCOME SCREEN
    # ==========================================================
    if len(sys.argv) == 1:
        show_banner()

        console.print("[bold white]Quick Start Examples:[/bold white]\n")
        console.print("  [cyan]towebp[/cyan]                            Convert images in current directory to 'webp/'")
        console.print("  [cyan]towebp -d ./images[/cyan]                 Convert images in './images' to './images/webp/'")
        console.print("  [cyan]towebp -d ./assets -r[/cyan]              Convert images recursively in './assets'")
        console.print("  [cyan]towebp -d ./assets -r -o . -q 90[/cyan]   Convert recursively, save next to originals, quality 90")

        console.print("\n[bold white]Help Options:[/bold white]\n")
        console.print("  [green]towebp --help[/green]                      Show this help message in English")
        console.print("  [green]towebp --help-s[/green]                    Show this help message in Spanish")
        console.print("  [green]towebp --hs[/green]                        Alias for --help-s")
        return

    # ==========================================================
    # SPANISH HELP
    # ==========================================================
    if "--help-s" in sys.argv or "--hs" in sys.argv:
        parser = build_spanish_parser()
        parser.print_help()
        return

    # ==========================================================
    # ENGLISH HELP / NORMAL EXECUTION
    # ==========================================================
    parser = build_english_parser()
    args = parser.parse_args()

    directory = os.path.abspath(args.directory)

    # ==========================================================
    # VALIDATIONS
    # ==========================================================
    if not os.path.isdir(directory):
        console.print(
            "\n[bold red]Error:[/bold red] "
            "The specified directory does not exist.\n"
        )
        return

    if args.quality < 0 or args.quality > 100:
        console.print(
            "\n[bold red]Error:[/bold red] "
            "Quality must be between 0 and 100.\n"
        )
        return

    # ==========================================================
    # START
    # ==========================================================
    show_banner()

    console.print("[bold green]Current Configuration[/bold green]\n")
    console.print(f"[cyan]Directory:[/cyan]      {directory}")
    console.print(f"[cyan]Recursive:[/cyan]     {args.recursive}")
    console.print(f"[cyan]Output:[/cyan]        {args.output_dir}")
    console.print(f"[cyan]Quality:[/cyan]      {args.quality}")
    console.print(f"[cyan]Overwrite:[/cyan]    {args.overwrite}\n")

    convert_images(
        directory=directory,
        recursive=args.recursive,
        output_dir=args.output_dir,
        quality=args.quality,
        overwrite=args.overwrite,
        skip_existing=args.skip_existing
    )


if __name__ == "__main__":
    main()