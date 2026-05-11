from django.urls import path, include
from . import views

urlpatterns = [
    # registration
    path('registration/', views.RegistrationAPIView.as_view(), name='registration')

    # change password
    # reset password
    # login token
    # login jwt
]