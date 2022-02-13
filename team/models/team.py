from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="teams"
    )

    pokemon = models.ManyToManyField(
        "pokemon.Pokemon",
        through="team.PokemonTeam",
        through_fields=("team", "pokemon"),
        related_name="teams"
    )

    def __str__(self):
        return f"{self.name}"
