from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, Events

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','email','password1','password2']
    


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
    

         