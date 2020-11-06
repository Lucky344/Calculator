from tkinter import *

root = Tk()
root.title("Calc")

e = Entry(root, width=40, bg='black', fg='white')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#def function and button

def my_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def my_clear():
    e.delete(0, END)

def my_add():
    first_number = e.get()
    global f_num
    global  math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def my_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)

def my_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def my_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)

def my_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
       e.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
         e.insert(0, f_num - int(second_number))
    elif math == 'multiplication':
         e.insert(0, f_num * int(second_number))
    elif math == 'division':
         e.insert(0, f_num / int(second_number))
    else :
         print("ERROR")

button_1 = Button(root, text='1', fg='red', bg='#dcdcdc', padx=40, pady=20, command=lambda: my_click(1))
button_2 = Button(root, text='2', fg='red', bg='#e8e8e8', padx=40, pady=20, command=lambda: my_click(2))
button_3 = Button(root, text='3', fg='red', bg='#dcdcdc', padx=40, pady=20, command=lambda: my_click(3))
button_4 = Button(root, text='4', fg='red', bg='#e8e8e8', padx=40, pady=20, command=lambda: my_click(4))
button_5 = Button(root, text='5', fg='red', bg='#dcdcdc', padx=40, pady=20, command=lambda: my_click(5))
button_6 = Button(root, text='6', fg='red', bg='#e8e8e8', padx=40, pady=20, command=lambda: my_click(6))
button_7 = Button(root, text='7', fg='red', bg='#dcdcdc', padx=40, pady=20, command=lambda: my_click(7))
button_8 = Button(root, text='8', fg='red', bg='#e8e8e8', padx=40, pady=20, command=lambda: my_click(8))
button_9 = Button(root, text='9', fg='red', bg='#dcdcdc', padx=40, pady=20, command=lambda: my_click(9))
button_0 = Button(root, text='0', fg='red', bg='#e8e8e8', padx=40, pady=20, command=lambda: my_click(0))
button_add = Button(root, text='+', fg='red', bg='#dcdcdc', padx=39, pady=20, command=lambda: my_add())
button_multiply = Button(root, text='*', fg='red', bg='#e8e8e8', padx=40, pady=20, command=lambda: my_multiply())
button_divide = Button(root, text='/', fg='red', bg='#dcdcdc', padx=40, pady=20, command=lambda: my_divide())
button_subtract = Button(root, text='-', fg='red', bg='#e8e8e8', padx=40, pady=20, command=lambda: my_subtract())
button_equal = Button(root, text='=', fg='red', bg='#c4c4c4', padx=135, pady=20, command=lambda: my_equal())
button_clear = Button(root, text='clear', fg='red', bg='#dcdcdc', padx=30.4, pady=20, command=lambda: my_clear())

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1,)
button_subtract.grid(row =4, column=2,)
button_multiply.grid(row=5, column=1,)
button_divide.grid(row=5, column=2,)
button_equal.grid(row=6, column=0, columnspan=3)
button_clear.grid(row=5, column=0,)

root.mainloop()
