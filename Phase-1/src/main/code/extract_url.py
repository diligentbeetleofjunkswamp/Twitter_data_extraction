import json

file = open("/Users/srividyavaranasi/BD/output.txt", "r")
for line in file:
    jsonStr=json.loads(line)
    entitiesStr=json.dumps(jsonStr['entities'])
    entitiesJsonStrArr=json.loads(entitiesStr)
    for a in entitiesJsonStrArr['urls']:
        htstr=json.loads(json.dumps(a))
        print(htstr['url'])
file.close()
