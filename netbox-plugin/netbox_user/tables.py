import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import UserList, ResourceAccess, Resources, Environment,Groups, Approver, Sector
from netbox.tables.columns import TagColumn  

class UserListTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    groups = tables.ManyToManyColumn()

    setor = tables.ManyToManyColumn()

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
        fields = ('pk', 'id', 'name', 'groups', 'comments', 'status_user','tags','setor','rules_count' )
        default_columns = ('name', 'groups','status_user','tags','setor', 'rules_count' )


class UserListRuleTable(NetBoxTable):

    user = tables.Column(
        linkify=True
    )
    index = tables.Column(
        linkify=True
    )

    tags = TagColumn()

    tipo_acesso = tables.Column(verbose_name="Tipo Acesso")
    data_concessao = tables.DateColumn(verbose_name="Data Concessão")
    data_expiracao = tables.DateColumn(verbose_name="Data Expiração")
    aprovador = tables.ManyToManyColumn(verbose_name="Aprovador")
    justificativa = tables.Column(verbose_name="Justificativa")
    ambiente = tables.ManyToManyColumn(verbose_name="Ambiente")
    recurso = tables.ManyToManyColumn(linkify=True)

    tipo_acesso = ChoiceFieldColumn()
    status = ChoiceFieldColumn()
    
    class Meta(NetBoxTable.Meta):
        model = ResourceAccess
        fields = (
            'pk', 'id', 'recurso', 'user','tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'justificativa', 'status','ambiente','comments','tags'
        )
        default_columns = (
            'recurso','user', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'justificativa', 'status','ambiente','comments','tags'
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
    ambiente = tables.Column(
        linkify=True
    )

    tags = TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Environment
        fields = ('pk', 'id', 'ambiente',  'comments', 'tags')
        default_columns = ('ambiente',  'comments', 'tags' )


class GroupTable(NetBoxTable):
    grupo = tables.Column(
        linkify=True
    )

    tags = TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Groups
        fields = ('pk', 'id', 'grupo',  'comments', 'tags')
        default_columns = ('grupo',  'comments', 'tags' )



class ApproverTable(NetBoxTable):
    aprovador = tables.Column(
        linkify=True
    )

    tags = TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Approver
        fields = ('pk', 'id', 'aprovador',  'comments', 'tags')
        default_columns = ('aprovador',  'comments', 'tags' )


class SectorTable(NetBoxTable):
    setor = tables.Column(
        linkify=True
    )

    tags = TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Sector
        fields = ('pk', 'id', 'setor',  'comments', 'tags')
        default_columns = ('setor',  'comments', 'tags' )

