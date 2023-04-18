from django.forms import Form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from .models import User

# possibly don't need this
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'pin')

class LoginForm(Form):
    pass

class CreatePlaceForm(Form):
    pass

class UpdatePlaceForm(Form):
    pass

class CreateSuggestionForm(Form):
    pass

class UpdateSuggestionForm(Form):
    pass
