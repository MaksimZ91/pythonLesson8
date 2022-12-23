import json
import xmltodict
import csv
import repository
import loger

def importFromJSONandCSV(data, fileName=False): 
  try:  
    flag = True   
    if fileName:
      payload = csvReader(fileName)
      loger.log("importCSV",payload)
    else:
      payload = json.loads(data)
      loger.log("importJSON",payload)
    for i in payload["contacts"]: 
      if not flag:        
        return False
      flag = repository.writer(i)
    return flag            
  except: return False



def importFromXML(data): 
  try: 
    flag = True
    payload = xmltodict.parse(data) 
    loger.log("importXML",payload)
    for i in payload["root"]["contacts"]:
      if not flag:
        return False
      flag = repository.writer(i) 
    return True 
  except: return False

  

def importFromTxT(payload):
  try:
    flag = True
    data = payload.split("\n")  
    for contact in data:
      entity = contact.split()
      loger.log("importTXT",entity)    
      tmp = {}
      for i in entity:
        a = i.split(":")
        tmp[a[0]] = a[1] 
      if not flag:
        return False 
      flag = repository.writer(tmp)
    return True 
  except: return False

  
def csvReader(fileName):  
  with open("inputData/" + fileName, "r",encoding='UTF-8') as file:
    data = csv.DictReader(file) 
    result = {"contacts":[]}
    for i in data:
      result["contacts"].append(i)
    return result 