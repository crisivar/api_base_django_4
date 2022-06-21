
from hashlib import md5
from django.contrib.auth.backends import ModelBackend

from users.models import User


class UserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']

        try:
            user = User.objects.get(username=username)

            encoded_password = md5(password.encode())

            valid = encoded_password.hexdigest() == user.password

            if valid is True:
                return user
        except User.DoesNotExist:
            pass
