from django.db import models

# Create your models here.
class Account(models.Model):
    Id = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=45, null=False)
    Password = models.CharField(max_length=45, null=False)

class Client(models.Model):
    Id = models.AutoField(primary_key=True)
    AccountId = models.ForeignKey(Account, on_delete=models.CASCADE)
    Name = models.CharField(max_length=45, null=False)
    Surname = models.CharField(max_length=45, null=False)
    PhoneNumber = models.CharField(max_length=45, null=False)
    PESEL = models.CharField(max_length=45, null=False)
    CompanyName = models.CharField(max_length=45, null=True)
    CompanyAddress = models.CharField(max_length=45, null=True)
    NIP = models.CharField(max_length=45, null=True)
    REGON = models.CharField(max_length=45, null=True)

class DocumentType(models.Model):
    Id = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=45, null=False)

class Document(models.Model):
    Id = models.AutoField(primary_key=True)
    DocumentTypeId = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    ClientId = models.ForeignKey(Client, on_delete=models.CASCADE)
    Date = models.DateTimeField()

class Currency(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45, null=False)

class PurchasesSales(models.Model):
    Id = models.AutoField(primary_key=True)
    DocumentId = models.ForeignKey(Document, on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=45, null=False)
    NetAmount = models.DecimalField(decimal_places=2, max_digits=2)
    GrossAmount = models.DecimalField(decimal_places=2, max_digits=2)
    CurrencyId = models.ForeignKey(Currency, on_delete=models.CASCADE)
    Tax = models.IntegerField()
    
class PIT(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45, null=False)
    Tax = models.IntegerField()

class Declaration(models.Model):
    Id = models.AutoField(primary_key=True)
    DocumentId = models.ForeignKey(Document, on_delete=models.CASCADE)
    PIT_Id = models.ForeignKey(PIT, on_delete=models.CASCADE)
    Ammount = models.CharField(max_length=45)
    Department = models.CharField(max_length=45)
    DateFrom = models.DateTimeField()
    DateTo = models.DateTimeField()