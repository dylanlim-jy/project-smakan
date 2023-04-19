from django.contrib.auth.backends import BaseBackend
from .models import User

class PinBackend(BaseBackend):
    def authenticate(self, request, email=None, pin=None, **kwargs):    
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_pin(pin):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
