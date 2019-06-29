from . import Preset


class MailDevPreset(Preset):
    title = 'maildev'
    verbose_name = 'MailDev'

    options = {
        'enabled': False,
        'use_tls': False,
        'host': '127.0.0.1',
        'port': 1025,
        'host_user': None,
        'default_from_email': None,
        'feedback_email': None,
    }
