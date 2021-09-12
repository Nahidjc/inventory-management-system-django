from django.db import models

# Create your models here.


class inventory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    units = models.PositiveIntegerField()

    def __str__(self):
        return self.name
