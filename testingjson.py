import json


with open("storage.json","r") as storage:
    data = json.load(storage)


print(data["serverID"][0]["fee"])

data["serverID"][0]["fee"] = 1

with open("storage.json","w") as storage:
    json.dump(data,storage,indent=4)