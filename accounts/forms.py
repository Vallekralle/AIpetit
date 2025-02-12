from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django import forms


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=100, label="Vorname")
    last_name = forms.CharField(required=True, max_length=100, label="Nachname")
    email = forms.EmailField(required=True, label="Ihre Email")

    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields