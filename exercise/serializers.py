from rest_framework import serializers
from .models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Exercise
        fields = [
            "id",
            "name",
            "description",
            "silent",
            "equipment",
            "type",
            "author"
        ]