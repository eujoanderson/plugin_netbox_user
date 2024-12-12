
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
        
    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        name_print = UserList.objects.filter(name__iexact=name).values_list('name', flat=True)

        if UserList.objects.filter(name__iexact=name).exists():
            for user_name in name_print:
                raise ValidationError(f"Já existe um usuário com o nome '{user_name}', insira outro.")
        return name

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
        
        for field_name, field in self.fields.items():
            if field.required and cleaned_data.get(field_name) is None:
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
        
    def clean_recurso(self):
        
        recurso = self.cleaned_data['recurso'].strip()
        name_print = Resources.objects.filter(recurso__iexact=recurso).values_list('recurso', flat=True)

        if Resources.objects.filter(recurso__iexact=recurso).exists():
            for recurso_name in name_print:
                raise ValidationError(f"Já existe um recurso com o nome '{recurso_name}', insira outro.")
        return recurso
        
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
        
    def clean_ambiente(self):
        
        ambiente = self.cleaned_data['ambiente'].strip()
        
        ambiente_print = Environment.objects.filter(ambiente__iexact=ambiente).values_list('ambiente', flat=True)

        if Environment.objects.filter(ambiente__iexact=ambiente).exists():
            for ambiente_name in ambiente_print:
                raise ValidationError(f"Já existe um ambiente com o nome '{ambiente_name}', insira outro.")
        return ambiente
    

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
        
        
    def clean_grupo(self):
        
        grupo = self.cleaned_data['grupo'].strip()
        
        grupo_print = Groups.objects.filter(grupo__iexact=grupo).values_list('grupo', flat=True)

        if Groups.objects.filter(grupo__iexact=grupo).exists():
            for grupo_name in grupo_print:
                raise ValidationError(f"Já existe um grupo com o nome '{grupo_name}', insira outro.")
        return grupo

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
    
    def clean_aprovador(self):
        
        aprovador = self.cleaned_data['aprovador'].strip()
        
        aprovador_print = Approver.objects.filter(aprovador__iexact=aprovador).values_list('aprovador', flat=True)

        if Approver.objects.filter(aprovador__iexact=aprovador).exists():
            for aprovador_name in aprovador_print:
                raise ValidationError(f"Já existe um aprovador com o nome '{aprovador_name}', insira outro.")
        return aprovador

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
        
    def clean_setor(self):
        
        setor = self.cleaned_data['setor'].strip()
        
        setor_print = Sector.objects.filter(setor__iexact=setor).values_list('setor', flat=True)

        if Sector.objects.filter(setor__iexact=setor).exists():
            for setor_name in setor_print:
                raise ValidationError(f"Já existe um setor com o nome '{setor_name}', insira outro.")
        return setor

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
        
