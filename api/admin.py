from django.contrib import admin
from .models import Contacts, Task, Subtask

admin.site.register(Contacts)
admin.site.register(Task)
admin.site.register(Subtask)