from django.db import models


class Product(models.Model):
    name = models.CharField('nome', max_length=20)
    description = models.CharField('description', max_length=200)
    value = models.FloatField('value')
