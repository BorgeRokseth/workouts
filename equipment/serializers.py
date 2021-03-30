from rest_framework import serializers
from .models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Equipment
        fields = [
            "id",
            "name",
            "description",
            "author"
        ]