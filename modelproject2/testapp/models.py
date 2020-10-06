from django.db import models

# Create your models here.

class Job(models.Model):
    pdate = models.DateField()
    loc = models.CharField(max_length=64)
    sal = models.FloatField()
    qual = models.CharField(max_length=64)

    def __str__(self):
        return self.loc
