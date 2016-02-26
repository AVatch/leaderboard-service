from django.contrib import admin

from .models import Leaderboard
from .models import Entry


class LeaderboardAdmin(admin.ModelAdmin):
    pass
admin.site.register(Leaderboard, LeaderboardAdmin)


class EntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entry, EntryAdmin)