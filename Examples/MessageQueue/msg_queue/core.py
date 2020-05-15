import json
from .utils.msg_utils import generate_id


def parse_message(json_msg: str) -> dict:
    msg = json.loads(json_msg)
    if not msg.get('id'):
        msg.id = generate_id()
    return msg


def process_message(msg: dict, middleware: list = []) -> None:
    result = msg
    for m in middleware:
        result = m(result)
    print(result)


def process_json(json_msg: str, middleware: list = []) -> None:
    msg = parse_message(json_msg)
    process_message(msg, middleware)
