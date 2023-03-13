from django.contrib import admin
from .models import Group, Queue, Status, PlaseQueue

admin.site.register(Group)
admin.site.register(Queue)
admin.site.register(Status)
admin.site.register(PlaseQueue)
