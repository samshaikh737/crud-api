from django.contrib import admin
#import models
from .models import Database
#register model into admin
@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ['id',"name","email","age",'city']