from rest_framework import serializers
from firmaksiegowa.models import Account,Client, Document, Declarations
from datetime import date
from django.core.exceptions import ValidationError
from . import models as model


def create(self, validated_data):
    return Client.objects.create(**validated_data)


def update(self, instance, validated_data):
    instance.AccountId = validated_data.get('AccountId', instance.AccountId)
    instance.Name = validated_data.get('Name', instance.Name)
    instance.Surname = validated_data.get('Surname', instance.Surname)
    instance.PhoneNumber = validated_data.get('PhoneNumber', instance.PhoneNumber)
    instance.PESEL = validated_data.get('PESEL', instance.PESEL)
    instance.CompanyName = validated_data.get('CompanyName', instance.CompanyName)
    instance.CompanyAdress = validated_data.get('CompanyAdress', instance.CompanyAdress)
    instance.NIP = validated_data.get('NIP', instance.NIP)
    instance.REGON = validated_data.get('REGON', instance.REGON)
    instance.save()
    return instance

#class AccountSerializer(serializers.ModelSerializer):
#    Id = serializers.IntegerField(read_only=True)
#    Email = serializers.EmailField(allow_null=False, max_length=45 )
#    Password = serializers.CharField(allow_null=False, max_length=45)

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    data = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='accountDetail'
    )
    class Meta:
        model = model.Client
        fields = ['Id', 'Email', 'Password', 'data']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    #Id = serializers.IntegerField(read_only=True)
    #AccountId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    #Name = serializers.CharField(allow_null=False, max_length=45)
    #Surname = serializers.CharField(allow_null=False, max_length=45)
    #PhoneNumber = serializers.CharField(allow_null=False, max_length=45)
    #PESEL = serializers.CharField(allow_null=False, max_length=45)
    #CompanyName = serializers.CharField(allow_null=True, max_length=45)
    #CompanyAdress = serializers.CharField(allow_null=True, max_length=45)
    #NIP = serializers.IntegerField(allow_null=True)
    #REGON = serializers.IntegerField(allow_null=True)

    class Meta:
        model = model.Account
        fields = ['Id', 'AccountId', 'Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON', 'data']



class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    DocumentTypeId = serializers.SlugRelatedField(queryset=model.DocumentType.objects.all(), slug_field='Type')
    ClientId = serializers.SlugRelatedField(queryset=model.Client.objects.all(), slug_field='Name')

    def validate_date(self, value):
        today = date.today()
        if value > today:
            raise ValidationError('Data nie może być w przyszłości')

    Date = serializers.DateTimeField(validators=[validate_date])


    class Meta:
        model = model.Document
        fields = ['Id', 'DocumentTypeId', 'ClientId', 'Date']

def validate_amount(self, value):
    if value < 0:
        raise serializers.ValidationError("Suma pieniędzy nie może być ujemna")
    return  value

class DeclarationSerializer(serializers.HyperlinkedModelSerializer):
    PIT_Id = serializers.SlugRelatedField(queryset=model.PIT.objects.all(), slug_field='Name')
    def validate_date(self, value):
        today = date.today()
        if value > today:
            raise ValidationError('Data nie może być w przyszłości')
    #Id = serializers.IntegerField(read_only=True)
    #DocumentId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # PIT_Id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # Amount = serializers.CharField(allow_null=False, max_length=45, validators=[validate_amount])
    # Department = serializers.CharField(allow_null=False, max_length=45)
    #DateFrom = serializers.DateTimeField(allow_null=False, validators=[validate_date])
    #DateTo = serializers.DateTimeField(allow_null=False, validators=[validate_date])

    class Meta:
        model = model.Declarations
        fields = ['Id', 'DocumentId', 'PIT_Id', 'Ammount', 'Department', 'DateFrom', 'DateTo']

class DocumentTypeSerializer(serializers.ModelSerializer):
    #Id = serializers.IntegerField(read_only=True)
    #Type = serializers.CharField(allow_null=False, max_length=45)

    class Meta:
        model = model.DocumentType
        fields = ['Id', 'Type']

class CurrencySerializer(serializers.Serializer):
    #Id = serializers.IntegerField(read_only=True)
    #Name = serializers.CharField(allow_null=False, max_length=45)

    class Meta:
        model = model.Currency
        fields = ['Id', 'Name']

def validate_tax(self, value):
    if value < 0:
        raise serializers.ValidationError("Podatek musi być dodatni.")
    return value


class Purchases_SalesSerializer(serializers.HyperlinkedModelSerializer):
    #Id = serializers.IntegerField(read_only=True)
    #DocumentTypeId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    #ProductName = serializers.CharField(allow_null=False, max_length=45)
    #NetAmount = serializers.DecimalField(allow_null=False, decimal_places=2, max_digits=2, validators=[validate_amount])
    #GrossAmount = serializers.DecimalField(allow_null=False, decimal_places=2, max_digits=2, validators=[validate_amount])
    #CurrencyId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    #Tax = serializers.IntegerField(allow_null=False, validators=[validate_tax])
    CurrencyId = serializers.SlugRelatedField(queryset=model.Currency.objects.all(), slug_field='Name')

    class Meta:
        model = model.Purchases_Sales
        fields = ['Id', 'ProductName', 'NetAmount', 'GrossAmount', 'CurrencyId', 'Tax']

class PITSerializer(serializers.Serializer):
    #Id = serializers.IntegerField(read_only=True)
    #Name = serializers.CharField(allow_null=False, max_length=45)
    #Tax = serializers.IntegerField(allow_null=False, validators=[validate_tax])

    class Meta:
        model = model.PIT
        fields = ['Id', 'Name', 'Tax']