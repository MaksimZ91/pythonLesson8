from pathlib import Path 

def reader(folderName, fileName, options=False): 
  with open(folderName + "/" + fileName, "r", encoding="utf-8") as file:
    if options:
      payload = file.readlines()  
      return payload 
    payload = file.read()   
  return payload


def writer(payload):
  try: 
    path = Path("outputDataOrMemory", "outputData.txt")  
    with open(path, "a+", encoding="utf-8") as file:
      file.writelines(f'\n')
      for key, value in payload.items():      
        file.writelines(f'{key}:{value} ')
    return payload 
  except:
    return False   
    

def update(payload):
  try:
    path = Path("outputDataOrMemory", "outputData.txt")  
    with open(path, "w+", encoding="utf-8") as file:       
      file.writelines("%s\n" % line for line in payload)
    return payload
  except:
    False   


def eport(fileName, payload):
  try:
    path = Path("exportFile", fileName)  
    with open(path, "w+", encoding="utf-8") as file:       
      file.writelines("%s\n" % line for line in payload)
    return payload
  except:
    False      
