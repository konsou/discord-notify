from typing import NamedTuple

import dotenv
import requests
import argparse
import os

import _args

dotenv.load_dotenv()


def main():
    args = _args.parse_args()

    # Prepare the data payload
    data = {
        'content': args.message
    }

    # Prepare the file payload if a file path is provided
    files = {}
    if args.file_path:
        files['file'] = load_file(args.file_path)

    # Post the message and file to the Discord webhook
    response = requests.post(args.webhook_url, data=data, files=files)

    # Check for success
    if response.status_code in (200, 204):
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")


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


if __name__ == '__main__':
    main()
