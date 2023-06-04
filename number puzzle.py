from tkinter import*
from tkinter import messagebox

def onclick8():
    value=v8.get()
    print(value)

    
    if v9.get()=='':
        v9.set(value)
        v8.set('')
    
    elif v7.get()=='':
        v7.set(value)
        v8.set('')
    elif v5.get()=='':
        v5.set(value)
        v8.set('')
    win1()

def onclick7():
    value=v7.get()
    print(value)       

    if v8.get()=='':
        v8.set(value)
        v7.set('')
    elif v4.get()=='':
        v4.set(value)
        v7.set('')
    win1()
def onclick4():
    value=v4.get()
    print(value)
    if v7.get()=='':
        v7.set(value)
        v4.set('')
    elif v5.get()=='':
        v5.set(value)
        v4.set('')
    elif v1.get()=='':
        v1.set(value)
        v4.set('')
    win1()
    
        
def onclick5():
    value=v5.get()
    print(value)
    if v4.get()=='':
        v4.set(value)
        v5.set('')
    elif v6.get()=='':
        v6.set(value)
        v5.set('')
    elif v2.get()=='':
        v2.set(value)
        v5.set('')
    elif v8.get()=='':
        v8.set(value)
        v5.set('')
    win1() 

def onclick6():
    value=v6.get()
    print(value)
    if v5.get()=='':
        v5.set(value)
        v6.set('')
    elif v9.get()=='':
        v9.set(value)
        v6.set('')
    elif v3.get()=='':
        v3.set(value)
        v6.set('')
    win1()
    
    
    
def onclick9():
    Value=v9.get()
    print(Value)
    if v6.get()=='':
        v6.set(Value)
        v9.set('')
    elif v8.get()=='':
        v8.set(Value)
        v9.set('')
    win1()
    
    
def onclick3():
    value=v3.get()
    print(value)
    if v6.get()=='':
        v6.set(value)
        v3.set('')
    elif v2.get()=='':
        v2.set(value)
        v3.set('')
    win1()
    
    
def onclick2():
    value=v2.get()
    print(value)
    if v1.get()=='':
        v1.set(value)
        v2.set('')
    elif v3.get()=='':
        v3.set(value) 
        v2.set('')
    elif v5.get()=='':
        v5.set(value)
        v2.set('')
    win1()
def onclick1():
    value=v1.get()
    print(value)
    if v2.get()=='':
        v2.set(value)
        v1.set('')
    elif v4.get()=='':
        v4.set(value)
        v1.set('')
   
    win1()

def win1(): 
    if v1.get()=='1'and v2.get()=='2'and v3.get()=='3'and v4.get()=='4'and v5.get()=='5'and v6.get()=='6'and v7.get()=='7'and v8.get()=='8'and v9.get()=='':
        msg=messagebox.showinfo("WINNER BOX","YOU ARE WINNER")   

win=Tk()
win.title("NUMBER PUZZLE")
win.geometry("400x400")

    
    
v1=StringVar()
v1.set('1')
b1=Button(textvariable=v1,padx=40,pady=35,fg="white",bg="black",command=onclick1)
b1.place(x=30,y=25)

v2=StringVar()
v2.set('2')
b2=Button(textvariable=v2,padx=40,pady=35,fg="white",bg="black",command=onclick2)
b2.place(x=150,y=25)

v3=StringVar()
v3.set('3')
b3=Button(textvariable=v3,padx=40,pady=35,fg="white",bg="black",command=onclick3)
b3.place(x=260,y=25)

v4=StringVar()
v4.set('4')
b4=Button(textvariable=v4,padx=40,pady=35,fg="white",bg="black",command=onclick4)
b4.place(x=30,y=130)

v5=StringVar()
v5.set('5')
b5=Button(textvariable=v5,padx=40,pady=35,fg="white",bg="black",command=onclick5)
b5.place(x=150,y=130)

v6=StringVar()
v6.set('6')

b6=Button(textvariable=v6,padx=40,pady=35,fg="white",bg="black",command=onclick6)
b6.place(x=260,y=130)

v7=StringVar()
v7.set('7')

b7=Button(textvariable=v7,padx=40,pady=35,fg="white",bg="black",command=onclick7)
b7.place(x=30,y=240)

v8=StringVar()
v8.set('8')

b8=Button(textvariable=v8,padx=40,pady=35,fg="white",bg="black",command=onclick8)
b8.place(x=150,y=240)

v9=StringVar()
v9.set('')

b9=Button(textvariable=v9,padx=40,pady=35,fg="white",bg="black",command=onclick9)
b9.place(x=260,y=240)





win.mainloop()