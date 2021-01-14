from django.http import HttpResponse, Http404
from django.contrib.auth.models import User, Group
from django.db.models import Prefetch
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser
from rest_framework.response import Response
from django_filters import FilterSet, DateTimeFilter, AllValuesFilter, NumberFilter

from .models import Client, Document, DocumentType, PurchasesSales, Declaration, Currency, PIT
from .serializers import UserSerializer, ClientSerializer, ClientDetailSerializer, DocumentSerializer, DocumentTypeSerializer, PurchasesSalesSerializer, PurchasesSalesDetailSerializer, DeclarationSerializer, DeclarationDetailSerializer, CurrencySerializer, PITSerializer

class UserList(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            user = User.objects.all()
        else:
            user = User.objects.filter(id=user.id)

        return user

class ClientList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name='client-list'
    filter_fields = ['Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON']
    search_fields = ['Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON']
    ordering_fields = ['Name', 'Surname', 'User', 'REGON']

    def get(self, request, format=None):
        user = self.request.user

        serializer_context = {
            'request': request,
        }

        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            client = Client.objects.all()
        else:
            client = Client.objects.filter(User=user)

        queryset = self.filter_queryset(client)
        page = self.paginate_queryset(queryset)

        serializer = ClientSerializer(page, many=True, context=serializer_context)
        return self.get_paginated_response(serializer.data)

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    name='client-detail'

    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            client = Client.objects.all()
        else:
            client = Client.objects.filter(User=user)

        return client

class DocumentFilter(FilterSet):
    CreationDateFrom = DateTimeFilter(field_name='CreationDate', lookup_expr='gte')
    CreationDateTo = DateTimeFilter(field_name='CreationDate', lookup_expr='lte')

    class Meta:
        model = Document
        fields = ['CreationDateFrom', 'CreationDateTo', 'Client', 'DocumentType']

class DocumentList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    name='document-list'
    search_fields = ['CreationDate', 'CreatedBy', 'DocumentType']
    ordering_fields = ['CreationDate', 'CreatedBy', 'DocumentType']
    filter_class = DocumentFilter

    def get(self, request, format=None):
        user = self.request.user

        serializer_context = {
            'request': request,
        }

        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            document = Document.objects.all()
        else:
            client = Client.objects.get(User=user)
            document = Document.objects.filter(Client=client)

        queryset = self.filter_queryset(document)
        page = self.paginate_queryset(queryset)

        serializer = DocumentSerializer(page, many=True, context=serializer_context)
        return self.get_paginated_response(serializer.data)

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    name='document-detail'

    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            document = Document.objects.all()
        else:
            client = Client.objects.get(User=user)
            document = Document.objects.filter(Client=client)

        return document

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
    search_fields = ['ProductName']
    ordering_fields = ['ProductName', 'NetAmount', 'GrossAmount']
    filter_class = PurchasesSalesFilter

    def get(self, request, format=None):
        user = self.request.user

        serializer_context = {
            'request': request,
        }

        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            purchasesSales = PurchasesSales.objects.all()
        else:
            client = Client.objects.get(User=user)
            documents = Document.objects.filter(Client=client)
            documentsData = DocumentSerializer(documents, many=True, context=serializer_context).data

            documentsId = []

            for document in documentsData:
                id = document['Id']
                documentsId.append(id)

            purchasesSales = PurchasesSales.objects.filter(Document_id__in=documentsId)

        queryset = self.filter_queryset(purchasesSales)
        page = self.paginate_queryset(queryset)

        serializer = PurchasesSalesSerializer(page, many=True, context=serializer_context)
        return self.get_paginated_response(serializer.data)

class PurchasesSalesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = PurchasesSales.objects.all()
    serializer_class = PurchasesSalesDetailSerializer
    name='purchasessales-detail'

    def get_queryset(self):
        user = self.request.user
        path = self.request.get_full_path()
        purchasesSalesId = int(path.split('/')[2])
        
        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            purchasesSales = PurchasesSales.objects.all()
        else:
            try:
                client = Client.objects.get(User=user)
                purchasesSales = PurchasesSales.objects.get(Id=purchasesSalesId)
                document = Document.objects.get(Id=purchasesSales.Document.Id)
            except Client.DoesNotExist:
                return PurchasesSales.objects.none()
            except PurchasesSales.DoesNotExist:
                return PurchasesSales.objects.none()
            except Document.DoesNotExist:
                return PurchasesSales.objects.none()

            if document.Client != client:
                return PurchasesSales.objects.none()

            purchasesSales = PurchasesSales.objects.filter(Document_id=document.Id)

        return purchasesSales

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
    search_fields = ['Department', 'DateFrom', 'DateTo']
    ordering_fields = ['Department', 'DateFrom', 'DateTo']
    filter_class = DeclarationFilter

    def get(self, request, format=None):
        user = self.request.user

        serializer_context = {
            'request': request,
        }

        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            declaration = Declaration.objects.all()
        else:
            client = Client.objects.get(User=user)
            documents = Document.objects.filter(Client=client)
            documentsData = DocumentSerializer(documents, many=True, context=serializer_context).data

            documentsId = []

            for document in documentsData:
                id = document['Id']
                documentsId.append(id)

            declaration = Declaration.objects.filter(Document_id__in=documentsId)

        queryset = self.filter_queryset(declaration)
        page = self.paginate_queryset(queryset)

        serializer = DeclarationSerializer(page, many=True, context=serializer_context)
        return self.get_paginated_response(serializer.data)

class DeclarationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Declaration.objects.all()
    serializer_class = DeclarationDetailSerializer
    name='declaration-detail'
    
    def get_queryset(self):
        user = self.request.user
        path = self.request.get_full_path()
        declarationId = int(path.split('/')[2])
        
        if user.is_superuser or Group.objects.get(name='Employees').user_set.filter(id=user.id).exists():
            declaration = Declaration.objects.all()
        else:
            try:
                client = Client.objects.get(User=user)
                declaration = Declaration.objects.get(Id=declarationId)
                document = Document.objects.get(Id=declaration.Document.Id)
            except Client.DoesNotExist:
                return Declaration.objects.none()
            except Declaration.DoesNotExist:
                return Declaration.objects.none()
            except Document.DoesNotExist:
                return Declaration.objects.none()

            if document.Client != client:
                declaration = Declaration.objects.none()
                return declaration

            declaration = Declaration.objects.filter(Document_id=document.Id)

        return declaration

class CurrencyList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    name='currency-list'
    filter_fields = ['Name']
    search_fields = ['Name', 'Code', 'Country']
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
    search_fields = ['Name', 'Desc', 'Deadline']
    ordering_fields = ['Name', 'Deadline']

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
