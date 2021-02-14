from django.db import models

class TypesOfExercises(models.TextChoices):
    CARDIO = "Cardio", "Cardio"
    STRENGTH = "Strength", "Strength"
    STRETCH = "Stretch", "Stretch"


class Exercise(models.Model):
    name = models.TextField("Name of exercise")
    description = models.TextField("Description of exercise")
    # instruction_video = models.URLField(max_length=500)
    silent = models.BooleanField(default=False)
    equipment = models.BooleanField(default=False)
    type = models.CharField(max_length=100, choices=TypesOfExercises.choices)

