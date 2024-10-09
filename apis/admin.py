from django.contrib import admin
from .models import Contacts, Task, Subtasks

admin.site.register(Contacts)
admin.site.register(Task)
admin.site.register(Subtasks)
