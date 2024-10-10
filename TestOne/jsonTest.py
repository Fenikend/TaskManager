import json
from datetime import datetime
from jsonHandler import jsonCheck,readJsonData,writeJsonData



# def readJsonData():
#     with open('Tasks.json','r') as f:
#         data=json.load(f)
#     return data
# def writeJsonData(data): 
#     with open('Tasks.json','w') as f:
#         json.dump(data,f,indent=2)


now = datetime.now()
jsonCheck()

jsonData=readJsonData()
ids = [item['id'] for item in jsonData['Tasks']]
updatedAt=now.strftime("%m/%d/%Y, %H:%M:%S")
# def integrityCheck():
    
#     pass


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
            # print(data)
    checker(data)

def updateItem(data,ID,description):
    for item in data['Tasks']: 
        # print(ID==item['id'])
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

    
       

# addItem(ids,'jija1')
#listTasks(jsonData,'')
# markTask(jsonData,1,'done')
# print(jsonData)
# deleteItem(jsonData,0)
# print(jsonData)
# updateItem(jsonData,1,)
# writeJsonData(jsonData)
if __name__ == "__main__":
    for item in jsonData['Tasks']:
        print(item['id'])


