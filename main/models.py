from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
	"""
    Non-Admin's Posts here
	"""
	username = models.CharField(max_length=30)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Admins_Post(models.Model):
	"""
	Admin's Posts here
	"""
	title = models.CharField(max_length=50)
	admins_info = models.CharField(max_length=500)

	def __str__(self):
		return self.title