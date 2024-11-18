from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'plugin-user'

router = NetBoxRouter()
router.register('plugin-user', views.UserListViewSet)
router.register('plugin-user-rules', views.UserListRuleViewSet)

# Define urlpatterns explicitamente
urlpatterns = router.urls
