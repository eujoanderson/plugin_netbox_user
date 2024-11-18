from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import UserList, ResourceAccess
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer



class ResourceAccessSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserList.objects.all())

    class Meta:
        model = ResourceAccess
        fields = (
            'id', 'user', 'recurso', 'tipo_acesso', 'data_concessao', 'data_expiracao',
            'aprovador', 'justificativa', 'status', 'observacoes', 'ambiente'
        )


class UserListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:userlist-detail'
    )
    rule_count = serializers.IntegerField(read_only=True)
	
    class Meta:
        model = UserList
        fields = ('id', 'name', 'comments','rule_count', 'url')      

class NestedAccessListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:userlist-detail'
    )

    class Meta:
        model = UserList
        fields = ('id', 'url', 'name')

class NestedAccessListRuleSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:-api:pluginuserrule-detail'
    )

    class Meta:
        model = ResourceAccess
        fields = ('id', 'url', 'index')
        

class UserListRuleSerializer(NetBoxModelSerializer):
    data_concessao = serializers.DateField(format="%Y/%m/%d") 
    data_expiracao = serializers.DateField(format="%Y/%m/%d")

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:pluginuserrule-detail'
    )
    user_list = NestedAccessListSerializer()

    class Meta:
        model = ResourceAccess
        fields = ('id', 'user','index', 'recurso', 'tipo_acesso', 'data_concessao',
                  'data_expiracao', 'aprovador', 'justificativa', 'status', 'observacoes', 'ambiente', 'url')