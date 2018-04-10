from ..generic import EmailPreset


class MailDevPreset(EmailPreset):
    DEFAULTS = {
        'title': 'maildev',
        'use_tls': False,
        'host': '127.0.0.1',
        'host_user': None,
        'port': 1025,
    }

    def __init__(self, enabled, default_from_email=None, feedback_email=None, **kwargs):
        params = {
            'enabled': enabled,
            'default_from_email': default_from_email,
            'feedback_email': feedback_email,
        }
        params = self.merge_defaults(params, **kwargs)
        super(MailDevPreset, self).__init__(**params)
