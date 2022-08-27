from django.shortcuts import render
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
import re

#Models
from user_auth.models import MyUser
from user_auth.serializers import UserSerializer

#Exceptions
from user_auth.exceptions import EmailAlreadyExists, InvalidDateOfBirth, InvalidEmail, InvalidInformation, PasswordTooShort, InvalidPassword, UserNotFound

#BASE VIEW
class BaseView(APIView):
    """
        This is the base view that every view will inherit. It contains methods that may be used across different views.
    """
    def validate(self, type, phrase):
        """
            Function that validates the form data.
            *Takes two arguments:
                1) type -- ['email-field' or 'text-field' or 'password-field']
                2) phrase -- [the string that is to be validated]
            *If the form data is valid then it will be returned
            *If the form data is invalid then an error will be thrown
        """

        if type == 'email-field':
            #The email regular expression
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            if(re.fullmatch(email_regex, phrase)):
                #if the email is valid we return it
                return phrase

            else:
                raise InvalidEmail
        
        elif type == 'text-field':
            #We only check the length for the other fields
            if(len(phrase) > 0):
                return phrase
            
            else:
                raise InvalidInformation
                return None
            
        elif type == 'password-field':
            #Password has to be more than 6 characters
            chars = len(phrase)
            if chars >= 6 :
                return phrase
            elif chars <=1:
                raise InvalidPassword
                return None
            else:
                raise PasswordTooShort
                raise None


# Signup View
class SignupView(BaseView):
    """
        A simple View for signing up.
        *Only takes POST request*
        *Returns status code 201 HTTP CREATED on success*
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
        email = self.validate(type='email-field', phrase=data['email'] )
        first_name = self.validate( type='text-field', phrase=data['first_name'] )
        last_name = self.validate( type='text-field', phrase=data['last_name'] )
        dob = self.validate( type='text-field', phrase=data['date_of_birth'] )
        password = self.validate( type='password-field', phrase=data['password'] )
        #Validating information

        try:
            #creating the new user
            new_user = MyUser(email=email, first_name=first_name, last_name=last_name, date_of_birth=dob, password='')
            new_user.set_password(password)
            new_user.save()
            return {'message':'User successfully registered. You can now log in.'}
        
        except(IntegrityError):
        #An integrity error will be raised if the email address is associated with another account.
            raise EmailAlreadyExists

        except(ValidationError):
        #This means the date was captured wrong
            raise InvalidDateOfBirth

    def post(self, request):
        resp = self.createUser(request_object=request)
        return Response(resp, status=201)


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
            serializer = UserSerializer(user)
            user = serializer.data
            return Response(user)
        else:
            #if authentication failed
            try:
                the_user = MyUser.objects.get(email=user_email)
                raise
            except MyUser.DoesNotExist:
                raise