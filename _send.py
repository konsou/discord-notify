import requests

import _data
import _files
from _args import ParsedArgs


def send(args: ParsedArgs):
    data = _data.data(args)
    files = _files.files(args)

    response = requests.post(args.webhook_url, data=data, files=files)

    if response.status_code in (200, 204):
        print(f"Discord {args.message_level.value} notification sent successfully")
    else:
        print(
            f"Failed to send Discord {args.message_level.value} message. Status code: {response.status_code}"
        )
