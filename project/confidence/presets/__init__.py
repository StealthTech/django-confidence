# TODO: Service presets

class Preset:
    # defaults = None
    title = None
    verbose_name = None

    options = dict()

    @classmethod
    def get_full_verbose_name(cls):
        return f'{cls.verbose_name} Preset'

    # def __init__(self, options=None, **kwargs):
    #     self.options = options if options is not None else dict()
    #
    #     allowed_params = self._prepare_params(kwargs)
    #     self.options.update(allowed_params)
    #
    #     if self.defaults is not None:
    #         self.options.update(self.defaults)
    #
    # def _prepare_params(self, params):
    #     whitelist = self.get_allowed_params()
    #     result = dict()
    #
    #     if not len(whitelist):
    #         return result
    #
    #     for key in whitelist:
    #         value = params.get(key)
    #         result[key] = value
    #
    #     return result
    #
    # def get_allowed_params(self):
    #     raise NotImplementedError
    #
    # @property
    # def markup(self):
    #     return {self.title: self.options}
