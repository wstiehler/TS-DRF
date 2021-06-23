from django.db import models


class Product(models.Model):
    name = models.CharField('nome', max_length=20)
    description = models.CharField('description', max_length=200)
    value = models.FloatField('value')


    def validate_filds(self):
        if (self.name != str) and (self.description != str):
            raise ValueError('Type incorrect')
        
        if self.value != float:
            raise ValueError('Type incorrect')
        
