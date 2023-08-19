from django.urls import path
from systemadmin import views

urlpatterns = [

    path('', views.list_employees, name="list_employees"),

    # Employees
    path('employees/', views.list_employees, name="list_employees"),
    path('add_employees/', views.add_employee, name="add_employee"),
    path('edit_employees/<int:employee_id>/', views.edit_employee, name="edit_employee"),
    path('delete_employees/<int:employee_id>/', views.delete_employee, name="delete_employee"),

    # Client Categories
    path('clientcategories/', views.list_clientcategories, name="list_clientcategories"),
    path('add_clientcategory/', views.add_clientcategory, name="add_clientcategory"),
    path('edit_clientcategory/<int:category_id>/', views.edit_clientcategory, name="edit_clientcategory"),
    path('delete_clientcategory/<int:category_id>/', views.delete_clientcategory, name="delete_clientcategory"),

    # Groups
    path('groups/', views.list_groups, name='list_groups'),
    path('add_group/', views.add_group, name='add_group'),
    path('delete_group/<int:group_id>/', views.delete_group, name='delete_group'),

]

