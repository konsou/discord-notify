import requests

import _data
import _files
from _args import ParsedArgs


def send(args: ParsedArgs):
    data = _data.data(args)
    files = _files.files(args)

    response = requests.post(args.webhook_url, data=data, files=files)

    # Check for success
    if response.status_code in (200, 204):
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
