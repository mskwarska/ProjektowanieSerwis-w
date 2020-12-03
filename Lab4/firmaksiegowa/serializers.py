from rest_framework import serializers
from firmaksiegowa.models import Account,Client, Document, Declarations
from datetime import date
from django.core.exceptions import ValidationError


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

class AccountSerializer(serializers.ModelSerializer):
    Id = serializers.IntegerField(read_only=True)
    Email = serializers.EmailField(allow_null=False, max_length=45 )
    Password = serializers.CharField(allow_null=False, max_length=45)


class ClientSerializer(serializers.ModelSerializer):
    Id = serializers.IntegerField(read_only=True)
    AccountId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    Name = serializers.CharField(allow_null=False, max_length=45)
    Surname = serializers.CharField(allow_null=False, max_length=45)
    PhoneNumber = serializers.CharField(allow_null=False, max_length=45)
    PESEL = serializers.CharField(allow_null=False, max_length=45)
    CompanyName = serializers.CharField(allow_null=True, max_length=45)
    CompanyAdress = serializers.CharField(allow_null=True, max_length=45)
    NIP = serializers.IntegerField(allow_null=True, max_length=45)
    REGON = serializers.IntegerField(allow_null=True, max_length=45)

def validate_date(value):
        today = date.today()
        if value > today:
            raise ValidationError('Data nie może być w przyszłości')

class DocumentSerializer(serializers.ModelSerializer):
    Id = serializers.IntegerField(read_only=True)
    DocumentTypeId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    ClientId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    Date = serializers.DateTimeField(validators=[validate_date(limit_value=date.today)])


def validate_amount(self, value):
    if value < 0:
        raise serializers.ValidationError("Suma pieniędzy nie może być ujemna")
    return  value

class DeclarationsSerializer(serializers.ModelSerializer):
    Id = serializers.IntegerField(read_only=True)
    DocumentId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    PIT_Id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    Amount = serializers.CharField(allow_null=False, max_length=45, validators=[validate_amount()])
    Department = serializers.CharField(allow_null=False, max_length=45)
    DateFrom = serializers.DateTimeField(allow_null=False, validators=[validate_date(limit_value=date.today)])
    DateTo = serializers.DateTimeField(allow_null=False, validators=[validate_date(limit_value=date.today)])

class DocumentTypeSerializer(serializers.ModelSerializer):
    Id = serializers.IntegerField(read_only=True)
    Type = serializers.CharField(allow_null=False, max_length=45)

class CurrencySerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(allow_null=False, max_length=45)

def validate_tax(self, value):
    if value < 0:
        raise serializers.ValidationError("Podatek musi być dodatni.")
    return value


class Purchases_SalesSerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    DocumentTypeId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    ProductName = serializers.CharField(allow_null=False, max_length=45)
    NetAmount = serializers.DecimalField(allow_null=False, decimal_places=2, max_digits=2, validators=[validate_amount()])
    GrossAmount = serializers.DecimalField(allow_null=False, decimal_places=2, max_digits=2, validators=[validate_amount()])
    CurrencyId = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    Tax = serializers.IntegerField(allow_null=False, validators=[validate_tax])

class PITSerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(allow_null=False, max_length=45)
    Tax = serializers.IntegerField(allow_null=False, validators=[validate_tax])