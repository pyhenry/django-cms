# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def cms(request):
    return render(request, 'base.html')

def cad_novo_usuario(request):
    return render(request, 'novo_usuario.html')

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