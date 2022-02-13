from rest_framework import serializers

from pokemon.models import Ability


class AbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Ability
        fields = (
            "id",
            "name"
        )
