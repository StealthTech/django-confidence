from ..generic import CachePreset


class RedisPreset(CachePreset):
    DEFAULTS = {
        'title': 'redis',
        'tcp_addr': 'redis://127.0.0.1',
        'tcp_port': 6379,
    }

    def __init__(self, enabled, **kwargs):
        params = {
            'enabled': enabled,
        }
        params = self.merge_defaults(params, **kwargs)
        super(RedisPreset, self).__init__(**params)
