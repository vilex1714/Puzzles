from tkinter import*
from tkinter import messagebox


class demo:


    def __init__(self):

        self.win=Tk()
        self.win.geometry("390x390")
        self.win.resizable(0,0)

        self.b1=Button(self.win,text='B2D',padx=40,pady=35,fg="white",bg="black",command=self.onclick)
        self.b1.place(x=30,y=25)

        self.win.mainloop()

    def onclick(self):

        self.win.destroy()
        self.win1=Tk()
        self.win1.geometry("390x390")
        self.win1.resizable(0,0)

        self.e1=Entry(self.win1)
        self.e1.place(x=50,y=10)

        self.e2=Entry(self.win1)
        self.e2.place(x=50,y=30)

        self.b1=Button(self.win1,text='convert',padx=40,pady=10,fg="white",bg="black",command=self.click)
        self.b1.place(x=30,y=100)

        self.win.mainloop()

    def click(self):

            value=int(self.e1.get())
            a=1
            n=value
            rem=[]
            while n>0:
                r=n%2
                n=n//2
                rem.append(r)
            rem.reverse()
            print(rem) 
            
            self.e2.delete(0,0)
            self.e2.insert(0,rem)
            self.e2.update()
d=demo()



