import json
import xmltodict
import csv
import repository


def importFromJSONandCSV(data, fileName=False): 
    if fileName:
      payload = csvReader(fileName)
    else:
      payload = json.loads(data)
    for i in payload["contacts"]:
        repository.writer(i) 
    return True  


def importFromXML(data):  
  payload = xmltodict.parse(data) 
  for i in payload["root"]["contacts"]:
      repository.writer(i) 
  return True 
  

def importFromTxT(payload):
  data = payload.split("\n")  
  for contact in data:
     entity = contact.split()    
     tmp = {}
     for i in entity:
       a = i.split(":")
       tmp[a[0]] = a[1]         
     repository.writer(tmp)
  return True 

  
def csvReader(fileName):  
  with open("inputData/" + fileName, "r",encoding='UTF-8') as file:
    data = csv.DictReader(file) 
    result = {"contacts":[]}
    for i in data:
      result["contacts"].append(i)
    return result 