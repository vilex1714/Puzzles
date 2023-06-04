from tkinter import*


def d2b(self):


    a=1
    n=a
    rem=[]
    while n>0:
        r=n%2
        n=n//2
        rem.append(r)
    rem.reverse()
    print(rem) 
    text=b.cget('text')
    print(text)


def click(self):
            v=Tk()
            v.geometry('300x300')
            v.resizable(0,0)
            f=Frame(v)
            f.pack()

            b=Button(f,text="DECIMAL")
            b.pack(side=LEFT)


            e=Entry(f)
            e.pack(side=LEFT)

            f1=Frame(v)
            f1.pack()

            b1=Button(f1,text="BINARY")
            b1.pack(side=LEFT)

            e1=Entry(f1)
            e1.pack(side=LEFT)

            f2=Frame(v)
            f2.pack() 

            b=Button(   f2,text="CONVERT")
            b.pack()
            b.bind('<Button-1>',d2b)
        
        


   
def click1(event):
    k=Tk()
    k.geometry('300x300')
    k.resizable(0,0)
    f=Frame(k)
    f.pack()

    b=Button(f,text="BINARY")
    b.pack(side=LEFT)
    e=Entry(f,text=" ")
    e.pack(side=LEFT)

    f1=Frame(k)
    f1.pack()
    b1=Button(f1,text="DECIMAL")
    b1.pack(side=LEFT)
    e1=Entry(f1,text="")
    e1.pack(side=LEFT)  

    f2=Frame(k)
    f2.pack() 

    b2=Button(f2,text="CONVERT")
    b2.pack()

 
def click2(event):
    s=Tk()
    s.geometry('300x300')
    s.resizable(0,0)
    f=Frame(s)
    f.pack()

    b=Button(f,text="BINARY")
    b.pack(side=LEFT)
    e=Entry(f,text=" ")
    e.pack(side=LEFT)

    f1=Frame(s)
    f1.pack()
    b1=Button(f1,text="HEXA")
    b1.pack(side=LEFT)
    e1=Entry(f1,text="")
    e1.pack(side=LEFT)

    f2=Frame(s)
    f2.pack() 

    b2=Button(f2,text="CONVERT")
    b2.pack()

def click3(event):
    c=Tk()
    c.geometry('300x300')
    c.resizable(0,0)
    f=Frame(c)
    f.pack()

    b=Button(f,text="HEXA")
    b.pack(side=LEFT)
    e=Entry(f,text=" ")
    e.pack(side=LEFT)

    f1=Frame(c)
    f1.pack()
    b1=Button(f1,text="DECIMAL")
    b1.pack(side=LEFT)
    e1=Entry(f1,text="")
    e1.pack(side=LEFT)

    f2=Frame(c)
    f2.pack() 

    b2=Button(f2,text="CONVERT")
    b2.pack()

def click4(event):
    r=Tk()
    r.geometry('300x300')
    r.resizable(0,0)
    f=Frame(r)
    f.pack()

    b=Button(f,text="DECIMAL")
    b.pack(side=LEFT)
    e=Entry(f,text=" ")
    e.pack(side=LEFT)

    f1=Frame(r)
    f1.pack()
    b1=Button(f1,text="HEXA")
    b1.pack(side=LEFT)
    e1=Entry(f1,text="")
    e1.pack(side=LEFT)

    f2=Frame(r)
    f2.pack() 

    b2=Button(f2,text="CONVERT")
    b2.pack()
def click5(event):
    l=Tk()
    l.geometry('300x300')
    l.resizable(0,0)
    f=Frame(l)
    f.pack()

    b=Button(f,text="DECIMAL")
    b.pack(side=LEFT)
    e=Entry(f,text=" ")
    e.pack(side=LEFT)

    f1=Frame(l)
    f1.pack()
    b1=Button(f1,text="OCATUL")
    b1.pack(side=LEFT)
    e1=Entry(f1,text="")
    e1.pack(side=LEFT)

    f2=Frame(l)
    f2.pack() 

    b2=Button(f2,text="CONVERT")
    b2.pack()

def click6(event):
    o=Tk()
    o.geometry('300x300')
    o.resizable(0,0)
    f=Frame(o)
    f.pack()

    b=Button(f,text="OCATUL")
    b.pack(side=LEFT)
    e=Entry(f,text=" ")
    e.pack(side=LEFT)

    f1=Frame(o)
    f1.pack()
    b1=Button(f1,text="DECIMAL")
    b1.pack(side=LEFT)
    e1=Entry(f1,text="")
    e1.pack(side=LEFT)

    f2=Frame(o)
    f2.pack() 

    b2=Button(f2,text="CONVERT")
    b2.pack()


m=Tk()
m.geometry("500x500")
m.resizable(0,0)
m.title("CONVETER")

f=Frame(m)
f.pack()

tilteLabel=Label(f,text='CONVETER',font=('Algerian',20))
tilteLabel.pack(padx=10,pady=5)

b=Button(f,text="BINARY TO DECIMAL",font=('AlGERIAN',10),width=15,height=10)
b.pack(side=LEFT,padx=10,pady=5)
b.bind('<Button-1>',click1)


b1=Button(f,text="DECIMAL TO BINARY",font=('AlGERIAN',10),width=15,height=10)
b1.pack(side=LEFT,padx=10,pady=5)
b1.bind('<Button-1>',click)

b2=Button(f,text="BINARY TO HEXA",font=('AlGERIAN',10),width=15,height=10)
b2.pack(side=LEFT,padx=10,pady=5)
b2.bind('<Button-1>',click2)

f1=Frame(m)
f1.pack()

b3=Button(f1,text="HEXA TO DECIMAL",font=('AlGERIAN',10),width=15,height=10)
b3.pack(side=LEFT,padx=10,pady=5)
b3.bind('<Button-1>',click3)



b4=Button(f1,text="DECIMAL TO HEXA",font=('AlGERIAN',10),width=15,height=10)
b4.pack(side=LEFT,padx=10,pady=5)
b4.bind('<Button-1>',click4)


b5=Button(f1,text="DECIMAL TO OCATUL",font=('AlGERIAN',10),width=15,height=10)
b5.pack(side=LEFT,padx=10,pady=5)
b5.bind('<Button-1>',click5)


f2=Frame(m)
f2.pack()

b6=Button(f2,text="OCATUL TO DECIMAL",font=('AlGERIAN',10),width=15,height=10)
b6.pack(side=LEFT,padx=10,pady=5)
b6.bind('<Button-1>',click6)









m.mainloop()