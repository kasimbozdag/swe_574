from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from topics.models import Course


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    version = models.IntegerField(default=1)
