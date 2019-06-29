from . import Preset


class RedisPreset(Preset):
    title = 'redis'
    verbose_name = 'Redis'

    options = {
        'enabled': False,
        'tcp_addr': 'redis://127.0.0.1',
        'tcp_port': 6379,
    }
