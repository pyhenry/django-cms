# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Novo_Usuario
from .forms import FormNovoUsuario

def cms(request):
    return render(request, 'base.html')

def cad_novo_usuario(request):

    '''
    Tenho dúvida nessa parte, não entendo porque o atributo .save() não roda
    Ou talvez seja em models
    '''


    form = FormNovoUsuario(request.POST)
    if request.method == 'POST':
        novo_usuario = model.Novo_Usuario()
        novo_usuario.nome = form.cleaned_data('nome')
        # ... daí um para cada campo que você tiver ...
        novo_usuario.save()
    return form.save()
    return render(request, 'novo_usuario.html', {'form': form})

def cad_novo_cliente(request):
    return render(request, 'novo_cliente.html')

def cad_novo_produto(request):
    return render(request, 'novo_produto.html')

def cad_notas(request):
    return render(request, 'cadastrar_nota.html')

def nova_venda(request):
    return render(request, 'nova_venda.html')

def estoque(request):
    return render(request, 'estoque.html')