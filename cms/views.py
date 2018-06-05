# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Novo_Usuario
from .forms import FormNovoUsuario
from .forms import ContactForm

def cms(request):
    return render(request, 'base.html')

def cad_novo_usuario(request):

    #form_inst = get_object_or_404(pk = pk)
    if request.method == 'POST':
        form = FormNovoUsuario(request.POST)
        if form.is_valid():
            salvar = form.save(commit=False)
            salvar.sobrenome = form.cleaned_data['sobrenome']
            salvar.senha = form.cleaned_data['senha']
            salvar.save()
            return redirect('novo_usuario.html')
    else:
        form = FormNovoUsuario()

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

def contato(request):
    form_class = ContactForm
    return render(request, 'contato.html', {'form': form_class})