import json
fileName='Tasks.json'

def readJsonData():
    with open(fileName,'r') as f:
        data=json.load(f)
    return data

def writeJsonData(data): 
    with open(fileName,'w') as f:
        json.dump(data,f,indent=2)

def createJson():
    json_data=dict()

    json_data={
        'Tasks':[]
    }
    with open(fileName,'w') as f:
        json.dump(json_data,f)

    
def jsonCheck():
    try:
        jsonData=readJsonData()
    except json.JSONDecodeError:
        createJson()
    except FileNotFoundError:
        createJson()
        print('file is not existing')
