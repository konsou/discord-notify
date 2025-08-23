import requests

import _data
import _files
from _args import ParsedArgs
from _exit_codes import ExitCode


def send(args: ParsedArgs) -> ExitCode:
    data = _data.data(args)
    files = _files.files(args)
    exit_code = ExitCode.SUCCESS

    response = requests.post(args.webhook_url, data=data, files=files)

    if response.status_code == 413:  # Payload too large
        exit_code = ExitCode.WARNING
        print(
            f"WARNING: Failed to send Discord message - got response 413 (payload too large). Retrying without attachment..."
        )
        response = requests.post(args.webhook_url, data=data)

    if response.status_code in (200, 204):
        print(f"Discord {args.message_level.value} message sent successfully")
    else:
        exit_code = ExitCode.ERROR
        print(
            f"Failed to send Discord {args.message_level.value} message. Status code: {response.status_code}"
        )

    return exit_code
