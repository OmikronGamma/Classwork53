from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# class Registration(UserCreationForm):
#     username = forms.CharField(label='Login', help_text='')
#     password1 = forms.CharField(label='Password', help_text='', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
#     password2 = forms.CharField(label='Confirm password', help_text='', widget=forms.PasswordInput())
#
#
#     class Meta():
#         model = User
#         fields = {'email', 'first_name', 'last_name'}



class Registration(UserCreationForm):
    username = forms.CharField(label='Login')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput())
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'qwe@asd.zxc'}))
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name', required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')


class Searchform(forms.Form):
    search_field = forms.CharField(label='Search movies:')
