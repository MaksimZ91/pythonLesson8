from tkinter import *
import logic

def finde():
  findeData = findeEntry.get()
  data = logic.findeOneContact(findeData)
  listBox.delete(0,END)
  [listBox.insert(0,i) for i in data]    
  return data

def delete():
  data = listBox.curselection()
  deleteData = listBox.get(data[0])
  logic.deleteContact(deleteData)
  data = logic.findAll()
  text.delete(1.0, 'end')
  listBox.delete(0,END)
  [text.insert("end", f"{i}\n") for i in data]



root = Tk()

root.geometry("800x400")
text = Text(width=40, height=20)

findeEntry = Entry(root)
findeEntry.place(x=275, y=20, width=230, height=20)
listBox = Listbox()
listBox.place(x=30, y=60, width=250, height=80)

findeButton = Button(root, text="Найти", command=finde).place(x=530, y=20)
deleteButton = Button(root, text="Удалить", command=delete).place(x=630, y=20)

data = logic.findAll()

[text.insert("end", f"{i}\n") for i in data] 
text.place(x=475, y=60, width=300, height=300)

root.mainloop()



