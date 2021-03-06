from django.db import models
from django.conf import settings
from equipment.models import Equipment


class TypesOfExercises(models.TextChoices):
    CARDIO = "Cardio", "Cardio"
    STRENGTH = "Strength", "Strength"
    STRETCH = "Stretch", "Stretch"


class Exercise(models.Model):
    name = models.TextField("Name of exercise")
    description = models.TextField("Description of exercise")
    silent = models.BooleanField(default=False)
    equipment = models.ManyToManyField(Equipment, null=True, blank=True)
    type = models.CharField(max_length=100, choices=TypesOfExercises.choices)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return self.name

