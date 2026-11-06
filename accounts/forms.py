from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[c for c in User.Role.choices if c[0] != User.Role.ADMIN]
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "company_name", "role")