from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import UserList, ResourceAccess, Resources, Environment, Groups, Approver, Sector, ResourceGroups
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer



class ResourceAccessSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserList.objects.all())

    class Meta:
        model = ResourceAccess
        fields = (
            'id', 'user', 'recurso', 'tipo_acesso', 'data_concessao', 'data_expiracao',
            'aprovador', 'justificativa', 'status', 'ambiente'
        )






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
            'id', 'ambiente', 'comments', 'tags'
        )

class EnvironmentListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:environmentlist-detail' 
        )
    
    class Meta:
        model = Environment
        fields = (
            'id', 'ambiente', 'comments', 'tags','url',
        )


class NestedEnvironmentListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:environmentlist-detail'
    )

    class Meta:
        model = Environment
        fields = ('id', 'ambiente', 'comments', 'tags','url')
### ///// ENVIRONMENT



### GROUPS
class GroupsSerializer(NetBoxModelSerializer):

    class Meta:
        model = Groups
        fields = (
            'id', 'grupo', 'comments', 'tags'
        )

class GroupsListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:grouplist-detail' 
        )
    
    class Meta:
        model = Groups
        fields = (
            'id', 'grupo', 'comments', 'tags','url',
        )


class NestedGroupsListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:grouplist-detail'
    )

    class Meta:
        model = Groups
        fields = ('id', 'recurso', 'comments', 'tags','url')
### ///// ENVIRONMENT



class UserListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:userlist-detail'
    )
    rule_count = serializers.IntegerField(read_only=True)

    groups = GroupsSerializer(many=True, read_only=True)
	
    class Meta:
        model = UserList
        fields = ('id', 'name','groups', 'setor','comments','rule_count', 'url')


### Approver
class ApproverSerializer(NetBoxModelSerializer):

    class Meta:
        model = Approver
        fields = (
            'id', 'aprovador', 'comments', 'tags'
        )

class ApproverListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:approverlist-detail' 
        )
    
    class Meta:
        model = Approver
        fields = (
            'id', 'aprovador', 'comments', 'tags','url',
        )


class NestedApproverListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:approverlist-detail'
    )

    class Meta:
        model = Approver
        fields = ('id', 'aprovador', 'comments', 'tags','url')
### ///// Approver




### Sector
class SectorSerializer(NetBoxModelSerializer):

    class Meta:
        model = Sector
        fields = (
            'id', 'setor', 'comments', 'tags'
        )

class SectorListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:sectorlist-detail' 
        )
    
    class Meta:
        model = Sector
        fields = (
            'id', 'setor', 'comments', 'tags','url',
        )


class NestedSectorListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:sectorlist-detail'
    )

    class Meta:
        model = Sector
        fields = ('id', 'setor', 'comments', 'tags','url')
### ///// Sector






### Resource Groups
class ResourceGroupsSerializer(NetBoxModelSerializer):

    class Meta:
        model = ResourceGroups
        fields = (
            'id', 'recurso','groupslist', 'tipo_acesso', 'aprovador', 'ambiente','comments'
        )

class ResourceGroupsListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:resourcegroups-detail' 
        )
    
    
    class Meta:
        model = ResourceGroups
        fields = (
            'id', 'recurso','groupslist', 'tipo_acesso', 'aprovador','ambiente','comments', 'url'
        )


class NestedResourceGroupsListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:resourcegroups-detail'
    )

    class Meta:
        model = ResourceGroups
        fields = ('id', 'recurso','groupslist', 'tipo_acesso', 'aprovador', 'ambiente','comments','url')
### ///// Sector


class NestedAccessListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:userlist-detail'
    )

    class Meta:
        model = UserList
        fields = ('id', 'url', 'name')

class NestedAccessListRuleSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:pluginuserrule-detail'
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
                  'data_expiracao', 'aprovador', 'justificativa', 'status', 'ambiente', 'url')