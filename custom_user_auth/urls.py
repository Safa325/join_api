from django.urls import path, include

urlpatterns = [
    path('api/', include('custom_user_auth.api.urls')),
]
