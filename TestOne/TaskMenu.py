import json
from jsonHandler import jsonCheck 

def readJsonData():
    with open('Tasks.json') as f:
        data=json.load(f)
    return data
def writeJsonData(data): 
    with open('Tasks.json','w') as f:
        json.dump(data,f,indent=2)



#------------------------------------------------------------------------------
###task must have 'id' 'description' 'status' and date of creaton or updating
### status of the task  can be in 3 states (todo, in-progress, done)
### to conv time in json :item['now']=datetime.now(),strftime(%d/%m/%y')
### if there a ? after some variable or function its meant that it can change later
### must save all tasks in json 

#------------------------------------------------------------------------------
#to save task
def saveChanges():
    pass

#------------------------------------------------------------------------------
#To create task
def addItem(Ids,newId,description,createdAt='',updatedAt='',status='in progress'):
    if Ids.count(str(newId))==1:
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
   

#------------------------------------------------------------------------------
#to update task
#must look like : update 1 "Buy groceries and cook dinner"
#def update(id?,description?)

#------------------------------------------------------------------------------
#must look like: delete 1
#to delete task
#def delete(id?)

#------------------------------------------------------------------------------
# Marking a task as in progress or done
# must look like :mark_in_progress 1
#def mark_in_progress()
# must look like :mark-done 1
#def mark_in_progress()\

#------------------------------------------------------------------------------
#Listing all task
#def lists()

# Listing tasks by status
#lists done
#lists todo
#lists in-progress


def main():
    try:
        readJsonData()
        print('Data scanned')
    except:
        print('Data error')
    else:
        jsonCheck()
    jsonData=readJsonData()
    ids=list()

    for items in jsonData['Tasks']:
        ids.append(items['id'])
    lastId=int(ids[-1])
    print(lastId)

main()

