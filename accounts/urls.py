from django.urls import path

from .views import BlacklistTokenUpdateView, RegisterView

app_name = 'accounts'

urlpatterns = [
       path('register/', RegisterView.as_view(), name="create_user"),
]
