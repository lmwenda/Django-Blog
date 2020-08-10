from django.contrib import admin
from django.urls import path, include
from register import views 

# Create your urls here.

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register, name="register"),  # <-- added
    path('', include("main.urls")),
]