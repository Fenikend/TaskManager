import json
from datetime import datetime
from jsonHandler import jsonCheck,readJsonData,writeJsonData




now = datetime.now()
jsonCheck()

jsonData=readJsonData()
ids=list()
for items in jsonData['Tasks']:
    ids.append(items['id'])  
updatedAt=now.strftime("%m/%d/%Y, %H:%M:%S")



def addItem(data,description,createdAt='',status='todo'):
    if len(data)==0:
        newId=0
    else:
        newId=int(data[-1])+1
    if createdAt=='':
        createdAt=updatedAt

    newString={
        'id':f'{str(newId)}',
        'description':f'{description}',
        'createdAt':f'{createdAt}',
        'updatedAt':f'{updatedAt}',
        'status':f'{status}'}
    jsonData['Tasks'].append(newString)

def checker(data):
    oldId=0
    for item in data['Tasks']:
        if int(item['id'])==oldId:
            oldId=oldId+1
        else:
            item['id']=str(oldId)
            oldId=oldId+1

def deleteItem(data,ID):
    for item in data['Tasks']:
        if item['id']==f'{ID}':
            print(item)
            data['Tasks'].remove(item)
            # print(data)
    checker(data)

def updateItem(data,ID,description):
    for item in data['Tasks']: 
        if item['id']==(str(ID)):
            print(ID)
            item['description']=f'{description}'
            item['updatedAt']=f'{updatedAt}'
    print('updated')



def markTask(data,ID,status):
    for item in data['Tasks']:
        if f'{ID}' in ids:
            print('')
        else:
            print('No such id')
            return 0
        if item['id']==(f'{ID}'):
            item['status'] = f'{status}'
            item['updatedAt']=f'{updatedAt}'
        

def listTasks(data,status):
    checkline=''
    if status =='':
        for item in data['Tasks']:
            print (item['id'],' ',item['description'])
        return 1
    
    for item in data['Tasks']:
        if item['status']==status:
            checkline+=item['id']
            print (item['id'],' ',item['description'])
    if checkline=='':
        print('No tasks')

    



