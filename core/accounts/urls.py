from django.urls import path, include


app_name = "accounts"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('api/v1/', include('account.api.v1.urls'))
]