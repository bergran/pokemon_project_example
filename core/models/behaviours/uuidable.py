# -*- coding: utf-8 -*-

from uuid import uuid4
from django.db import models


class Uuidable(models.Model):
    uuid = models.UUIDField(default=uuid4)

    class Meta:
        abstract = True
