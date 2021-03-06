from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User)
    
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' % (self.name,)


class Entry(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    leaderboard = models.ForeignKey(Leaderboard)

    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.name,)
    
    def increment_score(self, delta=1):
        self.score += delta
        self.save()
    
    def decrement_score(self, delta=1):
        self.score -= delta
        self.save()