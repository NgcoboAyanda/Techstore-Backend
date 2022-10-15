from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),

    path('login/', views.LoginView.as_view(), name='login'),
    
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]
