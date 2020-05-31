from django import forms
from django.forms import ModelForm

from . models import News,DataRegistro

# class RegistroForm(forms.Form):
#     username = forms.CharField(max_length=100,
#                                widget=forms.TextInput(attrs={'class':'form-control',
#                                                              'placeholder':'Digite username'
#                                                              }))
#     password = forms.CharField(max_length=100,
#                                widget=forms.PasswordInput(attrs={'class':'form-control',
#                                                              'placeholder':'Digite a senha'
#                                                              }))
#     email = forms.CharField(max_length=100,
#                                widget=forms.EmailInput(attrs={'class':'form-control',
#                                                              'placeholder':'Digite o email'
#                                                              }))
#     tel = forms.CharField(max_length=100,
#                                widget=forms.NumberInput(attrs={'class':'form-control',
#                                                              'placeholder':'Digite o telefone'
#                                                              }))

class RegistroForm(ModelForm):

    class Meta:
        model = DataRegistro
        fields = ['username', 'password','email','tel']

# class LoginForm(ModelForm):forms.Form
class LoginForm(ModelForm):
    password = forms.CharField(max_length=100,
                                   widget=forms.PasswordInput(attrs={'class':'form-control'
                                                                 }))
    class Meta:
        model = DataRegistro
        fields = ['username']
