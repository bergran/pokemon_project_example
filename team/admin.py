from django.contrib import admin

from team.models import Team, PokemonTeam


class PokemonTeamInline(admin.TabularInline):
    model = PokemonTeam


class TeamAdmin(admin.ModelAdmin):
    inlines = [
        PokemonTeamInline
    ]
    list_display = (
        "id",
        "name",
        "username",
    )

    @staticmethod
    def username(instance: Team):
        return instance.user.username


admin.site.register(Team, TeamAdmin)
