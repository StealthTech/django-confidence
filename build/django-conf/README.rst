=====
Django Configuration
=====

Django Configuration is a Django app to make configuration files automatically.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "conf" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'conf',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('conf/', include('conf.urls')),
