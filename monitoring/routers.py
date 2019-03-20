from django.conf import settings
from django.db import connections

import socket


def test_connection_to_db(database_name):
    try:
        db_definition = getattr(settings, 'DATABASES')[database_name]
        s = socket.create_connection((db_definition['HOST'], db_definition['PORT']), 5)
        s.close()
        return True
    except (AttributeError, socket.timeout) as e:
        return False


class MonitoringRouter(object):
    """A router that defaults reads to the follower but provides a failover back to the default"""

    def db_for_read(self, model, **hints):

        return 'local'

    def db_for_write(self, model, **hints):

        return 'local'
