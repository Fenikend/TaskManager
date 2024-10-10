import json
from datetime import datetime
from jsonHandler import jsonCheck,readJsonData,writeJsonData



now = datetime.now()
jsonCheck()

jsonData=readJsonData()
ids = [item['id'] for item in jsonData['Tasks']]
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
    return jsonData

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
    checker(data)

def updateItem(data,ID,description):
    for item in data['Tasks']: 
        if item['id']==(str(ID)):
            # print(ID)
            item['description']=f'{description}'
            item['updatedAt']=f'{updatedAt}'
            print('updated')



def markTask(data,ID,status):
    for item in data['Tasks']:
        if item['id']==(f'{ID}'):
            item['status'] = f'{status}'
            item['updatedAt']=f'{updatedAt}'
            return 0
    print('No such id')
    
        
    #writeJsonData(data)

def listTasks(data,status):
    checkline=''
    if status =='':
        for item in data['Tasks']:
            print (item['id'],' '
                   ,item['description'],' ',
                   f'({item['status']})')
        return 1
    
    for item in data['Tasks']:
        if item['status']==status:
            checkline+=item['id']
            print (item['id'],' '
                   ,item['description'],' '
                   ,f'({item['status']})')
    if checkline=='':
        print('No tasks')

    
       


if __name__ == "__main__":
    for item in jsonData['Tasks']:
        print(item['id'])


