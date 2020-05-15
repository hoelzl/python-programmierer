import datetime


def timestamp(msg: dict) -> dict:
    msg['timestamp'] = datetime.datetime.now()
    return msg
