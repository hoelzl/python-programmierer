import argparse

from ..middleware.authenticate import Authenticator
from ..middleware.log import log
from ..middleware.timestamp import timestamp


def configure_middleware(args: argparse.Namespace) -> list:
    middleware = []
    if args.log:
        middleware.append(log)
    if args.auth:
        middleware.append(Authenticator(args.auth))
    if args.timestamp:
        middleware.append(timestamp)
    return middleware
