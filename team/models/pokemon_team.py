from django.db import models


class PokemonTeam(models.Model):
    pokemon = models.ForeignKey(
        "pokemon.Pokemon", on_delete=models.CASCADE, related_name="pokemon_team"
    )
    team = models.ForeignKey(
        "team.Team", on_delete=models.CASCADE, related_name="pokemon_team"
    )
