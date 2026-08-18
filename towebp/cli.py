import argparse
import os
import sys

from rich.console import Console
from rich_argparse import RichHelpFormatter

from .banner import show_banner
from .converter import convert_file, convert_directory

console = Console()


# ==========================================================
# ENGLISH HELP
# ==========================================================

def build_english_parser():
    parser = argparse.ArgumentParser(
        prog="towebp",
        formatter_class=RichHelpFormatter,
        usage="towebp <target> [OPTIONS]",
        description="""
Professional image to WEBP converter.

Convert a single file or an entire directory to WEBP format.
Directories are searched recursively by default.
""",
        epilog="""
EXAMPLES:

  Single file:
    towebp photo.png                    Convert to photo.webp in same folder
    towebp photo.png -q 90              Convert with quality 90
    towebp photo.png -outdir /tmp       Save to /tmp/photo.webp

  Directory (recursive by default):
    towebp ./images                     Convert all -> ./images/webp/
    towebp ./images --same-dir          Convert all -> next to originals
    towebp ./images -outdir /tmp        Convert all -> /tmp/
    towebp ./images -q 90 --overwrite   Quality 90, overwrite existing

DEFAULT BEHAVIOR:
  File:      Output in same directory as source
  Directory: Output in <directory>/webp/ subfolder (recursive)

SUPPORTED FORMATS: PNG, JPG, JPEG

TOWEBP by theFunadou
"""
    )

    parser.add_argument(
        "target",
        metavar="TARGET",
        help="File or directory to convert."
    )

    # OUTPUT OPTIONS
    output_group = parser.add_argument_group("OUTPUT OPTIONS")

    output_group.add_argument(
        "-outdir", "--output-dir",
        default=None,
        metavar="DIR",
        help="Custom output directory (created if it doesn't exist)."
    )

    output_group.add_argument(
        "--same-dir",
        action="store_true",
        help="Save output next to original files."
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

    return parser


# ==========================================================
# SPANISH HELP
# ==========================================================

def build_spanish_parser():
    parser = argparse.ArgumentParser(
        prog="towebp",
        formatter_class=RichHelpFormatter,
        usage="towebp <objetivo> [OPCIONES]",
        description="""
Conversor profesional de imágenes a WEBP.

Convierte un archivo individual o un directorio completo a formato WEBP.
Los directorios se buscan recursivamente por defecto.
""",
        epilog="""
EJEMPLOS:

  Archivo individual:
    towebp foto.png                     Convertir a foto.webp en la misma carpeta
    towebp foto.png -q 90               Convertir con calidad 90
    towebp foto.png -outdir /tmp        Guardar en /tmp/foto.webp

  Directorio (recursivo por defecto):
    towebp ./imagenes                   Convertir todo -> ./imagenes/webp/
    towebp ./imagenes --same-dir        Convertir todo -> junto a los originales
    towebp ./imagenes -outdir /tmp      Convertir todo -> /tmp/
    towebp ./imagenes -q 90 --overwrite Calidad 90, sobrescribir existentes

COMPORTAMIENTO POR DEFECTO:
  Archivo:      Output en la misma carpeta del archivo original
  Directorio:   Output en subcarpeta <directorio>/webp/ (recursivo)

FORMATOS SOPORTADOS: PNG, JPG, JPEG

TOWEBP por theFunadou
"""
    )

    parser.add_argument(
        "target",
        metavar="OBJETIVO",
        help="Archivo o directorio a convertir."
    )

    # OPCIONES DE SALIDA
    output_group = parser.add_argument_group("OPCIONES DE SALIDA")

    output_group.add_argument(
        "-outdir", "--output-dir",
        default=None,
        metavar="DIR",
        help="Directorio de salida personalizado (se crea si no existe)."
    )

    output_group.add_argument(
        "--same-dir",
        action="store_true",
        help="Guardar junto a los archivos originales."
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
        help="Sobrescribir archivos WEBP existentes."
    )

    return parser


# ==========================================================
# MAIN
# ==========================================================

def main():
    if len(sys.argv) == 1:
        show_banner()

        console.print("[bold white]Quick Start Examples:[/bold white]\n")
        console.print("  [cyan]towebp photo.png[/cyan]                     Convert file to photo.webp")
        console.print("  [cyan]towebp ./images[/cyan]                     Convert directory to ./images/webp/")
        console.print("  [cyan]towebp ./images --same-dir[/cyan]          Convert next to originals")
        console.print("  [cyan]towebp ./images -q 90 --overwrite[/cyan]  Quality 90, overwrite existing\n")

        console.print("[bold white]Help Options:[/bold white]\n")
        console.print("  [green]towebp --help[/green]                      Show help in English")
        console.print("  [green]towebp --help-s[/green]                    Show help in Spanish")
        console.print("  [green]towebp --hs[/green]                        Alias for --help-s")
        return

    if "--help-s" in sys.argv or "--hs" in sys.argv:
        parser = build_spanish_parser()
        parser.print_help()
        return

    parser = build_english_parser()
    args = parser.parse_args()

    target = os.path.abspath(args.target)

    if not os.path.exists(target):
        console.print(
            "\n[bold red]Error:[/bold red] "
            f"Target does not exist: {target}\n"
        )
        return

    if args.quality < 0 or args.quality > 100:
        console.print(
            "\n[bold red]Error:[/bold red] "
            "Quality must be between 0 and 100.\n"
        )
        return

    if args.same_dir and args.output_dir:
        console.print(
            "\n[bold red]Error:[/bold red] "
            "Cannot use --same-dir and -outdir together.\n"
        )
        return

    show_banner()

    console.print("[bold green]Configuration[/bold green]\n")
    console.print(f"[cyan]Target:[/cyan]       {target}")
    console.print(f"[cyan]Quality:[/cyan]     {args.quality}")

    if os.path.isfile(target):
        console.print(f"[cyan]Type:[/cyan]        File")
        if args.output_dir:
            console.print(f"[cyan]Output:[/cyan]      {args.output_dir}")
        elif args.same_dir:
            console.print(f"[cyan]Output:[/cyan]      Same directory")
        else:
            console.print(f"[cyan]Output:[/cyan]      Same directory")
        console.print(f"[cyan]Overwrite:[/cyan]   {args.overwrite}\n")

        convert_file(
            filepath=target,
            quality=args.quality,
            output_dir=args.output_dir,
            overwrite=args.overwrite,
        )
    else:
        console.print(f"[cyan]Type:[/cyan]        Directory (recursive)")
        if args.output_dir:
            console.print(f"[cyan]Output:[/cyan]      {args.output_dir}")
        elif args.same_dir:
            console.print(f"[cyan]Output:[/cyan]      Same as originals")
        else:
            console.print(f"[cyan]Output:[/cyan]      {target}/webp/")
        console.print(f"[cyan]Overwrite:[/cyan]   {args.overwrite}\n")

        convert_directory(
            directory=target,
            quality=args.quality,
            output_dir=args.output_dir,
            same_dir=args.same_dir,
            overwrite=args.overwrite,
        )


if __name__ == "__main__":
    main()
