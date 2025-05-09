import argparse
import os
import sys
from typing import NamedTuple, Optional, Literal

import dotenv

import _conf
import _message_level
import _message_level as message_

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
    parser.add_argument("message", help="The message to send")
    parser.add_argument(
        "--level",
        required=False,
        default=message_.MessageLevel.INFO,
        type=message_.MessageLevel,
        help=f"Message level. Valid values: {', '.join([i.value for i in message_.MessageLevel])}",
    )
    parser.add_argument("--file", help="The path to the file to attach", default=None)
    parser.add_argument(
        "--webhook-url",
        required=False,
        help="The Discord Webhook URL (read from .env if not set)",
    )
    parser.add_argument(
        "--settings-file",
        required=False,
        default=f"{os.getenv('HOME')}/.config/discord-notify/config.json",
        help="The path to settings file to read WEBHOOK_URL and WEBHOOK_URL_ERROR from. Default: %(default)s",
    )
    parser.epilog = "Env vars read: WEBHOOK_URL for info level message, WEBHOOK_URL_ERROR for error level message. Webhook lookup order: command line argument > .env file > environment variable > config file"

    args = parser.parse_args()
    webhook_url = _conf.webhook_url(args)

    if webhook_url is None:
        print(f"{_message_level.WEBHOOK_ENV_NAME.get(args.level)} not set")
        sys.exit(1)

    return ParsedArgs(
        webhook_url=webhook_url,
        message=args.message,
        message_level=args.level,
        file_path=args.file,
    )
