from django.urls import path
from accountmanager import views

urlpatterns = [

    path('',views.list_claims,name="list_claims" ),

    # Claims
    path('claims/',views.list_claims, name="list_claims"),
    path('claimshistory/',views.list_claimshistory, name="list_claimshistory"),
    path('approve_claim/<int:claim_id>/', views.approve_claim, name='approve_claim'),
    path('deny_claim/<int:claim_id>/', views.deny_claim, name='deny_claim'),
]
