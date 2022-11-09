import datetime
import re
import environ
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

#Models & Serializers
from user_auth.models import MyUser
from . import serializers

#Exceptions
from user_auth import exceptions

# django-environ
env = environ.Env()

#BASE VIEW
class BaseView(APIView):
    """
        This is the base view that every view will inherit. It contains methods that may be used across different views.
    """
    def validate(self, field_type, field_content):
        """
            Function that validates the form data.
            *Takes two arguments:
                1) field_type -- ['email-field' or 'text-field' or 'password-field']
                2) field_content -- [the string that is to be validated]
            *If the form data is valid then it will be returned
            *If the form data is invalid then an error will be thrown
        """

        if field_type == 'email-field':
            #The email regular expression
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            if(re.fullmatch(email_regex, field_content)):
                #if the email is valid we return it
                return field_content

            else:
                raise exceptions.InvalidEmail
        
        elif field_type == 'phone':
            #we will validate phone number here
            return field_content
        
        elif field_type == 'text-field':
            #We only check the length for the other fields
            if(len(field_content) > 0):
                return field_content
            
            else:
                raise exceptions.InvalidInformation
                return None
            
        elif field_type == 'password-field':
            #Password has to be more than 6 characters
            chars = len(field_content)
            if chars >= 6 :
                return field_content
            elif chars <=1:
                raise exceptions.InvalidPassword
                return None
            else:
                raise exceptions.PasswordTooShort
                raise None
    
    def serializedUser(self, user_object):
        """Returns serialized user object with authentication token.
        """
        serialized = serializers.UserSerializer(user_object).data
        token, _ = Token.objects.get_or_create(user=user_object)
        serialized['auth_token'] = token.key #Adding the token to serialized data
        return serialized


# Signup View
class SignupView(BaseView):
    """
        A simple View for signing up.
        *Only takes POST request*
        *Returns status code 201 HTTP CREATED on success*
        *Returns user object if user successfully registered
    """

    def createUser(self, request_object):
        """
            A function that signs the user up.
            *Takes one argument:
                request_object -- [this is the request object]
            *If there are no errors then the user is created and a response with HTTP_STATUS_CODE-201-CREATED is returned.
            *If there are errors then they are handled.
        """
        data = request_object.data
        #EVERY VALUE IS VALIDATED BY self.validate() function
        email = self.validate(field_type='email-field', field_content=data['email'] )
        first_name = self.validate( field_type='text-field', field_content=data['first_name'] )
        last_name = self.validate( field_type='text-field', field_content=data['last_name'] )
        password = self.validate( field_type='password-field', field_content=data['password'] )
        phone = self.validate(field_type='phone-field', field_content=data['phone'])
        #Validating information

        try:
            #creating the new user
            new_user = MyUser(email=email, first_name=first_name, last_name=last_name, password='')
            new_user.set_password(password)
            new_user.save()
            token = Token.objects.create(user=new_user)
            #Returning serialized user with a token too
            return None
        
        except(IntegrityError):
        #An integrity error will be raised if the email address is associated with another account.
            raise exceptions.EmailAlreadyExists

        except(ValidationError):
        #This means the date was captured wrong
            raise exceptions.InvalidDateOfBirth

    def post(self, request):
        resp = self.createUser(request_object=request)
        return Response(resp, status=status.HTTP_201_CREATED)


#Login View
class LoginView(BaseView):
    """
    A simple view for logging in.
    *Only takes POST request
    *Returns user object if user is succesfully authenticated. 
    """
    def post(self, request):
        form_data = request.data
        user_email = form_data['email']
        user_password = form_data['password']
        user_auth = authenticate(email=user_email, password=user_password)
        if user_auth is not None:
            #if authentication was successful
            #return the user token
            token = self.serializedUser(user_auth)['auth_token']
            user_serialized = serializers.UserSerializer(user_auth).data
            return Response({
                'user': user_serialized,
                'token': token
            }, status=status.HTTP_200_OK)
        else:
            #if authentication failed
            try:
                the_user = MyUser.objects.get(email=user_email)
                raise exceptions.WrongPassword
            except MyUser.DoesNotExist:
                raise exceptions.UserDoesNotExist

class GetUserView(BaseView):
    """
    A simple view for getting user information.
    *Takes the user token as a parameter
    """

    def get(self, request, user_token):
        try:
            user = Token.objects.get(key=user_token).user
            user = serializers.UserSerializer(user).data
            return Response(user, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            raise exceptions.UserDoesNotExist
        pass