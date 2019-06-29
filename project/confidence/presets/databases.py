from . import Preset


class MySQLPreset(Preset):
    title = 'mysql'
    verbose_name = 'MySQL'

    options = {
        'enabled': False,
        'name': None,
        'user': None,
        'password': None,
        'tcp_addr': '127.0.0.1',
        'tcp_port': 3306,
    }


class PostgreSQLPreset(Preset):
    title = 'postgresql'
    verbose_name = 'PostgreSQL'

    options = {
        'enabled': False,
        'name': None,
        'user': None,
        'password': None,
        'tcp_addr': '127.0.0.1',
        'tcp_port': 5432,
    }

