from django import forms
from captcha.fields import CaptchaField
#from . import models

class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=128, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password', max_length=256, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField(label='validation code',)

class RegisterForm(forms.Form):
    gender = (
        ('male','Man'),
        ('female','Woman')
    )
    username = forms.CharField(label='username', max_length=128, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='password', max_length=256, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password', max_length=256, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email-addrs',widget=forms.EmailInput(attrs={'class':'form-control'}))
    sex = forms.ChoiceField(label='gender',choices=gender)
    captcha = CaptchaField(label='validation')
'''ModelForm

    class Meta:
            model = models.User
            fields = ['name', 'password']

        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['name'].label = 'username'
            self.fields['password'].label = 'password'
'''