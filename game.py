from tkinter import*
from tkinter import messagebox
turn="X"
turn="o"
def play(event):
    global turn
    button=event.widget
    if turn=="X":
        button['text']="X"
        turn="O"
    else:
        button["text"]="O"
        turn="X"

def win():
    
    msg=messagebox.showinfo("WINNER BOX","YOU ARE WINNER")


M=Tk()
M.geometry("500x500")
M.resizable(0,0)
M.title("TIC TAC TOE")

f=Frame(M)
f.pack()
titleLabel=Label(f,text="TIC TAC TOE",font=('Arial',30))
titleLabel.pack()

f1=Frame(M)
f1.pack()

b1=Button(f1,text=' ',width=10,height=5,padx=20,pady=15)
b1.grid(row=0,column=0,padx=10,pady=5)
b1.bind("<Button-1>",play)

b2=Button(f1,text=' ',width=10,height=5,padx=20,pady=15)
b2.grid(row=0,column=1,padx=10,pady=5)
b2.bind("<Button-1>",play)


b3=Button(f1,text=' ',width=10,height=5,padx=20,pady=15)
b3.grid(row=0,column=2,padx=10,pady=5)
b3.bind("<Button-1>",play)

f2=Frame(M)
f2.pack()

b4=Button(f2,text=' ',width=10,height=5,padx=20,pady=15)
b4.grid(row=2,column=0,padx=10,pady=5)
b4.bind("<Button-1>",play)


b5=Button(f2,text=' ',width=10,height=5,padx=20,pady=15)
b5.grid(row=2,column=1,padx=10,pady=5)
b5.bind("<Button-1>",play)


b6=Button(f2,text=' ',width=10,height=5,padx=20,pady=15)
b6.grid(row=2,column=2,padx=10,pady=5)
b6.bind("<Button-1>",play)

f3=Frame(M)
f3.pack()

b7=Button(f3,text=' ',width=10,height=5,padx=20,pady=15)
b7.grid(row=3,column=0,padx=10,pady=5)
b7.bind("<Button-1>",play)

b8=Button(f3,text=' ',width=10,height=5,padx=20,pady=15)
b8.grid(row=3,column=1,padx=10,pady=5)
b8.bind("<Button-1>",play)

b9=Button(f3,text=' ',width=10,height=5,padx=20,pady=15)
b9.grid(row=3,column=2,padx=10,pady=5)
b9.bind("<Button-1>",play)


M.mainloop()