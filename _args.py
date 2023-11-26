import argparse
import os
import sys
from typing import NamedTuple, Optional, Literal

import dotenv

dotenv.load_dotenv()


class ParsedArgs(NamedTuple):
    webhook_url: str
    message: str
    file_path: Optional[str]


def parse_args(
        webhook_url_type: Optional[Literal['webhook_url_error', 'webhook_url_info']] = None
) -> ParsedArgs:
    parser = argparse.ArgumentParser(
        description="Send a message (with an optional attachment) to a Discord channel via webhook")
    parser.add_argument('--webhook_url', required=False, help='The Discord Webhook URL (read from .env if not set)')
    parser.add_argument('--message', required=True, help='The message to send')
    parser.add_argument('--file', help='The path to the file to attach', default=None)

    args = parser.parse_args()

    webhook_url = args.webhook_url or os.getenv('webhook_url')

    if webhook_url_type is not None and os.getenv(webhook_url_type):
        webhook_url = os.getenv(webhook_url_type)

    if webhook_url is None:
        print(f"{webhook_url_type or 'webhook_url'} not found in .env or as an env var, and --webhook_url not set")
        sys.exit(1)

    return ParsedArgs(
        webhook_url=webhook_url,
        message=args.message,
        file_path=args.file,
    )
