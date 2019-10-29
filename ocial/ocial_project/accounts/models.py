from django.db import models
from django.contrib.auth.models import User


class Learner(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default= '../static/default.jpg')
    

    def __str__(self):
    	return self.user.username