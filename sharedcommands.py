import json


def getconf(serverid):

    with open("storage.json","r") as storage:
       data = json.load(storage)
    try:
        messagecontent = [data[serverid]["cashier"].replace("!",""), data[serverid]["fee"]]
        print(messagecontent)
        return messagecontent
    except Exception:
        return False


    
                
