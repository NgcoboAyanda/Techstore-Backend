from django.shortcuts import render
from django.db.utils import IntegrityError
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from user_auth.models import MyUser

# 409 Exception
class EmailAlreadyExists(APIException):
    status_code = 409
    default_detail = 'Error! A user with that email address already exists.'
    default_code = 'Email Already Exists.'

# Create your views here.
class SignupView(APIView):
    """
    A simple View for signing up.
    *Only takes POST request*
    *Returns status code 200 on success*
    """
    def createUser(self, request_object):
        data = request_object.data
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        dob = data['date_of_birth']
        
        try:
            #creating the new user
            MyUser.objects.create(email=email, first_name=first_name, last_name=last_name, date_of_birth=dob)
            return {'Message':'User successfully registered. You can now log in.'}
        
        except(IntegrityError):
        #An integrity error will be raised if the email address is associated with another account.
            raise EmailAlreadyExists


    def post(self, request):
        resp = self.createUser(request_object=request)
        return Response(resp)

