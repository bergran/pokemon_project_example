from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from team.models import Team
from team.serializers.teams import TeamSerializer


class TeamView(
    GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
