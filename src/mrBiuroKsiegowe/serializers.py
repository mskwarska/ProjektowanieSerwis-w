from rest_framework import serializers
from . import models as md

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.Account
        fields = ['Id', 'Email', 'Password']

class ClientSerializer(serializers.HyperlinkedModelSerializer):

    documents = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='document-detail'
    )

    def create(self, validated_data):
        client = md.Client.objects.create(**validated_data)
        return client

    def update(self, instance, validated_data, accountId):
        instance = validated_data
        instance.AccountId = accountId
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Surname = validated_data.get('Surname', instance.Surname)
        instance.PhoneNumber = validated_data.get('PhoneNumber', instance.PhoneNumber)
        instance.PESEL = validated_data.get('PESEL', instance.PESEL)
        instance.CompanyName = validated_data.get('CompanyName', instance.CompanyName)
        instance.CompanyAddress = validated_data.get('CompanyAddress', instance.CompanyAddress)
        instance.NIP = validated_data.get('NIP', instance.NIP)
        instance.REGON = validated_data.get('REGON', instance.REGON)
        instance.save()

        return instance

    class Meta:
        model = md.Client
        fields = ['Id', 'AccountId', 'Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON', 'documents']

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.DocumentType
        fields = ['Id', 'Type']

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    DocumentTypeId = serializers.SlugRelatedField(queryset=md.DocumentType.objects.all(), slug_field='Type')
    ClientId = serializers.SlugRelatedField(queryset=md.Client.objects.all(), slug_field='GetClient')
    class Meta:
        model = md.Document
        fields = ['Id', 'DocumentTypeId', 'ClientId', 'Date']

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
