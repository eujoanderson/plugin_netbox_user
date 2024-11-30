
from utilities.forms.fields import CommentField, ColorField
from django import forms
import pdb

from utilities.forms.fields import DynamicModelChoiceField

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelBulkEditForm
from .models import UserList, ResourceAccess, Resources, Environment,Groups,Approver, Sector, ResourceGroups, Tag
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
        fields = ('name','groups', 'status_user','setor','comments','tags',)


class UserListBulkEditForm(NetBoxModelBulkEditForm):    

    groups = forms.ModelMultipleChoiceField(
        queryset=Groups.objects.all(),
        required=False,
        help_text="Adicione o usuário ao grupo",
    )

    setor = forms.ModelMultipleChoiceField(
        queryset=Sector.objects.all(),
        required=False,
        help_text="Adicione o usuário ao setor",
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )

    model = UserList

    fieldsets = (
        ('Informações', ('groups', 'setor')), 
    )

class UserListFilterForm(NetBoxModelFilterSetForm):
    model = UserList
    name = forms.ModelMultipleChoiceField(queryset=UserList.objects.all(), required=False)
    
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )

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

class UserListRuleFilterForm(NetBoxModelFilterSetForm):

    model = ResourceAccess

    user = forms.ModelMultipleChoiceField(
        queryset=UserList.objects.all(),
        required=False
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )

    recurso = forms.ModelMultipleChoiceField(
        queryset=Resources.objects.all(),
        required=False,
    )

    aprovador = forms.ModelMultipleChoiceField(
        queryset=Approver.objects.all(),
        required=False,
    )

    class Meta:
        model = UserList 
        fields = ['user','recurso', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'status','ambiente','recurso','justificativa','tags',]  

class UserListRuleBulkEditForm(NetBoxModelBulkEditForm):
    user = forms.ModelChoiceField(queryset=UserList.objects.all(), required=False)
    recurso = forms.ModelChoiceField(queryset=Resources.objects.all(), required=False)
    aprovador = forms.ModelChoiceField(queryset=Approver.objects.all(), required=False)
    ambiente = forms.ModelMultipleChoiceField(queryset=Environment.objects.all(), required=False)
    data_concessao = forms.DateField(widget=DatePicker(attrs={'autocomplete': 'off'}), required=False)
    data_expiracao = forms.DateField(widget=DatePicker(attrs={'autocomplete': 'off'}), required=False)
    
    # Adicionando campos obrigatórios como opcionais no formulário
    action = forms.CharField(max_length=30, required=False)
    tipo_acesso = forms.ChoiceField( required=False)
    status = forms.ChoiceField( required=False)

    model = ResourceAccess

    fieldsets = (
        ('Informações', ('aprovador', 'ambiente', )), 
    )

    def clean(self):
        pdb.set_trace()  # Pausa a execução aqui
        cleaned_data = super().clean()  # Valida os dados

        # Agora você pode verificar os erros depois de validar
        if self.errors:
            for field, error in self.errors.items():
                print(f"{field}: {error}")

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


class ResourceGroupsFilterForm(NetBoxModelFilterSetForm):
    model = ResourceGroups

    recurso = forms.ModelChoiceField(queryset=Resources.objects.all(), required=False)
    groupslist = forms.ModelChoiceField(queryset=Groups.objects.all(), required=False)
    aprovador = forms.ModelChoiceField(queryset=Approver.objects.all(), required=False)

    ambiente = forms.ModelMultipleChoiceField(queryset=Environment.objects.all(), required=False)

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )

    class Meta:
        model = ResourceGroups
        fields = (
            'recurso', 'groupslist','tipo_acesso', 'aprovador', 'ambiente','tags'
        )


class ResourceGroupsBulkEditForm(NetBoxModelBulkEditForm):    
    model = ResourceGroups

    groupslist = forms.ModelChoiceField(queryset=Groups.objects.all(), required=False)
    aprovador = forms.ModelChoiceField(queryset=Approver.objects.all(), required=False)

    ambiente = forms.ModelMultipleChoiceField(queryset=Environment.objects.all(), required=False)

    fieldsets = (
        ('Informações', ('groupslist', 'aprovador', 'ambiente')), 
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






