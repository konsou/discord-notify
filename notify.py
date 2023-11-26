import _args
import _send


def main():
    args = _args.parse_args()
    _send.send(args)


if __name__ == '__main__':
    main()
