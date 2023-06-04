from tkinter import*

class demo:
    def __init__(self):

        self.win=Tk()
        self.win.geometry("300x300")
        self.win.resizable(0,0)
        self.win.title("binary to decimal")
        self.b=Button(self.win,text='B2D',padx=40,pady=35,fg='white',bg='black',command=self.onclick1)
        self.b.place(x=150,y=25)

        self.win.mainloop()

    def onclick1(self):

        self.win.destroy()
        self.win1=Tk()
        self.win1.geometry("390x390")
        self.win1.resizable(0,0)
        
        

        self.e1=Entry(self.win1)
        self.e1.place(x=50,y=10)

        self.e2=Entry(self.win1)
        self.e2.place(x=50,y=30)

        self.b1=Button(self.win1,text='convert',padx=40,pady=10,fg="white",bg="black",command=self.click1)
        self.b1.place(x=30,y=100)

        self.win.mainloop()


    def click1(self):
            value=int(self.e1.get())
            x=value
            rem=0
            sum=0
            y=0
            while x!=0:
                rem=x%10
                sum=int((sum+rem*pow(2,y)))
                x=x//10
                y=y+1
            print(sum)

            self.e2.delete(0,0)
            self.e2.insert(0,sum)
            self.e2.update()

d=demo()
            