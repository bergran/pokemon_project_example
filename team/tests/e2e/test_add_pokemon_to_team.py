from typing import Dict, Any

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from pokemon.models import Pokemon
from team.models import Team, PokemonTeam


class TestAddPokemonToTeam(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "username", "username@g.c", "some_password"
        )
        self.user2 = User.objects.create_user(
            "username 2", "username2@g.c", "some_password"
        )
        self.team = Team.objects.create(user=self.user, name="team 1")
        self.team2 = Team.objects.create(user=self.user2, name="team 1")
        Pokemon.objects.bulk_create(
            [
                Pokemon(name="bulbasaur", number=1),
                Pokemon(name="charmander", number=4),
                Pokemon(name="squirtle", number=7),
            ]
        )

    def _request_without_auth(self, team_pk: int, data: Dict[str, Any]):
        return self.client.post(f"/api/v1/teams/{team_pk}/pokemon-team/", data)

    def _request_with_auth(self, user, team_pk: int, data: Dict[str, Any]):
        self.client.force_login(user)
        response = self.client.post(
            f"/api/v1/teams/{team_pk}/pokemon-team/", data
        )
        self.client.logout()
        return response

    def test_add_pokemon_no_auth(self):
        payload = {"pokemon": [1, 2, 3]}

        response = self._request_without_auth(self.team.pk, payload)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_add_pokemon_for_user_team(self):
        payload = {"pokemon": [1, 2, 3]}

        response = self._request_with_auth(self.user, self.team.pk, payload)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == payload
        assert (
            PokemonTeam.objects.filter(
                team=self.team, pokemon__id__in=[1, 2, 3]
            ).count()
            == 3
        )

    def test_add_pokemon_to_no_user_team(self):
        payload = {"pokemon": [1, 2, 3]}

        response = self._request_with_auth(self.user, self.team2.pk, payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert (
            PokemonTeam.objects.filter(
                team=self.team2, pokemon__id__in=[1, 2, 3]
            ).count()
            == 0
        )

    def test_add_pokemon_with_non_existent_pokemon(self):
        payload = {"pokemon": [400]}

        response = self._request_with_auth(self.user, self.team.pk, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            PokemonTeam.objects.filter(
                team=self.team, pokemon__id__in=[400]
            ).count()
            == 0
        )
