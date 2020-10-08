from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model): # Community Blog Post Model
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	blog_date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=40)
	description = models.CharField(max_length=400)

	def __str__(self):
		return self.title

# Comments Model
class Comment(models.Model):
	post = models.ForeignKey(Post, null=True, related_name="comments", on_delete=models.CASCADE)
	host = models.ForeignKey(User, null=True, related_name="authors", on_delete=models.CASCADE)
	current_date = models.DateTimeField(auto_now_add=True)
	body = models.CharField(max_length=100)

	def __str__(self):
		return self.body

# Admins Post Model
class AdminsPost(models.Model):
	"""
	Admin's Posts here
	"""
	title = models.CharField(max_length=50)
	date_posted = models.DateTimeField(auto_now_add=True)
	admins_info = models.TextField(max_length=500)

	def __str__(self):
		return self.title