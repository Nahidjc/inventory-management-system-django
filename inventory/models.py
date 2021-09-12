from django.db import models

# Create your models here.


class inventory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    units = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class createSupplier(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=250)
    email = models.EmailField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    gstinNo = models.CharField(blank=True, unique=True, max_length=250)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
