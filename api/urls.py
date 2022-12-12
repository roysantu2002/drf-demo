from accounts.views import TokenObtainPairView, TokenRefreshView
from django.urls import URLPattern, path

from . import views

# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView)


app_name = 'api'

urlpatterns = [
    # path('api/', views.login, name='login'),
    path('token', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),


]
