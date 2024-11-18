from netbox.views import generic
from . import forms, models, tables
from django.db.models import Count
from . import filtersets, forms, models, tables

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