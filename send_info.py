import _args
import _send


def send_info():
    args = _args.parse_args(webhook_url_type='WEBHOOK_URL_INFO')
    _send.send(args)


if __name__ == '__main__':
    send_info()
