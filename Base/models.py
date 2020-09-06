from django.db import models


# Create your models here.

class Siteinventory(models.Model):
    store = models.IntegerField(blank=False)
    model = models.CharField(max_length=100, blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    scantype1 = models.CharField(max_length=100, blank=True, null=True)
    scannum1 = models.CharField(max_length=100, blank=True, null=True)
    scantype2 = models.CharField(max_length=100, blank=True, null=True)
    scannum2 = models.CharField(max_length=100, blank=True, null=True)
    scantype3 = models.CharField(max_length=100, blank=True, null=True)
    scannum3 = models.CharField(max_length=100, blank=True, null=True)
    scantype4 = models.CharField(max_length=100, blank=True, null=True)
    scannum4 = models.CharField(max_length=100, blank=True, null=True)
    sitetype = models.CharField(max_length=100, choices=(("Red", "Red"), ("Blue", "Blue")), blank=False)
    podnumber = models.IntegerField(blank=False)
    salesorder = models.CharField(max_length=100, blank=True, null=True)

    # client = models.PositiveIntegerField(primary_key=True,validators=[MaxValueValidator(9999999999)],blank=False)

    class Meta:
        ordering = ['store']

    def __str__(self):
        return "{} : {}".format(self.store, self.model)
