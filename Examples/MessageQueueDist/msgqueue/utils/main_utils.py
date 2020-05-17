import argparse

from ..middleware.authenticate import authenticate
from ..middleware.log import log
from ..middleware.timestamp import timestamp


def configure_middleware(args: argparse.Namespace) -> list:
    middleware = []
    if args.log:
        middleware.append(log)
    if args.auth:
        middleware.append(authenticate)
    if args.timestamp:
        middleware.append(timestamp)
    return middleware
