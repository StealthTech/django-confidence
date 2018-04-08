class Preset:
    def __init__(self, title, options):
        self.__title = title
        self.__options = options

    @property
    def markup(self):
        # print({self.__title: self.__options})
        return {self.__title: self.__options}


class ProjectPreset(Preset):
    def __init__(self, name, version, site_url, title='project', **kwargs):
        markup = {
            'name': name,
            'version': version,
            'site_url': site_url,
        }
        markup.update(**kwargs)
        super(ProjectPreset, self).__init__(title, markup)


class OptionsPreset(Preset):
    def __init__(self, debug, allowed_hosts, secret_key=None, title='options', **kwargs):
        markup = {
            'secret_key': secret_key,
            'debug': debug,
            'allowed_hosts': allowed_hosts,
            'database': None,
            'cache': None,
        }
        markup.update(**kwargs)
        super(OptionsPreset, self).__init__(title, markup)


class DatabasePreset(Preset):
    def __init__(self, title, name, user, password, tcp_addr, tcp_port, **kwargs):
        markup = {
            'name': name,
            'user': user,
            'password': password,
            'tcp_addr': tcp_addr,
            'tcp_port': tcp_port,
        }
        markup.update(**kwargs)
        super(DatabasePreset, self).__init__(title, markup)


class CachePreset(Preset):
    def __init__(self, title, enabled, tcp_addr, tcp_port, **kwargs):
        markup = {
            'enabled': enabled,
            'tcp_addr': tcp_addr,
            'tcp_port': tcp_port
        }
        markup.update(**kwargs)
        super(CachePreset, self).__init__(title, markup)
