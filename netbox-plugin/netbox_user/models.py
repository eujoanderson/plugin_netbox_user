from django.db import models
from netbox.models import NetBoxModel

from utilities.choices import ChoiceSet
from django.urls import reverse # type: ignore
from django.db.models import Max
from extras.models import Tag


class Resources(NetBoxModel):
    recurso = models.CharField(max_length=100, blank=True)

    comments = models.TextField(blank=True)

    class Meta:
        ordering = ('recurso',)
        verbose_name = "Recurso"

    def __str__(self):
        return self.recurso
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:resourceslist', args=[self.pk])



class Environment(NetBoxModel):
    ambiente = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ('ambiente', )
        verbose_name = "Ambiente"

    def __str__(self):
        return self.ambiente
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:environmentlist', args=[self.pk])


class Approver(NetBoxModel):
    aprovador = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ('aprovador', )
        verbose_name = "Aprovador"

    def __str__(self):
        return self.aprovador
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:approverlist', args=[self.pk])






class Sector(NetBoxModel):
    setor = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ('setor',)
        verbose_name = "Setor"

    def __str__(self):
        return str(self.setor)
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:sectorlist', args=[self.pk])





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

class ActionChoicesType(ChoiceSet):
    key = 'ResourceAccess.tipo_acesso'

    CHOICES = [
        ('leitura', 'Leitura', 'purple'),
        ('leituraescrita', 'Leitura e Escrita', 'purple'),
    ]


# Modelo para grupos
class Groups(NetBoxModel):
    grupo = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ('grupo', )
        verbose_name = "Grupo"

    def __str__(self):
        return self.grupo

    def get_absolute_url(self):
        return reverse('plugins:netbox_user:groupslist', args=[self.pk])



# Modelo para o usuário
class UserList(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    comments = models.TextField(blank=True)

    groups = models.ManyToManyField(Groups,blank=True)

    tags = models.ManyToManyField(Tag, blank=True)

    setor = models.ManyToManyField(Sector, blank=True)

    status_user = models.CharField(
        max_length=30,
        choices=ActionChoicesStatusUserColor._choices,
        verbose_name="Status User"
    )

    class Meta:
        ordering = ('name',)
        verbose_name = "User"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:userlist', args=[self.pk])

    def get_status_user_color(self):
        return ActionChoicesStatusUserColor.colors.get(self.status_user)

## Falta realizar o processo ainda
    def clone(self):
        attrs = super().clone()
        attrs['extra-value'] = 123
        return attrs    


class ResourceAccess(NetBoxModel):
    user = models.ForeignKey(
        to=UserList,
        on_delete=models.CASCADE,
        related_name='rules'
    )

    index = models.IntegerField()

    comments = models.TextField(blank=True)

    action = models.CharField(
        max_length=30
    )

    tipo_acesso = models.CharField(
        choices=ActionChoicesType._choices,
        blank=True
    )

    data_concessao = models.DateTimeField()
    data_expiracao = models.DateTimeField()

    justificativa = models.TextField(blank=True)

    recurso = models.ForeignKey(
        to=Resources,
        on_delete=models.CASCADE,
        related_name='rules'
    )

    aprovador = models.ForeignKey(
        to=Approver,
        on_delete=models.CASCADE,
        related_name='rules'
    )

    ambiente = models.ManyToManyField(Environment, blank=True)

    status = models.CharField(
        max_length=30,
        choices=ActionChoices._choices,
    )

    class Meta:
        ordering = ('user', 'index')
        verbose_name = "Resource User"

    def __str__(self):
        return self.recurso.recurso
    
    def get_status_color(self):
        return ActionChoices.colors.get(self.status)

    def get_tipo_acesso_color(self):
        return ActionChoicesType.colors.get(self.tipo_acesso)

    def get_absolute_url(self):
        return reverse('plugins:netbox_user:pluginuserrule', args=[self.pk])
    
    def save(self, *args, **kwargs):
        # Auto-generate the index if it's not provided
        if self.index is None:
            last_index = ResourceAccess.objects.filter(user=self.user).aggregate(Max('index'))['index__max']
            self.index = (last_index or 0) + 1  # Start from 1 if no records exist
        super().save(*args, **kwargs)
