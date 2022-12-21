import repository
import controller
import importLogic 
import UI

def createContact():  
  fio = UI.createContact()  
  data = {"surname":fio[0],"name":fio[1],"patronymic":fio[2],"telephone":fio[3]} 
  payload = repository.writer(data) 
  backStep = UI.creatNewContact(payload)
  if backStep == 0 :
    controller.mainMenu()
  return


def  findAll():  
  path = "outputData.txt" 
  folderName = "outputDataOrMemory" 
  data =  repository.reader(folderName,path)
  payload = assistPrint(data)
  return payload
  # backStep = UI.findeAllprint(data) 
  # if backStep == (len(data.split('\n')) + 1) or backStep == -1:
  #   controller.mainMenu()
  # return  


def updateContact(fio):
  path = "outputData.txt" 
  folderName = "outputDataOrMemory" 
  #fio = UI.userRequest("Введите данные для посика: ")
  data = repository.reader(folderName,path) 
  #contacts = [i for i in assistPrint(data) if fio in i]   
  #number = UI.updateorDeleteConact(contacts)
 # if number == -1:
    #controller.mainMenu()
  formatData =  assistPrint(data) 
 # updateNumber = int(UI.updateMenu())
  result = data.split("\n")
  for i in formatData:
    if fio == i:
      newContact = fio.split()   
      print(i) 
      # match updateNumber:
      #   case 1:
      #     newContact[0] = UI.userRequest("Введите Фамилию: ")
      #   case 2:
      #     newContact[1] = UI.userRequest("Введите Имя: ")
      #   case 3:
      #     newContact[2] = UI.userRequest("Введите Отчество: ")
      #   case 4:
      #     newContact[3] = UI.userRequest("Введите Телефон: ")  
        #case 5:
            #controller.mainMenu()   
     # result[i] = f"surname:{newContact[0]} name:{newContact[1]} patronymic:{newContact[2]} telephone:{newContact[3]}"  
      #payload = repository.update(result)
      # backStep = UI.creatNewContact(payload)      
      # if backStep == 0 :
      #   controller.mainMenu()
      # return


def findeOneContact(fio):  
  path = "outputData.txt" 
  folderName = "outputDataOrMemory" 
  #fio = UI.userRequest("Введите данные для посика: ")
  data = repository.reader(folderName,path)     
  result = [i for i in assistPrint(data) if fio in i] 
  return result
  # backStep = UI.findeContact(result)
  # if backStep == (len(result)) or backStep == -1:
  #   controller.mainMenu()
  # return


def deleteContact(fio):
  path = "outputData.txt" 
  folderName = "outputDataOrMemory"
  data = repository.reader(folderName,path)  
  #fio = UI.userRequest("Введите данные для посика (Фамили or Имя): ")
  #contacts = [i for i in assistPrint(data) if fio in i]  
  #number = UI.updateorDeleteConact(contacts)
  formatData =  assistPrint(data)   
  result = data.split("\n")  
  [result.remove(result[i]) for i,j in enumerate(formatData) if j == fio]
  repository.update(result)
  # backStep = UI.deleteContact(payload)      
  # if backStep == 0 :
  #   controller.mainMenu()
  # return


def importContats(): 
  fileName = UI.importFileName()
  data = repository.reader("inputData", fileName)   
  match fileName.split(".")[1]:
    case "json":
      payload = importLogic.importFromJSONandCSV(data)
      backStep = UI.importContacts(payload)
      if backStep == 0 :
        controller.mainMenu()
      return
    case "xml":
      payload = importLogic.importFromXML(data)
      backStep = UI.importContacts(payload)
      if backStep == 0 :
        controller.mainMenu()
      return
    case "csv":  
      payload = importLogic.importFromJSONandCSV(data,fileName)
      backStep = UI.importContacts(payload)
      if backStep == 0 :
        controller.mainMenu()      
      return
    case "txt":
      payload = importLogic.importFromTxT(data) 
      backStep = UI.importContacts(payload)
      if backStep == 0 :
        controller.mainMenu()      
      return

      
def exportContacts():
  path = "outputData.txt" 
  folderName = "outputDataOrMemory"
  data = repository.reader(folderName,path, True)
  fileName = UI.userRequest("Введите название файла в формате .txt для экспорта:")
  payload = repository.eport(fileName, data)
  backStep = UI.exportContact(payload)      
  if backStep == 0 :
    controller.mainMenu()
  return


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


