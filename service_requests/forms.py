

from django import forms
from .models import ServiceRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = [ 'name','request_type', 'details','attachment']
class UserLoginForm(AuthenticationForm):
    pass        



class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1']
