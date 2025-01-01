import argparse

import os
import shutil

from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Clear the pycache of a particular "
            "folder (Recursive clear supported)."
        ),
    )

    parser.add_argument(
        "directory",
        type=str,
        help="Path of the directory to clear."
    )

    parser.add_argument(
        "-r",
        "--recursive",
        type=bool,
        required=False,
        default=False,
        help="Clear directory recursively."
    )

    args = parser.parse_args()

    path = Path(args.directory)

    clear_pycache(
        path,
        is_recursive=args.recursive
    )


def clear_pycache(
    path: Path,
    is_recursive: bool,
):
    if not path.exists():
        print(
            f"Directory not found at: {path}"
        )
    elif path.is_dir():
        contents = os.listdir(path)

        for content in contents:
            if content == '__pycache__':
                shutil.rmtree(
                    Path(content)
                )
            elif is_recursive:
                clear_pycache(
                    Path(content),
                    is_recursive=is_recursive
                )


if __name__ == '__main__':
    main()
