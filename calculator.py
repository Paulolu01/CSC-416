from tkinter import *

root = Tk()
root.title("CSC426 Calculator")
root.geometry("300x400")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def clear():
    e.delete(0, END)

def equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

buttons = [
'7','8','9','/',
'4','5','6','*',
'1','2','3','-',
'0','%','=','+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        Button(root,text=button,padx=20,pady=20,command=equal).grid(row=row,column=col)
    else:
        Button(root,text=button,padx=20,pady=20,
               command=lambda b=button: click(b)).grid(row=row,column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

Button(root,text="C",padx=90,pady=20,command=clear).grid(row=6,column=0,columnspan=4)

root.mainloop()