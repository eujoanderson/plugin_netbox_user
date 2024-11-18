from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView



urlpatterns = (
    # User list
    path('plugin-user/', views.UserListListView.as_view(), name='userlist_list'),
    path('plugin-user/add/', views.UserListEditView.as_view(), name='userlist_add'),
    path('plugin-user/<int:pk>/', views.UserListView.as_view(), name='userlist'),
    path('plugin-user/<int:pk>/edit/', views.UserListEditView.as_view(), name='userlist_edit'),
    path('plugin-user/<int:pk>/delete/', views.UserListDeleteView.as_view(), name='userlist_delete'),

    path('plugin-user/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='userlist_changelog', kwargs={
        'model': models.UserList
    }),

    # User list rules
    path('rules/', views.UserListRuleListView.as_view(), name='resourceaccess_list'),
    path('rules/add/', views.UserListRuleEditView.as_view(), name='resourceaccess_add'),
    path('rules/<int:pk>/', views.UserListRuleView.as_view(), name='pluginuserrule'),
    path('rules/<int:pk>/edit/', views.UserListRuleEditView.as_view(), name='resourceaccess_edit'),
    path('rules/<int:pk>/delete/', views.UserListRuleDeleteView.as_view(), name='resourceaccess_delete'),

    path('rules/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='resourceaccess_changelog', kwargs={
        'model': models.ResourceAccess
    }),
)

