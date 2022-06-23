from django.urls import URLPattern, path

from . import views

app_name = 'api'

urlpatterns = [
    path('api/', views.login, name='login')
]
