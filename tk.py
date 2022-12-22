from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd 
from tkinter import messagebox as mb
import logic

def finde():
  findeData = findeEntry.get()
  data = logic.findeOneContact(findeData)
  if not data:
    mb.showinfo("Информация","Данных по вашему запросу не найденно!") 
  listBox.delete(0,END)
  [listBox.insert(0,i) for i in data]    
  return data

def delete():
  try:
    data = listBox.curselection()
    deleteData = listBox.get(data[0])
    flag = logic.deleteContact(deleteData)
    if not flag:
      mb.showerror("Ошибка", "Не удалось удалить контакт, при удаление произошла ошибка.")   
    listBox.delete(0,END)
    updateContactList()    
    return mb.showinfo("Информация"," Контакт успешко удален!") 
  except:
      mb.showinfo("Внимание","Не выбран контакт!") 


def update():
    try:
      data = listBox.curselection()
      updateData = listBox.get(data[0])
      selection = combobox.get() 
      updateDataInfo = updateEntry.get() 
      if not updateDataInfo:
        return mb.showinfo("Внимание","Заполните поле с изменениями и выберите контакт из списка!") 
      flag = logic.updateContact(updateData,selection,updateDataInfo)
      if not flag:
        mb.showerror("Ошибка", "Не удалось обновить контакт, при обновление произошла ошибка.")    
      listBox.delete(0,END)
      updateContactList()      
      return mb.showinfo("Внимание", "Контакт изменен!")
    except:
      mb.showinfo("Внимание","Заполните поле с изменениями и выберите контакт из списка!") 




def created():
  try:
      dataSurname = surnameEntry.get()
      dataName = nameEntry.get()
      dataPatronymic = patronymicEntry.get()
      dataTelephone = telephoneEntry.get()
      if not dataName or not dataPatronymic or not dataSurname or not dataTelephone:
        return mb.showinfo("Внимание", "Не заполнено одно из полей фамилия/имя/отчество/телефон!")
      flag = logic.createContact(dataSurname, dataName, dataPatronymic, dataTelephone)
      if not flag:
        mb.showerror("Ошибка", "Не удалось создать контакт, при создании произошла ошибка.")
      updateContactList()
      return mb.showinfo("Внимание", "Контакт создан!")
  except:
      mb.showerror("Ошибка", "Не удалось создать контакт, при создании произошла ошибка.")

      
def openFileFromImport():
  importEntry.delete(0, END)
  fileName = fd.askopenfilename()   
  importEntry.insert(0, fileName)

def openFileFromExport():
  exportEntry.delete(0, END)
  fileName = fd.askdirectory()   
  exportEntry.insert(0, fileName)  

def importFile():
  try:
    path = importEntry.get()
    fileName = path.split("/") 
    if not path:
      return mb.showinfo("Внимание", "Не выбран путь к файлу!")
    flag = logic.importContats(path,fileName[len(fileName)-1]) 
    if not flag:
        mb.showerror("Ошибка", "Не удалось импортировать контакты, при импортировании произошла ошибка.")
    updateContactList()
    return mb.showinfo("Внимание", "Контакты успешно импортированы!")
  except:    
      mb.showerror("Ошибка", "Не удалось импортировать контакты, при импортировании произошла ошибка.")


def exportFile():
  try:
    path = exportEntry.get()
    if not path:
      return mb.showinfo("Внимание", "Не выбран путь к файлу!")
    flag = logic.exportContacts(path)
    if not flag:
      mb.showerror("Ошибка", "Не удалось экспортировать контакты, при экспортировании произошла ошибка.")
    return mb.showinfo("Внимание", "Контакты успешно экспортированы!")  
  except:
    mb.showerror("Ошибка", "Не удалось экспортировать контакты, при экспортировании произошла ошибка.")

def updateContactList():
  try:
    data = logic.findAll()
    text.delete(1.0, 'end')
    [text.insert("end", f"{i}\n") for i in data]
  except:
    mb.showerror("Ошибка", "При получении списка контактов произошла ошибка.")




root = Tk()

root.geometry("800x500")
root.resizable(width=False, height=False)
root.title("Список контактов")
data = logic.findAll()
textLabel = Label(text="Список контактов").place(x=570, y=30)
text = Text(width=40, height=20)
text.place(x=475, y=60, width=300, height=400)
[text.insert("end", f"{i}\n") for i in data] 

findeEntry = Entry(root)
findeLabel = Label(text="Поиск по ФИО").place(x=80, y=30)
findeEntry.place(x=30, y=60, width=180, height=20)
findeButton = Button(root, text="Найти", command=finde).place(x=220, y=57)

listBox = Listbox()
listBox.place(x=30, y=120, width=305, height=80)
listBoxLabel = Label(text="Выберите контакт из списка для изменения/удаления").place(x=30, y=90)
deleteButton = Button(root, text="Удалить", command=delete).place(x=280, y=57)

updateInfo = ["Фамилия", "Имя", "Отчество", "Телефон"]
combobox = ttk.Combobox(value=updateInfo)	
combobox.current(0)
comboboxLabel = Label(text="Выберите что бы вы хотели изменить").place(x=40, y=210)
combobox.place(x=30, y=240, width=100)
updateEntry = Entry(root)

updateEntry.place(x=150, y=240, width=100, height=20)
updateButton = Button(root, text="Изменить", command=update).place(x=270, y=237, height=24)

surnameEntry = Entry(root)
newContactLabel = Label(text="Добавление нового контакта").place(x=330, y=5)
surnameLabel = Label(text="Фамилия").place(x=380, y=30)
surnameEntry.place(x=355, y=60, width=100, height=20)
nameEntry = Entry(root)
nameLabel = Label(text="Имя").place(x=390, y=90)
nameEntry.place(x=355, y=120, width=100, height=20)
patronymicEntry = Entry(root)
patronymicLabel = Label(text="Отчество").place(x=380, y=150)
patronymicEntry.place(x=355, y=180, width=100, height=20)
telephoneEntry = Entry(root)
telephoneLabel = Label(text="Отчество").place(x=380, y=210)
telephoneEntry.place(x=355, y=240, width=100, height=20)
createdButtn = Button(root, text="Создать", command=created).place(x=375, y=280)

importEntry = Entry(root)
importEntry.place(x=30, y=300, width=300, height=20)
importLabel = Label(text="Выберите файл для импорта").place(x=90, y=270)
selectFileButtn = Button(root, text="Выбрать файл",command=openFileFromImport).place(x=50, y=330)
importButtn = Button(root, text="Импортировать", command=importFile).place(x=190, y=330)

exportEntry = Entry(root)
exportLabel = Label(text="Выберите файл для экспорта").place(x=90, y=360)
exportEntry.place(x=30, y=390, width=300, height=20)
selectFileButtn = Button(root, text="Выбрать путь",command=openFileFromExport).place(x=50, y=420)
exportButtn = Button(root, text="Эскпортировать", command=exportFile).place(x=190, y=420)

root.mainloop()



