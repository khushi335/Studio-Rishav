import os
import sys

# Project directory
project_home = "/home1/studiori/studiorishav.com/rishav"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtual environment
activate_this = "/home1/studiori/virtualenv/studiorishav.com/rishav/3.10/bin/activate_this.py"
with open(activate_this) as file_:
    exec(file_.read(), {"__file__": activate_this})

# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rishav.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()