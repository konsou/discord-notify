from _args import ParsedArgs


def data(args: ParsedArgs) -> dict:
    return {'content': args.message}

