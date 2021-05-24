from django.db import models
from django.contrib.auth.models import User


class task(models.Model):
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500, null=True, blank=True)
    complete = models.BooleanField(default=False)
    person = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
