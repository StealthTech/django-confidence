=====
Django Confidence
=====

Django Confidence is a Django app to make configuration files automatically.

This app is developed to help developers create their own layout to configuration files quick and simple with built-in dictionaries or by using configuration presets (that make it even more easier).

Quick start
-----------

1. Add "confidence" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        'django.contrib.admin', 
        'django.contrib.auth',
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

5. Run python manage.py makeconfig. Configuration file will be created.

6. Edit your configuration file as you want to.

7. Use it in your settings.py by using get-like methods::

	PROJECT_NAME = PROJECT_CONF.get('project', 'project_name')
	DEBUG = PROJECT_CONF.get_bool('options', 'debug')
	ALLOWED_HOSTS = PROJECT_CONF.get_csv('options', 'allowed_hosts')

8. Enjoy!
