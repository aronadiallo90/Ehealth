# from django import forms
import email
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms




class SignupForm(UserCreationForm,forms.Form):
    first_name = forms.CharField(max_length=63, label = 'Prénom',widget=forms.TextInput(attrs={'required':True}))
    last_name = forms.CharField(max_length=63, label = 'Nom',widget=forms.TextInput(attrs={'required':True}))
    email = forms.EmailField(max_length=63, label = 'Adresse Electronique',widget=forms.TextInput(attrs={'required':True}))
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','email','first_name', 'last_name','role')
    
        
        



class LoginForm(forms.Form):

    username = forms.CharField(max_length=63, label="Nom D'utilisateur")
    password = forms.CharField(max_length=63, widget = forms.PasswordInput, label='Mot de passe')


