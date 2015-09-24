"""
WSGI config for goal_tracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

## assuming your django settings file is at '/home/bshaurette/mysite/mysite/settings.py'
## and your manage.py is is at '/home/bshaurette/mysite/manage.py'
path = '/home/bshaurette/goal_tracker/goal_tracker'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'goal_tracker.settings'

## then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

## or, for older django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
