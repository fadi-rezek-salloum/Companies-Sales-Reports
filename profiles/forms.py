from django import forms
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=75, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50)

    password = forms.CharField(max_length=75, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(max_length=75, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            msg = 'passwords do not match'
            self.add_error('confirm_password', msg)

        return self.cleaned_data


    class Meta:
        model = Profile
        exclude = ('user',)