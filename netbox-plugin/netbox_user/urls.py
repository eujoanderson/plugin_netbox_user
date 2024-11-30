from django.urls import include,path
from . import models, views
from netbox.views.generic import ObjectChangeLogView


urlpatterns = (
    # User list
    path('plugin-user/', views.UserListListView.as_view(), name='userlist_list'),
    path('plugin-user/add/', views.UserListEditView.as_view(), name='userlist_add'),
    path('plugin-user/<int:pk>/', views.UserListView.as_view(), name='userlist'),

    #### User List BULK
	path('plugin-user/edit/', views.UserListBulkEditView.as_view(), name='userlist_bulk_edit'),
	path('plugin-user/delete/', views.UserListBulkDeleteView.as_view(), name='userlist_bulk_delete'),

    path('plugin-user/<int:pk>/edit/', views.UserListEditView.as_view(), name='userlist_edit'),
    path('plugin-user/<int:pk>/delete/', views.UserListDeleteView.as_view(), name='userlist_delete'),

    path('plugin-user/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='userlist_changelog', kwargs={
        'model': models.UserList
    }),

    # User list rules
    path('rules/', views.UserListRuleListView.as_view(), name='resourceaccess_list'),
    path('rules/add/', views.UserListRuleEditView.as_view(), name='resourceaccess_add'),
    path('rules/<int:pk>/', views.UserListRuleView.as_view(), name='pluginuserrule'),
    
    #### Rules BULK
    path('rules/edit/', views.UserListRuleBulkEditView.as_view(), name='resourceaccess_bulk_edit'),
	path('rules/delete/', views.UserListRuleBulkDeleteView.as_view(), name='resourceaccess_bulk_delete'),

    path('rules/<int:pk>/edit/', views.UserListRuleEditView.as_view(), name='resourceaccess_edit'),
    path('rules/<int:pk>/delete/', views.UserListRuleDeleteView.as_view(), name='resourceaccess_delete'),

    path('rules/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='resourceaccess_changelog', kwargs={
        'model': models.ResourceAccess
    }),


    # Resources 
    path('resources/', views.ResourcesListListView.as_view(), name='resources_list'),
    path('resources/add/', views.ResourcesListEditView.as_view(), name='resources_add'),
    path('resources/<int:pk>/', views.ResourcesView.as_view(), name='resourceslist'),

    #### Resources BULK
    path('resources/edit/', views.ResourcesBulkEditView.as_view(), name='resources_bulk_edit'),
    path('resources/delete/', views.ResourcesBulkDeleteView.as_view(), name='resources_bulk_delete'),

    path('resources/<int:pk>/edit/', views.ResourcesListEditView.as_view(), name='resources_edit'),
    path('resources/<int:pk>/delete/', views.ResourcesListDeleteView.as_view(), name='resources_delete'),

    path('resources/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='resources_changelog', kwargs={
        'model': models.Resources
    }),


    # environment 
    path('environment/', views.EnvironmentListListView.as_view(), name='environment_list'),
    path('environment/add/', views.EnvironmentListEditView.as_view(), name='environment_add'),
    path('environment/<int:pk>/', views.EnvironmentView.as_view(), name='environmentlist'),

    #### Environment BULK
    path('environment/edit/', views.EnvironmentBulkEditView.as_view(), name='environment_bulk_edit'),
    path('environment/delete/', views.EnvironmentBulkDeleteView.as_view(), name='environment_bulk_delete'),

    path('environment/<int:pk>/edit/', views.EnvironmentListEditView.as_view(), name='environment_edit'),
    path('environment/<int:pk>/delete/', views.EnvironmentListDeleteView.as_view(), name='environment_delete'),

    path('environment/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='environment_changelog', kwargs={
        'model': models.Environment
    }),

    # group 
    path('group/', views.GroupListListView.as_view(), name='groups_list'),
    path('group/add/', views.GroupListEditView.as_view(), name='groups_add'),
    path('group/<int:pk>/', views.GroupView.as_view(), name='groupslist'),


    #### Group BULK
    path('group/edit/', views.GroupListBulkEditView.as_view(), name='groups_bulk_edit'),
    path('group/delete/', views.GroupListBulkDeleteView.as_view(), name='groups_bulk_delete'),

    path('group/<int:pk>/edit/', views.GroupListEditView.as_view(), name='groups_edit'),
    path('group/<int:pk>/delete/', views.GroupListDeleteView.as_view(), name='groups_delete'),

    path('group/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='groups_changelog', kwargs={
        'model': models.Groups
    }),
	
    path('groups/', views.GroupView.as_view(), name='groups-list'),
    
	
	

    # Approver 
    path('approver/', views.ApproverListListView.as_view(), name='approver_list'),
    path('approver/add/', views.ApproverListEditView.as_view(), name='approver_add'),
    path('approver/<int:pk>/', views.ApproverView.as_view(), name='approverlist'),

    #### Approver BULK
    path('approver/edit/', views.ApproverBulkEditView.as_view(), name='approver_bulk_edit'),
    path('approver/delete/', views.ApproverBulkDeleteView.as_view(), name='approver_bulk_delete'),

    path('approver/<int:pk>/edit/', views.ApproverListEditView.as_view(), name='approver_edit'),
    path('approver/<int:pk>/delete/', views.ApproverListDeleteView.as_view(), name='approver_delete'),

    path('approver/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='approver_changelog', kwargs={
        'model': models.Approver
    }),
	

    # Sector 
    path('sector/', views.SectorListListView.as_view(), name='sector_list'),
    path('sector/add/', views.SectorListEditView.as_view(), name='sector_add'),
    path('sector/<int:pk>/', views.SectorView.as_view(), name='sectorlist'),

    #### Sector BULK
    path('sector/edit/', views.SectorBulkEditView.as_view(), name='sector_bulk_edit'),
    path('sector/delete/', views.SectorBulkDeleteView.as_view(), name='sector_bulk_delete'),

    path('sector/<int:pk>/edit/', views.SectorListEditView.as_view(), name='sector_edit'),
    path('sector/<int:pk>/delete/', views.SectorListDeleteView.as_view(), name='sector_delete'),

    path('sector/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='sector_changelog', kwargs={
        'model': models.Sector
    }),
	

    # resource groups 
    path('resourcegroups/', views.ResourceGroupsListListView.as_view(), name='resourcegroups_list'),
    path('resourcegroups/add/', views.ResourceGroupsListEditView.as_view(), name='resourcegroups_add'),
    path('resourcegroups/<int:pk>/', views.ResourceGroupsView.as_view(), name='resourcegroups'),
 
    #### Resources Groups BULK
	path('resourcegroups/edit/', views.ResourceGroupsBulkEditView.as_view(), name='resourcegroups_bulk_edit'),
	path('resourcegroups/delete/', views.ResourceGroupsBulkDeleteView.as_view(), name='resourcegroups_bulk_delete'),
	
    path('resourcegroups/<int:pk>/edit/', views.ResourceGroupsListEditView.as_view(), name='resourcegroups_edit'),
    path('resourcegroups/<int:pk>/delete/', views.ResourceGroupsListDeleteView.as_view(), name='resourcegroups_delete'),

    path('resourcegroups/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='resourcegroups_changelog', kwargs={
        'model': models.ResourceGroups
    }),	
)

