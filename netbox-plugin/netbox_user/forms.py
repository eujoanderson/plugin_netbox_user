
from .models import UserList, ResourceAccess
from utilities.forms.fields import CommentField
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm


class UserListForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = UserList
        fields = ('name', 'comments','status_user', 'tags')


class UserListRuleForm(NetBoxModelForm):
    comments = CommentField()

    user = forms.ModelChoiceField(queryset=UserList.objects.all(), required=True)

    data_concessao = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        label="Data de Concessão"
    )

    data_expiracao = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        label="Data de Expiração"
    )


    class Meta:
        model = ResourceAccess
        fields = (
            'user','recurso', 'tipo_acesso', 'data_concessao',
            'data_expiracao', 'aprovador', 'justificativa', 'status','observacoes','ambiente','comments','tags'
        )

class UserListRuleFilterForm(NetBoxModelFilterSetForm):
    model = ResourceAccess

    user_list = forms.ModelMultipleChoiceField(
        queryset=UserList.objects.all(),
        required=False
    )

    index = forms.IntegerField(
        required=False
    )