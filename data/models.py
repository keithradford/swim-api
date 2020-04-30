from django.conf import settings
from django.db import models

class Swimmer(models.Model):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    # club = reference to club class

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=75)
    # club

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=75)
    city = models.CharField(max_length=35)
    pool = models.CharField(max_length=75)
    # coach = refer to a coach class
    # swimmers = +1 everytime swimmer is added to club

    def __str__(self):
        return self.name

