from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
User = get_user_model()

class EmailPhoneAuthBackend(BaseBackend):
    """
    Custom authentication backend for authenticating users using email or phone number.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(phone_no=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None