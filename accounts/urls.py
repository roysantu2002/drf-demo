from django.urls import path

from .views import BlacklistTokenUpdateView, CustomUserCreate

app_name = 'accounts'

urlpatterns = [
       path('register/', CustomUserCreate.as_view(), name="create_user"),
]
