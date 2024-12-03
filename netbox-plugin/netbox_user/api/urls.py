from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'plugin-user'

router = NetBoxRouter()
router.register('plugin-user', views.UserListViewSet, basename='userlist')
router.register('resourceaccess', views.UserListRuleViewSet, basename='resourceaccess')
router.register('resources', views.ResourcesListViewSet, basename='resources')

router.register('environment', views.EnvironmentListViewSet, basename='environment')
router.register('groups', views.GroupsListViewSet, basename='groups')
router.register('approver', views.ApproverListViewSet, basename='approver')
router.register('sector', views.SectorListViewSet, basename='sector')
router.register('resourcegroups', views.ResourceGroupsListViewSet, basename='resourcegroups')


# Define urlpatterns explicitamente
urlpatterns = router.urls

