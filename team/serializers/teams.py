from rest_framework import serializers

from pokemon.serializers.pokemon import PokemonSimpleSerializer
from team.models import Team


class TeamSerializer(serializers.ModelSerializer):
    pokemon = PokemonSimpleSerializer(many=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "pokemon"
        )
