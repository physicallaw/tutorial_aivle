from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()