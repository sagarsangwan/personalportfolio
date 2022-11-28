from .models import UserIpAddress, Contactme

# from django.contrib.auth.models import User
# import requests

from django import forms
from .models import *


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = Contactme
        fields = ['name', 'email', 'message']
