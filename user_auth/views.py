from django.shortcuts import render
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import re

#Models
from user_auth.models import MyUser

#Exceptions
from user_auth.exceptions import EmailAlreadyExists, InvalidDateOfBirth, InvalidEmail, InvalidInformation, PasswordTooShort

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
            
        elif type == 'password-field':
            #Password has to be more than 6 characters
            if( len(phrase) >= 6 ):
                return phrase
            
            else:
                raise PasswordTooShort()


# Signup View
class SignupView(BaseView):
    """
        A simple View for signing up.
        *Only takes POST request*
        *Returns status code 200 on success*
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
            MyUser.objects.create(email=email, first_name=first_name, last_name=last_name, date_of_birth=dob, password=password)
            return {'Message':'User successfully registered. You can now log in.'}
        
        except(IntegrityError):
        #An integrity error will be raised if the email address is associated with another account.
            raise EmailAlreadyExists

        except(ValidationError):
        #This means the date was captured wrong
            raise InvalidDateOfBirth

    def post(self, request):
        resp = self.createUser(request_object=request)
        return Response(resp, status=201)

