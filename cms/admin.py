# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Novo_Usuario

class AdminUsuario(admin.ModelAdmin):
	list_display = ['nome', 'sobrenome', 'senha']

admin.site.register(Novo_Usuario, AdminUsuario)