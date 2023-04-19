from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def _create_user(self, email, username, pin, **kwargs):
        if not email:
            raise ValueError('Please provide a valid e-mail.')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_pin(pin)
        user.save()
        return user
    
    def create_user(self, email=None, username=None, pin=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        if pin is None:
            raise ValueError('A 4-digit PIN must be supplied.')
        
        return self._create_user(email=email, username=username, pin=pin, **kwargs)

    def create_superuser(self, email=None, username=None, pin=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if pin is None:
            raise ValueError('A 4-digit PIN must be supplied.')

        return self._create_user(email=email, username=username, pin=pin, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=False, default='', unique=True)
    username = models.CharField(max_length=255, blank=False, default='')
    pin_regex = RegexValidator(regex=r"^[0-9]{4,4}$", message="Please enter a 4-digit pin")
    pin = models.IntegerField(blank=False, validators=[pin_regex])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_name(self):
        return self.username

    def set_pin(self, pin):
        self.pin = pin
        self.save()

    def check_pin(self, pin):
        return self.pin == pin

