from telnetlib import STATUS
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Contacts, Subtasks
from .serializers import TaskSerializer, ContactsSerializer, SubtasksSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [] # permissions.IsAuthenticated
   
class ContactsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [] # permissions.IsAuthenticated
    
class SubtasksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Subtasks.objects.all()
    serializer_class = SubtasksSerializer
    permission_classes = [] # permissions.IsAuthenticated
