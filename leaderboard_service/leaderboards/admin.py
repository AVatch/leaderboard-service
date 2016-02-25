from django.contrib import admin

from .models import Leaderboard

class LeaderboardAdmin(admin.ModelAdmin):
    pass
admin.site.register(Leaderboard, LeaderboardAdmin)