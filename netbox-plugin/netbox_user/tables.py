import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import UserList, ResourceAccess, Resources, Environment,Groups
from netbox.tables.columns import TagColumn  

class UserListTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    groups = tables.Column(
        verbose_name="Grupo",
        accessor='groups.name',
        linkify=True
    )

    def render_groups(self, value):
        """
        Renderiza os nomes dos grupos associados ao usuário.
        Assume que 'value' é uma lista de objetos de grupos.
        """
        # Se 'value' for uma lista de grupos, retorna uma string com os nomes
        return ", ".join([group.name for group in value])

    rules_count = tables.Column(
        verbose_name="Recursos",
        accessor="rules.count", 
    )

    status_user = tables.Column(
        verbose_name="Status User",
    )

    tags = TagColumn()
    
    status_user = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = UserList
        fields = ('pk', 'id', 'name', 'groups', 'comments', 'status_user','tags','setor', 'rules_count' )
        default_columns = ('name', 'groups','status_user','tags','setor', 'rules_count' )


class UserListRuleTable(NetBoxTable):

    user = tables.Column(
        linkify=True
    )
    index = tables.Column(
        linkify=True
    )

    recurso = tables.Column(
        linkify=True
    )

    tags = TagColumn()

    tipo_acesso = tables.Column(verbose_name="Tipo Acesso")
    data_concessao = tables.DateColumn(verbose_name="Data Concessão")
    data_expiracao = tables.DateColumn(verbose_name="Data Expiração")
    aprovador = tables.Column(verbose_name="Aprovador")
    justificativa = tables.Column(verbose_name="Justificativa")
    observacoes = tables.Column(verbose_name="Observações")
    ambiente = tables.Column(verbose_name="Ambiente")

    tipo_acesso = ChoiceFieldColumn()
    ambiente = ChoiceFieldColumn()
    status = ChoiceFieldColumn()
    
    class Meta(NetBoxTable.Meta):
        model = ResourceAccess
        fields = (
            'pk', 'id', 'recurso', 'user','tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'justificativa', 'status','observacoes','ambiente', 'tags'
        )
        default_columns = (
            'recurso','user', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'justificativa', 'status','observacoes','ambiente', 'tags'
        )




class ResourcesTable(NetBoxTable):
    recurso = tables.Column(
        linkify=True
    )

    tags = TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Resources
        fields = ('pk', 'id', 'recurso',  'comments', 'tags')
        default_columns = ('recurso',  'comments', 'tags' )



class EnvironmentTable(NetBoxTable):
    environment = tables.Column(
        linkify=True
    )

    tags = TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Environment
        fields = ('pk', 'id', 'environment',  'comments', 'tags')
        default_columns = ('environment',  'comments', 'tags' )


class GroupTable(NetBoxTable):
    group = tables.Column(
        linkify=True
    )

    tags = TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Groups
        fields = ('pk', 'id', 'group',  'comments', 'tags')
        default_columns = ('group',  'comments', 'tags' )



