from django.db import models
from netbox.models import NetBoxModel

from utilities.choices import ChoiceSet
from django.urls import reverse # type: ignore
from django.db.models import Max
from extras.models import Tag
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver



class Resources(NetBoxModel):
    recurso = models.CharField(max_length=100,unique=True, blank=True)
    comments = models.TextField(blank=True)
    
    clone_fields = (
        'tags',
    )
    class Meta:
        ordering = ('recurso',)
        verbose_name = "Recurso"

    def __str__(self):
        return self.recurso
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:resourceslist', args=[self.pk])
    
    def clone(self):
        attrs = super().clone()
        attrs['extra-value'] = 123
        return attrs


class Environment(NetBoxModel):
    ambiente = models.CharField(max_length=100,unique=True, blank=True)
    comments = models.TextField(blank=True)

    clone_fields = (
        'tags',
    )

    class Meta:
        ordering = ('ambiente', )
        verbose_name = "Ambiente"

    def __str__(self):
        return self.ambiente
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:environmentlist', args=[self.pk])
    
    def clone(self):
        attrs = super().clone()
        attrs['extra-value'] = 123
        return attrs


class Approver(NetBoxModel):
    aprovador = models.CharField(max_length=100,unique=True, blank=True)
    comments = models.TextField(blank=True)

    clone_fields = (
        'tags',
    )
    class Meta:
        ordering = ('aprovador', )
        verbose_name = "Aprovador"

    def __str__(self):
        return self.aprovador
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:approverlist', args=[self.pk])
    
    def clone(self):
        attrs = super().clone()
        attrs['extra-value'] = 123
        return attrs


class Sector(NetBoxModel):
    setor = models.CharField(max_length=100,unique=True, blank=True)
    comments = models.TextField(blank=True)

    clone_fields = (
        'tags',
    )

    class Meta:
        ordering = ('setor',)
        verbose_name = "Setore"

    def __str__(self):
        return str(self.setor)
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:sectorlist', args=[self.pk])
    
    def clone(self):
        attrs = super().clone()
        attrs['extra-value'] = 123
        return attrs





class ActionChoicesStatusUserColor(ChoiceSet):
    key = 'UserList.status_user'

    CHOICES = [
        ('active', 'Active', 'green'),
        ('deactivate', 'Deactivate', 'red'),
    ]
class ActionChoicesSetor(ChoiceSet):
    key = 'UserList.setor'

    CHOICES = [
        ('infraestutura', 'Infraestutura',),
        ('desenvolvimento', 'Desenvolvimento'),
        ('administrativo', 'Administrativo'),
    ]
class ActionChoices(ChoiceSet):
    CHOICES = [
        ('active', 'Active', 'green'),
        ('expired', 'Expired', 'red'),
    ]

class ActionChoicesPeriodo(ChoiceSet):
    key = 'ResourceAccess.periodo'
    CHOICES = [
        ('permanente', 'Permanente', 'yellow'),
        ('temporario', 'Temporário', 'purple'),
    ]

class ActionChoicesType(ChoiceSet):
    key = 'ResourceAccess.tipo_acesso'

    CHOICES = [
        ('leitura', 'Leitura', 'purple'),
        ('leituraescrita', 'Leitura e Escrita', 'purple'),
    ]


# Modelo para grupos
class Groups(NetBoxModel):
    grupo = models.CharField(max_length=100, unique=True, blank=True,)
    comments = models.TextField(blank=True)

    clone_fields = (
         'tags',
    )

    class Meta:
        ordering = ('grupo', )
        verbose_name = "Grupo"

    def __str__(self):
        return self.grupo

    def get_absolute_url(self):
        return reverse('plugins:netbox_user:groupslist', args=[self.pk])
    
    def clone(self):
        attrs = super().clone()
        attrs['extra-value'] = 123
        return attrs



# Modelo para o usuário
class UserList(NetBoxModel):
    name = models.CharField(max_length=100,unique=True)
    comments = models.TextField(blank=True)

    groups = models.ManyToManyField(Groups,blank=True, related_name='users', through='UserGroupAssociation')

    tags = models.ManyToManyField(Tag, blank=True)
    
    setor = models.ManyToManyField(Sector, blank=True, related_name='users')

    status_user = models.CharField(
        max_length=30,
        choices=ActionChoicesStatusUserColor._choices,
        verbose_name="Status User",
        default='active'
    )
    
    clone_fields = (
        'tags','status_user', 'setor',
    )


    class Meta:
        ordering = ('name',)
        verbose_name = "Usuário"

    def __str__(self):
        return self.name
    
    def get_related_groups(self):
        return self.groups.all()

    def get_absolute_url(self):
        return reverse('plugins:netbox_user:userlist', args=[self.pk])

    def get_status_user_color(self):
        return ActionChoicesStatusUserColor.colors.get(self.status_user)
    
    def total_resources_count(self):
        user_resources_count = ResourceAccess.objects.filter(user=self).count() 
        group_resources_count = ResourceGroups.objects.filter(groupslist__in=self.groups.all()).count()

        return user_resources_count + group_resources_count
    
    def save(self, *args, **kwargs):
        # Salva o usuário normalmente
        super().save(*args, **kwargs)
        
    def get_group_association_date(self, group):
        try:
            association = self.group_associations.get(group=group)
            return association.data_associacao
        except UserGroupAssociation.DoesNotExist:
            return None
        
    def clone(self):
        attrs = super().clone()
        attrs['extra-value'] = 123
        return attrs



class ResourceAccess(NetBoxModel):
    user = models.ForeignKey(
        to=UserList,
        on_delete=models.CASCADE,
        related_name='rules',
        blank=True
    )

    periodo = models.CharField(
        max_length=30,
        choices=ActionChoicesPeriodo._choices,
    )

    index = models.IntegerField()

    comments = models.TextField(blank=True)

    action = models.CharField(
        max_length=30,
        blank=True
    )

    tipo_acesso = models.CharField(
        choices=ActionChoicesType._choices,
        blank=True
    )

    data_concessao = models.DateField(blank=True)
    data_expiracao = models.DateField(blank=True, null=True)

    justificativa = models.TextField(blank=True)

    recurso = models.ForeignKey(
        to=Resources,
        on_delete=models.CASCADE,
        related_name='rules',
        blank=True
    )

    aprovador = models.ForeignKey(
        to=Approver,
        on_delete=models.CASCADE,
        related_name='rules',
        blank=True
    )

    ambiente = models.ManyToManyField(Environment, blank=True)

    status = models.CharField(
        max_length=30,
        choices=ActionChoices._choices,
        blank=True
    )

    clone_fields = (
        'recurso', 'tipo_acesso', 'aprovador', 'status','ambiente','tags'
    )

    prerequisite_models = (
        'netbox_user.Environment',
        'netbox_user.Approver',
    )

    class Meta:
        ordering = ('user', 'index')
        verbose_name = "Recursos dos Usuário"

        unique_together = ('user', 'recurso')

    def __str__(self):
        return self.recurso.recurso
    
    def get_status_color(self):
        return ActionChoices.colors.get(self.status)

    def get_tipo_acesso_color(self):
        return ActionChoicesType.colors.get(self.tipo_acesso)
    
    def get_periodo_color(self):
        return ActionChoicesPeriodo.colors.get(self.periodo)
    

    def get_absolute_url(self):
        return reverse('plugins:netbox_user:pluginuserrule', args=[self.pk])
    
    def save(self, *args, **kwargs):
        if self.index is None:
            last_index = ResourceAccess.objects.filter(user=self.user).aggregate(Max('index'))['index__max']
            self.index = (last_index or 0) + 1  
        super().save(*args, **kwargs)

    def clean(self):
        
        if self.data_concessao and self.data_expiracao:
            if self.data_concessao > self.data_expiracao:
                raise ValidationError({
                    'data_concessao': 'A data de concessão não pode ser maior que a data de expiração.'
                })
        if not self.data_expiracao:  
            if self.periodo != 'permanente': 
                raise ValidationError({
                    'periodo': 'Quando a data de expiração está vazia, o período deve ser permanente.'
                })
        else:  
            if self.periodo != 'temporario':
                raise ValidationError({
                    'periodo': 'Quando a data de expiração é preenchida, o período deve ser temporário.'
                })

        super().clean()

class ResourceGroups(NetBoxModel):
    index = models.IntegerField()

    groupslist = models.ForeignKey(
        to=Groups,
        on_delete=models.CASCADE,
        related_name='resource_group_rules'
    )

    recurso = models.ForeignKey(
        to=Resources,
        on_delete=models.CASCADE,
        related_name='resource_group_rules'
    )

    tipo_acesso = models.CharField(
        choices=ActionChoicesType._choices,
        blank=True
    )

    aprovador = models.ForeignKey(
        to=Approver,
        on_delete=models.CASCADE,
        related_name='resource_aprovador'
    )

    ambiente = models.ManyToManyField(
        Environment, blank=True
    )
    comments = models.TextField(blank=True)


    clone_fields = (
        'groupslist', 'tipo_acesso', 'aprovador','ambiente','tags'
    )

    prerequisite_models = (
        'netbox_user.Environment',
        'netbox_user.Approver',
        'netbox_user.Groups',
        'netbox_user.Resources',
    )

    class Meta:
        ordering = ('groupslist','index' )
        verbose_name = "Recursos dos grupo"
        unique_together = ('groupslist', 'recurso')

    def __str__(self):
        return self.recurso.recurso
    
    def clean(self):
        
        existing_resource = ResourceGroups.objects.filter(
            groupslist=self.groupslist, 
            recurso=self.recurso
        ).exclude(pk=self.pk) 
        
        if existing_resource.exists():
            raise ValidationError(f'O recurso "{self.recurso}" já está atribuído a este grupo.')
        
        super().clean()

    def get_absolute_url(self):
        return reverse('plugins:netbox_user:resourcegroups', args=[self.pk])
    
    def get_user_access(self, user):
        return self.user_access.filter(user=user).first()
    
    def save(self, *args, **kwargs):
        # Auto-generate the index if it's not provided
        if self.index is None:
            last_index = ResourceGroups.objects.filter(groupslist=self.groupslist).aggregate(Max('index'))['index__max']
            self.index = (last_index or 0) + 1  # Start from 1 if no records exist
        super().save(*args, **kwargs)
        
        
class UserGroupAssociation(models.Model):
    user = models.ForeignKey(UserList, on_delete=models.CASCADE, related_name='group_associations')
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='user_associations')
    data_associacao = models.DateField(auto_now_add=True)  
    
    class Meta:
        unique_together = ('user', 'group') 
        
    def __str__(self):
        return f"{self.user.name} - {self.group.grupo} ({self.data_associacao})"




