from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
