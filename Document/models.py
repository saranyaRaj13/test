from django.db import models

# Create your models here.
class DocumentModel(models.Model):
    name=models.CharField(max_length=100)
class Farmer(models.Model):
    name=models.CharField(max_length=100)
    capacity=models.IntegerField(null=True)
class CropDetails(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField(null=True)

class CargoShip(models.Model):
    name=models.CharField(max_length=100)
    capacity=models.IntegerField(null=True)
class Cargo(models.Model):
    name=models.CharField(max_length=100)
    CargoShip=models.ForeignKey(CargoShip,on_delete=models.CASCADE)
    unit=models.IntegerField(null=True)
