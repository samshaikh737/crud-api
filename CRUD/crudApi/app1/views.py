from functools import partial
import io
import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.fields import set_value
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import DatabaseSerializer
from django.views.decorators.csrf import csrf_exempt
#import database
from .models import Database

@csrf_exempt
def databaseApi(request):
    if request.method == "GET":
        #request body
        requestBody = request.body
        #converting into str
        stream = io.BytesIO(requestBody)
        #converting into json
        jsonData = JSONParser().parse(stream)
        #if id is available return id else return None
        id = jsonData.get("id",None)
        if id is not None:
            db  = Database.objects.filter(id = id)
            #db is available
            if db.first() is not None:
                serializer = DatabaseSerializer(db.first())
                return JsonResponse(serializer.data)
        
        db = Database.objects.all()
        serializer = DatabaseSerializer(db,many=True)
        jsonData = JSONRenderer().render(serializer.data)
        return HttpResponse(jsonData,content_type="application/json")

    if request.method == "POST":
        #request body
        requestBody = request.body
        #convert into str
        stream = io.BytesIO(requestBody)
        #convert into json
        jsonData = JSONParser().parse(stream)
        print(jsonData)
        serializer = DatabaseSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg":"data created"})
        jsonData = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonData,content_type="application/json")
    if request.method == "PUT":
        #request body
        requestBody = request.body
        #convert into str
        stream = io.BytesIO(requestBody)
        #convert into json
        jsonData = JSONParser().parse(stream)
        id = jsonData.get("id")
        db = Database.objects.filter(id=id)
        
        if db.exists():
            serializer = DatabaseSerializer(db.first(),data=jsonData,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg":"data is updated"})
            jsonData = JSONRenderer().render(serializer.errors)
            return HttpResponse(jsonData,content_type="application/json")
        else:
            return JsonResponse({"msg":"id not found"})
    if request.method == "DELETE":
        #request body
        requestBody = request.body
        #converting into str
        stream = io.BytesIO(requestBody)
        #converting into json
        jsonData = JSONParser().parse(stream)
        #if id is available return id else return None
        id = jsonData.get("id",None)
        if id is not None:
            db  = Database.objects.filter(id = id)
            #db is available
            if db.first() is not None:
                db.delete()
                return JsonResponse({"msg":"data deleted"})
        return JsonResponse({"msg":"id not found"})
      

def viewsAlldata(request):           
    db = Database.objects.all()
    serializer = DatabaseSerializer(db,many=True)
    jsonData = JSONRenderer().render(serializer.data)
    return HttpResponse(jsonData,content_type="application/json")