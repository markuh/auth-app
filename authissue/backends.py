# coding:utf-8
from django.contrib.auth import get_user_model


class EmailBackend(object):
    @staticmethod
    def authenticate(email=None, password=None, **kwargs):
        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    @staticmethod
    def get_user(user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
