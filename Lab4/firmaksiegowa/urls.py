from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('account/', views.AccountList.as_view()),
    path('account/<int:pk>/', views.AccountDetail.as_view()),
    path('client/', views.ClientList.as_view()),
    path('client/<int:pk>/', views.ClientDetail.as_view()),
    path('document/', views.DocumentList.as_view()),
    path('document/<int:pk>/', views.DocumentDetail.as_view()),
    path('documentType/', views.DocumentTypeList.as_view()),
    path('documentType/<int:pk>/', views.DocumentTypeDetail.as_view()),
    path('purchasesSales/', views.Purchases_SalesList.as_view()),
    path('purchasesSales/<int:pk>/', views.Purchases_SalesDetail.as_view()),
    path('declaration/', views.DeclarationsList.as_view()),
    path('declaration/<int:pk>/', views.DeclarationsDetail.as_view()),
    path('currency/', views.CurrencyList.as_view()),
    path('currency/<int:pk>/', views.CurrencyDetail.as_view()),
    path('pit/', views.PITList.as_view()),
    path('pit/<int:pk>/', views.PITDetail.as_view()),
]