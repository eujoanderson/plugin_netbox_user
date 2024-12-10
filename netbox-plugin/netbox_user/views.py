from netbox.views import generic
from . import forms, models, tables
from django.db.models import Count
from . import filtersets, forms, models, tables
from django_tables2 import RequestConfig
from django.shortcuts import render, redirect
from .forms import UserListForm
from django.utils import timezone
from .models import ResourceAccess


# USER LIST
class UserListView(generic.ObjectView):
    queryset = models.UserList.objects.all()

    

    def get_extra_context(self, request, instance):

        update_resource_access_status() 

        table = tables.UserListRuleTable(instance.rules.all())
        table.configure(request)

        table2 = tables.GroupTable(instance.groups.all())
        table2.configure(request)
        
        resource_groups_list = []
        for grupo in instance.groups.all():

            resource_groups = grupo.resource_group_rules.all() 
            for rg in resource_groups:
                resource_groups_list.append(rg)

        resource_groups_table = tables.ResourceGroupsTable(resource_groups_list)
        resource_groups_table.configure(request)
        
        user_group_associations = instance.group_associations.select_related('group').order_by('-data_associacao')

        return {
            'recurso': table,
            'recurso_grupo': resource_groups_table,
            'user_group_associations': user_group_associations,
        } 

class UserListListView(generic.ObjectListView):
    queryset = models.UserList.objects.annotate(
        rule_count=Count('rules')
    )

    table = tables.UserListTable
    filterset = filtersets.UserListFilterSet
    filterset_form = forms.UserListFilterForm

class UserListEditView(generic.ObjectEditView):
    queryset = models.UserList.objects.all()
    form = forms.UserListForm

class UserListDeleteView(generic.ObjectDeleteView):
    queryset = models.UserList.objects.all()

class UserListBulkEditView(generic.BulkEditView):
    queryset = models.UserList.objects.all()
    table = tables.UserListTable
    form = forms.UserListBulkEditForm
    #filtersets = filtersets.UserListFilterSet

class UserListBulkDeleteView(generic.BulkDeleteView):
    queryset = models.UserList.objects.all()

    filtersets = filtersets.UserListFilterSet
    table = tables.UserListTable



# RESOURCES RULE LIST
class UserListRuleView(generic.ObjectView):
    queryset = models.ResourceAccess.objects.all()
    

    
    

class UserListRuleListView(generic.ObjectListView):
    queryset = models.ResourceAccess.objects.all()
    table = tables.UserListRuleTable
    
    def get_queryset(self, request):
        update_resource_access_status() 
        return ResourceAccess.objects.all()

    filterset = filtersets.UserListRuleFilterSet
    filterset_form = forms.UserListRuleFilterForm
    
class UserListRuleEditView(generic.ObjectEditView):
    queryset = models.ResourceAccess.objects.all()
    form = forms.UserListRuleForm
    
class UserListRuleDeleteView(generic.ObjectDeleteView):
    queryset = models.ResourceAccess.objects.all()

class UserListRuleBulkEditView(generic.BulkEditView):
    queryset = models.ResourceAccess.objects.all()

    table = tables.UserListRuleTable
    filtersets = filtersets.UserListRuleFilterSet
    form = forms.UserListRuleBulkEditForm

class UserListRuleBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ResourceAccess.objects.all()
    
    table = tables.UserListRuleTable
    filtersets = filtersets.UserListRuleFilterSet



# RESOURCES LIST
class ResourcesView(generic.ObjectView):
    queryset = models.Resources.objects.all()

class ResourcesListListView(generic.ObjectListView):
    queryset = models.Resources.objects.all()

    table = tables.ResourcesTable
    filterset = filtersets.ResourcesFilterSet
    filterset_form = forms.ResourcesFormFilterForm

class ResourcesListEditView(generic.ObjectEditView):
    queryset = models.Resources.objects.all()
    form = forms.ResourcesForm

class ResourcesListDeleteView(generic.ObjectDeleteView):
    queryset = models.Resources.objects.all()

class ResourcesBulkEditView(generic.BulkEditView):
    queryset = models.Resources.objects.all()

    table = tables.ResourcesTable
    filtersets = filtersets.ResourcesFilterSet
    form = forms.ResourcesBulkEditForm

class ResourcesBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Resources.objects.all()
    
    table = tables.ResourcesTable
    filtersets = filtersets.ResourcesFilterSet





# Environment LIST
class EnvironmentView(generic.ObjectView):
    queryset = models.Environment.objects.all()

class EnvironmentListListView(generic.ObjectListView):
    queryset = models.Environment.objects.all()

    table = tables.EnvironmentTable
    filterset = filtersets.EnvironmentFilterSet
    filterset_form = forms.EnvironmentFormFilterForm

class EnvironmentListEditView(generic.ObjectEditView):
    queryset = models.Environment.objects.all()
    form = forms.EnvironmentForm

class EnvironmentListDeleteView(generic.ObjectDeleteView):
    queryset = models.Environment.objects.all()

class EnvironmentBulkEditView(generic.BulkEditView):
    queryset = models.Environment.objects.all()

    table = tables.EnvironmentTable
    filtersets = filtersets.EnvironmentFilterSet
    form = forms.EnvironmentBulkEditForm

class EnvironmentBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Environment.objects.all()
    
    table = tables.EnvironmentTable
    filtersets = filtersets.EnvironmentFilterSet




# Group LIST
class GroupView(generic.ObjectView):
    queryset = models.Groups.objects.all()
    def get_extra_context(self, request, instance):
        table = tables.ResourceGroupsTable(instance.resource_group_rules.all())
        table.configure(request)

        users = instance.users.all()  
        
        users_table = tables.UserListTable(users)
        users_table.configure(request)

        related_models = [
            (users, 'groups'),
        ]
        
        return {
            'groups': table,
            'related_models': related_models,
        }
   
class GroupListListView(generic.ObjectListView):
    queryset = models.Groups.objects.all()

    table = tables.GroupTable
    filterset = filtersets.GroupsFilterSet
    filterset_form = forms.GroupsFormFilterForm

class GroupListEditView(generic.ObjectEditView):
    queryset = models.Groups.objects.all()
    form = forms.GroupForm

class GroupListDeleteView(generic.ObjectDeleteView):
    queryset = models.Groups.objects.all()

class GroupListBulkEditView(generic.BulkEditView):
    queryset = models.Groups.objects.all()

    table = tables.GroupTable
    filtersets = filtersets.GroupsFilterSet
    form = forms.GroupsBulkEditForm

class GroupListBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Groups.objects.all()
    
    table = tables.GroupTable
    filtersets = filtersets.GroupsFilterSet



# Approver LIST
class ApproverView(generic.ObjectView):
    queryset = models.Approver.objects.all()

class ApproverListListView(generic.ObjectListView):
    queryset = models.Approver.objects.all()

    table = tables.ApproverTable
    filterset = filtersets.ApproverFilterSet
    filterset_form = forms.ApproverFormFilterForm

class ApproverListEditView(generic.ObjectEditView):
    queryset = models.Approver.objects.all()
    form = forms.ApproverForm

class ApproverListDeleteView(generic.ObjectDeleteView):
    queryset = models.Approver.objects.all()

class ApproverBulkEditView(generic.BulkEditView):
    queryset = models.Approver.objects.all()

    table = tables.ApproverTable
    filtersets = filtersets.ApproverFilterSet
    form = forms.ApproverBulkEditForm

class ApproverBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Approver.objects.all()
    
    table = tables.ApproverTable
    filtersets = filtersets.ApproverFilterSet



# Sector LIST
class SectorView(generic.ObjectView):
    queryset = models.Sector.objects.all()


    def get_extra_context(self, request, instance):
        users = instance.users.all() 
        print(users) 
        
        users_table = tables.UserListTable(users)
        users_table.configure(request)

        related_models = [
            (users, 'setor'),
        ]
        
        return {
            'related_models': related_models,
        }

class SectorListListView(generic.ObjectListView):
    queryset = models.Sector.objects.all()

    table = tables.SectorTable
    filterset = filtersets.SectorFilterSet
    filterset_form = forms.SectorFormFilterForm

class SectorListEditView(generic.ObjectEditView):
    queryset = models.Sector.objects.all()
    form = forms.SectorForm

class SectorListDeleteView(generic.ObjectDeleteView):
    queryset = models.Sector.objects.all()

class SectorBulkEditView(generic.BulkEditView):
    queryset = models.Sector.objects.all()

    table = tables.SectorTable
    filtersets = filtersets.SectorFilterSet
    form = forms.SectorBulkEditForm

class SectorBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Sector.objects.all()
    
    table = tables.SectorTable
    filtersets = filtersets.SectorFilterSet





# Groups Resources LIST
class ResourceGroupsView(generic.ObjectView):
    queryset = models.ResourceGroups.objects.all()


class ResourceGroupsListListView(generic.ObjectListView):
    queryset = models.ResourceGroups.objects.all()

    table = tables.ResourceGroupsTable
    filterset = filtersets.ResourceGroupsFilterSet
    filterset_form = forms.ResourceGroupsFilterForm

class ResourceGroupsListEditView(generic.ObjectEditView):
    queryset = models.ResourceGroups.objects.all()
    form = forms.ResourceGroupsForm

class ResourceGroupsListDeleteView(generic.ObjectDeleteView):
    queryset = models.ResourceGroups.objects.all()

class ResourceGroupsBulkEditView(generic.BulkEditView):
    queryset = models.ResourceGroups.objects.all()
    
    table = tables.ResourceGroupsTable
    filterset = filtersets.ResourceGroupsFilterSet
    form = forms.ResourceGroupsBulkEditForm

class ResourceGroupsBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ResourceGroups.objects.all()
    
    table = tables.ResourceGroupsTable
    filterset = filtersets.ResourceGroupsFilterSet




def update_resource_access_status():
    today = timezone.now().date()
    ResourceAccess.objects.filter(data_expiracao__lt=today).update(status='expired')
    ResourceAccess.objects.filter(data_expiracao__gte=today).update(status='active')