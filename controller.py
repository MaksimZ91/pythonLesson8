import logic 





def finds():
 return logic.findAll()

def findOne(findeData):
 return logic.findeOneContact(findeData)

def createds(dataSurname, dataName, dataPatronymic, dataTelephone):
 return logic.createContact(dataSurname, dataName, dataPatronymic, dataTelephone)

def updated(updateData,selection,updateDataInfo):
 return logic.updateContact(updateData,selection,updateDataInfo)

def remove(deleteData):
 return logic.deleteContact(deleteData)

def imports(path,fileName):
  return logic.importContats(path,fileName)

def exportss(path):
  return logic.exportContacts(path) 