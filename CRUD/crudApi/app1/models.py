from django.db import models

class Database(models.Model):
    name = models.CharField(max_length=50,blank=False)
    age = models.IntegerField()
    email = models.EmailField(blank=False)
    city = models.CharField(max_length=50,blank=True)