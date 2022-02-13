from rest_framework import serializers

from pokemon.models import PokemonType


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = (
            "id",
            "name"
        )
