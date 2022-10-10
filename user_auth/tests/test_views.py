from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APITransactionTestCase
from user_auth.models import MyUser
from user_auth.factories import UserFactory
import factory
from user_auth.serializers import UserSerializer

class BaseViewTests(APITransactionTestCase):
    """
    The base class that all test classes will inherit.
    Contains methods that are used across all view tests.
    """
    def createUsers(self, number):
        """Create a certain number of users in the db.
        """
        for _ in range(number):
            user = UserFactory()
            user.set_password(f'user{number}password')#e.g the password for user 1 will be user1password
            user.save()


class UserSignupTests(BaseViewTests):
    """
        Tests the user signup view.
    """

    def setUp(self):
        """
        Add users to the db before the test is run.
        """
        self.createUsers(3)
    

    def test_invalid_dob(self):
        """
        Ensure the correct error if returned when an invalid date of birth is submitted.
        """
        url = reverse('signup')
        #data contains the user form
        form_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        #adding normal password
        form_data['password'] = 'normalpassword'
        #adding invalid dob
        form_data['date_of_birth'] = '10-99-20'
        response = self.client.post(url, form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)


    def test_password_too_short(self):
        """
        Ensure that the correct response (error) is sent back when a user attempts to use a password that is too short. (i.e less than 6 characters)
        """
        url = reverse('signup')
        #data contains the user form data
        user = UserFactory.build()
        form_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        #adding password to user object
        form_data['password'] = '123'
        #Checking that the password we pass in for this test is really less than 6 characters.
        self.assertLess(
            len(form_data['password']), 
            6, 
            msg = f'Error! data["password"] has {len(form_data["password"])} characters. In order for this test to run, the data["password"] value should be less than 6 characters.'
        )
        response = self.client.post(url, form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)


    def test_invalid_password(self):
        """
        Ensure that the correct response (error) is sent back when a user attempts to use an invalid password. (i.e password that has 0 or 1 character.)
        """
        url = reverse('signup')
        #data contains the user form data
        form_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        #adding password to user object
        form_data['password'] = ''
        #Checking that the password we pass in for this test is really invalid.
        self.assertLessEqual(
            len(form_data['password']), 
            1, 
            msg = f'Error! data["password"] has {len(form_data["password"])} characters. In order for this test to run, the data["password"] value should be between 0-1 characters..'
        )
        response = self.client.post(url, form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)


    def test_invalid_information(self):
        """
        Ensure that the correct response (error) is sent back when a user tries to signup but leaves some required fields empty. (i.e first_name, last_name and password)
        """
        url = reverse('signup')
        #data contains the user form data
        form_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        #adding password to user object
        form_data['password'] = 'normalpassword'
        #making sure that the first_name field is empty
        form_data['first_name'] = ''
        response = self.client.post(url, form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)


    def test_email_already_exists(self):
        """
        Ensure that the correct response (error) is sent back when a user tries to signup with an email address that is already registered.
        """
        url = reverse('signup')
        #get the email of the user that already exists on the db
        user_that_already_exists = MyUser.objects.all().last()
        email = user_that_already_exists.email
        #form_data contains the user form data
        form_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        #adding password to user object
        form_data['password'] = 'normalpassword'
        form_data['email'] = email
        response = self.client.post(url, form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)


    def test_invalid_email(self):
        """
        Ensure the correct response (error) is sent back when user submits an invalid email.
        """
        url = reverse('signup')
        form_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        #adding invalid email
        form_data['email'] = 'invalidemail555.z0'
        response = self.client.post(url, form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)


    def test_create_account(self):
        """
        Ensure that the user is created when all form data is submitted and is in the correct format.
        """
        url = reverse('signup')
        form_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        #adding a password
        form_data['password'] = 'normalpassword'
        response = self.client.post(url, form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserLoginTests(BaseViewTests):
        """
        Test the user login view
        """
        url = reverse('login')

        def setUp(self):
            """
            Add users to the db before the test is run.
            """
            self.createUsers(3)

        def test_login(self):
            """
            Ensure that the user can log in when the correct credentials are supplied.
            """
            user = MyUser.objects.all().last()
            form_data = {
                'email': str(user.email),
                'password': 'user3password'
            }
            #posting the data
            response = self.client.post(self.url, form_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
        
        def test_wrong_password(self):
            """
            Ensure that the correct response (401) is sent back when a user attempts to login with a password that is incorrect.
            """
            user = MyUser.objects.all().last()
            form_data = {
                'email': str(user.email),
                'password': 'wrongpassword'
            }
            response = self.client.post(self.url, form_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)