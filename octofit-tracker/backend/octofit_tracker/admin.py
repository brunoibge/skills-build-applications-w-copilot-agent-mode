from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, User, Workout

admin.site.register([User, Team, Activity, LeaderboardEntry, Workout])