from django.db import models
from netbox.models import NetBoxModel

from utilities.choices import ChoiceSet
from django.urls import reverse # type: ignore
from django.db.models import Max

class ActionChoicesStatusUser(ChoiceSet):
    key = 'UserList.status_user'

    CHOICES = [
        ('active', 'Active', 'green'),
        ('deactivate', 'Deactivate', 'red'),
    ]

# Modelo para o usuário
class UserList(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    comments = models.TextField(blank=True)

    status_user = models.CharField(
        max_length=30,
        choices=ActionChoicesStatusUser
    )

    class Meta:
        app_label = "netbox_user"
        ordering = ('name',)
        verbose_name = "User"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_user:userlist', args=[self.pk])

    def get_status_user_color(self):
        return ActionChoicesStatusUser.colors.get(self.status_user)


class ActionChoices(ChoiceSet):
    key = 'ResourceAccess.status'

    CHOICES = [
        ('active', 'Active', 'green'),
        ('expired', 'Expired', 'red'),
    ]


class ActionChoicesType(ChoiceSet):
    key = 'ResourceAccess.access'

    CHOICES = [
        ('leitura', 'Leitura', 'green'),
        ('leituraescrita', 'Leitura e Escrita', 'orange'),
    ]


class ActionChoicesAmbiente(ChoiceSet):
    key = 'ResourceAccess.ambiente'

    CHOICES = [
        ('phoebuslocal', 'Phoebus Local', 'green'),
        ('phoebusteste', 'Phoebus Teste', 'green'),
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
        choices=ActionChoicesType,
        blank=True
    )

    data_concessao = models.DateField()
    data_expiracao = models.DateField()
    aprovador = models.CharField(max_length=100, blank=True)
    justificativa = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    

    ambiente = models.CharField(
        max_length=30,
        choices=ActionChoicesAmbiente
    )

    status = models.CharField(
        max_length=30,
        choices=ActionChoices
    )

    class Meta:
        ordering = ('user', 'index')
        unique_together = ('user', 'index')
        verbose_name = "Resource User"

    def __str__(self):
        # Alterado para garantir que o nome completo do usuário seja usado
        return self.recurso
    
    def get_choices_color(self):
        return ActionChoices.colors.get(self.status)

    def get_ambiente_color(self):
        return ActionChoicesAmbiente.colors.get(self.ambiente)

    def get_absolute_url(self):
        return reverse('plugins:netbox_user:pluginuserrule', args=[self.pk])
    
    def save(self, *args, **kwargs):
        # Auto-generate the index if it's not provided
        if self.index is None:
            # Find the max index for the user and increment it
            last_index = ResourceAccess.objects.filter(user=self.user).aggregate(Max('index'))['index__max']
            self.index = (last_index or 0) + 1  # Start from 1 if no records exist
        super().save(*args, **kwargs)
