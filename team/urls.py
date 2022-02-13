from rest_framework.routers import SimpleRouter

from team.views.teams import TeamView

router = SimpleRouter()
router.register("api/v1/teams", TeamView)

urlpatterns = router.urls
