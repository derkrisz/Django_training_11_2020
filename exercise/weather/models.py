from django.db import models

# Create your models here.


class Weather(models.Model):
    city = models.CharField(max_length=80, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=260, blank=True, null=True)
    temperature = models.FloatField(default=20.0)

    def __str__(self):
        return f'{self.city} {self.description} {self.temperature}'