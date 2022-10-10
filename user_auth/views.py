from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
import smtplib
from django.core import mail
from django.conf import settings
import environ
import socket

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status

import re
import uuid

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
        dob = self.validate( field_type='text-field', field_content=data['date_of_birth'] )
        password = self.validate( field_type='password-field', field_content=data['password'] )
        phone = self.validate(field_type='phone-field', field_content=data['phone'])
        #Validating information

        try:
            #creating the new user
            new_user = MyUser(email=email, first_name=first_name, last_name=last_name, date_of_birth=dob, password='')
            new_user.set_password(password)
            new_user.save()
            #Returning serialized user with a token too
            return self.serializedUser(user_object=new_user)
        
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
            #return serialized user object with token
            user_obj = self.serializedUser(user_object=user_auth)
            return Response(user_obj, status=status.HTTP_200_OK)
        else:
            #if authentication failed
            try:
                the_user = MyUser.objects.filter(email=user_email)
                if the_user.count() == 1:
                    raise exceptions.WrongPassword
            except MyUser.DoesNotExist:
                raise exceptions.UserDoesNotExist

#Forgot Password view
class ForgotPasswordView(BaseView):
    """View responsible for resetting user password.
        *Should return status 200 if the email is registered and the reset link was sent.
        *Should return status 404 if there is no user associated with the given email address.
    """
    renderer_classes = [JSONRenderer]

    def sendOTP(self, recipient):
        otp = 5555
        try:
            mail.send_mail(
            subject="Techstore password reset OTP"
            , 
            message=f"Your OTP is {otp}"
            ,
            from_email=env('GMAIL_USERNAME') 
            , 
            recipient_list=[recipient]
            ,
            fail_silently=False
        )
        except smtplib.SMTPException:
            raise exceptions.OTPSendError
        except socket.gaierror:
            raise exceptions.NetworkError

    def post(self, request):
        form_data = request.data
        user_email = form_data['email']
        #gettin user
        try:
            the_user = MyUser.objects.get(email=user_email)
            the_user = self.serializedUser(user_object=the_user)
            self.sendOTP(user_email)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MyUser.DoesNotExist:
            raise exceptions.UserDoesNotExist
