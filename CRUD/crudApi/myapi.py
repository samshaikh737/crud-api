#package
import requests
import json
#page url
url = "http://localhost:8000/api"

def getData(id):
    data = {}
    if id:
        data = {"id":id}
        json_data = json.dumps(data)
        r = requests.get(url=url,data=json_data)
        print(r.json())
# getData(10)

def sendData():
    data = {
        "name":"sameer",
        "age":14,
        "email":"ali@gmail.com",
        "city":"mumbai"
    }
    jsonData = json.dumps(data)
    r = requests.post(url=url,data=jsonData)
    print(r.json())
# sendData()

def updateData(id):
    data = {
        "id":id,
        "age":16,
        "email":"sameer@gmail.com",
        "city":"mumbai"
    }
    jsonData = json.dumps(data)
    r = requests.put(url=url,data=jsonData)
    print(r.json())

def deleteData(id):
    data = {    
        "id":id
    }
    jsonData = json.dumps(data)
    r = requests.delete(url=url,data=jsonData)
    print(r.json())
# deleteData(8)