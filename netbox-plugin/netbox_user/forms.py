
from utilities.forms.fields import CommentField, ColorField
from django import forms
import pdb

from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelBulkEditForm
from .models import UserList, ResourceAccess, Resources, Environment,Groups,Approver, Sector, ResourceGroups, Tag
from django.core.exceptions import ValidationError
from utilities.forms.widgets import APISelectMultiple, DatePicker
from django.urls import reverse_lazy
from django.db.models import Subquery


## User List 
class UserListForm(NetBoxModelForm):
    comments = CommentField()

    groups = DynamicModelMultipleChoiceField(
        queryset=Groups.objects.all(),
        required=False,
        help_text="Adicione o usuário ao grupo",
    )

    setor = DynamicModelMultipleChoiceField(
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

    setor = DynamicModelMultipleChoiceField(
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


## User List Rule 

class UserListRuleForm(NetBoxModelForm):

    user = DynamicModelChoiceField(queryset=UserList.objects.all(), required=True)

    recurso = DynamicModelChoiceField(queryset=Resources.objects.all(), required=True, query_params={'exclude_assigned': True})

    aprovador = DynamicModelChoiceField(queryset=Approver.objects.all(), required=True)

    ambiente = DynamicModelMultipleChoiceField(queryset=Environment.objects.all(), required=True)

    comments = CommentField()

    data_concessao = forms.DateField(
        widget=DatePicker(attrs={'autocomplete': 'off'}),
        required=True,
        label="Data de Concessão"
    )

    data_expiracao = forms.DateField(
        widget=DatePicker(attrs={'autocomplete': 'off'}),
        required=False,
        label="Data de Expiração"
    )

    class Meta:
        model = ResourceAccess
        fields = (
            'user','recurso', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador','periodo','ambiente','recurso','justificativa','comments','tags'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obter IDs dos recursos já atribuídos aos grupos
        assigned_resources = ResourceGroups.objects.values_list('recurso', flat=True)
        
        # Atualizar o queryset do campo 'recurso' para excluir os atribuídos
        self.fields['recurso'].queryset = Resources.objects.exclude(id__in=assigned_resources)
        
        # Debugging para verificar os valores
        print("Assigned Resources:", list(assigned_resources))
        print("Filtered Resources:", list(self.fields['recurso'].queryset))

class UserListRuleFilterForm(NetBoxModelFilterSetForm):

    model = ResourceAccess

    user = forms.ModelMultipleChoiceField(
        queryset=UserList.objects.all(),
        required=False
    )

    recurso = forms.ModelMultipleChoiceField(
        queryset=Resources.objects.all(),
        required=False,
    )

    aprovador = forms.ModelMultipleChoiceField(
        queryset=Approver.objects.all(),
        required=False,
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )

    class Meta:
        model = UserList 
        fields = ['user','recurso', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'status','ambiente','recurso','justificativa','tags',]  

class UserListRuleBulkEditForm(NetBoxModelBulkEditForm):
    model = ResourceAccess
    aprovador = DynamicModelChoiceField(queryset=Approver.objects.all(), required=False)
    ambiente = DynamicModelMultipleChoiceField(queryset=Environment.objects.all(), required=False)

    fieldsets = (
        ('Informações', ('aprovador', 'ambiente', )), 
    )


## Resouces Groups
class ResourceGroupsForm(NetBoxModelForm):

    recurso = DynamicModelChoiceField(queryset=Resources.objects.all(), required=True)
    groupslist = DynamicModelChoiceField(queryset=Groups.objects.all(), required=True)
    aprovador = DynamicModelChoiceField(queryset=Approver.objects.all(), required=True)

    ambiente = DynamicModelMultipleChoiceField(queryset=Environment.objects.all(), required=True)

    comments = CommentField()

    class Meta:
        model = ResourceGroups
        fields = (
            'recurso', 'groupslist','tipo_acesso','aprovador', 'ambiente','comments','tags'
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

    def clean(self):
        cleaned_data = super().clean()
        print("Dados limpos:", cleaned_data)

        for field_name, field in self.fields.items():
            print(f"Campo: {field_name}, Valor: {cleaned_data.get(field_name)}")
            if field.required and cleaned_data.get(field_name) is None:
                print(f"Erro no campo obrigatório: {field_name}")
                self.add_error(field_name, "Este campo não pode estar vazio.")

        return cleaned_data


### Resourcer
class ResourcesForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = Resources
        fields = (
            'recurso',  'comments', 'tags'
        )
        
class ResourcesFormFilterForm(NetBoxModelFilterSetForm):
    model = Resources
    recurso = forms.ModelChoiceField(queryset=Resources.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )
    class Meta:
        model = Resources
        fields = (
            'recurso',  'comments', 'tags'
        )

class ResourcesBulkEditForm(NetBoxModelBulkEditForm):    

    model = Resources



## Ambientes 
class EnvironmentForm(NetBoxModelForm):

    class Meta:
        model = Environment
        fields = (
            'ambiente',  'comments', 'tags'
        )

class EnvironmentFormFilterForm(NetBoxModelFilterSetForm):
    model = Environment
    ambiente = forms.ModelChoiceField(queryset=Environment.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )
    class Meta:
        model = Environment
        fields = (
            'ambiente', 'tags'
        )

class EnvironmentBulkEditForm(NetBoxModelBulkEditForm):    

    model = Environment

    


## Groups 
class GroupForm(NetBoxModelForm):

    comments = CommentField()
    class Meta:
        model = Groups
        fields = (
            'grupo',  'comments', 'tags'
        )

class GroupsFormFilterForm(NetBoxModelFilterSetForm):
    model = Groups
    grupo = forms.ModelChoiceField(queryset=Groups.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )
    class Meta:
        model = Groups
        fields = (
            'grupo', 'tags'
        )

class GroupsBulkEditForm(NetBoxModelBulkEditForm):    

    model = Groups







## Approver 
class ApproverForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = Approver
        fields = (
            'aprovador','comments', 'tags'
        )

class ApproverFormFilterForm(NetBoxModelFilterSetForm):
    model = Approver
    aprovador = forms.ModelChoiceField(queryset=Approver.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )
    class Meta:
        model = Groups
        fields = (
            'aprovador', 'tags'
        )

class ApproverBulkEditForm(NetBoxModelBulkEditForm):    

    model = Approver





## Sector 
class SectorForm(NetBoxModelForm):

    comments = CommentField()
    class Meta:
        model = Sector
        fields = (
            'setor',  'comments', 'tags'
        )

class SectorFormFilterForm(NetBoxModelFilterSetForm):
    model = Sector
    setor = forms.ModelChoiceField(queryset=Sector.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )
    class Meta:
        model = Sector
        fields = (
            'setor', 'tags'
        )

class SectorBulkEditForm(NetBoxModelBulkEditForm):    

    model = Sector


## Resouces 
class ResourcesFormFilterForm(NetBoxModelFilterSetForm):
    model = Resources
    recurso = forms.ModelChoiceField(queryset=Resources.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )
    class Meta:
        model = Resources
        fields = (
            'recurso',  'comments', 'tags'
        )

class ResourcesBulkEditForm(NetBoxModelBulkEditForm):    

    model = Resources

class ResourcesFormFilterForm(NetBoxModelFilterSetForm):
    model = Resources
    recurso = forms.ModelChoiceField(queryset=Resources.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Selecione as tags"
    )
    class Meta:
        model = Resources
        fields = (
            'recurso',  'comments', 'tags'
        )
        
