from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APITransactionTestCase
from user_auth.models import MyUser
from user_auth.factories import UserFactory
from user_auth.serializers import UserSerializer


class UserSignupTests(APITransactionTestCase):
    """
        Tests the user signup view.
    """
    #fixtures = ["user_auth.json"] #Adds 2 users to db

    def setUp(self):
        """
        Add users to the db before the test is run.
        """
        UserFactory.create_batch(3)
    

    def test_invalid_dob(self):
        """
        Ensure the correct error if returned when an invalid date of birth is submitted.
        """
        url = reverse('signup')
        #data contains the user form
        user = UserFactory.build()
        data = UserSerializer(user).data
        #adding password to user object
        data['password'] = 'normalpassword'
        #adding invalid dob
        data['date_of_birth'] = '10-99-20'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        error_object = response.data['detail']
        self.assertEqual(str(error_object), 'Invalid date of birth!')


    def test_password_too_short(self):
        """
        Ensure that the correct response (error) is sent back when a user attempts to use a password that is too short. (i.e less than 6 characters)
        """
        url = reverse('signup')
        #data contains the user form data
        user = UserFactory.build()
        data = UserSerializer(user).data
        #adding password to user object
        data['password'] = '123'
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


    def test_invalid_password(self):
        """
        Ensure that the correct response (error) is sent back when a user attempts to use an invalid password. (i.e password that has 0 or 1 character.)
        """
        url = reverse('signup')
        #data contains the user form data
        user = UserFactory.build()
        data = UserSerializer(user).data
        #adding password to user object
        data['password'] = ''
        #Checking that the password we pass in for this test is really invalid.
        self.assertLessEqual(
            len(data['password']), 
            1, 
            msg = f'Error! data["password"] has {len(data["password"])} characters. In order for this test to run, the data["password"] value should be between 0-1 characters..'
        )
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        error_object = response.data['detail']
        self.assertEqual(str(error_object), 'Enter a valid password.')


    def test_invalid_information(self):
        """
        Ensure that the correct response (error) is sent back when a user tries to signup but leaves some required fields empty. (i.e first_name, last_name and password)
        """
        url = reverse('signup')
        #data contains the user form data
        user = UserFactory.build()
        data = UserSerializer(user).data
        #adding password to user object
        data['password'] = 'normalpassword'
        #making sure that the first_name field is empty
        data['first_name'] = ''
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        error_object = response.data['detail']
        self.assertEqual(str(error_object), 'Required fields have not been submitted!')


    def test_email_already_exists(self):
        """
        Ensure that the correct response (error) is sent back when a user tries to signup with an email address that is already registered.
        """
        url = reverse('signup')
        #get the email of the user that already exists on the db
        user_that_already_exists = MyUser.objects.all().last()
        email = user_that_already_exists.email
        #data contains the user form data
        user = UserFactory.build()
        data = UserSerializer(user).data
        #adding password to user object
        data['password'] = 'normalpassword'
        data['email'] = email
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