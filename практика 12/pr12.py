import requests
import json
from tkinter import *
from tkinter import messagebox


def dumping(user_data):
    kluchi=['company','created_at','email','id','name','url']
    filter_data={}
    for i in kluchi:
        filter_data[i] = user_data[i]
    with open('C:/piton progi/практика 12/NEMOVGITREPOZIT.json','w') as file_vvod:
        pretty=json.dump(filter_data, file_vvod, indent=4)
    messagebox.showinfo('удачно','откройте файл NEMOVGITREPOZIT.json')
    vvod.delete(0, END)

def zapros():
    username = vvod.get()   # Имя пользователя github 
    url = f"https://api.github.com/users/{username}"  # url для запроса
    user_data = requests.get(url).json()    # делаем запрос и возвращаем json
    dumping(user_data)

#окно
window = Tk()
window.title('дамп запроса')
window.geometry('300x150')
lbl1 = Label(window, text='введите название репозитория', font=('Arial',15))
lbl1.grid(column=2, row=0, columnspan=3)
but1  = Button(window, text='запрос+дамп', bd=5, font=('Arial',13), fg='red', command=zapros)
but1.grid(column=3, row=2)
#ввод
vvod = Entry(window, font=('Arial',15), width=15)
vvod.grid(row=1, column=2, columnspan=3, stick='we')





