from django import forms
from .models import Novo_Usuario

class FormNovoUsuario(forms.Form):
    
    class Meta:
    	fields = ('__all__')
    	models = Novo_Usuario