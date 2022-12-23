import repository
import importLogic 
import loger


def createContact(surname,name, patronymic,telephone):  
  try:  
    data = {"surname":surname,"name":name,"patronymic":patronymic,"telephone":telephone}
    loger.log("create", data ) 
    return repository.writer(data) 
  except: return False



def  findAll():  
  path = "outputDataOrMemory/outputData.txt"  
  data =  repository.reader(path)
  payload = assistPrint(data)
  return payload


def updateContact(fio, selected, updateData):
  try:    
    path = "outputDataOrMemory/outputData.txt"  
    data = repository.reader(path) 
    formatData =  assistPrint(data) 
    result = data.split("\n")  
    for i in range(len(formatData)):
      if fio == formatData[i]:
        newContact = fio.split()         
        match selected:
          case "Фамилия":
            newContact[0] = updateData
          case "Имя":
            newContact[1] = updateData
          case "Отчество":
            newContact[2] = updateData
          case "Телефон":
            newContact[3] = updateData  
        result[i] = f"surname:{newContact[0]} name:{newContact[1]} patronymic:{newContact[2]} telephone:{newContact[3]}"
        loger.log("update", result[i] )   
        return repository.update(result)
  except: return  False      



def findeOneContact(fio):   
  path = "outputDataOrMemory/outputData.txt" 
  data = repository.reader(path)     
  result = [i for i in assistPrint(data) if fio in i] 
  loger.log("findeOne", fio)
  return result


def deleteContact(fio):
  try:
    path = "outputDataOrMemory/outputData.txt"  
    data = repository.reader(path)  
    formatData =  assistPrint(data)   
    result = data.split("\n")  
    [result.remove(result[i]) for i,j in enumerate(formatData) if j == fio]
    loger.log("delete", fio )
    return repository.update(result)
  except: return False  



def importContats(filePath, fileName):   
  try:
    data = repository.reader(filePath) 
    match fileName.split(".")[1]:
      case "json":
        return importLogic.importFromJSONandCSV(data)   
      case "xml":
        return importLogic.importFromXML(data)    
      case "csv":  
        return importLogic.importFromJSONandCSV(data,fileName)   
      case "txt":
        return importLogic.importFromTxT(data) 
  except: return False

 

      
def exportContacts(path):
  try:
    fileName = "export.txt"
    pathRead = "outputDataOrMemory/outputData.txt"   
    data = repository.reader(pathRead, True) 
    loger.log("export", data)
    return repository.export(path, fileName, data)
  except: return False




def assistPrint(list):
  data = list.split('\n') 
  result = []
  for contact in data:
        entity = contact.split() 
        tmp = []             
        for i in entity:
          tmp.append(i.split(":")[1])  
        result.append(" ".join(tmp))  
  return result


