from django.urls import path

from . import views

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='exercises'),
]