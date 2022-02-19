from django import forms
from django.forms import Form

from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a new task...'}))

    class Meta:
        model = Task
        fields = ['title', 'completed']