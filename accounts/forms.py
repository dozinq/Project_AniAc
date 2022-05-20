from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    last_name = forms.CharField(label="별명")

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'last_name')
