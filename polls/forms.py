from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class RegisterForm(forms.Form):
    pass

class LoginForm(forms.Form):
    pass

class CreatePlaceForm(forms.Form):
    pass

class UpdatePlaceForm(forms.Form):
    pass

class CreateSuggestionForm(forms.Form):
    pass

class UpdateSuggestionForm(forms.Form):
    pass
