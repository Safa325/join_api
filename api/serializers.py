from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Contacts, Subtask
from django.db import transaction

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'title', 'done']

class ContactsSerializer(serializers.ModelSerializer):
    Username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Contacts
        fields = ['id', 'Username', 'badgecolor', 'initials', 'register', 'name', 'email', 'phone', 'selected']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)
    assignedTo = ContactsSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assignedTo', 'priority', 'category', 'dueDate', 'status', 'subtasks']

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_to_data = validated_data.pop('assignedTo', [])

        with transaction.atomic():
            # Erstelle die Hauptaufgabe (`task`)
            task = Task.objects.create(**validated_data)

            # Füge Kontakte hinzu oder erstelle sie, falls nicht vorhanden
            contact_ids = []
            for contact_data in assigned_to_data:
                contact, created = Contacts.objects.get_or_create(**contact_data)
                contact_ids.append(contact.id)
            task.assignedTo.set(contact_ids)

            # Erstelle die `subtasks` und verknüpfe sie mit der `task`
            for subtask_data in subtasks_data:
                Subtask.objects.create(task=task, **subtask_data)

        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_to_data = validated_data.pop('assignedTo', [])

        # Aktualisiere die Felder der Hauptaufgabe (`task`)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.category = validated_data.get('category', instance.category)
        instance.dueDate = validated_data.get('dueDate', instance.dueDate)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        # Kontakte aktualisieren oder erstellen und zuordnen
        contact_ids = []
        for contact_data in assigned_to_data:
            contact, created = Contacts.objects.get_or_create(**contact_data)
            contact_ids.append(contact.id)
        instance.assignedTo.set(contact_ids)

        # Bestehende Subtasks aktualisieren, hinzufügen oder entfernen
        existing_subtask_ids = [subtask.id for subtask in instance.subtasks.all()]
        new_subtask_ids = [subtask.get('id') for subtask in subtasks_data if subtask.get('id')]

        # Entferne `subtasks`, die nicht in `subtasks_data` vorhanden sind
        for subtask in instance.subtasks.all():
            if subtask.id not in new_subtask_ids:
                subtask.delete()

        # Aktualisiere oder erstelle `subtasks`
        for subtask_data in subtasks_data:
            subtask_id = subtask_data.get('id')
            if subtask_id and subtask_id in existing_subtask_ids:
                # Subtask aktualisieren, wenn die ID existiert
                Subtask.objects.filter(id=subtask_id).update(**subtask_data)
            else:
                # Neuen Subtask erstellen, wenn keine ID vorhanden ist
                Subtask.objects.create(task=instance, **subtask_data)

        return instance

class UserSerializer(serializers.ModelSerializer):
    user_contacts = ContactsSerializer(many=True, source='contacts_set')
    user_tasks = TaskSerializer(many=True, source='task_set')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_contacts', 'user_tasks']
