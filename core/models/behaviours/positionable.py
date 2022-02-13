# -*- coding: utf-8 -*-

from django.db import models


class Positionable(models.Model):
    position = models.IntegerField()

    class Meta:
        abstract = True
