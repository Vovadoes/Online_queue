from django.db import models
from account.models import Profile
from datetime import datetime


class Group(models.Model):
    # queue_id = models.ManyToManyField()
    profils = models.ManyToManyField(
        Profile, related_name='profile_group', blank=True, null=True
        )
    admins = models.ManyToManyField(Profile, related_name='profile_admin_grop')


class Queue(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    creater_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=datetime.now())
    last_number = models.PositiveBigIntegerField(default=0)
    parallelization = models.IntegerField(default=0)
    waiting_time_max = models.PositiveBigIntegerField(default=0)


class Status(models.Model):
    name = models.TextField()


class PlaseQueue(models.Model):
    queues = models.ManyToManyField(Queue)
    profiles = models.ManyToManyField(Profile)
    number = models.PositiveBigIntegerField(default=0)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=datetime.now())
    date_finish = models.DateTimeField(blank=True, null=True)
