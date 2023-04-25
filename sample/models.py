from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class NamedCountryList(models.Model):
    name = models.CharField(max_length=255, unique=True)
    countries = CountryField(multiple=True)
