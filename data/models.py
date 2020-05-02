from datetime import datetime, date

from django.conf import settings
from django.db import models


def getAge(date):
    pass


class Club(models.Model):
    name = models.CharField(max_length=75)
    city = models.CharField(max_length=35)
    pool = models.CharField(max_length=75)
    # coach = refer to a coach class
    # swimmers = +1 everytime swimmer is added to club

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=75)
    # club

    def __str__(self):
        return self.name


class Swimmer(models.Model):
    GENDERS = (
        ('N', 'Select...'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    name = models.CharField(max_length=75)
    birthday = models.DateField(verbose_name="Birthday", null=True)
    age = models.IntegerField(default=0)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, default='')
    gender = models.CharField(
        max_length=2,
        choices=GENDERS,
        default='N'
    )

    @property
    def get_age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return int(age)


    def save(self, *args, **kwargs):
        self.age = self.get_age
        super(Swimmer, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

