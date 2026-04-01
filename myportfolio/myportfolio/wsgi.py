import os
import sys

# Add your project directory to the Python path
project_home = '/home/maricarpordan/personal_portfolio/myportfolio'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'myportfolio.settings'

# Activate your virtual environment
activate_this = '/home/maricarpordan/.virtualenvs/myportfolio-venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Get WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
