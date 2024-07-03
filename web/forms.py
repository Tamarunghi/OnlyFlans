from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #clase interna de django proporciona datos o configuracion adicional#
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
