from django.contrib import admin
from pokemon.models import Pokemon, PokemonType, Ability


class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "number",
        "name",
        "pre_evolution_name"
    )

    def pre_evolution_name(self, instance: Pokemon):
        return instance.pre_evolution.name if instance.pre_evolution else None


class PokemonTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


class AbilityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonType, PokemonTypeAdmin)
admin.site.register(Ability, AbilityAdmin)
