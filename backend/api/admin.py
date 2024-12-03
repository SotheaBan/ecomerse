from django.contrib import admin
from .models import User_core
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')


admin.site.register(User_core,UserAdmin)