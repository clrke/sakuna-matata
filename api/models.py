from django.db import models
from django.contrib.auth.models import User


class Channel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '#%s' % self.name


class Message(models.Model):
    channel = models.ForeignKey(Channel)
    message = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    sentiment = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[%s] %s...' % (self.channel, self.message[:80])


class DisasterManager(models.Model):
    user = models.ForeignKey(User)
    channel = models.ForeignKey(Channel)

    def __str__(self):
        return '[%s] %s' % (self.channel, self.user)
