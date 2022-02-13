# -*- coding: utf-8 -*-

from django.db import models


class Nameable(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        abstract = True
