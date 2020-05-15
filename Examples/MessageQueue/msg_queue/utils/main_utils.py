import argparse

from msg_queue.middleware.authenticate import authenticate
from msg_queue.middleware.log import log
from msg_queue.middleware.timestamp import timestamp


def configure_middleware(args: argparse.Namespace) -> list:
    middleware = []
    if args.log:
        middleware.append(log)
    if args.auth:
        middleware.append(authenticate)
    if args.timestamp:
        middleware.append(timestamp)
    return middleware