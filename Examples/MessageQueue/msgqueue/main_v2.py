import argparse
import json
import os

from msgqueue.utils.main_utils import configure_middleware
from .core import process_messages


def get_args():
    parser = argparse.ArgumentParser(
        description="Process messages in json format.")
    parser.add_argument('messages',
                        help="a file with messages in json format")
    parser.add_argument('--log', action='store_true',
                        help="enable logging")
    parser.add_argument("--auth", action='store_true',
                        help="require authentication in messages")
    parser.add_argument('--timestamp', action='store_true',
                        help="add a timestamp to the messages")
    return parser.parse_args()


def compute_input_file_name(args):
    if os.path.isabs(args.messages):
        return args.messages
    else:
        return os.path.join(os.getcwd(), args.messages)


def main():
    args = get_args()
    middleware = configure_middleware(args)
    input_file_name = compute_input_file_name(args)

    with open(input_file_name, 'r') as input_file:
        msgs = json.load(input_file)

    process_messages(msgs, middleware)


if __name__ == '__main__':
    main()
