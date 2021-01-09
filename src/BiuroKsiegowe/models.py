import datetime
from django.db import models

class Client(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.ForeignKey('auth.User', related_name='Client', on_delete=models.CASCADE)
    Name = models.CharField(max_length=45, null=False)
    Surname = models.CharField(max_length=45, null=False)
    PhoneNumber = models.CharField(max_length=45, null=False)
    PESEL = models.CharField(max_length=45, null=False)
    CompanyName = models.CharField(max_length=45, null=True)
    CompanyAddress = models.CharField(max_length=45, null=True)
    NIP = models.CharField(max_length=45, null=True)
    REGON = models.CharField(max_length=45, null=True)

    class Meta:
        ordering = ('Name', 'Surname')

    @property
    def GetClient(self):
        return self.Name + ' ' + self.Surname

    def __str__(self):
        return self.User.email

class DocumentType(models.Model):
    Id = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=45, null=False)

    class Meta:
        ordering = ('Type',)

    def __str__(self):
        return self.Type

class Document(models.Model):
    Id = models.AutoField(primary_key=True)
    DocumentType = models.ForeignKey(DocumentType, null=True, on_delete=models.SET_NULL)
    Client = models.ForeignKey(Client, related_name='Documents', on_delete=models.CASCADE)
    CreatedBy = models.ForeignKey('auth.User', related_name='DocumentCreatedBy', null=True, on_delete=models.SET_NULL)
    CreationDate = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ('CreationDate',)

    def __str__(self):
        return str(self.Client) + ' | ' + str(self.DocumentType) + ' | ' + str(self.CreationDate.strftime("%d.%m.%Y %H:%M"))

class Currency(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45, null=False)
    Code = models.CharField(max_length=45, null=False)
    Country = models.CharField(max_length=45, null=False)

    class Meta:
        ordering = ('Name',)

    def __str__(self):
        return self.Code

class PurchasesSales(models.Model):
    Id = models.AutoField(primary_key=True)
    Document = models.ForeignKey(Document, on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=45, null=False)
    NetAmount = models.DecimalField(decimal_places=2, max_digits=10)
    GrossAmount = models.DecimalField(decimal_places=2, max_digits=10)
    Currency = models.ForeignKey(Currency, null=True, on_delete=models.SET_NULL)
    Tax = models.IntegerField()

    class Meta:
        ordering = ('ProductName',)

class PIT(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45, null=False)
    Desc = models.TextField(default=None, null=False)
    Deadline = models.CharField(max_length=255, default=None, null=False)

    class Meta:
        ordering = ('Name',)

    def __str__(self):
        return self.Name

class Declaration(models.Model):
    Id = models.AutoField(primary_key=True)
    Document = models.ForeignKey(Document, on_delete=models.CASCADE)
    PIT = models.ForeignKey(PIT, null=True, on_delete=models.SET_NULL)
    Desc = models.TextField(default=None)
    Amount = models.CharField(max_length=45)
    Department = models.CharField(max_length=45)
    DateFrom = models.DateTimeField()
    DateTo = models.DateTimeField()

    class Meta:
        ordering = ('DateFrom', 'DateTo')