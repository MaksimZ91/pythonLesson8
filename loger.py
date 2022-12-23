from datetime import datetime

def log(comand, data):
    curentDate = datetime.now() 
    with open("log/loger.txt", "a+",  encoding="utf-8") as file:
      file.writelines(f'\n')  
      file.writelines(f'время: {curentDate}, дествие: {comand}, данные:{data}\n')