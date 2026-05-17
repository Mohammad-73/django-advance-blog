from django.urls import path, include
from .. import views
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # Registration
    path('registration/', views.RegistrationAPIView.as_view(), name='registration'),

    path('test-email/', views.TestEmailSend.as_view(), name='test-email'),
    # Activation
    # path('activation/confirm/')
    
    # Resend activation
    # path('activation/resend/')

    # Change password
    path('change-password/', views.ChangePasswordAPIView.as_view(), name='change-password'),
    
    # Reset password
    
    # Login token
    path('token/login', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout', views.CustomDiscardAuthToken.as_view(), name='token-logout'),

    # Login jwt
    path('token/create/', views.CustomTokenObtainPairView.as_view(),name="jwt-create"),
    path('token/refresh/', TokenRefreshView.as_view(),name="jwt-refresh"),
    path('token/verify/', TokenVerifyView.as_view(),name="jwt-verify"),
]