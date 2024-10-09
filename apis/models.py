from django.db import models

class Contacts(models.Model):
    badgecolor = models.CharField(max_length=8)
    initials = models.CharField(max_length=2)
    register = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    selected = models.BooleanField(default=False)
    
class Subtasks(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    assignedTo = models.ManyToManyField(Contacts, related_name='tasks', blank=True)
    priority = models.CharField(max_length=10, blank=True)
    category = models.CharField(max_length=100, blank=True)
    dueDate = models.DateField(blank=True)
    status = models.CharField(max_length=20, blank=True)
    subtasks = models.ManyToManyField(Subtasks, related_name='tasks', blank=True)