import json
import os
from simple_msgqueue.core import process_messages
from simple_msgqueue.middleware.log import log
from simple_msgqueue.middleware.authenticate import authenticate
from simple_msgqueue.middleware.timestamp import timestamp

full_middleware = [log, authenticate, timestamp]
no_auth_middleware = [log, timestamp]
no_middleware = []

middleware = full_middleware

if __name__ == '__main__':
    input_file_name = os.path.join(os.getcwd(), 'messages.json')
    with open(input_file_name, 'r') as input_file:
        msgs = json.load(input_file)
    process_messages(msgs, middleware)
