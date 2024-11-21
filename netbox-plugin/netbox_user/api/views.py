from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import UserListSerializer, UserListRuleSerializer, ResourcesListSerializer, EnvironmentListSerializer, GroupsListSerializer, ApproverListSerializer, SectorListSerializer

class ResourcesListViewSet(NetBoxModelViewSet):
    queryset = models.Resources.objects.prefetch_related('tags')
    serializer_class = ResourcesListSerializer


class EnvironmentListViewSet(NetBoxModelViewSet):
    queryset = models.Environment.objects.prefetch_related('tags')
    serializer_class = EnvironmentListSerializer


class GroupsListViewSet(NetBoxModelViewSet):
    queryset = models.Groups.objects.prefetch_related('tags')
    serializer_class = GroupsListSerializer


class ApproverListViewSet(NetBoxModelViewSet):
    queryset = models.Approver.objects.prefetch_related('tags')
    serializer_class = ApproverListSerializer


class SectorListViewSet(NetBoxModelViewSet):
    queryset = models.Sector.objects.prefetch_related('tags')
    serializer_class = SectorListSerializer




## ///////////////
class UserListViewSet(NetBoxModelViewSet):
    queryset = models.UserList.objects.prefetch_related('tags')
    serializer_class = UserListSerializer
    

class UserListViewSet(NetBoxModelViewSet):
    queryset = models.UserList.objects.prefetch_related('tags').annotate(
        rule_count=Count('rules')
    )
    serializer_class = UserListSerializer
    

class UserListRuleViewSet(NetBoxModelViewSet):
    queryset = models.ResourceAccess.objects.prefetch_related(
        'user', 'tags'
    )
    serializer_class = UserListRuleSerializer
    filterset_class = filtersets.UserListRuleFilterSet