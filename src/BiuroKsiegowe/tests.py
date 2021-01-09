from django.utils.http import urlencode
from rest_framework import status, reverse, test
from . import views
from .models import DocumentType, Currency, PIT
from django.contrib.auth.models import User
from django.core import serializers

#Zakomentowac permission_classes w views.py

class DocumentTypeTests(test.APITestCase):
    def post_documentType(self, type):
        url = reverse.reverse(views.DocumentTypeList.name)
        data = {'Type': type}
        response = self.client.post(url, data, format='json')
        return response;

    def test_post_and_get_documentType(self):
        newType = 'NowyTyp'
        response = self.post_documentType(newType)

        assert response.status_code == status.HTTP_201_CREATED
        
        assert DocumentType.objects.count() == 1

        assert DocumentType.objects.get().Type == newType

    def test_CRUD_documentType(self):

        #--------------POST--------------
        newType = 'NowyTyp'

        url = reverse.reverse(views.DocumentTypeList.name)
        data = {'Type': newType}
        response = self.client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        
        assert DocumentType.objects.count() == 1

        assert DocumentType.objects.get().Type == newType

        #--------------POST--------------


        #-------------UPDATE-------------
        updatedType = 'AktualizacjaTypu'

        url = reverse.reverse(views.DocumentTypeDetail.name, args=str(DocumentType.objects.get().Id))
        data = {'Id': DocumentType.objects.get().Id, 'Type': updatedType}
        response = self.client.put(url, data, format='json')

        assert response.status_code == status.HTTP_200_OK

        assert DocumentType.objects.count() == 1

        assert DocumentType.objects.get().Type == updatedType

        #-------------UPDATE-------------


        #-------------DELETE-------------
        url = reverse.reverse(views.DocumentTypeDetail.name, args=str(DocumentType.objects.get().Id))

        response = self.client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT

        #-------------DELETE-------------

class CurrencyTests(test.APITestCase):
    def post_currency(self, name, code, country):
        url = reverse.reverse(views.CurrencyList.name)
        data = {'Name': name, 'Code': code, 'Country': country}
        response = self.client.post(url, data, format='json')
        return response;

    def test_post_and_get_currency(self):
        newName = 'NowaNazwaWaluty'
        newCode = 'NEW'
        newCountry = 'NowePanstwo'
        respone = self.post_currency(newName, newCode, newCountry)

        assert respone.status_code == status.HTTP_201_CREATED

        assert Currency.objects.count() == 1

        assert Currency.objects.get().Name == newName
        assert Currency.objects.get().Code == newCode
        assert Currency.objects.get().Country == newCountry

    def test_filter_currency(self):
        newName = 'Polski złoty'
        newCode = 'PLN'
        newCountry = 'Polska'
        newName2 = 'Euro'
        newCode2 = 'EUR'
        newCountry2 = 'Kraje europejskie'

        self.post_currency(newName, newCode, newCountry)
        self.post_currency(newName2, newCode2, newCountry2)

        filter_currency = {'Name': newName2}
        url = '{0}?{1}'.format(reverse.reverse(views.CurrencyList.name), urlencode(filter_currency))

        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK

        assert response.data['count'] == 1

        assert response.data['results'][0]['Name'] == newName2
        assert response.data['results'][0]['Code'] == newCode2
        assert response.data['results'][0]['Country'] == newCountry2
    
class PitTests(test.APITestCase):
    def post_pit(self, name, desc, deadline):
        url = reverse.reverse(views.PITList.name)
        data = {'Name': name, 'Desc': desc, 'Deadline': deadline}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_tax(self):
        newName = 'PIT 214231e54132'
        newDesc = "DESC TREWGDS"
        newDeadline = "DEADLINE FSDAG"

        respone = self.post_pit(newName, newDesc, newDeadline)

        assert respone.status_code == status.HTTP_201_CREATED

        assert PIT.objects.count() == 1

        assert PIT.objects.get().Name == newName
        assert PIT.objects.get().Desc == newDesc
        assert PIT.objects.get().Deadline == newDeadline

    def test_filter_name(self):
        newName1 = 'PIT'
        newDesc1 = 'DESC 1'
        newDeadline1 = 'DEADLINE 1'

        newName2 = 'PIT'
        newDesc2 = 'DESC 2'
        newDeadline2 = 'DEADLINE 2'

        newName3 = 'AKC'
        newDesc3 = 'DESC 3'
        newDeadline3 = 'DEADLINE 3'

        self.post_pit(newName1, newDesc1, newDeadline1)
        self.post_pit(newName2, newDesc2, newDeadline2)
        self.post_pit(newName3, newDesc3, newDeadline3)

        filter_tax = {'search': newName2}
        url = '{0}?{1}'.format(reverse.reverse(views.PITList.name), urlencode(filter_tax))

        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK

        assert response.data['count'] == 2

        assert response.data['results'][0]['Name'] == newName1
        assert response.data['results'][0]['Desc'] == newDesc1
        assert response.data['results'][0]['Deadline'] == newDeadline1

        assert response.data['results'][1]['Name'] == newName2
        assert response.data['results'][1]['Desc'] == newDesc2
        assert response.data['results'][1]['Deadline'] == newDeadline2

# class DocumentTest(test.APITestCase):
#     def test_post_document(self):
#         user = User.objects.create(username='testUser', email='test@test.com', password='Password123456789')
#         client = {'Name': 'Imie', 'User': User.objects.get(), 'Surname': 'Nazwisko', 'PhoneNumber': '123-456-789', 'PESEL': '12345678912'}
#         url = reverse.reverse(views.ClientList.name)
#         response = self.client.post(url, client, format='json')

#         assert response.status_code == status.HTTP_201_CREATED
        
#         assert Client.objects.count() == 1

#         url = reverse.reverse(views.DocumentList.name)
#         data = {'DcoumentType': documentType, 'Client_id': Client.objects.get(), 'CreatedBy_id': user.id, 'CreationDate': '2021-01-08 12:42:26.928488'}
#         response = self.client.post(url, data, format='json')

#         assert response.status_code == status.HTTP_201_CREATED