from rest_framework.routers import SimpleRouter

from pokemon.views.pokemon import PokemonReadView

router = SimpleRouter()
router.register("api/v1/pokemon", PokemonReadView)

urlpatterns = router.urls
