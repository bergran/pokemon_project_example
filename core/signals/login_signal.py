# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.conf import settings


def get_key_user(username):
    return 'user_attempts:{}'.format(username)


def login_success(sender, user, request, **kwargs):
    cache.set(get_key_user(user.username), 0, 0)


def login_fail(sender, credentials, request, **kwargs):
    from django.contrib.auth.models import User

    username = credentials.get('username')
    user_prefix = get_key_user(username)
    attempts = cache.get(user_prefix, 0) + 1

    cache.set(
        get_key_user(user_prefix), attempts, 300
    )

    if attempts > settings.LOGIN_ATTEMPTS:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return

        user.is_active = False
