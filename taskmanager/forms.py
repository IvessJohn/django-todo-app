from django import forms
from django.forms import Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *


class TaskForm(forms.ModelForm):
    """A form for quickly creating new tasks."""

    title: forms.CharField = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Add a new task..."})
    )

    class Meta:
        model = Task
        fields = ["title", "completed"]


class RegisterForm(UserCreationForm):
    """A custom form for user creation."""

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        exclude = []