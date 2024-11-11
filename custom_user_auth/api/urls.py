from django.urls import path
from .views import UserProfileList, UserProfileDetail, RegisterView, CustomLoginView


urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view() , name='login'),
]
