# Django Confidence

![Python Supported Version](https://img.shields.io/badge/python-3.6-blue.svg)

Django Confidence is a Django app to make configuration files automatically.

## Quick start

1. Add "confidence" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'confidence',
    ]

2. In your settings.py import "Configuration" class from "confidence" package like this::

    from confidence import Configuration

3. Create a dictionary of config fieldsets like this::

	markup = {
		'section': {
			'option': 'value'
		},

		'project': {
			'project_name': 'Awesome Project',
		}
	}

4. In your settings.py create a variable called PROJECT_CONF and fill it with a Configuration instance::

	PROJECT_CONF = Configuration(filepath:str, markup:dict)

4.1 Optional. You can use library of preset configuration files by importing from conf.presets. Example::

	from confidence import Configuration
	from confidence.presets import ProjectPreset, OptionsPreset

	PROJECT_CONF = Configuration.compile_from_presets(filepath, [
		ProjectPreset(name='Awesome Project', version='1.0', site_url='http://awesome!'),
		OptionsPreset(debug=True, allowed_hosts=['127.0.0.1']),
	])

5. Run python manage.py makeconf. Configuration file will be created.

6. Edit your configuration file as you want to.

7. Use it in your settings.py by using get-like methods::

	PROJECT_NAME = PROJECT_CONF.get('project', 'project_name')
	DEBUG = PROJECT_CONF.get_bool('options', 'debug')
	ALLOWED_HOSTS = PROJECT_CONF.get_csv('options', 'allowed_hosts')

8. Enjoy!

## Currently distributed presets

Configuration presets are intended to simplify the process of setting up configuration files.

Presets are using default and most common options for provided services.

At this moment there are different presets for some of common database management systems, cache and mailing modules.

Usage: `from confidence.presets import [PRESET_NAME]`

### Databases

1. MySQL: `confidence.presets.MySQLPreset`

2. PostgreSQL: `confidence.presets.PostgreSQLPreset`

### Cache

1. Redis: `confidence.presets.RedisPresets`

### Mailing

1. MailDev: `confidence.presets.MailDevPreset`
