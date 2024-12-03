from django.contrib import admin
from django.urls import path
from .views import user_listing,User_Login

urlpatterns = [
    
    path('user/',  user_listing ),
    path('login/', User_Login)

]