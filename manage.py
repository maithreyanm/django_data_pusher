#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_data_pusher.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# python manage.py makemigrations data_push
# python manage.py migrate
# https://www.talentica.com/blogs/building-a-basic-rest-api-using-django-rest-framework/
# https://books.agiliq.com/projects/django-orm-cookbook/en/latest/one_to_many.html
# https://www.dev2qa.com/how-to-enable-or-disable-csrf-validation-in-django-web-application/

