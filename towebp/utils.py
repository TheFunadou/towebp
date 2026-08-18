import os


SUPPORTED_FORMATS = (
    ".png",
    ".jpg",
    ".jpeg"
)


def is_supported_image(filename):

    return filename.lower().endswith(
        SUPPORTED_FORMATS
    )


def get_output_filename(filename):

    return os.path.splitext(filename)[0] + ".webp"


def get_output_path_for_file(
    root,
    filename,
    output_dir
):

    output_filename = get_output_filename(filename)

    if output_dir:
        final_dir = os.path.abspath(output_dir)
    else:
        final_dir = root

    os.makedirs(final_dir, exist_ok=True)

    return os.path.join(
        final_dir,
        output_filename
    )


def get_output_path_for_directory(
    root,
    filename,
    base_directory,
    output_dir,
    same_dir
):

    output_filename = get_output_filename(filename)

    if same_dir:
        final_dir = root
    elif output_dir:
        final_dir = os.path.abspath(output_dir)
    else:
        relative_path = os.path.relpath(
            root,
            base_directory
        )

        if relative_path == ".":
            final_dir = os.path.join(
                base_directory,
                "webp"
            )
        else:
            final_dir = os.path.join(
                base_directory,
                "webp",
                relative_path
            )

    os.makedirs(final_dir, exist_ok=True)

    return os.path.join(
        final_dir,
        output_filename
    )
