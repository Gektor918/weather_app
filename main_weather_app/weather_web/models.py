from django.db import models


class WeatherInfo(models.Model):

    city = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.CharField(max_length=50)
    atmosphere_pressure = models.CharField(max_length=50)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city
