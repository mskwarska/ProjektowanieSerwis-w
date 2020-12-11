from django.urls import path
from . import views

urlpatterns  = [
    path('account/', views.AccountList.as_view(), name=views.AccountList.name),
    path('account/<int:pk>/', views.AccountDetail.as_view(), name=views.AccountDetail.name),
    path('client/', views.ClientList.as_view(), name=views.ClientList.name),
    path('client/<int:pk>/', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('document/', views.DocumentList.as_view(), name=views.DocumentList.name),
    path('document/<int:pk>/', views.DocumentDetail.as_view(), name=views.DocumentDetail.name),
    path('documentType/', views.DocumentTypeList.as_view(), name=views.DocumentTypeList.name),
    path('documentType/<int:pk>/', views.DocumentTypeDetail.as_view(), name=views.DocumentTypeDetail.name),
    path('purchasesSales/', views.PurchasesSalesList.as_view(), name=views.PurchasesSalesList.name),
    path('purchasesSales/<int:pk>/', views.PurchasesSalesDetail.as_view(), name=views.PurchasesSalesDetail.name),
    path('declaration/', views.DeclarationList.as_view(), name=views.DeclarationList.name),
    path('declaration/<int:pk>/', views.DeclarationDetail.as_view(), name=views.DeclarationDetail.name),
    path('currency/', views.CurrencyList.as_view(), name=views.CurrencyList.name),
    path('currency/<int:pk>/', views.CurrencyDetail.as_view(), name=views.CurrencyDetail.name),
    path('pit/', views.PITList.as_view(), name=views.PITList.name),
    path('pit/<int:pk>/', views.PITDetail.as_view(), name=views.PITDetail.name),
]