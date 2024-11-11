from rest_framework import viewsets, permissions
from .models import Task, Contacts, Subtask
from .serializers import TaskSerializer, UserSerializer, ContactsSerializer, SubtaskSerializer
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, pk, user):
        try:
            return Task.objects.get(pk=pk, user=user)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk, request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk, request.user)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk, request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ContactsList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        contacts = Contacts.objects.filter(user=request.user)
        serializer = ContactsSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactsDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, pk, user):
        try:
            return Contacts.objects.get(pk=pk, user=user)
        except Contacts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contact = self.get_object(pk, request.user)
        serializer = ContactsSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contact = self.get_object(pk, request.user)
        serializer = ContactsSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contact = self.get_object(pk, request.user)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubtasksList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        subtasks = Subtask.objects.filter(task__user=request.user)
        serializer = SubtaskSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubtaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class SubtaskDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, pk, user):
        try:
            return Subtask.objects.get(pk=pk, task__user=user)
        except Subtask.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subtask = self.get_object(pk, request.user)
        serializer = SubtaskSerializer(subtask)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subtask = self.get_object(pk, request.user)
        serializer = SubtaskSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subtask = self.get_object(pk, request.user)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
