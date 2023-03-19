from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterUser(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username',]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=True)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user_profile = Profile(
            user = user
        )

        user_profile.save()
        return user, user_profile

class LoginUser(forms.Form):
    username =  forms.CharField(label="Email Address", max_length=200)
    password = forms.CharField(label="Password", max_length=200, widget=forms.PasswordInput())