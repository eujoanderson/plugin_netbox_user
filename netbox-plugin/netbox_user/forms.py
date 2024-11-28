
from .models import UserList, ResourceAccess
from utilities.forms.fields import CommentField, ColorField
from django import forms

from utilities.forms.fields import DynamicModelMultipleChoiceField

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import UserList, ResourceAccess, Resources, Environment,Groups,Approver, Sector, ResourceGroups
from django.core.exceptions import ValidationError
from utilities.forms.widgets import APISelectMultiple, DatePicker
from django.urls import reverse_lazy


class UserListForm(NetBoxModelForm):
    comments = CommentField()

    groups = forms.ModelMultipleChoiceField(
        queryset=Groups.objects.all(),
        required=True,
        widget=forms.SelectMultiple,
        help_text="Adicione o usuário ao grupo",
    )


    setor = forms.ModelMultipleChoiceField(
        queryset=Sector.objects.all(),
        required=False,
        help_text="Adicione o usuário ao setor",
    )

    class Meta:
        model = UserList
        fields = ('name','groups', 'comments', 'status_user','setor','tags',)


class UserListFilterForm(NetBoxModelFilterSetForm):
    model = UserList

    groups = forms.ModelMultipleChoiceField(
        queryset=Groups.objects.all(),
        required=False,
        help_text="Adicione o usuário ao grupo",
        #widget=APISelectMultiple(  # Adiciona o widget com botão de atualização
        #api_url='/api/plugins/plugin-user/grouplist/'  # Endpoint da API para grupos
        #)
    )


    setor = forms.ModelMultipleChoiceField(
        queryset=Sector.objects.all(),
        required=False,
        help_text="Adicione o usuário ao setor",
    )

    class Meta:
        model = UserList 
        fields = ['name','groups', 'status_user','setor','tags',]  


############################################################################################################################

class UserListRuleForm(NetBoxModelForm):

    user = forms.ModelChoiceField(queryset=UserList.objects.all(), required=True)

    recurso = forms.ModelChoiceField(queryset=Resources.objects.all(), required=True)

    aprovador = forms.ModelChoiceField(queryset=Approver.objects.all(), required=True)

    ambiente = forms.ModelMultipleChoiceField(queryset=Environment.objects.all(), required=True)

    comments = CommentField()

    data_concessao = forms.DateField(
        widget=DatePicker(attrs={'autocomplete': 'off'}),
        required=True,
        label="Data de Concessão"
    )

    data_expiracao = forms.DateField(
        widget=DatePicker(attrs={'autocomplete': 'off'}),
        required=True,
        label="Data de Expiração"
    )

    class Meta:
        model = ResourceAccess
        fields = (
            'user','recurso', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'status','ambiente','recurso','justificativa','comments','tags'
        )



class ResourceGroupsForm(NetBoxModelForm):

    recurso = forms.ModelChoiceField(queryset=Resources.objects.all(), required=True)
    groupslist = forms.ModelChoiceField(queryset=Groups.objects.all(), required=True)
    aprovador = forms.ModelChoiceField(queryset=Approver.objects.all(), required=True)

    ambiente = forms.ModelMultipleChoiceField(queryset=Environment.objects.all(), required=True)

    comments = CommentField()

    class Meta:
        model = ResourceGroups
        fields = (
            'recurso', 'groupslist','tipo_acesso', 'aprovador', 'ambiente','comments','tags'
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
            'aprovador','comments', 'tags'
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



