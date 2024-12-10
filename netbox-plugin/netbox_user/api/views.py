from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count


from .. import filtersets, models
from .serializers import  UserListSerializer, ResourceAccessSerializer, ResourcesSerializer, EnvironmentSerializer, GroupsSerializer, ApproverSerializer, SectorSerializer, ResourceGroupsSerializer

class ResourcesListViewSet(NetBoxModelViewSet):
    queryset = models.Resources.objects.prefetch_related('tags')
    serializer_class = ResourcesSerializer
    filterset_class = filtersets.ResourcesFilter


class EnvironmentListViewSet(NetBoxModelViewSet):
    queryset = models.Environment.objects.prefetch_related('tags')
    serializer_class = EnvironmentSerializer


class GroupsListViewSet(NetBoxModelViewSet):
    queryset = models.Groups.objects.prefetch_related('tags')
    serializer_class = GroupsSerializer


class ApproverListViewSet(NetBoxModelViewSet):
    queryset = models.Approver.objects.prefetch_related('tags')
    serializer_class = ApproverSerializer


class SectorListViewSet(NetBoxModelViewSet):
    queryset = models.Sector.objects.prefetch_related('tags')
    serializer_class = SectorSerializer


class ResourceGroupsListViewSet(NetBoxModelViewSet):
    queryset = models.ResourceGroups.objects.prefetch_related('tags')
    serializer_class = ResourceGroupsSerializer





class UserListViewSet(NetBoxModelViewSet):
    queryset = models.UserList.objects.prefetch_related('tags').annotate(
        rule_count=Count('rules')
    )
    serializer_class = UserListSerializer
    

class UserListRuleViewSet(NetBoxModelViewSet):
    queryset = models.ResourceAccess.objects.prefetch_related(
        'user', 'tags'
    )
    serializer_class = ResourceAccessSerializer
    filterset_class = filtersets.UserListRuleFilterSet
