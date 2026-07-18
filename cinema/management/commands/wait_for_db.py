import time

from django.db import connections
from psycopg import OperationalError


def wait_for_db():
    while True:
        try:
            connections["default"].cursor()
            break
        except OperationalError:
            time.sleep(1)
