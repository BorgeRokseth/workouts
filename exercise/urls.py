from django.urls import path

from . import views

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='exercise_list'),
    path('<int:pk>/', views.ExerciseDetailView.as_view(), name='exercise_details')
]