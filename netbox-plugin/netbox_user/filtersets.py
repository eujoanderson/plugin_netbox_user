import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from .models import ResourceAccess, UserList, Resources, Groups, Approver, Sector, ResourceGroups, Environment, Tag
from django.db.models import Q



class UserListRuleFilterSet(NetBoxModelFilterSet):

    user = django_filters.ModelMultipleChoiceFilter(queryset=UserList.objects.all(), required=False)

    aprovador = django_filters.ModelMultipleChoiceFilter(queryset=Approver.objects.all(), required=False)
    
    recurso = django_filters.ModelMultipleChoiceFilter(queryset=Resources.objects.all(), required=False)

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        required=False,
        label="Selecione as tags"
    )

    class Meta:
        model = ResourceAccess
        fields = ('id', 'user', 'recurso', 'tipo_acesso', 'data_concessao',
                  'data_expiracao', 'aprovador', 'justificativa', 'status', 'ambiente','tags')
    
    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
           Q(status__icontains=value) | Q(recurso__recurso__icontains=value)  | Q(ambiente__ambiente__icontains=value) 
        )


class UserListFilterSet(NetBoxModelFilterSet):

    name = django_filters.ModelMultipleChoiceFilter(queryset=UserList.objects.all(), required=False)

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        required=False,
        label="Selecione as tags"
    )

    class Meta:
        model = UserList
        fields = ('name','groups','setor','tags')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) | Q(setor__setor__icontains=value) | Q(status_user__icontains=value)
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
    recurso = django_filters.ModelMultipleChoiceFilter(queryset=Resources.objects.all(), required=False)
    groupslist = django_filters.ModelMultipleChoiceFilter(queryset=Groups.objects.all(), required=False)
    aprovador = django_filters.ModelMultipleChoiceFilter(queryset=Approver.objects.all(), required=False)
    ambiente = django_filters.ModelMultipleChoiceFilter(queryset=Environment.objects.all(), required=False)

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        required=False,
        label="Selecione as tags"
    )

    class Meta:
        model = ResourceGroups
        fields = ('recurso','groupslist', 'tipo_acesso', 'aprovador','ambiente','tags',)


    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(recurso__recurso__icontains=value) | Q(groupslist__grupo__icontains=value) | Q(ambiente__ambiente__icontains=value)
        )