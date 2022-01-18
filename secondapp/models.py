from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()