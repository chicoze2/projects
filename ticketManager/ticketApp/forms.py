from django.forms  import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import admin


from .models import *

class CreateProtocolForm(ModelForm):
    class Meta:
        model = Protocolo
        fields = ['name', 'description']

class EditProtocolForm(ModelForm):
   class Meta:
      model = Protocolo
      fields = ['name', 'description']


class CustomUserCreationForm(UserCreationForm):
   class Meta(UserCreationForm.Meta):
      model = User
      fields = UserCreationForm.Meta.fields + ('name', 'username')




class SimpleUserEditForm(ModelForm):
   class Meta:
      model = User
      fields = ['username', 'name', 'password']

class AdvancedUserEditForm(ModelForm):
   class Meta:
      model = User
      fields = '__all__'
