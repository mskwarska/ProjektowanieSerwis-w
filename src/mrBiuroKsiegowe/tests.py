from django.utils.http import urlencode
from rest_framework import status, reverse, test
from . import views
from .models import DocumentType, Currency, PIT

#Zakomentowac permission_classes w views.py

class DocumentTypeTests(test.APITestCase):
    def post_documentType(self, type):
        url = reverse.reverse(views.DocumentTypeList.name)
        data = {'Type': type}
        response = self.client.post(url, data, format='json')
        return response;

    def test_post_and_get_documentType(self):
        newType = 'NowyTyp'
        respone = self.post_documentType(newType)

        #assert co ma byc spelnione
        assert respone.status_code == status.HTTP_201_CREATED
        assert DocumentType.objects.count() == 1
        assert DocumentType.objects.get().Type == newType

class CurrencyTests(test.APITestCase):
    def post_currency(self, name):
        url = reverse.reverse(views.CurrencyList.name)
        data = {'Name': name}
        response = self.client.post(url, data, format='json')
        return response;

    def test_post_and_get_currency(self):
        newName = 'NowaNazwaWaluty'
        respone = self.post_currency(newName)

        #assert co ma byc spelnione
        assert respone.status_code == status.HTTP_201_CREATED
        assert Currency.objects.count() == 1
        assert Currency.objects.get().Name == newName

    def test_filter_currency(self):
        newName = 'USD'
        newName2 = 'ARS'

        self.post_currency(newName)
        self.post_currency(newName2)

        filter_currency = {'Name': newName2}
        url = '{0}?{1}'.format(reverse.reverse(views.CurrencyList.name), urlencode(filter_currency))

        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['Name'] == newName2
    
class PitTests(test.APITestCase):
    def post_pit(self, name, tax):
        url = reverse.reverse(views.PITList.name)
        data = {'Name': name, 'Tax': tax}
        response = self.client.post(url, data, format='json')
        return response;

    def test_post_and_get_tax(self):
        newName = 'PIT 214231e54132'
        tax = 20

        respone = self.post_pit(newName, tax)

        #assert co ma byc spelnione
        assert respone.status_code == status.HTTP_201_CREATED
        assert PIT.objects.count() == 1
        assert PIT.objects.get().Name == newName
        assert PIT.objects.get().Tax == tax

    def test_filter_tax(self):
        newName1 = 'PIT 1'
        newTax1 = 20

        newName2 = 'PIT 2'
        newTax2 = 40

        newName3 = 'PIT 3'
        newTax3 = 29

        self.post_pit(newName1, newTax1)
        self.post_pit(newName2, newTax2)
        self.post_pit(newName3, newTax3)

        filter_tax = {'TaxAmountFrom': newTax1, 'TaxAmountTo': newTax3}
        url = '{0}?{1}'.format(reverse.reverse(views.PITList.name), urlencode(filter_tax))

        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2
        assert response.data['results'][0]['Name'] == newName1
        assert response.data['results'][0]['Tax'] == newTax1

        assert response.data['results'][1]['Name'] == newName3
        assert response.data['results'][1]['Tax'] == newTax3
