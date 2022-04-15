# !/usr/bin/env python3
#  -*- coding: utf-8 -*-
# maintainer (@pandanz)
"""
Ensure coding standards are used.
"""

import difflib
from pathlib import Path
import sys
import pkgutil
from hooks.config import FILES

DOCUMENTATION = """
Ensures that files related to coding standards are consistent with pre-defined templates.
If there is difference between these files, the files are updated with the repo.
"""

RETURNS = """
PASS/FAIL
Lists files that were modified or created.
"""


def diff_file(filename, content):
    """Diff a file."""

    # full_path = Path(__file__).parent.joinpath(content)
    # print(full_path)
    return list(
        difflib.context_diff(
            [f"{line}\n" for line in Path(filename).read_text().split("\n")],
            [f"{line}\n" for line in content.split("\n")],
            # [f"{line}\n" for line in Path(content).read_text().split("\n")],
            filename,
            "generated",
        )
    )


def _coding_standards():
    """
    Inital entrypoint from __main__:
    Prints: files that were modified or created
    Returns: bool
    """
    error = False
    files = FILES

    differences = []
    files_modified = []
    # print(f"Working Directory {Path().resolve()}")

    for filename, template in files:
        file = Path(filename)
        content = pkgutil.get_data("hooks", template).decode()
        file.parent.mkdir(exist_ok=True, parents=True)
        file.touch(exist_ok=True)
        diff = diff_file(filename, content)
        if diff:
            differences.append("".join(diff))
            files_modified.append(filename)
            print("ERROR - FOUND THE FOLLOWING DIFFERENCES")
            print()
            print()
            print("\n\n".join(differences))
            print()
            Path(filename).write_text(content)

    if files_modified:
        for file in files_modified:
            print(f"{file} was modified, defaulting back to standard")
        error = True

    return error


def main():
    """
    Checks local repo files are consistent with templates
    Returns: bool as sys.exit code.  True = 1, False = 0.  Zero is good.
    """
    error = False

    error = _coding_standards()

    if error is True:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    sys.exit(main())
