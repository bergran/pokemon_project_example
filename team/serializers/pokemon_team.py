from rest_framework import serializers

from pokemon.models import Pokemon
from team.models import PokemonTeam


class PokemonSerializer(serializers.Serializer):
    pokemon = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=Pokemon.objects.all())
    )


class PokemonTeamSerializer(serializers.Serializer):
    instances = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=PokemonTeam.objects.all()
        )
    )

    def validate_instances(self, instances):
        user = self.context.get("request").user

        any_not_from_user = any(
            [instance.team.user != user for instance in instances]
        )

        if any_not_from_user:
            raise serializers.ValidationError(
                "Any instance wasn't from the user"
            )

        return instances
