# Django Confidence

![Python Supported Version](https://img.shields.io/badge/python-3.6-blue.svg)

Django Confidence is a Django app to make configuration files automatically.

This app is developed to help developers create their own layout to configuration files quick and simple with built-in **dictionaries** or by using **configuration presets** (that make it even more easier).

## Quick start

0. Run `pip install django-confidence`

1. Add the `confidence` package to your `INSTALLED_APPS` setting like this:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
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

5. Run `python manage.py makeconfig`. Configuration file will be created.

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

**Usage**: `from confidence.presets import [PRESET_NAME]`

### Databases

* **MySQL**: `confidence.presets.MySQLPreset`

* **PostgreSQL**: `confidence.presets.PostgreSQLPreset`

### Cache

* **Redis**: `confidence.presets.RedisPresets`

### Mailing

* **MailDev**: `confidence.presets.MailDevPreset`

## Available management commands

* **makeconfig [--force]**: creates a configuration file at specified in `PROJECT_CONF` (`Configuration` instance) declared at `settings.py`. Optional: use [--force] to overwrite file if it exists.

* **repairconfig**: repairs configuration file if any configuration sections or options are missing.
