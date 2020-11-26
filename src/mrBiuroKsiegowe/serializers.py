from rest_framework import serializers
import models as md

class AccountSerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField(read_only=True)
    # Email = serializers.CharField(max_length=45, allow_null=False)
    # Password = serializers.CharField(max_length=45, allow_null=False)

    class Meta:
        model = md.Account
        fields = ['Id', 'Email', 'Password']

class ClientSerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField(read_only=True)
    # AccountId = serializers.PrimaryKeyRelatedField(many=False)
    # Name = serializers.CharField(max_length=45, allow_null=False)
    # Surname = serializers.CharField(max_length=45, allow_null=False)
    # PhoneNumber = serializers.CharField(max_length=45, allow_null=False)
    # PESEL = serializers.CharField(max_length=45, allow_null=False)
    # CompanyName = serializers.CharField(max_length=45, allow_null=True)
    # CompanyAddress = serializers.CharField(max_length=45, allow_null=True)
    # NIP = serializers.CharField(max_length=45, allow_null=True)
    # REGON = serializers.CharField(max_length=45, allow_null=True)

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

    class Meta:
        model = md.Client
        fields = ['Id', 'AccountId', 'Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'ComapnyAddress', 'NIP', 'REGON']

class DocumentTypeSerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField(read_only=True)
    # Type = serializers.CharField(max_length=45, allow_null=False)

    class Meta:
        model = md.DocumentType
        fields = ['Id', 'Type']

class DocumentSerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField(read_only=True)
    # DocumentTypeId = serializers.PrimaryKeyRelatedField(many=False)
    # ClientId = serializers.postgres_fields(many=False)
    # Date = serializers.DateTimeField()

    class Meta:
        model = md.Document
        fields = ['Id', 'DocumentTypeId', 'ClientId', 'Date']

class CurrencySerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField(read_only=True)
    # Name = serializers.CharField(max_length=45, allow_null=False)

    class Meta:
        model = md.Currency
        fields = ['Id', 'Name']

class PurchasesSalesSerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField(read_only=True)
    # DocumentTypeId = serializers.PrimaryKeyRelatedField(many=False)
    # ProductName = serializers.CharField(max_length=45, allow_null=False)
    # NetAmount = serializers.DecimalField(decimal_places=2, max_digits=2, validators=[validate_netAmount])
    # GrossAmount = serializers.DecimalField(decimal_places=2, max_digits=2, validators=[validate_grossAmount])
    # CurrencyId = serializers.PrimaryKeyRelatedField(many=False)
    # Tax = serializers.IntegerField(validators=[validate_Tax])

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
        fields = ['Id', 'DocumentTypeId', 'ProductName', 'NetAmount', 'GrossAmount', 'CurrencyId', 'Tax']

class PITSerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField(read_only=True)
    # Name = serializers.CharField(max_length=45, allow_null=False)
    # Tax = serializers.IntegerField(validators=[validate_Tax])

    def validate_Tax(self, value):
        if value < 0:
            raise serializers.ValidationError("Podatek nie może być ujemny.")
        return value

    class Meta:
        model = md.PIT
        fields = ['Id', 'Name', 'Tax']

class DeclarationSerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField(read_only=True)
    # DocumentId = serializers.PrimaryKeyRelatedField(many=False)
    # PIT_Id = serializers.PrimaryKeyRelatedField(many=False)
    # Ammount = serializers.CharField(max_length=45, allow_null=True, validators=[validate_Amount])
    # Department = serializers.CharField(max_length=45, allow_null=True)
    # DateFrom = serializers.DateTimeField()
    # DateTo = serializers.DateTimeField()

    def validate_Amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Ilość nie może być ujemna.")
        return value

    class Meta:
        model = md.Declaration
        fields = ['Id', 'DocumentId', 'PIT_Id', 'Amount', 'Department', 'DateFrom', 'DateTo']
