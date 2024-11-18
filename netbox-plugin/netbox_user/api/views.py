from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import UserListSerializer, UserListRuleSerializer


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
        'user', 'recurso', 'tipo_acesso', 'tags'
    )
    serializer_class = UserListRuleSerializer
    filterset_class = filtersets.UserListRuleFilterSet