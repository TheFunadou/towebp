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


def create_output_path(
    root,
    filename,
    output_dir
):

    output_filename = (
        os.path.splitext(filename)[0]
        + ".webp"
    )

    if output_dir == ".":
        final_dir = root
    else:
        final_dir = os.path.join(
            root,
            output_dir
        )

    os.makedirs(final_dir, exist_ok=True)

    return os.path.join(
        final_dir,
        output_filename
    )