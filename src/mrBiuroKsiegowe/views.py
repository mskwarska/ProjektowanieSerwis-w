from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Account, Client, Document, DocumentType, PurchasesSales, Declaration, Currency, PIT
from .serializers import AccountSerializer, ClientSerializer, DocumentSerializer, DocumentTypeSerializer, PurchasesSalesSerializer, DeclarationSerializer, CurrencySerializer, PITSerializer

class AccountList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ClientList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DocumentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentTypeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

class DocumentTypeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

class PurchasesSalesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchasesSales.objects.all()
    serializer_class = PurchasesSalesSerializer

class PurchasesSalesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchasesSales.objects.all()
    serializer_class = PurchasesSalesSerializer

class DeclarationList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Declaration.objects.all()
    serializer_class = DeclarationSerializer

class DeclarationDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Declaration.objects.all()
    serializer_class = DeclarationSerializer

class CurrencyList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CurrencyDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class PITList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PIT.objects.all()
    serializer_class = PITSerializer

class PITDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PIT.objects.all()
    serializer_class = PITSerializer