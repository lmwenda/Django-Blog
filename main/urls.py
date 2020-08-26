from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Create my urls here.

urlpatterns = [
path('', views.index, name='index'),
path('signin/', views.signin, name="signin"),
path('create/', views.create, name="create"),
path('contact/', views.contact, name="contact"),
path('logout/', views.logoutUser, name="logout"),
path('community/', views.community, name="community"),
path('adminblog/', views.AdminsBlog, name="adminblog"),
path('postform/',  views.postform, name="postform"),
path('delete/str:<post_id>/',views.delete_post,name='delete'),

# Reset Password Views
path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
path('password_reset_complete/complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]