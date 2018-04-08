from ..generic import DatabasePreset


class MySQLPreset(DatabasePreset):
    def __init__(self, name, user, password, tcp_addr, tcp_port, **kwargs):
        title = 'mysql'
        super(MySQLPreset, self).__init__(title, name, user, password, tcp_addr, tcp_port, **kwargs)


class PostgreSQLPreset(DatabasePreset):
    def __init__(self, name, user, password, tcp_addr, tcp_port, **kwargs):
        title = 'postgresql'
        super(PostgreSQLPreset, self).__init__(title, name, user, password, tcp_addr, tcp_port, **kwargs)

