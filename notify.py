from typing import NamedTuple

import requests
import argparse
import os


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Send a message (with an optional attachment) to a Discord channel via webhook")
    parser.add_argument('--webhook_url', required=True, help='The Discord Webhook URL')
    parser.add_argument('--message', required=True, help='The message to send')
    parser.add_argument('--file', help='The path to the file to attach', default=None)

    # Parse the arguments
    args = parser.parse_args()

    # Prepare the data payload
    data = {
        'content': args.message
    }

    # Prepare the file payload if a file path is provided
    files = {}
    if args.file:
        files['file'] = load_file(args.file)

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
