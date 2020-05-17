def log(msg: dict) -> dict:
    print(f"log: processing message {msg.get('id', '<no id>')}")
    return msg
