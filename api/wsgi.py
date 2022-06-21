"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = get_wsgi_application()


"""
# Add the site-packages of the chosen virtualenv to work with

import os
import sys
import site
from django.core.wsgi import get_wsgi_application
site.addsitedir('/var/www/html/api/env/lib/python3.8/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/html/api/backend')
sys.path.append('/var/www/html/api/backend/api')

os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'

# Activate your virtual env
activate_env = os.path.expanduser('/var/www/html/api/env/bin/activate_this.py')
exec(open(activate_env).read(), {'__file__': activate_env})


application = get_wsgi_application()
"""
