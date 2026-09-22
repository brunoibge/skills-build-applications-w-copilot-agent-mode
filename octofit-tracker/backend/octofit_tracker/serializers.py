from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, User, Workout


def _stringify_object_ids(value):
    if isinstance(value, dict):
        payload = value.copy()
        for key, item in payload.items():
            if key == 'id' and item is not None:
                payload[key] = str(item)
            else:
                payload[key] = _stringify_object_ids(item)
        return payload
    if isinstance(value, list):
        return [_stringify_object_ids(item) for item in value]
    return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return _stringify_object_ids(data)


class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return _stringify_object_ids(data)


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return _stringify_object_ids(data)


class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return _stringify_object_ids(data)


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return _stringify_object_ids(data)