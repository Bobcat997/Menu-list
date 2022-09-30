from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    dishes = models.ManyToManyField('Dish')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name
