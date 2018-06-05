from django import forms
from .models import Novo_Usuario

class FormNovoUsuario(forms.ModelForm):

    #nome = forms.CharField(max_length=200, label='nome')
    #sobrenome = forms.CharField(max_length=200, label='sobrenome')
    #senha = forms.CharField(max_length=50, label='senha')


    class Meta:
        model = Novo_Usuario
        fields = ('nome', 'sobrenome', 'senha')

class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)