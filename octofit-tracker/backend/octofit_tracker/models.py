from django.db import models


class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    avatar = models.URLField(blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='teams', blank=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=40)
    duration_minutes = models.PositiveIntegerField()
    points = models.PositiveIntegerField(default=0)
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'


class LeaderboardEntry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard_entry')
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank', '-points']


class Workout(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    target = models.CharField(max_length=60)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name