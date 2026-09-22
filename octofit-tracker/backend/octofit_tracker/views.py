import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Activity, LeaderboardEntry, Team, User, Workout
from .serializers import (ActivitySerializer, LeaderboardSerializer,
                          TeamSerializer, UserSerializer, WorkoutSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.prefetch_related('members').all()
    serializer_class = TeamSerializer


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.select_related('user').all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(ModelViewSet):
    queryset = LeaderboardEntry.objects.select_related('user').all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


@api_view(['GET'])
def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    base_url = (
        f'https://{codespace_name}-8000.app.github.dev'
        if codespace_name
        else request.build_absolute_uri('/').rstrip('/')
    )
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
    })