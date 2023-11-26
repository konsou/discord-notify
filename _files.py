import os
from typing import NamedTuple

from _args import ParsedArgs


def files(args: ParsedArgs) -> dict:
    # Prepare the file payload if a file path is provided
    files = {}
    if args.file_path:
        files['file'] = load_file(args.file_path)
    return files


class Attachment(NamedTuple):
    name: str
    content: bytes


def load_file(filename: str) -> Attachment:
    with open(filename, 'rb') as f:
        content = f.read()

    return Attachment(
        name=os.path.basename(filename),
        content=content,
    )
