import requests
import json
BASE_URL=' http://127.0.0.1:8000/'
ENDPOINT='api/'


# def get_res(id):
#     response=requests.get(BASE_URL+ENDPOINT+id+'/')
#     print(response.status_code)
#     print(response.json())
#
# #id=input('enter some id:')
# #get_res(id)
# def get_all():
#     response=requests.get(BASE_URL+ENDPOINT)
#     print(response.status_code)
#     print(response.json())

def create_resource():
    new_emp={
    'eno':900,
    'ename':'lonewolf',
    'esal':8000,
    'eaddr':'chennai',
    }
    response=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(response.status_code)
    print(response.json())
#create_resource()

def update_resource(id):
    new_emp={
    'id':id,
    'esal':7050,
    'eaddr':'pune',
    }
    response=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(response.status_code)
    print(response.json())
#update_resource(4)


def delete_resource(id):
    data={}
    if id is not None:
        data={
        'id':id
        }
    response=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))

    print(response.status_code)
    print(response.json())
#delete_resource(4)

def get_resource(id=None):
    data={}
    if id is not None:
        data={
        'id':id
        }
    response=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(response.json())
# get_resource(5)
