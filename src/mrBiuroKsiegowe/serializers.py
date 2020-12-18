from django.contrib.auth.models import User
from rest_framework import serializers
from . import models as md

class UserClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = md.Client
        fields = ['GetClient']
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    Clients = UserClientSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['Clients', 'pk', 'username']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    User = serializers.ReadOnlyField(source='User.email')
    documents = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='document-detail'
    )

    class Meta:
        model = md.Client
        fields = ['Id', 'User', 'Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON', 'documents']

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.DocumentType
        fields = ['Id', 'Type']

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    DocumentTypeId = serializers.SlugRelatedField(queryset=md.DocumentType.objects.all(), slug_field='Type')
    ClientId = serializers.SlugRelatedField(queryset=md.Client.objects.all(), slug_field='GetClient')

    def perform_create(self, serializer):
        serializer.save(CreatedBy=self.request.user)

    class Meta:
        model = md.Document
        fields = ['Id', 'DocumentTypeId', 'ClientId', 'CreatedBy', 'Date']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = md.Currency
        fields = ['Id', 'Name']

class PurchasesSalesSerializer(serializers.HyperlinkedModelSerializer):
    CurrencyId = serializers.SlugRelatedField(queryset=md.Currency.objects.all(), slug_field='Name')
    def validate_netAmount(self, value):
        if value < 0:
            raise serializers.ValidationError("Kwota netto nie może być ujemna.")
        return value

    def validate_grossAmount(self, value):
        if value < 0:
            raise serializers.ValidationError("Kwota brutto nie może być ujemna.")
        return value

    def validate_Tax(self, value):
        if value < 0:
            raise serializers.ValidationError("Podatek nie może być ujemny.")
        return value

    class Meta:
        model = md.PurchasesSales
        fields = ['Id', 'ProductName', 'NetAmount', 'GrossAmount', 'CurrencyId', 'Tax']

class PITSerializer(serializers.ModelSerializer):
    def validate_Tax(self, value):
        if value < 0:
            raise serializers.ValidationError("Podatek nie może być ujemny.")
        return value

    class Meta:
        model = md.PIT
        fields = ['Id', 'Name', 'Tax']

class DeclarationSerializer(serializers.HyperlinkedModelSerializer):
    PIT_Id = serializers.SlugRelatedField(queryset=md.PIT.objects.all(), slug_field='Name')

    def validate_Amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Ilość nie może być ujemna.")
        return value

    class Meta:
        model = md.Declaration
        fields = ['Id', 'DocumentId', 'PIT_Id', 'Ammount', 'Department', 'DateFrom', 'DateTo']
