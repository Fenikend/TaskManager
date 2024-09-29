import json

def jsonCheck(fileName='Tasks1.json'):
    json_data=dict()

    json_data={
        'Tasks':[]
    }

    with open(fileName,'w') as f:
        json.dump(json_data,f)