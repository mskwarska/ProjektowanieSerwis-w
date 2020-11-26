from rest_framework import serializers
import models as md

class AccountSerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    Email = serializers.CharField(max_length=45, allow_blank=False)
    Password = serializers.CharField(max_length=45, allow_blank=False)

class ClientSerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    AccountId = serializers.PrimaryKeyRelatedField(many=False)
    Name = serializers.CharField(max_length=45, allow_blank=False)
    Surname = serializers.CharField(max_length=45, allow_blank=False)
    PhoneNumber = serializers.CharField(max_length=45, allow_blank=False)
    PESEL = serializers.CharField(max_length=45, allow_blank=False)
    CompanyName = serializers.CharField(max_length=45, allow_blank=True)
    CompanyAddress = serializers.CharField(max_length=45, allow_blank=True)
    NIP = serializers.CharField(max_length=45, allow_blank=True)
    REGON = serializers.CharField(max_length=45, allow_blank=True)

    def create(self, validated_data, accountId):
        validated_data.AccountId = accountId
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

class DocumentTypeSerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    Type = serializers.CharField(max_length=45, allow_blank=False)

class DocumentSerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    DocumentTypeId = serializers.PrimaryKeyRelatedField(many=False)
    ClientId = serializers.postgres_fields(many=False)
    Date = serializers.DateTimeField()

class CurrencySerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(max_length=45, allow_blank=False)

class PurchasesSalesSerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    DocumentTypeId = serializers.PrimaryKeyRelatedField(many=False)
    ProductName = serializers.CharField(max_length=45, allow_blank=False)
    NetAmount = serializers.DecimalField(decimal_places=2, max_digits=2, validators=[validate_netAmount])
    GrossAmount = serializers.DecimalField(decimal_places=2, max_digits=2, validators=[validate_grossAmount])
    CurrencyId = serializers.PrimaryKeyRelatedField(many=False)
    Tax = serializers.IntegerField(validators=[validate_Tax])

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

class PITSerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(max_length=45, allow_blank=False)
    Tax = serializers.IntegerField(validators=[validate_Tax])

    def validate_Tax(self, value):
        if value < 0:
            raise serializers.ValidationError("Podatek nie może być ujemny.")
        return value

class DeclarationSerializer(serializers.Serializer):
    Id = serializers.IntegerField(read_only=True)
    DocumentId = serializers.PrimaryKeyRelatedField(many=False)
    PIT_Id = serializers.PrimaryKeyRelatedField(many=False)
    Ammount = serializers.CharField(max_length=45, allow_blank=True, validators=[validate_Amount])
    Department = serializers.CharField(max_length=45, allow_blank=True)
    DateFrom = serializers.DateTimeField()
    DateTo = serializers.DateTimeField()

    def validate_Amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Ilość nie może być ujemna.")
        return value