# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Novo_Usuario(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
