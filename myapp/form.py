from django import forms
from django.http import request
from .models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'email',)
