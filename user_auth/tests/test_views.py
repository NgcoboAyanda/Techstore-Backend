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
        """
        Ensure the correct error if returned when an invalid date of birth is submitted.
        """
        url = reverse('signup')
        data = {
            "email": 'ilikepie@suck.co.za',
            "first_name": 'Jack',
            "last_name": 'Reacher',
            #the correct format is YYYY-MM-DD
            #the date below uses yyyy-dd-mm which is wrong
            #this should make our server return status_code 422
            "date_of_birth": '1952-22-11',
            "password": 'ilikeartnigga11'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        error_object = response.data['detail']
        self.assertEqual(str(error_object), 'Invalid date of birth!')

    def test_password_too_short(self):
        """
        Ensure that the correct response (error) is sent back when a user attempts to use a password that is too short. (i.e less than 6 characters)
        """
        url = reverse('signup')
        data = {
            "email": 'realNigg@msickmail.com',
            "first_name": 'Bulford',
            "last_name": 'OGE',
            "date_of_birth": '1995-03-18',
            "password": 'qwera'
        }
        #Checking that the password we pass in for this test is really less than 6 characters.
        self.assertLess(
            len(data['password']), 
            6, 
            msg = f'Error! data["password"] has {len(data["password"])} characters. In order for this test to run, the data["password"] value should be less than 6 characters.'
        )
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        error_object = response.data['detail']
        self.assertEqual(str(error_object), 'Password has less than 6 characters. Password is too short!')

    def test_invalid_information(self):
        """
        Ensure that the correct response (error) is sent back when a user tries to signup but leaves some required fields empty. (i.e first_name, last_name and password)
        """
        data = {
            "email": 'goodemai@tool.com',
            "first_name": 'Doba',
            "last_name": '',
            "date_of_birth": '1990-02-02',
            "password": 'realskreetnigga!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        error_object = response.data['detail']
        self.assertEqual(str(error_object), 'A user with that email address already exists.')

    def test_email_already_exists(self):
        """
        Ensure that the correct response (error) is sent back when a user tries to signup with an email address that is already registered.
        """
        url = reverse('signup')
        #the email of the user that already exists on the db
        email = 'gorilla99@mail.com'
        #ensure the user really exists on the db before proceeding
        try:
            user = MyUser.objects.get(email=email)
        except MyUser.DoesNotExist:
            user = None
        self.assertTrue(
            user
            ,
            msg = f'Error! User associated with the email "{email}" was not found. Please ensure that the fixtures file is loaded correctly and that a user with the email {email} exists on the fixtures file. In order for this test to run successfully, you have to use an email that is already registered with another user in the db.')
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
            "email": 'correctemail@zmail.org',
            "first_name": 'Correct',
            "last_name": 'Name',
            "date_of_birth": '1990-02-09',
            "password": 'correct-password'
        }
    
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MyUser.objects.count(), 3)