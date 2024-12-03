from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import UserList, ResourceAccess, Resources, Environment, Groups, Approver, Sector, ResourceGroups
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer



### //// NESTED


class NestedUserListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:userlist-detail'
    )

    class Meta:
        model = UserList
        fields = ('id', 'display','url', 'name','groups', 'setor', 'comments')

class NestedResourceAccessSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:pluginuserrule-detail'
    )

    class Meta:
        model = ResourceAccess
        fields = ('id', 'display','user','index', 'recurso', 'tipo_acesso', 'data_concessao',
                  'data_expiracao', 'aprovador', 'justificativa', 'status', 'ambiente','url', 'comments')


class NestedResourcesSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:resources-detail'
    )

    class Meta:
        model = Resources
        fields = ('id', 'grupo','display','url',)


class NestedSectorSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:sector-detail'
    )

    class Meta:
        model = Sector
        fields = ('id','setor','display', 'comments', 'url')


class NestedApproverSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:approver-detail'
    )

    class Meta:
        model = Approver
        fields = ('id', 'display','aprovador', 'comments', 'url')


class NestedGroupsSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:groups-detail'
    )

    class Meta:
        model = Groups
        fields = ('id', 'grupo','display','comments','url')


class NestedEnvironmentSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:environment-detail'
    )

    class Meta:
        model = Environment
        fields = ('id', 'display','ambiente', 'comments', 'url')


class NestedResourcesSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:resources-detail'
    )

    class Meta:
        model = Resources
        fields = ('id', 'display','recurso', 'comments','url')

class NestedResourceGroupsListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:resourcegroups-detail'
    )

    class Meta:
        model = ResourceGroups
        fields = ('id', 'recurso','groupslist', 'tipo_acesso', 'aprovador', 'ambiente','comments','url')
### //// Nested





### ENVIRONMENT
class EnvironmentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:environment-detail' 
        )
    
    class Meta:
        model = Environment
        fields = (
            'id', 'ambiente', 'comments', 'tags','url',
        )
### ///// ENVIRONMENT



### GROUPS
class GroupsSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:groups-detail' 
        )
    
    class Meta:
        model = Groups
        fields = (
            'id', 'grupo', 'comments', 'tags','url',
        )

### ///// GROUPS



class UserListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:userlist-detail'
    )
    rule_count = serializers.IntegerField(read_only=True)

    groups = NestedGroupsSerializer(many=True)
    setor = NestedSectorSerializer(many=True)
	
    class Meta:
        model = UserList
        fields = ('id', 'name','groups', 'setor','comments','rule_count','tags','url')


### Approver

class ApproverSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:approver-detail' 
        )
    
    class Meta:
        model = Approver
        fields = (
            'id', 'aprovador', 'comments', 'tags','url',
        )

### ///// Approver




### Sector

class SectorSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:sector-detail' 
        )
    
    class Meta:
        model = Sector
        fields = (
            'id', 'comments', 'tags','url',
        )

### ///// Sector






### Resource Groups
class ResourceGroupsSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:resourcegroups-detail' 
        )
    
    recurso = NestedResourcesSerializer()
    groupslist = NestedGroupsSerializer()
    aprovador = NestedApproverSerializer()
    ambiente = NestedEnvironmentSerializer(many=True)
    
    
    class Meta:
        model = ResourceGroups
        fields = (
            'id', 'recurso','groupslist', 'tipo_acesso', 'aprovador','ambiente','comments', 'url'
        )

### ///// Sector

        

class ResourceAccessSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_user-api:resourceaccess-detail'
    )

    user = NestedUserListSerializer()
    recurso = NestedResourcesSerializer()
    aprovador = NestedApproverSerializer()
    ambiente = NestedEnvironmentSerializer(many=True)

    class Meta:
        model = ResourceAccess
        fields = ('id', 'user','index', 'recurso', 'tipo_acesso', 'data_concessao',
                  'data_expiracao', 'aprovador', 'justificativa', 'status', 'ambiente', 'url')
        



### RESOURCES
class ResourcesSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_user-api:resources-detail' 
        )

    class Meta:
        model = Resources
        fields = (
            'id', 'recurso', 'comments', 'tags','url',
        )
        
