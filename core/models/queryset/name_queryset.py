# -*- coding: utf-8 -*-

from django.db import models


class NameQuerySet(models.QuerySet):
    def named_by(self, name):
        return self.filter(name=name)
