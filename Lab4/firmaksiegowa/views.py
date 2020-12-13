from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, generics
from django.contrib.auth.models import User
from firmaksiegowa.serializers import AccountSerializer, ClientSerializer, DocumentSerializer, \
    DeclarationsSerializer, DocumentTypeSerializer, CurrencySerializer, Purchases_SalesSerializer, PITSerializer
from firmaksiegowa.models import Account, Client, DocumentType, Document, Currency, Purchases_Sales, PIT, Declarations
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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

class AccountDetail(generics.RetrieveDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
class ClientDetail(generics.RetrieveDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]



class DocumentTypeList(generics.ListCreateAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsAuthenticated]
class DocumentTypeDetail(generics.RetrieveDestroyAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsAuthenticated]


class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
class DocumentDetail(generics.RetrieveDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]


class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]
class CurrencyDetail(generics.RetrieveDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]


class Purchases_SalesList(generics.ListCreateAPIView):
    queryset = Purchases_Sales.objects.all()
    serializer_class = Purchases_SalesSerializer
    permission_classes = [IsAuthenticated]
class Purchases_SalesDetail(generics.RetrieveDestroyAPIView):
    queryset = Purchases_Sales.objects.all()
    serializer_class = Purchases_SalesSerializer
    permission_classes = [IsAuthenticated]


class PITList(generics.ListCreateAPIView):
    queryset = PIT.objects.all()
    serializer_class = PITSerializer
    permission_classes = [IsAuthenticated]
class PITDetail(generics.RetrieveDestroyAPIView):
    queryset = PIT.objects.all()
    serializer_class = PITSerializer
    permission_classes = [IsAuthenticated]


class DeclarationsList(generics.ListCreateAPIView):
    queryset = Declarations.objects.all()
    serializer_class = DeclarationsSerializer
    permission_classes = [IsAuthenticated]
class DeclarationsDetail(generics.RetrieveDestroyAPIView):
    queryset = Declarations.objects.all()
    serializer_class = DeclarationsSerializer
    permission_classes = [IsAuthenticated]











