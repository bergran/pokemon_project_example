from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from pokemon.models import Pokemon
from pokemon.serializers.pokemon import PokemonSerializer


class PokemonReadView(
    GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
