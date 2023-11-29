from tkinter import *
from tkinter import ttk
from tkinter.ttk import Checkbutton
from tkinter import messagebox
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import filedialog


#окно
window = Tk()
window.title('Немов Герман Антонович')
window.geometry('700x450')


#вкладки
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая')
tab_control.add(tab3, text='Третья')
lbl1 = Label(tab1, text='Вкладка 1 Калькулятор')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='Вкладка 2 Чекбоксы')
lbl2.grid(column=0, row=0)
lbl3 = Label(tab3, text='Вкладка 3 Файл')
lbl3.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')


#БАТОНЫ
def info1():
    messagebox.showinfo('внимание','вы выбрали первый вариант')
    chk_state1.set(False)

def info2():
    messagebox.showinfo('внимание','вы выбрали второй вариант')
    chk_state2.set(False)

def info3():
    messagebox.showinfo('внимание','вы выбрали третий вариант')
    chk_state3.set(False)

    
chk_state1 = BooleanVar()
chk_state1.set(False) # задайте проверку состояния чекбокса
chk = Checkbutton(lbl2, text='Первый', var=chk_state1, command=info1)
chk.grid(column=0, row=2, padx=5, pady=5)
chk_state2 = BooleanVar()
chk_state2.set(False) # задайте проверку состояния чекбокса
chk = Checkbutton(lbl2, text='Второй', var=chk_state2, command=info2)
chk.grid(column=1, row=2, padx=5, pady=5)
chk_state3 = BooleanVar()
chk_state3.set(False) # задайте проверку состояния чекбокса
chk = Checkbutton(lbl2, text='Третий', var=chk_state3, command=info3)
chk.grid(column=2, row=2, padx=5, pady=5)

tab2.grid_columnconfigure(1, minsize=60)
tab2.grid_columnconfigure(2, minsize=60)
tab2.grid_columnconfigure(3, minsize=60)
tab2.grid_columnconfigure(4, minsize=60)

tab2.grid_rowconfigure(2, minsize=60)
tab2.grid_rowconfigure(3, minsize=60)
tab2.grid_rowconfigure(4, minsize=60)
tab2.grid_rowconfigure(5, minsize=60)

#калькулятор
def press_key(event):
    if event.char.isdigit():   #char - текст клавиши пк isdigit()- проверка кравиши на цифры
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char =='\r':   #\r - char клавиши энтер узнается через repr() в консоли
        calculate()

window.bind('<Key>', press_key)

def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value)==1:
        value=value[1:]
    calc['state']=NORMAL #возвращение в нормальное состояние ввода перед операциями и вводом
    calc.delete(0, END)
    calc.insert(0,value+digit)
    calc['state']=DISABLED #блокировка ввода ненужных символов

def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value=value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc['state']=NORMAL #возвращение в нормальное состояние ввода перед операциями и вводом
    calc.delete(0, END)
    calc.insert(0,value+operation)
    calc['state']=DISABLED #блокировка ввода ненужных символов

    
def make_digit_button(digit):
    return Button(tab1, text=digit, bd=5, font=('Arial',13), command=lambda : add_digit(digit))


def make_aperation_button(operation):
    return Button(tab1, text=operation, bd=5, font=('Arial',13), fg='red', command=lambda : add_operation(operation))

def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value+value[:-1]
    calc['state']=NORMAL #возвращение в нормальное состояние ввода перед операциями и вводом
    calc.delete(0, END)
    calc['state']=DISABLED #блокировка ввода ненужных символов
    try:          #обработка исключения
        calc['state']=NORMAL #возвращение в нормальное состояние ввода перед операциями и вводом
        calc.insert(0,eval(value)) #eval вычисляет из строчного ввода операции
        calc['state']=DISABLED #блокировка ввода ненужных символов
    except (NameError, SyntaxError):
        messagebox.showinfo('внимание','нужно вводить только цифры! Вы ввели другие символы')
        calc['state']=NORMAL #возвращение в нормальное состояние ввода перед операциями и вводом
        calc.insert(0, 0)
        calc['state']=DISABLED #блокировка ввода ненужных символов
    except ZeroDivisionError:
        messagebox.showinfo('внимание','на ноль делить нельзя')
        calc['state']=NORMAL #возвращение в нормальное состояние ввода перед операциями и вводом
        calc.insert(0, 0)
        calc['state']=DISABLED #блокировка ввода ненужных символов


def clear():
    calc['state']=NORMAL #возвращение в нормальное состояние ввода перед операциями и вводом
    calc.delete(0, END)
    calc.insert(0,'0')
    calc['state']=DISABLED #блокировка ввода ненужных символов
    

def make_calc_button(operation):
    return Button(tab1, text=operation, bd=5, font=('Arial',13), fg='red', command=calculate)

def make_clear_button(operation):
    return Button(tab1, text=operation, bd=5, font=('Arial',13), fg='red', command=clear)


calc = Entry(tab1, justify=RIGHT, font=('Arial',15), width=15) #justify=RIGHT - прижимаем ввод к правой границе
calc.insert(0,'0')
calc['state'] = DISABLED
calc.grid(row=1, column=1, columnspan=4, stick='we')  #columnspan объединяет 4 колонки

make_digit_button('1').grid(row=2, column=1, stick='wens', padx=5, pady=5) #stik кнопка расширяется на весь размер колонки по W E N S направлениям
make_digit_button('2').grid(row=2, column=2, stick='wens', padx=5, pady=5) #padx pady расстояние между кнопками
make_digit_button('3').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=4, column=3, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=5, column=1, stick='wens', padx=5, pady=5)

make_aperation_button('+').grid(row=2, column=4, stick='wens', padx=5, pady=5)
make_aperation_button('-').grid(row=3, column=4, stick='wens', padx=5, pady=5)
make_aperation_button('/').grid(row=4, column=4, stick='wens', padx=5, pady=5)
make_aperation_button('*').grid(row=5, column=4, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=5, column=3, stick='wens', padx=5, pady=5)

make_clear_button('c').grid(row=5, column=2, stick='wens', padx=5, pady=5)

tab1.grid_columnconfigure(1, minsize=60)
tab1.grid_columnconfigure(2, minsize=60)
tab1.grid_columnconfigure(3, minsize=60)
tab1.grid_columnconfigure(4, minsize=60)

tab1.grid_rowconfigure(2, minsize=60)
tab1.grid_rowconfigure(3, minsize=60)
tab1.grid_rowconfigure(4, minsize=60)
tab1.grid_rowconfigure(5, minsize=60)

#работа с текстом
def openfl():
    selectfl=filedialog.askopenfilename(defaultextension='txt')
    if selectfl != '':
        with open(selectfl, 'r') as f:
            text=file.read()
            txtfl.delete('1', END)
            txtfl.insert('1', text)
            file.close()

txtfl = Text(tab3,width=50)
txtfl.grid(row=0, column=1, stick='ns')



scrll=ttk.Scrollbar(tab3, orient=VERTICAL, command=txtfl.yview)
scrll.grid(row=0, column=2, stick='ns')
txtfl['yscrollcommand'] = scrll.set


window.mainloop()
