from django.urls import path
from projectmanager import views

urlpatterns = [

    path('',views.list_clients,name="list_clients" ),

    # Clients
    path('clients/',views.list_clients, name="list_clients"),
    path('add_client/', views.add_client, name="add_client"),
    path('edit_client/<int:client_id>/', views.edit_client, name="edit_client"),
    path('delete_client/<int:client_id>/', views.delete_client, name="delete_client"),

    # Projects
    path('projects/', views.list_projects, name='list_projects'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),

    # Assignments
    path('assignments/', views.list_assignments, name='list_assignments'),
    path('add_assignment/', views.add_assignment, name='add_assignment'),
    path('delete_assignment/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),

]
