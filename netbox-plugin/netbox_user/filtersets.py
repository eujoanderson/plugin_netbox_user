from netbox.filtersets import NetBoxModelFilterSet
from .models import ResourceAccess

class UserListRuleFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = ResourceAccess
        fields = ('id', 'user', 'recurso', 'tipo_acesso', 'data_concessao',
                  'data_expiracao', 'aprovador', 'justificativa', 'status', 'observacoes', 'ambiente',)
    
    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
