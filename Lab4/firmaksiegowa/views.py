from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, generics
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from firmaksiegowa.serializers import AccountSerializer, ClientSerializer, DocumentSerializer, \
    DeclarationSerializer, DocumentTypeSerializer, CurrencySerializer, Purchases_SalesSerializer, PITSerializer
from firmaksiegowa.models import Account, Client, DocumentType, Document, Currency, Purchases_Sales, PIT, Declarations
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import django_filters

# Można również w ten sposób
# class AccountList(APIView):
#     def get(self, request, format=None):
#         snippets = Account.objects.all()
#         serializer = AccountSerializer(many=False)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = AccountSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class AccountDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Account.objects.get(pk=pk)
#         except Account.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         account = self.get_object(pk)
#         serializer = AccountSerializer(account)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         account = self.get_object(pk)
#         serializer = AccountSerializer(account, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         account = self.get_object(pk)
#         account.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]
    name = 'accountList'

class AccountDetail(generics.RetrieveDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    name = 'accountDetail'

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    name = 'clientList'
    filter_fields = ['Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON']
    search_fields = ['Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON']
    ordering_fields = ['Name', 'Surname']


class ClientDetail(generics.RetrieveDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    name = 'clientDetail'

class DocumentTypeList(generics.ListCreateAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsAuthenticated]
    name = 'documentTypeList'
    filter_fields = ['Type']
    search_fields = ['Type']
    ordering_fields = ['Type']

class DocumentTypeDetail(generics.RetrieveDestroyAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsAuthenticated]
    name = 'documentTypeDetail'

class DocumentFilter(django_filters.FilterSet):
    DateFrom = django_filters.DateTimeFilter(field_name='Date', lookup_expr='gte')
    DateTo = django_filters.DateTimeFilter(field_name='Date', lookup_expr='lte')

    class Meta:
        model = Document
        fields = ['DateFrom', 'DateTo', 'ClientId', 'DocumentTypeId']

class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    name = 'documentList'
    search_fields = ['ClientId', 'Date', 'DocumentTypeId']
    ordering_fields = ['ClientId', 'Date', 'DocumentTypeId']
    filter_class = DocumentFilter

class DocumentDetail(generics.RetrieveDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    name = 'documentDetail'


class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]
    name = 'currencyList'
    filter_fields = ['Name']
    search_fields = ['Name']
    ordering_fields = ['Name']

class CurrencyDetail(generics.RetrieveDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]
    name = 'currencyDetail'

class PurchasesSalesFilter(django_filters.FilterSet):
    NetAmountFrom = django_filters.NumberFilter(field_name='NetAmount', lookup_expr='gte')
    NetAmountTo = django_filters.NumberFilter(field_name='NetAmount', lookup_expr='lte')
    GrossAmountFrom = django_filters.NumberFilter(field_name='GrossAmount', lookup_expr='gte')
    GrossAmountTo = django_filters.NumberFilter(field_name='GrossAmount', lookup_expr='lte')

    class Meta:
        model = Purchases_Sales
        fields = ['NetAmountFrom', 'NetAmountTo', 'GrossAmountFrom', 'GrossAmountTo', 'DocumentId', 'ProductName']


class Purchases_SalesList(generics.ListCreateAPIView):
    queryset = Purchases_Sales.objects.all()
    serializer_class = Purchases_SalesSerializer
    permission_classes = [IsAuthenticated]
    name = 'purchases_SalesList'
    search_fields = ['DocumentId', 'ProductName']
    ordering_fields = ['DocumentId', 'ProductName', 'NetAmount', 'GrossAmount']
    filter_class = PurchasesSalesFilter

class Purchases_SalesDetail(generics.RetrieveDestroyAPIView):
    queryset = Purchases_Sales.objects.all()
    serializer_class = Purchases_SalesSerializer
    permission_classes = [IsAuthenticated]
    name = 'purchases_SalesDetail'

class PitFilter(django_filters.FilterSet):
    TaxAmountFrom = django_filters.NumberFilter(field_name='Tax', lookup_expr='gte')
    TaxAmountTo = django_filters.NumberFilter(field_name='Tax', lookup_expr='lte')

    class Meta:
        model = PIT
        fields = ['TaxAmountFrom', 'TaxAmountTo', 'Name', 'Tax']


class PITList(generics.ListCreateAPIView):
    queryset = PIT.objects.all()
    serializer_class = PITSerializer
    permission_classes = [IsAuthenticated]
    name = 'pitList'
    search_fields = ['Name', 'Tax']
    ordering_fields = ['Name', 'Tax']
    filter_class = PitFilter

class PITDetail(generics.RetrieveDestroyAPIView):
    queryset = PIT.objects.all()
    serializer_class = PITSerializer
    permission_classes = [IsAuthenticated]
    name = 'pitDetail'


class DeclarationFilter(django_filters.FilterSet):
    AmmountFrom = django_filters.NumberFilter(field_name='Ammount', lookup_expr='gte')
    AmmountTo = django_filters.NumberFilter(field_name='Ammount', lookup_expr='lte')
    DateFrom_From = django_filters.DateTimeFilter(field_name='DateFrom', lookup_expr='gte')
    DateFrom_To = django_filters.DateTimeFilter(field_name='DateFrom', lookup_expr='lte')
    DateTo_From = django_filters.DateTimeFilter(field_name='DateTo', lookup_expr='gte')
    DateTo_To = django_filters.DateTimeFilter(field_name='DateTo', lookup_expr='lte')

    class Meta:
        model = Declarations
        fields = ['AmmountFrom', 'AmmountTo', 'DateFrom_From', 'DateFrom_To', 'DateTo_From', 'DateTo_To', 'DocumentId', 'PIT_Id', 'Department']

class DeclarationsList(generics.ListCreateAPIView):
    queryset = Declarations.objects.all()
    serializer_class = DeclarationSerializer
    permission_classes = [IsAuthenticated]
    name = 'declarationsList'
    search_fields = ['DocumentId', 'PIT_Id', 'Department', 'DateFrom', 'DateTo']
    ordering_fields = ['DocumentId', 'PIT_Id', 'Ammount', 'Department', 'DateFrom', 'DateTo']
    filter_class = DeclarationFilter

class DeclarationsDetail(generics.RetrieveDestroyAPIView):
    queryset = Declarations.objects.all()
    serializer_class = DeclarationSerializer
    permission_classes = [IsAuthenticated]
    name = 'declarationsDetails'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'client': reverse(ClientList.name, request=request),
                          'document': reverse(DocumentList.name, request=request),
                          'documentType': reverse(DocumentTypeList.name, request=request),
                          'purchasesSales': reverse(Purchases_SalesList.name, request=request),
                          'declaration': reverse(DeclarationsList.name, request=request),
                          'currency': reverse(CurrencyList.name, request=request),
                          'pit': reverse(PITList.name, request=request)
        })









