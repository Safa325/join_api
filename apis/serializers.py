from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, Contacts, Subtasks
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email',] 


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'
        
class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Contacts
        fields = '__all__'
        
class SubtasksSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Subtasks
        fields = '__all__'