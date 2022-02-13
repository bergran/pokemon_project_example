# -*- coding: utf-8 -*-

from django.db import models


class Descriptable(models.Model):
    description = models.TextField()

    class Meta:
        abstract = True
