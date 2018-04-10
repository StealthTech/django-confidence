from ..generic import DatabasePreset


class MySQLPreset(DatabasePreset):
    DEFAULTS = {
        'title': 'mysql',
        'tcp_addr': '127.0.0.1',
        'tcp_port': 3306,
    }

    def __init__(self, name, user, password, **kwargs):
        params = {
            'name': name,
            'user': user,
            'password': password,
        }
        params = self.merge_defaults(params, **kwargs)
        super(MySQLPreset, self).__init__(**params)


class PostgreSQLPreset(DatabasePreset):
    DEFAULTS = {
        'title': 'postgresql',
        'tcp_addr': '127.0.0.1',
        'tcp_port': 5432,
    }

    def __init__(self, name, user, password, **kwargs):
        params = {
            'name': name,
            'user': user,
            'password': password,
        }
        params = self.merge_defaults(params, **kwargs)
        super(PostgreSQLPreset, self).__init__(**params)

