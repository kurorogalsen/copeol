from django import forms
from .models import Commande, Facture, Fiche_analyse, Fiche_reception 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ),error_messages={
               'required': 'The username field is required.'
        })
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ),error_messages={
               'required': 'The password field is required.'
        })

# Create your forms here.
class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'

class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Fiche_reception
        fields = '__all__'

class AnalyseForm(forms.ModelForm):
    class Meta:
        model = Fiche_analyse
        fields = '__all__'

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = '__all__'


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'group')