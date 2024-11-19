from netbox.views import generic
from . import forms, models, tables
from django.db.models import Count
from . import filtersets, forms, models, tables

# USER LIST
class UserListView(generic.ObjectView):
    queryset = models.UserList.objects.all()

    def get_extra_context(self, request, instance):

        table = tables.UserListRuleTable(instance.rules.all())
        table.configure(request)

        return {
            'recurso': table,
        }


class UserListListView(generic.ObjectListView):
    queryset = models.UserList.objects.annotate(
        rule_count=Count('rules')
    )

    table = tables.UserListTable

class UserListEditView(generic.ObjectEditView):
    queryset = models.UserList.objects.all()
    form = forms.UserListForm


class UserListDeleteView(generic.ObjectDeleteView):
    queryset = models.UserList.objects.all()


# RESOURCES RULE LIST
class UserListRuleView(generic.ObjectView):
    queryset = models.ResourceAccess.objects.all()


class UserListRuleListView(generic.ObjectListView):
    queryset = models.ResourceAccess.objects.all()
    table = tables.UserListRuleTable

    filterset = filtersets.UserListRuleFilterSet
    filterset_form = forms.UserListRuleFilterForm


class UserListRuleEditView(generic.ObjectEditView):
    queryset = models.ResourceAccess.objects.all()
    form = forms.UserListRuleForm
    

class UserListRuleDeleteView(generic.ObjectDeleteView):
    queryset = models.ResourceAccess.objects.all()




# RESOURCES LIST
class ResourcesView(generic.ObjectView):
    queryset = models.UserList.objects.annotate(
        rule_count=Count('rules')
    )
    queryset = models.Resources.objects.all()


class ResourcesListListView(generic.ObjectListView):
    queryset = models.Resources.objects.all()

    table = tables.ResourcesTable

class ResourcesListEditView(generic.ObjectEditView):
    queryset = models.Resources.objects.all()
    form = forms.ResourcesForm


class ResourcesListDeleteView(generic.ObjectDeleteView):
    queryset = models.Resources.objects.all()





# environment LIST
class EnvironmentView(generic.ObjectView):
    queryset = models.Environment.objects.all()


class EnvironmentListListView(generic.ObjectListView):
    queryset = models.Environment.objects.all()

    table = tables.EnvironmentTable

class EnvironmentListEditView(generic.ObjectEditView):
    queryset = models.Environment.objects.all()
    form = forms.EnvironmentForm


class EnvironmentListDeleteView(generic.ObjectDeleteView):
    queryset = models.Environment.objects.all()



# Group LIST
class GroupView(generic.ObjectView):
    queryset = models.Groups.objects.all()


class GroupListListView(generic.ObjectListView):
    queryset = models.Groups.objects.all()

    table = tables.GroupTable

class GroupListEditView(generic.ObjectEditView):
    queryset = models.Groups.objects.all()
    form = forms.GroupForm


class GroupListDeleteView(generic.ObjectDeleteView):
    queryset = models.Groups.objects.all()