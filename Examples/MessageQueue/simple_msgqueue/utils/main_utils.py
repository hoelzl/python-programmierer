import argparse

from ..middleware.authenticate import authenticate, Authenticator
from ..middleware.log import log
from ..middleware.timestamp import timestamp


def configure_middleware_v1(args: argparse.Namespace) -> list:
    middleware = []
    if args.log:
        middleware.append(log)
    if args.auth:
        middleware.append(authenticate)
    if args.timestamp:
        middleware.append(timestamp)
    return middleware


def configure_middleware_v2(args: argparse.Namespace) -> list:
    middleware = []
    if args.log:
        middleware.append(log)
    if args.auth:
        middleware.append(Authenticator(args.auth))
    if args.timestamp:
        middleware.append(timestamp)
    return middleware
