from django.db import models
from django.conf import settings


class Equipment(models.Model):
    name = models.TextField("Name of equipment")
    description = models.TextField("Description of equipment", blank=True, null=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="equipment")

    def __str__(self):
        return self.name