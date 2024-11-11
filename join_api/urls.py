
from django.contrib import admin
from django.urls import path, include  # Importiere 'include', um andere URL-Dateien einzubinden

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('custom_user_auth.urls')),
    path('api/', include('api.urls')), 
    path('api-auth/', include('rest_framework.urls')), 
]

