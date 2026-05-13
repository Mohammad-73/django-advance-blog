from django.urls import path, include
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    # registration
    path('registration/', views.RegistrationAPIView.as_view(), name='registration'),

    # change password
    # reset password
    # login token
    path('token/login', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout', views.CustomDiscardAuthToken.as_view(), name='token-logout'),

    # login jwt
]