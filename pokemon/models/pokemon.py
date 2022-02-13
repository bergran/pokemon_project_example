from django.db import models


class Pokemon(models.Model):
    number = models.IntegerField(db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    pre_evolution = models.ForeignKey(
        "pokemon.Pokemon",
        on_delete=models.CASCADE,
        related_name="evolution",
        null=True,
        blank=True
    )

    types = models.ManyToManyField(
        "pokemon.PokemonType",
        related_name="pokemons"
    )

    abilities = models.ManyToManyField(
        "pokemon.Ability",
        related_name="pokemons"
    )

    def __str__(self):
        return f"{self.number} - {self.name}"
