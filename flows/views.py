from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from exercise.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

from .models import Set, Flow
from .serializers import SetSerializer, FlowSerializer


class FlowListView(APIView):
    """
    View to list all exercises in the database and post new ones
    """
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

    def get(self, request):
        flow = Flow.objects.filter(author=request.user)
        serializer = FlowSerializer(flow, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowDetailView(APIView):
    """
    View to see and edit details for, and delete, exercise
    """
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Flow, pk=pk)

    def get(self, request, pk):
        flow = self.get_object(pk)
        serializer = FlowSerializer(flow)
        return Response(serializer.data)

    def put(self, request, pk):
        flow = self.get_object(pk)
        serializer = FlowSerializer(flow, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flow = self.get_object(pk)
        flow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)