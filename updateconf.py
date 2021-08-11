import json

def updatenow(serverID, key, Value):
    
    with open("storage.json","r") as storage:
        data = json.load(storage)
    if str(serverID) in data:
        if key == "fee":
            try:
                Value = int(Value)
                if Value < 100 and Value >= 0:
                        data[str(serverID)][key] = Value
                else: 
                    return False
            except Exception:
                return False
        else:
            data[str(serverID)][key] = Value
        with open("storage.json","w") as storage:
            json.dump(data,storage,indent=4)
        return True

    else:

        data[serverID] = {    "cashier": "null",    "fee": 0}
        if key == "fee":
            try:
                data[serverID][key] = int(Value)
            except Exception:
                return False
        else:
            data[serverID][key] = Value
        with open("storage.json",'w') as storage: 
            json.dump(data, storage, indent=4)
        return True

#update(800587873623212032,"fee","9")