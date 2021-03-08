from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from exercise.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseListView(APIView):
    """
    View to list all exercises in the database and post new ones
    """
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    def get(self, request):
        exercise  = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseDetailView(APIView):
    """
    View to see and edit details for, and delete, exercise
    """
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Exercise, pk=pk)

    def get(self, request, pk):
        exercise = self.get_object(pk)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def put(self, request, pk):
        exercise = self.get_object(pk)
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        exercise = self.get_object(pk)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

