from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APITransactionTestCase
from user_auth.models import MyUser


class UserSignupTests(APITransactionTestCase):
    """
        Tests the user signup view.
    """
    fixtures = ["user_auth.json"] #Adds 2 users to db

    def test_invalid_dob(self):
        pass

    def test_password_too_short(self):
        pass

    def test_invalid_information(self):
        pass

    def test_email_already_exists(self):
        """
        Ensure that the correct response (error) is sent back when a user tries to signup with an email address that is already registered.
        """
        url = reverse('signup')
        #check that a user with this email already exists
        self.assertTrue(MyUser.objects.get(email='gorilla99@mail.com'))
        data = {
            "email": 'gorilla99@mail.com',
            "first_name": 'Stan',
            "last_name": 'Propenko',
            "date_of_birth": '1966-09-22',
            "password": 'ilikeartnigga11'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        error_object = response.data['detail']
        self.assertEqual(str(error_object), 'A user with that email address already exists.')


    def test_invalid_email(self):
        """
        Ensure the correct response (error) is sent back when user submits an invalid email.
        """
        url = reverse('signup')
        data = {
            "email": 'invalidemail.com',
            "first_name": 'John',
            "last_name": 'Doe',
            "date_of_birth": '1958-04-02',
            "password": 'password999#'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        error_object = response.data['detail']
        self.assertEqual(str(error_object), 'Invalid email address!')


    def test_create_account(self):
        """
        Ensure that the user is created when all form data is submitted and is in the correct format.
        """
        url = reverse('signup')
        data = {
            "email": 'SupaFaya@gmail.com',
            "first_name": 'Supa',
            "last_name": 'Faya',
            "date_of_birth": '1988-02-09',
            "password": 'thisismypassword'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MyUser.objects.count(), 3)