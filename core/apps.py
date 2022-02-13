from django.apps import AppConfig
from django.contrib.auth.signals import user_login_failed, user_logged_in
from .signals.login_signal import login_success, login_fail
from django.conf import settings


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        if settings.LOGIN_ACTIVATE == 'yes':
            user_login_failed.connect(login_fail)
            user_logged_in.connect(login_success)
