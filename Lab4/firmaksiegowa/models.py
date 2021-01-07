from django.db import models

class Account(models.Model):
    Id=models.AutoField(primary_key=True)
    Email=models.EmailField(max_length=45)
    Password=models.CharField(max_length=45)

    @property
    def GetAccount(self):
        return self.Id + ' ' + self.Email

class Client(models.Model):
    Id = models.AutoField(primary_key=True)
    AccountId = models.ForeignKey(Account, related_name='data', on_delete=models.CASCADE)
    Name = models.CharField(max_length=45)
    Surname = models.CharField(max_length=45)
    PhoneNumber = models.CharField(max_length=45)
    PESEL = models.CharField(max_length=45)
    CompanyName = models.CharField(max_length=45)
    CompanyAdress = models.CharField(max_length=45)
    NIP = models.CharField(max_length=45, null=True)
    REGON = models.CharField(max_length=45, null=True)

    class Meta:
        ordering = ('Name', 'Surname',)


class DocumentType(models.Model):
    Id = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=45, null=False)

    class Meta:
        ordering = ('Type',)

class Document(models.Model):
    Id = models.AutoField(primary_key=True)
    DocumentTypeId = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    ClientId = models.ForeignKey(Client, on_delete=models.CASCADE)
    Date = models.DateTimeField()

    class Meta:
        ordering = ('Date',)


class Currency(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45, null=False)

    class Meta:
        ordering = ('Name',)

class Purchases_Sales(models.Model):
    Id = models.AutoField(primary_key=True)
    DocumentId = models.ForeignKey(Document, on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=45)
    NetAmount = models.DecimalField(decimal_places=2, max_digits=2)
    GrossAmount = models.DecimalField(decimal_places=2, max_digits=2)
    CurrencyId = models.ForeignKey(Currency, on_delete=models.CASCADE)
    Tax = models.IntegerField()

    class Meta:
        ordering = ('ProductName',)

class PIT(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45)
    Tax = models.IntegerField()

    class Meta:
        ordering = ('Name',)

class Declarations(models.Model):
    Id = models.AutoField(primary_key=True)
    DocumentId = models.ForeignKey(Purchases_Sales, on_delete=models.CASCADE)
    PIT_Id = models.ForeignKey(PIT, on_delete=models.CASCADE)
    Amount = models.CharField(max_length=45)
    Department = models.CharField(max_length=45)
    DateFrom = models.DateTimeField()
    DateTo = models.DateTimeField()

    class Meta:
        ordering = ('DateFrom', 'DateTo',)









