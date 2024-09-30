import json
from testjson import jsonCheck 

def readJsonData():
    with open('Tasks.json') as f:
        data=json.load(f)
    return data
def writeJsonData(data): 
    with open('Tasks.json','w') as f:
        json.dump(data,f,indent=2)

jsonData=readJsonData()
ids=list()

    
for items in jsonData['Tasks']:
    ids.append(items['id']) 



def addItem(data,newId,description,createdAt='',updatedAt='',status='in progress'):
    if data.count(str(newId))==1:
       return(ValueError)
    else:
        newString={
            'id':f'{str(newId)}',
            'description':f'{description}',
            'createdAt':f'{createdAt}',
            'updatedAt':f'{updatedAt}',
            'status':f'{status}'
        }
        jsonData['Tasks'].append(newString)
   
def deleteItem(data,ID):
    for item in data['Tasks']:
        if item['id']==f'{ID}':
            print(item)
            data['Tasks'].remove(item)
            # print(data)

def updateItem(ID,description,data):
    for item in data['Tasks']:
        if item['id']==(f'{ID}'):
            item['description']=f'{description}'

def markTask(ID,status):
    for item in data['Tasks']:
        if item['id']==(f'{ID}'):
            item['status'] = f'{status}'
def listTasks(status=''):
    pass

try:
    readJsonData()
    print('Data scanned')
except:
    print('Data error')
else:
    jsonCheck()

# addItem(ids,2,'jija')

deleteItem(jsonData,0)
print(jsonData)

# writeJsonData(jsonData)


