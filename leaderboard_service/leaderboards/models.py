from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%' % self.name