from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.created_at
