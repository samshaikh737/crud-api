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

def sendData(name,age,email,city):
    data = {
        "name":name,
        "age":age,
        "email":email,
        "city":"mumbai"
    }
    jsonData = json.dumps(data)
    r = requests.post(url=url,data=jsonData)
    print(r.json())
sendData("sameer",16,"sameer@gmail.com","mumbai")

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