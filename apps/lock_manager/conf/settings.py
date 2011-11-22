from django.conf import settings

DEFAULT_LOCK_TIMEOUT_VALUE = 10

DEFAULT_LOCK_TIMEOUT = getattr(settings, 'LOCK_MANAGER_DEFAULT_LOCK_TIMEOUT', DEFAULT_LOCK_TIMEOUT_VALUE)