from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class AuthView(View):
    def get(self, request):
        return HttpResponse('<h1> This is the auth page </h1>')