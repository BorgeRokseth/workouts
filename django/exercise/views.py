from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseListView(APIView):
    """
    View to list all exercises in the database
    """
    def get(self, request):
        exercise  = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data)

