from typing import Dict, Any

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from pokemon.models import Pokemon
from team.models import Team, PokemonTeam


class TestDeletePokemonToTeam(APITestCase):
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
        return self.client.delete(f"/api/v1/teams/{team_pk}/pokemon-team/", data)

    def _request_with_auth(self, user, team_pk: int, data: Dict[str, Any]):
        self.client.force_login(user)
        response = self.client.delete(
            f"/api/v1/teams/{team_pk}/pokemon-team/", data
        )
        self.client.logout()
        return response

    def test_delete_pokemon_no_auth(self):
        pt1 = PokemonTeam.objects.create(pokemon_id=1, team=self.team)
        pt2 = PokemonTeam.objects.create(pokemon_id=2, team=self.team)
        payload = {"instances": [pt1.pk, pt2.pk]}

        response = self._request_without_auth(self.team.pk, payload)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_pokemon_for_user_team(self):
        pt1 = PokemonTeam.objects.create(pokemon_id=1, team=self.team)
        pt2 = PokemonTeam.objects.create(pokemon_id=2, team=self.team)
        payload = {"instances": [pt1.pk, pt2.pk]}

        response = self._request_with_auth(self.user, self.team.pk, payload)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_pokemon_to_no_user_team(self):
        payload = {"instances": [1, 2, 3]}

        response = self._request_with_auth(self.user, self.team2.pk, payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_pokemon_with_non_existent_pokemon(self):
        payload = {"instances": [400]}

        response = self._request_with_auth(self.user, self.team.pk, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
