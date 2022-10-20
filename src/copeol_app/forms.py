from django import forms
from .models import Commande, Facture, Fiche_analyse, Fiche_reception 

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
