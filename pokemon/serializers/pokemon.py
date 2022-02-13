from rest_framework import serializers

from pokemon.models import Pokemon
from pokemon.serializers.abilities import AbilitySerializer
from pokemon.serializers.types import PokemonTypeSerializer


class PokemonSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = (
            "number",
            "name"
        )


class PokemonSerializer(serializers.ModelSerializer):
    evolution = PokemonSimpleSerializer(many=True)
    pre_evolution = PokemonSimpleSerializer()
    types = PokemonTypeSerializer(many=True)
    abilities = AbilitySerializer(many=True)

    class Meta:
        model = Pokemon
        fields = (
            "id",
            "number",
            "name",
            "evolution",
            "pre_evolution",
            "types",
            "abilities"
        )
