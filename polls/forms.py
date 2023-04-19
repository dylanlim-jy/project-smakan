from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'pin')
        widgets = {
            
            'pin': forms.PasswordInput()
        }

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_cache = None
        self.fields['email'].label = 'Email'
        self.fields['pin'].label = 'PIN'
        self.fields.pop('username', None)
        self.fields.pop('password', None)
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    pin = forms.IntegerField(widget=forms.PasswordInput())
    # TODO add validation

    
    def clean(self):
        email = self.cleaned_data.get('email')
        pin = self.cleaned_data.get('pin')
        if email and pin:
            self.user_cache = authenticate(self.request, email=email, pin=pin)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data

class CreatePlaceForm(forms.Form):
    pass

class UpdatePlaceForm(forms.Form):
    pass

class CreateSuggestionForm(forms.Form):
    pass

class UpdateSuggestionForm(forms.Form):
    pass
