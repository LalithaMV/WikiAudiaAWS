# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from wa.models import CustomUser

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    OPTIONS = (("ENG","English"),("KAN","Kannada"),("TEL","Telgu"),("TAM","Tamil"))
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']
    Languages = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=OPTIONS)
    class Meta:
        model = CustomUser
        fields = ("email","languages_known","first_name",'phoneNo')

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser