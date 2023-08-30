from django.db import models
from cars.models import Brand


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE,
        related_name='car_brand'
    )
    factory_year = models.IntegerField()
    model_year = models.IntegerField()

    plate = models.CharField(max_length=7, blank=True, null=True)
    value = models.FloatField(max_length=10)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
