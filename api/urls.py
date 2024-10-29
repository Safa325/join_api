from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskList, TaskDetail, ContactsDetail, ContactsList, SubtasksList, SubtaskDetail

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'users', UserViewSet)

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('contacts/', ContactsList.as_view(), name='contacts-detail'),
    path('contacts/<int:pk>/', ContactsDetail.as_view(), name='contacts-detail'),
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='tasks-detail'),
    # path('subtasks/', SubtasksList.as_view()),
    # path('subtasks/<int:pk>/', SubtaskDetail.as_view(), name='subtasks-detail'),
]
