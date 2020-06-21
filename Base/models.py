from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Participant(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=100, blank=False)
    contact = models.PositiveIntegerField(primary_key=True,validators=[MaxValueValidator(9999999999)],blank=False)

    class Meta():
        ordering = ['created']

    def __str__(self):
        return self.name