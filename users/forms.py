from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from users.models import User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'description', 'image')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(), label="Ник или почта пользователя")
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")


class UserUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(), label='Фото профиля')

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "image",'description')
