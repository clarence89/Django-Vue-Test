from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Animal(models.Model):
        ANIMAL_CHOICES = (
        ('Bear','Bear'),
        ('Tiger','Tiger'),
        ('Snake','Snake'),
        ('Donkey','Donkey')
    )
        name = models.CharField(
        max_length = 20,
        unique = True,
        choices = ANIMAL_CHOICES,
        )
        def __str__(self):
            return self.name

class CustomUser(AbstractUser):
    COLOUR_CHOICES = (
        ('Blue','Blue'),
        ('Green','Green'),
        ('Red','Red'),
        ('Black','Black'),
        ('Brown','Brown'),
    )
    animals = models.ManyToManyField(Animal,blank=True)
    tiger_type = models.CharField(max_length = 30, blank=True)
    colour = models.CharField(
        max_length = 20,
        choices = COLOUR_CHOICES,
        default = 'Blue'
        )
