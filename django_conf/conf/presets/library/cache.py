from ..generic import CachePreset


class RedisPreset(CachePreset):
    def __init__(self, enabled, tcp_addr, tcp_port, **kwargs):
        title, system = 'redis', 'redis'
        super(RedisPreset, self).__init__(title, system, enabled, tcp_addr, tcp_port, **kwargs)

