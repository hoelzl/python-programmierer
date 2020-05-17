# The final version of the main file.
# Look at main_v1.py and main_v2.py first.

import argparse
import json

from msgqueue.utils.main_utils import configure_middleware
from .core import process_messages


def get_args():
    parser = argparse.ArgumentParser(
        description="Process messages in json format.")
    parser.add_argument('messages',
                        type=argparse.FileType('r'),
                        help="a file with messages in json format")
    parser.add_argument('--log', action='store_true',
                        help="enable logging")
    parser.add_argument("--auth", action='store_true',
                        help="require authentication in messages")
    parser.add_argument('--timestamp', action='store_true',
                        help="add a timestamp to the messages")
    return parser.parse_args()


def main():
    args = get_args()
    middleware = configure_middleware(args)
    msgs = json.load(args.messages)

    process_messages(msgs, middleware)


if __name__ == '__main__':
    main()
