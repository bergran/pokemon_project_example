# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Owneable(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s')

    class Meta:
        abstract = True
