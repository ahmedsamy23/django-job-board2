from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm): # UserCreationForm: is a form that is used to create a new user
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' ,'first_name','last_name','email']

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city' , 'phone_number' , 'image']

