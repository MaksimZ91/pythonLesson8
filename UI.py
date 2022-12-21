import logic 

def menu():
  mainMenu = ["1.Отобразить все конаткты.","2.Добавить контакт.","3.Найти контакт.","4.Изменить контакт", "5.Удалить контакт.",
              "6 Ипротировать контакты.","7.Эскпортировать контакты.", "0.Выход"]
  for i in mainMenu:
    print(i) 
  print()  
  number = int(input("Введите номер пункта меню: ")) 
  print()   
  return number   


def updateMenu():
  print("Каке данные требуется изменить: ")
  menu =  ["1. Фамилия", "2. Имя", "3.Отчество", "4.Телефон", "5.Главное меню."]
  for i in menu:
      print(i)
  print()  
  number = int(input("Введите номер пункта меню: ")) 
  print()   
  return number 


def findeAllprint(data):
  if not data:
    print("Данных не найденно.Список пуст")
    print()
    return -1
  payload = logic.assistPrint(data) 
  payload.append("Назад в главное меню ")
  print("Список контактов: ")
  [print(f"{i+1} {payload[i]}") for i in range(len(payload))]  
  number = int(input(f"Введите {len(payload)} для перехода в главное меню: ")) 
  print()
  return number


def creatNewContact(data):
  if not data:
    return print("Не удалось сохдать котнакт")  
  print(f"Контакт успешно сохранен.") 
  number = int(input("Введите 0 для перехода в главное меню: ")) 
  print()
  return number


def createContact():
  surname = input("Введите фамилию контакта: ")
  name = input("Введите имя контакта: ")
  patronymic = input("Введите отчество контакта: ")
  telephone = input("Введите номер телефона: ") 
  return [surname, name, patronymic, telephone]   


def importFileName():
  return input("Введите название файла с расширением: ")


def findeContact(data):
  if not data:
    print("Данных не найденно.Список пуст")
    print()
    return -1
  data.append("Назад в главное меню ")  
  [print(f"{i+1} {data[i]}") for i in range(len(data))] 
  number = int(input(f"Введите {len(data)} для перехода в главное меню: ")) 
  print()
  return number 


def updateorDeleteConact(data):
  if not data:
    print("Данных не найденно.Список пуст")
    print()
    return -1
  data.append("Назад в главное меню ")  
  [print(f"{i+1} {data[i]}") for i in range(len(data))] 
  number = int(input(f"Введите номер контакты или {len(data)} для перехода в главное меню : ")) 
  print()
  return number


def deleteContact(data):
  if not data:
    return print("Не удалось удалить котнакт")  
  print(f"Контакт успешно удален.") 
  number = int(input("Введите 0 для перехода в главное меню: ")) 
  print()
  return number


def importContacts(data):
  if not data:
    return print("Не удалось импортировать котнакт")  
  print(f"Контакты успешно импортированы.") 
  number = int(input("Введите 0 для перехода в главное меню: ")) 
  print()
  return number


def exportContact(data):
  if not data:
    return print("Не удалось экспортировать котнакты")  
  print(f"Контакт успешно экспортированы.") 
  number = int(input("Введите 0 для перехода в главное меню: ")) 
  print()
  return number


def printer(data):
  print(data)


def userRequest(data):
  payload = input(f"{data}: ")  
  return payload