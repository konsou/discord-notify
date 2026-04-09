from _args import ParsedArgs


def data(args: ParsedArgs) -> dict:
    # Discord rejects content with length over 2000
    if len(args.message) > 2000:
        print(f"WARNING: message length over 2000. Truncating.")
        args.message = args.message[:1988] + " [truncated]"
    return {"content": args.message}
