from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Login)
class displayUsers(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'added_on']