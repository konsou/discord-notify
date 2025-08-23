#!/usr/bin/python3
import sys

import _args
import _send


def main():
    args: _args.ParsedArgs = _args.parse_args()
    send_exit_code = _send.send(args)
    sys.exit(send_exit_code.value)


if __name__ == "__main__":
    main()
