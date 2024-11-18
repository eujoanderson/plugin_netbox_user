import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import UserList, ResourceAccess
from netbox.tables.columns import TagColumn  

class UserListTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

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
        fields = ('pk', 'id', 'name',  'comments', 'status_user','tags','setor', 'rules_count' )
        default_columns = ('name', 'comments','status_user','tags','setor', 'rules_count' )


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
            'pk', 'id', 'recurso', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'justificativa', 'status','observacoes','ambiente'
        )
        default_columns = (
            'user','recurso', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'justificativa', 'status','observacoes','ambiente'
        )


