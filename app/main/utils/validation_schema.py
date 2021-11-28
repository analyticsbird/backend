register_schema = {
        'type': 'object',
        'properties': {
            'full_name': {'type': 'string'},
            'email': {'type': 'string'},
            'password': {'type': 'string'}
        },
        'required': ['email', 'password','full_name']
}

login_schema = {
        'type': 'object',
        'properties': {
            'email': {'type': 'string'},
            'password': {'type': 'string'}
        },
        'required': ['email', 'password']
}

app_schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'}
        },
        'required': ['name']
}