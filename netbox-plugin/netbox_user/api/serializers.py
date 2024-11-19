from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import UserList, ResourceAccess, Resources, Environment, Groups
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
        fields = ('id', 'name','groups', 'comments','rule_count', 'url')



### RESOURCES
class ResourcesSerializer(NetBoxModelSerializer):

    class Meta:
        model = Resources
        fields = (
            'id', 'recurso', 'comments', 'tags'
        )

class ResourcesListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:resourceslist-detail' 
        )
    
    class Meta:
        model = Resources
        fields = (
            'id', 'recurso', 'comments', 'tags','url',
        )


class NestedResourcesListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:resourceslist-detail'
    )

    class Meta:
        model = Resources
        fields = ('id', 'recurso', 'comments', 'tags','url')
### //// RESOURCES






### ENVIRONMENT
class EnvironmentSerializer(NetBoxModelSerializer):

    class Meta:
        model = Environment
        fields = (
            'id', 'environment', 'comments', 'tags'
        )

class EnvironmentListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:environmentlist-detail' 
        )
    
    class Meta:
        model = Environment
        fields = (
            'id', 'environment', 'comments', 'tags','url',
        )


class NestedEnvironmentListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:environmentlist-detail'
    )

    class Meta:
        model = Environment
        fields = ('id', 'recurso', 'comments', 'tags','url')
### ///// ENVIRONMENT



### ENVIRONMENT
class GroupsSerializer(NetBoxModelSerializer):

    class Meta:
        model = Groups
        fields = (
            'id', 'group', 'comments', 'tags'
        )

class GroupsListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:grouplist-detail' 
        )
    
    class Meta:
        model = Groups
        fields = (
            'id', 'group', 'comments', 'tags','url',
        )


class NestedGroupsListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:grouplist-detail'
    )

    class Meta:
        model = Groups
        fields = ('id', 'recurso', 'comments', 'tags','url')
### ///// ENVIRONMENT



















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

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:pluginuserrule-detail'
    )

    class Meta:
        model = ResourceAccess
        fields = ('id', 'user','index', 'recurso', 'tipo_acesso', 'data_concessao',
                  'data_expiracao', 'aprovador', 'justificativa', 'status', 'observacoes', 'ambiente', 'url')