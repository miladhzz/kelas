from django.db import models

class City(models.Model):
  title = models.CharField(max_length=50, verbose_name='عنوان شهر')
  lat = models.FloatField(verbose_name='عرض جغرافیایی')
  lon = models.FloatField(verbose_name='طول جغرافیایی')

  def __str__(self):
    return f'{self.title} ({self.lat},{self.lon})'
