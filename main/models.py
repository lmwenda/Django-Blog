from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
	title = models.CharField(max_length=40)
	description = models.CharField(max_length=400)

	def __str__(self):
		return self.title

class AdminsPost(models.Model):
	"""
	Admin's Posts here
	"""
	title = models.CharField(max_length=50)
	admins_info = models.CharField(max_length=500)

	def __str__(self):
		return self.title