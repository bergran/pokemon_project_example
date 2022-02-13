# -*- coding: utf-8 -*-

from django.db import models


class Deleteable(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True