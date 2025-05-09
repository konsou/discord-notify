import argparse
import json
import os

import dotenv

import _message_level


def webhook_url(args: argparse.Namespace) -> str | None:
    """Priority: argument > env > conf file"""
    # Command-line argument
    if args.webhook_url:
        return args.webhook_url

    # Env var on .env file
    webhook_env_name = _message_level.WEBHOOK_ENV_NAME.get(args.level)
    dotenv.load_dotenv()
    webhook_url_ = os.getenv(webhook_env_name)
    if webhook_url_:
        return webhook_url_

    # Conf file
    try:
        with open(args.settings_file, encoding="utf-8") as f:
            conf = json.load(f)
            return conf[webhook_env_name]
    except OSError as e:
        print(f"Error reading {args.settings_file}: {e}. Does the file exist?")
        return None
    except json.JSONDecodeError as e:
        print(f"Error reading {args.settings_file}: {e}. Is the file valid JSON?")
        return None
    except KeyError as e:
        print(
            f"Error reading {args.settings_file}: {e}. Does the file contain key {webhook_env_name}?"
        )
        return None
