from django.http import HttpResponse
from django.http import Http404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django_filters import FilterSet, DateTimeFilter, AllValuesFilter, NumberFilter

from .models import Account, Client, Document, DocumentType, PurchasesSales, Declaration, Currency, PIT
from .serializers import AccountSerializer, ClientSerializer, DocumentSerializer, DocumentTypeSerializer, PurchasesSalesSerializer, DeclarationSerializer, CurrencySerializer, PITSerializer

class AccountList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    name = 'account-list'

class AccountDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    name = 'account-detail'

class ClientList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name='client-list'
    filter_fields = ['Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON']
    search_fields = ['Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON']
    ordering_fields = ['Name', 'Surname']

class ClientDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name='client-detail'

class DocumentFilter(FilterSet):
    DateFrom = DateTimeFilter(field_name='Date', lookup_expr='gte')
    DateTo = DateTimeFilter(field_name='Date', lookup_expr='lte')

    class Meta:
        model = Document
        fields = ['DateFrom', 'DateTo', 'ClientId', 'DocumentTypeId']

class DocumentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    name='document-list'
    search_fields = ['ClientId', 'Date', 'DocumentTypeId']
    ordering_fields = ['ClientId', 'Date', 'DocumentTypeId']
    filter_class = DocumentFilter

class DocumentDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    name='document-detail'

class DocumentTypeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    name='documenttype-list'
    filter_fields = ['Type']
    search_fields = ['Type']
    ordering_fields = ['Type']

class DocumentTypeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    name='documenttype-detail'

class PurchasesSalesFilter(FilterSet):
    NetAmountFrom = NumberFilter(field_name='NetAmount', lookup_expr='gte')
    NetAmountTo = NumberFilter(field_name='NetAmount', lookup_expr='lte')
    GrossAmountFrom = NumberFilter(field_name='GrossAmount', lookup_expr='gte')
    GrossAmountTo = NumberFilter(field_name='GrossAmount', lookup_expr='lte')

    class Meta:
        model = PurchasesSales
        fields = ['NetAmountFrom', 'NetAmountTo', 'GrossAmountFrom', 'GrossAmountTo', 'DocumentId', 'ProductName']

class PurchasesSalesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchasesSales.objects.all()
    serializer_class = PurchasesSalesSerializer
    name='purchasessales-list'
    search_fields = ['DocumentId', 'ProductName']
    ordering_fields = ['DocumentId', 'ProductName', 'NetAmount', 'GrossAmount']
    filter_class = PurchasesSalesFilter

class PurchasesSalesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchasesSales.objects.all()
    serializer_class = PurchasesSalesSerializer
    name='purchasessales-detail'

class DeclarationFilter(FilterSet):
    AmmountFrom = NumberFilter(field_name='Ammount', lookup_expr='gte')
    AmmountTo = NumberFilter(field_name='Ammount', lookup_expr='lte')
    DateFrom_From = DateTimeFilter(field_name='DateFrom', lookup_expr='gte')
    DateFrom_To = DateTimeFilter(field_name='DateFrom', lookup_expr='lte')
    DateTo_From = DateTimeFilter(field_name='DateTo', lookup_expr='gte')
    DateTo_To = DateTimeFilter(field_name='DateTo', lookup_expr='lte')

    class Meta:
        model = Declaration
        fields = ['AmmountFrom', 'AmmountTo', 'DateFrom_From', 'DateFrom_To', 'DateTo_From', 'DateTo_To', 'DocumentId', 'PIT_Id', 'Department']

class DeclarationList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Declaration.objects.all()
    serializer_class = DeclarationSerializer
    name='declaration-list'
    search_fields = ['DocumentId', 'PIT_Id', 'Department', 'DateFrom', 'DateTo']
    ordering_fields = ['DocumentId', 'PIT_Id', 'Ammount', 'Department', 'DateFrom', 'DateTo']
    filter_class = DeclarationFilter

class DeclarationDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Declaration.objects.all()
    serializer_class = DeclarationSerializer
    name='declaration-detail'

class CurrencyList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    name='currency-list'
    filter_fields = ['Name']
    search_fields = ['Name']
    ordering_fields = ['Name']

class CurrencyDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    name='currency-detail'

class PitFilter(FilterSet):
    TaxAmountFrom = NumberFilter(field_name='Tax', lookup_expr='gte')
    TaxAmountTo = NumberFilter(field_name='Tax', lookup_expr='lte')

    class Meta:
        model = PIT
        fields = ['TaxAmountFrom', 'TaxAmountTo', 'Name', 'Tax']

class PITList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PIT.objects.all()
    serializer_class = PITSerializer
    name='pit-list'
    search_fields = ['Name', 'Tax']
    ordering_fields = ['Name', 'Tax']
    filter_class = PitFilter

class PITDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PIT.objects.all()
    serializer_class = PITSerializer
    name='pit-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'client': reverse(ClientList.name, request=request),
                          'document': reverse(DocumentList.name, request=request),
                          'documentType': reverse(DocumentTypeList.name, request=request),
                          'purchasesSales': reverse(PurchasesSalesList.name, request=request),
                          'declaration': reverse(DeclarationList.name, request=request),
                          'currency': reverse(CurrencyList.name, request=request),
                          'pit': reverse(PITList.name, request=request)
})
