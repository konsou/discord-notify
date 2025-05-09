#!/usr/bin/python3
import _args
import _send


def main():
    args: _args.ParsedArgs = _args.parse_args()
    _send.send(args)


if __name__ == "__main__":
    main()
