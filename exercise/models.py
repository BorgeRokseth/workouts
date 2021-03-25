from django.db import models
from django.conf import settings


class TypesOfExercises(models.TextChoices):
    CARDIO = "Cardio", "Cardio"
    STRENGTH = "Strength", "Strength"
    STRETCH = "Stretch", "Stretch"


class Exercise(models.Model):
    name = models.TextField("Name of exercise")
    description = models.TextField("Description of exercise")
    # instruction_video = models.URLField(max_length=500)
    silent = models.BooleanField(default=False)
    equipment = models.CharField(max_length=120, default="None")
    type = models.CharField(max_length=100, choices=TypesOfExercises.choices)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return self.name


class SubFlow(models.Model):
    exercise = models.ForeignKey(to=Exercise, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField("Number of repetitions")


class Flow(models.Model):
    name = models.TextField("Name of Flow")
    exercise = models.ForeignKey(to=SubFlow, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField("Number of sets")
