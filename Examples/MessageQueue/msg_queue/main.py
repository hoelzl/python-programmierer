import json
import os
import msg_queue.core as core
from msg_queue.middleware.log import log
from msg_queue.middleware.authenticate import authenticate
from msg_queue.middleware.timestamp import timestamp

full_middleware = [log, authenticate, timestamp]
no_auth_middleware = [log, timestamp]
no_middleware = []

middleware = full_middleware

if __name__ == '__main__':
    input_file_name = os.path.join(os.getcwd(), 'messages.json')
    with open(input_file_name, 'r') as input_file:
        msgs = json.load(input_file)
        for msg in msgs:
            core.process_message(msg, middleware)
