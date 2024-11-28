from netbox.filtersets import NetBoxModelFilterSet
from .models import ResourceAccess, UserList, Resources, Groups, Approver, Sector, ResourceGroups, Environment
from django.db.models import Q



class UserListRuleFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = ResourceAccess
        fields = ('id', 'user', 'recurso', 'tipo_acesso', 'data_concessao',
                  'data_expiracao', 'aprovador', 'justificativa', 'status', 'ambiente',)
    
    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
           Q(status__icontains=value) | Q(recurso__recurso__icontains=value)  | Q(ambiente__ambiente__icontains=value)
        )


class UserListFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = UserList
        fields = ('name','groups','status_user','setor',)

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) | Q(setor__setor__icontains=value)
        )



    
class EnvironmentFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Environment
        fields = ('ambiente', 'comments',)


    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(ambiente__icontains=value) | Q(comments__icontains=value)
        )


class GroupsFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Groups
        fields = ('id', 'grupo', 'comments',)


    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(grupo__icontains=value)
        )
    

class ApproverFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Approver
        fields = ('aprovador', 'comments',)


    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(aprovador__icontains=value) | Q(comments__icontains=value)
        )


class SectorFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Sector
        fields = ('setor',  'comments',)


    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(setor__icontains=value)| Q(comments__icontains=value)
        )
    



class ResourcesFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Resources
        fields = ('id', 'recurso',  'comments', )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(recurso__recurso__icontains=value)
        )


class ResourceGroupsFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = ResourceGroups
        fields = ('recurso','groupslist', 'tipo_acesso', 'aprovador','ambiente','comments',)


    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(recurso__recurso__icontains=value) | Q(groupslist__grupo__icontains=value) | Q(ambiente__ambiente__icontains=value)
        )