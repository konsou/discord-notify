from _args import ParsedArgs


def data(args: ParsedArgs) -> dict:
    content = args.message
    # Discord rejects content with length over 2000
    if len(content) > 2000:
        print(f"WARNING: message length over 2000. Truncating.")
        content = content[:1988] + " [truncated]"
    return {"content": content}
