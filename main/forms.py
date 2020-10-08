from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password']

class ContactForm(forms.Form):
	name = forms.CharField(label="Username:", required=True, max_length="100")
	email = forms.EmailField(required=True, label="Email:", max_length="100")
	subject = forms.CharField(label="Subject:", max_length="100", required=True)
	description = forms.CharField(label="Description:", max_length="500", required=True)

class CreatePost(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'description']

class PostComment(ModelForm):
	class Meta:
		model = Comment
		fields = ['body']