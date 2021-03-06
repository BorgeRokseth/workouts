from django.db import models
from exercise.models import Exercise
from django.conf import settings


class Set(models.Model):
    exercise = models.ForeignKey(to=Exercise, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField()

    def __str__(self):
        if self.reps > 1:
            rep_string = "reps"
        else:
            rep_string = "rep"
        return f'{self.exercise.name} ({self.reps} {rep_string})'


class Flow(models.Model):
    name = models.TextField("Name of flow")
    description = models.TextField("Flow description")
    exercise = models.ManyToManyField(to=Set)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="flow")