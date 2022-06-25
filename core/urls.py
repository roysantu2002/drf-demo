"""
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls', namespace='api')),
    path('api/user/', include('accounts.urls')),
    path('api/user/', include('api.urls')),


]
