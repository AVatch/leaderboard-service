from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Leaderboard
from .models import Entry


class LeaderboardSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Leaderboard


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry