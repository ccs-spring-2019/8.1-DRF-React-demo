from django.db import models


class Pizza(models.Model):

    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField('Topping', related_name='pizzas')

    def __str__(self):
        return self.name


class Topping(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
