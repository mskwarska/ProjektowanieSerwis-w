from django.contrib.auth.models import User
from rest_framework import serializers
from . import models as md
from . import views
import datetime

class UserClientDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class UserClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = md.Client
        fields = ['url']
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    Client = UserClientSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['pk', 'username', 'Client']

class ClientSerializer(serializers.HyperlinkedModelSerializer):

    def validate_user(value):
        userEmail = value.email
        user = User.objects.get(email=userEmail)
        isExist = md.Client.objects.filter(User=user).exists()

        if isExist is True:
            raise serializers.ValidationError('Podany użytkownik posiada już konto.')

        return value

    def validate_PESEL(self, value):
        if len(value) != 11:
            raise serializers.ValidationError('PESEL musi składać sie z 11 cyfer.')

        return value

    def validate_NIP(self, value):
        if value is not None and len(value) != 10:
            raise serializers.ValidationError('NIP musi składać się z 10 znaków.')

        return value

    def validate_REGON(self, value):
        if value is not None and len(value) != 9:
            raise serializers.ValidationError('REGON musi składać się z 9 znaków.')

        return value

    User = serializers.SlugRelatedField(
        queryset=User.objects.filter(is_staff=False, is_superuser=False),
        slug_field='email',
        validators=[validate_user]
    )
    
    Documents = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='document-detail'
    )

    def create(self, validated_data):
        userEmail = validated_data['User'].email
        user = User.objects.get(email=userEmail)
        validated_data['User'] = user
        return md.Client.objects.create(**validated_data)

    class Meta:
        model = md.Client
        fields = ['Id', 'User', 'Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON', 'Documents']

class ClientDetailSerializer(serializers.HyperlinkedModelSerializer):
    User = UserClientDetailSerializer(many=False, read_only=True)
    Documents = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='document-detail'
    )

    class Meta:
        model = md.Client
        fields = ['Id', 'User', 'Name', 'Surname', 'PhoneNumber', 'PESEL', 'CompanyName', 'CompanyAddress', 'NIP', 'REGON', 'Documents']

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.DocumentType
        fields = ['Id', 'Type']

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    DocumentType = serializers.SlugRelatedField(
        queryset=md.DocumentType.objects.all(), 
        slug_field='Type'
    )

    Client = serializers.SlugRelatedField(
        queryset=md.Client.objects.all(), 
        slug_field='Id'
    )

    def create(self, validated_data):
        request = self.context.get('request', None)

        if request:
            validated_data['CreatedBy'] = request.user
            return md.Document.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['CreatedBy'] = instance.CreatedBy
        validated_data['Client'] = instance.Client
        validated_data['CreationDate'] = instance.CreationDate
        instance = validated_data

        return instance

    class Meta:
        model = md.Document
        fields = ['Id', 'DocumentType', 'Client', 'CreatedBy', 'CreationDate']
        read_only_fields = ['CreationDate']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = md.Currency
        fields = ['Id', 'Name', 'Code', 'Country']

class PurchasesSalesSerializer(serializers.HyperlinkedModelSerializer):
    Currency = serializers.SlugRelatedField(
        queryset=md.Currency.objects.all(), 
        slug_field='Name'
    )

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

    def validate_Document(self, value):
        isExists = md.Declaration.objects.filter(Document=value).exists() or md.PurchasesSales.objects.filter(Document=value).exists()

        if isExists is True:
            raise serializers.ValidationError('Podany dokument jest już powiązany z innym dokumentem.')

        return value

    class Meta:
        model = md.PurchasesSales
        fields = ['Id', 'Document', 'ProductName', 'NetAmount', 'GrossAmount', 'Currency', 'Tax']

class PurchasesSalesDetailSerializer(serializers.HyperlinkedModelSerializer):
    Currency = serializers.SlugRelatedField(
        queryset=md.Currency.objects.all(), 
        slug_field='Name'
    )

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
        fields = ['Id', 'Document', 'ProductName', 'NetAmount', 'GrossAmount', 'Currency', 'Tax']
        read_only_fields = ['Document',]

class PITSerializer(serializers.ModelSerializer):
    class Meta:
        model = md.PIT
        fields = ['Id', 'Name', 'Desc', 'Deadline']

class DeclarationSerializer(serializers.HyperlinkedModelSerializer):
    PIT = serializers.SlugRelatedField(
        queryset=md.PIT.objects.all(), 
        slug_field='Name'
    )

    def validate_Document(self, value):
        isExists = md.Declaration.objects.filter(Document=value).exists() or md.PurchasesSales.objects.filter(Document=value).exists()

        if isExists is True:
            raise serializers.ValidationError('Podany dokument jest już powiązany z innym dokumentem.')

        return value

    class Meta:
        model = md.Declaration
        fields = ['Id', 'Document', 'PIT', 'Desc', 'Amount', 'Department', 'DateFrom', 'DateTo']

class DeclarationDetailSerializer(serializers.HyperlinkedModelSerializer):
    PIT = serializers.SlugRelatedField(
        queryset=md.PIT.objects.all(), 
        slug_field='Name'
    )

    class Meta:
        model = md.Declaration
        fields = ['Id', 'Document', 'PIT', 'Desc', 'Amount', 'Department', 'DateFrom', 'DateTo']
        read_only_fields = ['Document',]
