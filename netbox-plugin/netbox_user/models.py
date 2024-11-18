from django.db import models
from netbox.models import NetBoxModel

from utilities.choices import ChoiceSet
from django.urls import reverse # type: ignore
from django.db.models import Max
from extras.models import Tag

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


# Modelo para o usuário
class UserList(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    comments = models.TextField(blank=True)
    
    tags = models.ManyToManyField(Tag, blank=True)

    status_user = models.CharField(
        max_length=30,
        choices=ActionChoicesStatusUserColor._choices,
        verbose_name="Status User"
    )

    setor = models.CharField(
        max_length=30,
        choices=ActionChoicesSetor._choices,
        verbose_name="Setor"
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


class ActionChoicesAmbiente(ChoiceSet):
    key = 'ResourceAccess.ambiente'

    CHOICES = [
        ('phoebuslocal', 'Phoebus Local', 'gray'),
        ('phoebusteste', 'Phoebus Teste', 'gray'),
    ]



class ResourceAccess(NetBoxModel):
    user = models.ForeignKey(
        to=UserList,
        on_delete=models.CASCADE,
        related_name='rules'
    )

    index = models.IntegerField()

    action = models.CharField(
        max_length=30
    )

    recurso = models.CharField(max_length=255)  # Nome ou caminho do recurso

    tipo_acesso = models.CharField(
        choices=ActionChoicesType._choices,
        blank=True
    )

    data_concessao = models.DateTimeField()
    data_expiracao = models.DateTimeField()
    aprovador = models.CharField(max_length=100, blank=True)
    justificativa = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    

    ambiente = models.CharField(
        max_length=30,
        choices=ActionChoicesAmbiente._choices,
    )

    status = models.CharField(
        max_length=30,
        choices=ActionChoices._choices,
    )

    class Meta:
        ordering = ('user', 'index')
        unique_together = ('user', 'index')
        verbose_name = "Resource User"

    def __str__(self):
        return self.recurso
    
    def get_status_color(self):
        return ActionChoices.colors.get(self.status)

    def get_ambiente_color(self):
        return ActionChoicesAmbiente.colors.get(self.ambiente)

    def get_tipo_acesso_color(self):
        return ActionChoicesType.colors.get(self.tipo_acesso)

    def get_absolute_url(self):
        return reverse('plugins:netbox_user:pluginuserrule', args=[self.pk])
    
    def save(self, *args, **kwargs):
        # Auto-generate the index if it's not provided
        if self.index is None:
            # Find the max index for the user and increment it
            last_index = ResourceAccess.objects.filter(user=self.user).aggregate(Max('index'))['index__max']
            self.index = (last_index or 0) + 1  # Start from 1 if no records exist
        super().save(*args, **kwargs)
