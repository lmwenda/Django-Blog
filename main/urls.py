from django.urls import path
from . import views

# Create my urls here.

urlpatterns = [
path('', views.index, name='index'),
path('signin/', views.signin, name="signin"),
path('create/', views.create, name="create"),
path('contact/', views.contact, name="contact"),
path('logout/', views.logoutUser, name="logout"),
path('community/', views.community, name="community"),
path('aboutus/', views.aboutus, name="aboutus"),
path('postform/',  views.postform, name="postform"),
path('delete/<post_id>',views.delete_post,name='delete')
]