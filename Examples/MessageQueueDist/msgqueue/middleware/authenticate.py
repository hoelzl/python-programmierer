def authenticate(msg: dict) -> dict:
    print(f"-> Authenticating message {msg.get('id', '<no id>')}")
    if msg.get('auth') == 'secret!':
        return msg
    else:
        return {
            'id': msg.get('id', "No ID!"),
            'error_code': 401,
            'error_msg': "Unauthorized"
        }
