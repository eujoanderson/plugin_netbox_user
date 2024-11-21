
from .models import UserList, ResourceAccess
from utilities.forms.fields import CommentField
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import UserList, ResourceAccess, Resources, Environment,Groups,Approver, Sector
from django.core.exceptions import ValidationError


class UserListForm(NetBoxModelForm):
    comments = CommentField()

    groups = forms.ModelMultipleChoiceField(
        queryset=Groups.objects.all(),
        required=False
    )

    class Meta:
        model = UserList
        fields = ('name','groups', 'comments', 'status_user','setor','tags',)


class UserListRuleForm(NetBoxModelForm):

    user = forms.ModelChoiceField(queryset=UserList.objects.all(), required=True)

    aprovador = forms.ModelChoiceField(queryset=Approver.objects.all(), required=True)

    ambiente = forms.ModelChoiceField(queryset=Environment.objects.all(), required=True)

    data_concessao = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        label="Data de Concessão"
    )

    data_expiracao = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        label="Data de Expiração"
    )

    class Meta:
        model = ResourceAccess
        fields = (
            'user','recurso', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'justificativa', 'status','ambiente','tags'
        )



### NOVOS CAMPOS


class ResourcesForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = Resources
        fields = (
            'recurso',  'comments', 'tags'
        )

class EnvironmentForm(NetBoxModelForm):
    comments = CommentField()


    class Meta:
        model = Environment
        fields = (
            'ambiente',  'comments', 'tags'
        )

class GroupForm(NetBoxModelForm):

    comments = CommentField()
    class Meta:
        model = Groups
        fields = (
            'grupo',  'comments', 'tags'
        )

class ApproverForm(NetBoxModelForm):

    comments = CommentField()
    class Meta:
        model = Approver
        fields = (
            'aprovador',  'comments', 'tags'
        )

class SectorForm(NetBoxModelForm):

    comments = CommentField()
    class Meta:
        model = Sector
        fields = (
            'setor',  'comments', 'tags'
        )



class UserListRuleFilterForm(NetBoxModelFilterSetForm):
    comments = CommentField()

    model = ResourceAccess

    user_list = forms.ModelMultipleChoiceField(
        queryset=UserList.objects.all(),
        required=False
    )

    index = forms.IntegerField(
        required=False
    )