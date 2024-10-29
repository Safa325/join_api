from django.db import models
from django.conf import settings

class Subtask(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    task = models.ForeignKey('Task', related_name='subtasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    # assignedTo = models.ManyToManyField('Contacts', related_name='tasks', blank=True)
    priority = models.CharField(max_length=10, blank=True)
    category = models.CharField(max_length=100, blank=True)
    dueDate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contacts(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    badgecolor = models.CharField(max_length=8)
    initials = models.CharField(max_length=2)
    register = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    selected = models.BooleanField(default=False)
    task = models.ManyToManyField(Task, related_name='assignedTo', blank=True)
    
    def __str__(self):
        return  self.name