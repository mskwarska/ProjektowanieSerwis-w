from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #url(r'^api-auth/', include('rest_framework.urls')),
    path('account/', views.AccountList.as_view(),  name=views.AccountList.name),
    path('account/<int:pk>/', views.AccountDetail.as_view(), name=views.AccountDetail.name),
    path('client/', views.ClientList.as_view(), name=views.ClientList.name),
    path('client/<int:pk>/', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('document/', views.DocumentList.as_view(), name=views.DocumentList.name),
    path('document/<int:pk>/', views.DocumentDetail.as_view(), name=views.DocumentDetail.name),
    path('documentType/', views.DocumentTypeList.as_view(), name=views.DocumentTypeList.name),
    path('documentType/<int:pk>/', views.DocumentTypeDetail.as_view(), name=views.DocumentTypeDetail.name),
    path('purchasesSales/', views.Purchases_SalesList.as_view(), name=views.Purchases_SalesList.name),
    path('purchasesSales/<int:pk>/', views.Purchases_SalesDetail.as_view(), name=views.Purchases_SalesDetail.name),
    path('declaration/', views.DeclarationsList.as_view(), name=views.DeclarationsList.name),
    path('declaration/<int:pk>/', views.DeclarationsDetail.as_view(), name=views.DeclarationsDetail.name),
    path('currency/', views.CurrencyList.as_view(), name=views.CurrencyList.name),
    path('currency/<int:pk>/', views.CurrencyDetail.as_view(), name=views.CurrencyDetail.name),
    path('pit/', views.PITList.as_view(), name=views.PITList.name),
    path('pit/<int:pk>/', views.PITDetail.as_view(), name=views.PITDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]