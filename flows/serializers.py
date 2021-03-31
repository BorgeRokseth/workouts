from rest_framework import serializers
from .models import Flow, Set


class SetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = Set
        fields = [
            "id",
            "exercise",
            "reps"
        ]


class FlowSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    exercise = SetSerializer(many=True)

    class Meta:
        model = Flow
        fields = [
            "id",
            "name",
            "description",
            "exercise",
            "created_at",
            "updated_at",
            "author"
        ]