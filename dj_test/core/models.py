from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.FloatField()
    current_position = models.CharField(max_length=50)
    timestamp = models.DateTimeField(null=True)
