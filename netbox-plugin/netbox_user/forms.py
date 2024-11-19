
from .models import UserList, ResourceAccess
from utilities.forms.fields import CommentField
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import UserList, ResourceAccess, Resources, Environment,Groups
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

    observacoes = CommentField(label="Comentário")


    class Meta:
        model = ResourceAccess
        fields = (
            'user','recurso', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'justificativa', 'status','observacoes','ambiente','tags'
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
            'environment',  'comments', 'tags'
        )

class GroupForm(NetBoxModelForm):

    comments = CommentField()
    class Meta:
        model = Groups
        fields = (
            'group',  'comments', 'tags'
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