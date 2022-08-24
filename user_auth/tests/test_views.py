from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APITransactionTestCase
from user_auth.models import MyUser


class UserTests(APITransactionTestCase):
    """
        Tests the user view.
    """
    fixtures = ["testdata.json"] #Adds 2 users to db

    def test_create_account(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('signup')
        data = {
            "email": 'supzeFire22@gmail.com',
            "first_name": 'Supa',
            "last_name": 'Faya',
            "date_of_birth": '1988-02-09',
            "password": 'thisismypassword'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MyUser.objects.count(), 3)