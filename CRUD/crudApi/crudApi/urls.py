from django.contrib import admin
from django.urls import path

#importing function from app1
from app1.views import viewsAlldata,databaseApi,deleteAllData

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",viewsAlldata,name= "home"),
    path("api",databaseApi),
    path("del",deleteAllData)
]
