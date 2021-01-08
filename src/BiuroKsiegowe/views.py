from django.http import HttpResponse, Http404
from django.contrib.auth.models import User, Group
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser
from rest_framework.response import Response
from django_filters import FilterSet, DateTimeFilter, AllValuesFilter, NumberFilter

from .models import Client, Document, DocumentType, PurchasesSales, Declaration, Currency, PIT
from .serializers import UserSerializer, ClientSerializer, ClientDetailSerializer, DocumentSerializer, DocumentTypeSerializer, PurchasesSalesSerializer, DeclarationSerializer, CurrencySerializer, PITSerializer

class UserList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class ClientList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name='client-list'
    filter_fields = ['Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON']
    search_fields = ['Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON']
    ordering_fields = ['Name', 'Surname']

    def get(self, request, format=None):
        user = self.request.user

        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            client = Client.objects.all()
        else:
            client = Client.objects.filter(User=user)

        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    name='client-detail'

class DocumentFilter(FilterSet):
    DateFrom = DateTimeFilter(field_name='Date', lookup_expr='gte')
    DateTo = DateTimeFilter(field_name='Date', lookup_expr='lte')

    class Meta:
        model = Document
        fields = ['DateFrom', 'DateTo', 'Client', 'DocumentType']

class DocumentList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    name='document-list'
    search_fields = ['Client', 'Date', 'DocumentType']
    ordering_fields = ['Client', 'Date', 'DocumentType']
    filter_class = DocumentFilter

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    name='document-detail'

class DocumentTypeList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    name='documenttype-list'
    filter_fields = ['Type']
    search_fields = ['Type']
    ordering_fields = ['Type']

class DocumentTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
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
        fields = ['NetAmountFrom', 'NetAmountTo', 'GrossAmountFrom', 'GrossAmountTo', 'Document', 'ProductName']

class PurchasesSalesList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = PurchasesSales.objects.all()
    serializer_class = PurchasesSalesSerializer
    name='purchasessales-list'
    search_fields = ['Document', 'ProductName']
    ordering_fields = ['Document', 'ProductName', 'NetAmount', 'GrossAmount']
    filter_class = PurchasesSalesFilter

class PurchasesSalesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = PurchasesSales.objects.all()
    serializer_class = PurchasesSalesSerializer
    name='purchasessales-detail'

class DeclarationFilter(FilterSet):
    DateFrom_From = DateTimeFilter(field_name='DateFrom', lookup_expr='gte')
    DateFrom_To = DateTimeFilter(field_name='DateFrom', lookup_expr='lte')
    DateTo_From = DateTimeFilter(field_name='DateTo', lookup_expr='gte')
    DateTo_To = DateTimeFilter(field_name='DateTo', lookup_expr='lte')

    class Meta:
        model = Declaration
        fields = ['DateFrom_From', 'DateFrom_To', 'DateTo_From', 'DateTo_To', 'Document', 'PIT', 'Department']

class DeclarationList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Declaration.objects.all()
    serializer_class = DeclarationSerializer
    name='declaration-list'
    search_fields = ['Document', 'PIT', 'Department', 'DateFrom', 'DateTo']
    ordering_fields = ['Document', 'PIT', 'Amount', 'Department', 'DateFrom', 'DateTo']
    filter_class = DeclarationFilter

class DeclarationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Declaration.objects.all()
    serializer_class = DeclarationSerializer
    name='declaration-detail'

class CurrencyList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    name='currency-list'
    filter_fields = ['Name']
    search_fields = ['Name']
    ordering_fields = ['Name']

class CurrencyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    name='currency-detail'

class PITList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = PIT.objects.all()
    serializer_class = PITSerializer
    name='pit-list'
    search_fields = ['Name',]
    ordering_fields = ['Name',]

class PITDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = PIT.objects.all()
    serializer_class = PITSerializer
    name='pit-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'Index'
    def get(self, request, *args, **kwargs):
        return Response({ 'Users': reverse(UserList.name, request=request),
                          'Clients': reverse(ClientList.name, request=request),
                          'Documents': reverse(DocumentList.name, request=request),
                          'Document types': reverse(DocumentTypeList.name, request=request),
                          'Purchases and sales': reverse(PurchasesSalesList.name, request=request),
                          'Declarations': reverse(DeclarationList.name, request=request),
                          'Currencies': reverse(CurrencyList.name, request=request),
                          'PITs': reverse(PITList.name, request=request)
})
