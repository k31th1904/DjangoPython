from django.urls import path
from worker import views

urlpatterns = [

    path('',views.list_myassignments,name="list_myassignments" ),

    # Assignments
    path('myassignments/', views.list_myassignments, name='list_myassignments'),
    path('claim/<int:assignment_id>', views.claim, name='claim'),
    path('myclaims/', views.list_myclaims, name='list_myclaims'),

]
