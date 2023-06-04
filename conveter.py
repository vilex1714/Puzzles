from tkinter import*
from tkinter import messagebox


class demo:


    def __init__(self):

        self.win=Tk()
        self.win.geometry("390x390")
        self.win.resizable(0,0)

        self.b1=Button(self.win,text='D2B',padx=40,pady=35,fg="white",bg="black",command=self.onclick)
        self.b1.place(x=30,y=25)

        self.b2=Button(self.win,text='B2D',padx=40,pady=35,fg='white',bg='black',command=self.onclick1)
        self.b2.place(x=150,y=25)

        self.b3=Button(self.win,text='B2H',padx=40,pady=35,fg='white',bg='black',command=self.onclick2)
        self.b3.place(x=270,y=25)

        
        self.b4=Button(self.win,text='H2D',padx=40,pady=35,fg='white',bg='black',command=self.onclick3)
        self.b4.place(x=30,y=130)

        self.b5=Button(self.win,text='D2H',padx=40,pady=35,fg='white',bg='black',command=self.onclick5)
        self.b5.place(x=150,y=130)
        
        self.b6=Button(self.win,text='D2O',padx=40,pady=35,fg='white',bg='black',command=self.onclick6)
        self.b6.place(x=270,y=130)
        
        self.b7=Button(self.win,text='O2D',padx=40,pady=35,fg='white',bg='black',command=self.onclick7)
        self.b7.place(x=30,y=240)
        





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

    def onclick2(self):
        self.win.destroy()
        self.win1=Tk()
        self.win1.geometry("390x390")
        self.win1.resizable(0,0)

        self.e1=Entry(self.win1)
        self.e1.place(x=50,y=10)

        self.e2=Entry(self.win1)
        self.e2.place(x=50,y=30)

        self.b1=Button(self.win1,text='convert',padx=40,pady=10,fg="white",bg="black",command=self.click2)
        self.b1.place(x=30,y=100)

        self.win1.mainloop()

    def onclick3(self):

        self.win.destroy()
        self.win1=Tk()
        self.win1.geometry("390x390")
        self.win1.resizable(0,0)

        self.e1=Entry(self.win1)
        self.e1.place(x=50,y=10)

        self.e2=Entry(self.win1)
        self.e2.place(x=50,y=30)

        self.b1=Button(self.win1,text='convert',padx=40,pady=10,fg="white",bg="black",command=self.click3)
        self.b1.place(x=30,y=100)

        self.win1.mainloop()

    def onclick4(self):

        self.win.destroy()
        self.win1=Tk()
        self.win1.geometry("390x390")
        self.win1.resizable(0,0)

        self.e1=Entry(self.win1)
        self.e1.place(x=50,y=10)

        self.e2=Entry(self.win1)
        self.e2.place(x=50,y=30)

        self.b1=Button(self.win1,text='convert',padx=40,pady=10,fg="white",bg="black",command=self.click4)
        self.b1.place(x=30,y=100)

        self.win1.mainloop()

    def onclick5(self):
        
        self.win.destroy()
        self.win1=Tk()
        self.win1.geometry("390x390")
        self.win1.resizable(0,0)

        self.e1=Entry(self.win1)
        self.e1.place(x=50,y=10)

        self.e2=Entry(self.win1)
        self.e2.place(x=50,y=30)

        self.b1=Button(self.win1,text='convert',padx=40,pady=10,fg="white",bg="black",command=self.click5)
        self.b1.place(x=30,y=100)

        self.win1.mainloop()

    def onclick6(self):
        
        self.win.destroy()
        self.win1=Tk()
        self.win1.geometry("390x390")
        self.win1.resizable(0,0)

        self.e1=Entry(self.win1)
        self.e1.place(x=50,y=10)

        self.e2=Entry(self.win1)
        self.e2.place(x=50,y=30)

        self.b1=Button(self.win1,text='convert',padx=40,pady=10,fg="white",bg="black",command=self.click6)
        self.b1.place(x=30,y=100)

        self.win1.mainloop()

    def onclick7(self):
        
        self.win.destroy()
        self.win1=Tk()
        self.win1.geometry("390x390")
        self.win1.resizable(0,0)

        self.e1=Entry(self.win1)
        self.e1.place(x=50,y=10)

        self.e2=Entry(self.win1)
        self.e2.place(x=50,y=30)

        self.b1=Button(self.win1,text='convert',padx=40,pady=10,fg="white",bg="black",command=self.click7)
        self.b1.place(x=30,y=100)

        self.win1.mainloop()

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

    def click2(self):
        value=int(self.e1.get())
        x=value
        rem=0
        sum=0
        y=0
        while x!=0:
            rem=x%10
            sum=int(sum+rem*pow(2,y))
            x=x//10
            y=y+1
        list=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E']
        while sum>0:
            rem=sum%16
            hex=list[rem]+hex
            sum=sum/16
            print(hex)


        self.e2.delete(0,0)
        self.e2.insert(0,hex)
        self.e2.update()
        
    def click3(self):
        self.e2.delete(0,0)
        self.e2.insert(0)
        self.e2.update()
    def click4(self):
        
        self.e2.delete(0,0)
        self.e2.insert(0)
        self.e2.update()
    def click5(self):
        
        self.e2.delete(0,0)
        self.e2.insert(0)
        self.e2.update()

    def click6(self):
        
        self.e2.delete(0,0)
        self.e2.insert(0)
        self.e2.update()

    def click7(self):
        
        self.e2.delete(0,0)
        self.e2.insert(0)
        self.e2.update()

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

