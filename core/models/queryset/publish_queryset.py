# -*- coding: utf-8 -*-

from django.db import models
from django.utils.timezone import now


class PublishQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish_date__lte=now())

    def not_published(self):
        return self.filter(publish_date__gt=now())
