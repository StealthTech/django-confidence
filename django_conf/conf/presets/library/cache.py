from ..generic import CachePreset


class RedisPreset(CachePreset):
    def __init__(self, enabled, tcp_addr, tcp_port, **kwargs):
        title = 'redis'
        super(RedisPreset, self).__init__(title, enabled, tcp_addr, tcp_port, **kwargs)

