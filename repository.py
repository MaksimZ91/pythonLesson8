from pathlib import Path 

def reader(path, options=False): 
  try:  
    with open(path, "r", encoding="utf-8") as file:
      if options:
        payload = file.readlines()  
        return payload 
      payload = file.read()   
    return payload
  except:
    return False  


def writer(payload):
  try:   
    path = Path("outputDataOrMemory", "outputData.txt")  
    with open(path, "a+", encoding="utf-8") as file:
      file.writelines(f'\n')
      for key, value in payload.items():      
        file.writelines(f'{key}:{value} ')
    return True
  except:
    return False   
    

def update(payload):
  try:
    path = Path("outputDataOrMemory", "outputData.txt")  
    with open(path, "w+", encoding="utf-8") as file:       
      file.writelines("%s\n" % line for line in payload)
    return True
  except:
    False   


def export(path, fileName, payload):
  try:     
    with open(f"{path}/{fileName}", "w+", encoding="utf-8") as file:       
      file.writelines("%s\n" % line for line in payload)
    return True
  except: return False      
