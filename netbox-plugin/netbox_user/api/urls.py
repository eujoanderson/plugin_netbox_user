from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'plugin-user'

router = NetBoxRouter()
router.register('plugin-user', views.UserListViewSet)
router.register('pluginuserrule', views.UserListRuleViewSet, basename='pluginuserrule')
router.register('resourceslist', views.ResourcesListViewSet, basename='resourceslist')
router.register('environmentlist', views.EnvironmentListViewSet, basename='environmentlist')
router.register('grouplist', views.GroupsListViewSet, basename='grouplist')
router.register('groups', views.GroupsListViewSet, basename='groups-list')
router.register('approverlist', views.ApproverListViewSet, basename='approverlist')
router.register('sectorlist', views.SectorListViewSet, basename='sectorlist')
router.register('resourcegroups', views.ResourceGroupsListViewSet, basename='resourcegroups')


# Define urlpatterns explicitamente
urlpatterns = router.urls

