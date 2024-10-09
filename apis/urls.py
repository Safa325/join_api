from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, ContactsViewSet, SubtasksViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'contacts', ContactsViewSet)
router.register(r'subtasks', SubtasksViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]