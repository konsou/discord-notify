import argparse
import os
import sys
from typing import NamedTuple, Optional, Literal

import dotenv

import message as message_

dotenv.load_dotenv()


class ParsedArgs(NamedTuple):
    webhook_url: str
    message: str
    message_level: message_.MessageLevel
    file_path: Optional[str]


def parse_args() -> ParsedArgs:
    parser = argparse.ArgumentParser(
        description="Send a message (with an optional attachment) to a Discord channel via a webhook"
    )
    parser.add_argument(
        "--webhook_url",
        required=False,
        help="The Discord Webhook URL (read from .env if not set)",
    )
    parser.add_argument("--message", required=True, help="The message to send")
    parser.add_argument(
        "--level",
        required=False,
        default=message_.MessageLevel.INFO,
        type=message_.MessageLevel,
        help=f"Message level. Valid values: {', '.join([i.value for i in message_.MessageLevel])}",
    )
    parser.add_argument("--file", help="The path to the file to attach", default=None)
    parser.epilog = "Env vars read: WEBHOOK_URL for info level message, WEBHOOK_URL_ERROR for error level message"

    args = parser.parse_args()

    if args.webhook_url:
        return ParsedArgs(
            webhook_url=args.webhook_url,
            message=args.message,
            message_level=args.level,
            file_path=args.file,
        )

    if args.level == message_.MessageLevel.INFO:
        webhook_env_name = "WEBHOOK_URL"
    else:
        webhook_env_name = "WEBHOOK_URL_ERROR"

    webhook_url = os.getenv(webhook_env_name)

    if webhook_url is None:
        print(
            f"{webhook_env_name} not found in .env or as an env var, and --webhook_url not set"
        )
        sys.exit(1)

    return ParsedArgs(
        webhook_url=webhook_url,
        message=args.message,
        message_level=args.level,
        file_path=args.file,
    )
