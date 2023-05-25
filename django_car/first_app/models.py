from django.db import models


class Car(models.Model):
    stamp = models.CharField(max_length=80)
    release = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.stamp} - {self.release} - {self.color} - {self.mileage} - {self.price}"
