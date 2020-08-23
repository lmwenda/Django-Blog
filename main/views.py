from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Messages import
from django.contrib import messages

# DataBase Imports
from .models import Post

# 404 import
from django.shortcuts import get_object_or_404

#View import
from django.views.generic import ListView, CreateView

# Authentication, login and logout imports
from django.contrib.auth import authenticate, login, logout

# Form imports
from .forms import CreateUserForm, LoginUserForm, ContactForm, CreatePost

# Decorators imports e.g Login Required
from django.contrib.auth.decorators import login_required

# Send Mail imports and settings
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def email(request):

	if request.method == 'POST':
		message = request.POST['message']

		send_mail('Contact Form',
		 message, 
		 settings.EMAIL_HOST_USER,
		 ['xBear@gmail.com'], 
		 fail_silently=False)
	return render(request, 'main/email.html')

def create(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data('username')
			send_mail('Contact Form',
			 message, 
			 settings.EMAIL_HOST_USER,
			 ['xBear@gmail.com'], 
			 fail_silently=False)
			message.success(request, 'Your Account has Successfully been Created.')
		return redirect('/signin')


	form = CreateUserForm()
	context = {'form':form}
	return render(request, "main/create.html", context)

def signin(request):
   
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'Incorrect username or password. Try again.')	

	context = {}
	return render(request, "main/signin.html", context)

def logoutUser(request):
	logout(request)
	return redirect('/signin')

@login_required(login_url="signin")
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']

			recipients = ['xBear@example.com']
			form.save()

			send_mail(name, email, subject, 'Your form has been recorded. Thanks!', recipients)
			return redirect('/')

	form = ContactForm()
	context = {'form':form}
	return render(request, "main/contact.html", context)

@login_required(login_url="signin")
def community(request):
    community_posts = Post.objects.all()
    return render(request, "main/community.html", {'community_posts': community_posts})

def aboutus(request):
	"""
	Gonna Update this to a FAQ later
	"""
	return render(request, "main/aboutus.html")

@login_required(login_url="signin")
def postform(request):
	form = CreatePost()

	if request.method == 'POST':
		form = CreatePost(request.POST)
		if form.is_valid():
		    form.save()
		return redirect('/community')

	context = {'form':form}
	return render(request, "main/createpost.html", context)

def delete_post(request,post_id=None):
    post_to_delete=get_object_or_404(Post, post_id=id)
    post_to_delete.delete()
    return redirect('/community')
