from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from team.models import Team, PokemonTeam
from team.serializers.pokemon_team import (
    PokemonSerializer,
    PokemonTeamSerializer,
)
from team.serializers.teams import TeamSerializer


class TeamView(
    GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        queryset = super(TeamView, self).get_queryset()

        if self.action == "pokemon_team":
            return queryset.filter(user=self.request.user)

        return queryset

    @action(
        detail=True,
        methods=["post", "delete"],
        url_path="pokemon-team",
        url_name="pokemon_team",
    )
    def pokemon_team(self, request: Request, *_, **__) -> Response:
        obj = self.get_object()
        request_method = request.method.lower()

        if request_method == "post":
            return self._add_pokemon_to_team(obj, request.data)
        elif request_method == "delete":
            return self._delete_pokemon_from_team(obj, request.data)

    def _add_pokemon_to_team(self, team, data) -> Response:
        serializer = PokemonSerializer(
            data=data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)

        PokemonTeam.objects.bulk_create(
            [
                PokemonTeam(pokemon=pokemon, team=team)
                for pokemon in serializer.validated_data.get("pokemon", [])
            ]
        )

        return Response(data=serializer.data)

    def _delete_pokemon_from_team(self, team, data) -> Response:
        serializer = PokemonTeamSerializer(
            data=data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)

        PokemonTeam.objects.filter(
            pokemon__in=serializer.initial_data.get("instances", []), team=team
        ).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
