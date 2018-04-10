# Django Confidence

![Python Supported Version](https://img.shields.io/badge/python-3.6-blue.svg)

Django Confidence is a Django app to make configuration files automatically.

## Quick start

1. Add the `confidence` package to your `INSTALLED_APPS` setting like this:

```python
    INSTALLED_APPS = [
        ...
        'confidence',
    ]
```

2. In your settings.py import `Configuration` class from `confidence` package like this:

```python
    from confidence import Configuration
```

3. Create a dictionary of config fieldsets like this:

```python
	markup = {
		'section': {
			'option': 'value'
		},

		'project': {
			'project_name': 'Awesome Project',
		}
	}
```

4. In your settings.py create a variable called `PROJECT_CONF` and fill it with a `Configuration` instance:

```python
	PROJECT_CONF = Configuration(filepath, markup)
```

**Optional**. You can use library of preset configuration files by importing from conf.presets. Example:

```python
	from confidence import Configuration
	from confidence.presets import ProjectPreset, OptionsPreset

	PROJECT_CONF = Configuration.compile_from_presets(filepath, [
		ProjectPreset(name='Awesome Project', version='1.0', site_url='http://awesome!'),
		OptionsPreset(debug=True, allowed_hosts=['127.0.0.1']),
	])
```

5. Run `python manage.py makeconf`. Configuration file will be created.

6. Edit your configuration file as you want to.

7. Use it in your `settings.py` by using get-like methods::

```python
	PROJECT_NAME = PROJECT_CONF.get('project', 'project_name')
	DEBUG = PROJECT_CONF.get_bool('options', 'debug')
	ALLOWED_HOSTS = PROJECT_CONF.get_csv('options', 'allowed_hosts')
```

8. Enjoy!

## Currently distributed presets

Configuration presets are intended to simplify the process of setting up configuration files.

Presets are using default and most common options for provided services.

At this moment there are different presets for some of common database management systems, cache and mailing modules.

Usage: `from confidence.presets import [PRESET_NAME]`

### Databases

* MySQL: `confidence.presets.MySQLPreset`

* PostgreSQL: `confidence.presets.PostgreSQLPreset`

### Cache

* Redis: `confidence.presets.RedisPresets`

### Mailing

* MailDev: `confidence.presets.MailDevPreset`
