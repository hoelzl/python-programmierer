import json
import os
from .core import process_messages
from .middleware.log import log
from .middleware.authenticate import authenticate
from .middleware.timestamp import timestamp

full_middleware = [log, authenticate, timestamp]
no_auth_middleware = [log, timestamp]
no_middleware = []

middleware = full_middleware

if __name__ == '__main__':
    input_file_name = os.path.join(os.getcwd(), 'messages.json')
    with open(input_file_name, 'r') as input_file:
        msgs = json.load(input_file)
    process_messages(msgs, middleware)
