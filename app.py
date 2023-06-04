from tkinter import*
from PIL import ImageTk,Image

class demo:
    def __init__(self):


            self.root=Tk()

            self.root.title("login form")

            self.root.iconbitmap('app.py')

            self.root.geometry("350x500")

            self.root.configure(background='#0096DC')

            self.img=Image.open('vilex.png')

            self.resized_img=self.img.resize((70,70))

            self.img=ImageTk.PhotoImage(self.resized_img)

            self.img_label=Label(self.root,image=self.img)
            self.img_label.pack(pady=(10,10))

            self.text_Label=Label(self.root,text='Flipkart',fg='white',bg='#0096DC')
            self.text_Label.pack()
            self.text_Label.config(font=('verdana',24))

            self.email_Label=Label(self.root,text="Enter Email",fg='white',bg="#0096DC")
            self.email_Label.pack(pady=(20,5))
            self.email_Label.config(font=('verdana',12))

            self.email_input=Entry(self.root,width=50)
            self.email_input.pack(padx=6,pady=(1,15))


            self.password_Label=Label(self.root,text="Enter Password",fg='white',bg="#0096DC")
            self.password_Label.pack(pady=(20,5))
            self.password_Label.config(font=('verdana',12))

            self.password_input=Entry(self.root,width=50)
            self.password_input.pack(padx=6,pady=(1,15))

            self.login_btn=Button(self.root,text='Login Here',bg='white',fg='black',width=20,height=2,command=self.onclick1)
            self.login_btn.pack(pady=(10,20))
            self.login_btn.config(font=('verdana',10))




            self.root.mainloop()

    def onclick1(self):
          self.root.destroy()
          self.win=Tk()
          self.win.geometry("700x700")
          self.win.resizable(0,0)

          self.win.iconbitmap('app.py')

          self.win.configure(background='#0096DC')

          self.l=Label(self.win,text="Welcome Flipkart")
          self.l.pack(pady=(1,15))
          self.l.config(font=('verdana',14))

          self.l1=Label(self.win,text="Mobile")
          self.l1.pack()
          self.l1.config(font=('verdana',14))
          

          
          
          self.img=Image.open('ll.png')

          self.resized_img=self.img.resize((100,100))

          self.img=ImageTk.PhotoImage(self.resized_img)

          self.img_label=Label(self.win,image=self.img)
          self.img_label.pack(pady=(10,10))
        
          self.b=Button(self.win,text='mobiles',command=self.onclick2)
          self.b.pack()
          self.b.config(font=('verdana',14))

          self.win.mainloop()

    def onclick2(self):
          self.win.destroy()
          self.m=Tk()
          self.m.geometry('650x650')
          self.m.resizable(0,0)
          self.m.configure(background='red')

          self.l1=Label(self.m,text="oppo")
          self.l1.pack()
          self.l1.config(font=('verdana',14))
          

          self.img=Image.open('oppo.png')

          self.resized_img=self.img.resize((100,100))

          self.img=ImageTk.PhotoImage(self.resized_img)

          self.img_label=Label(self.m,image=self.img)
          self.img_label.pack(pady=(10,10))

          self.l2=Label(self.m,text="oppo Reno8 pro 5G(Glazed Black,256)(12 GB Ram )")
          self.l2.pack(padx=15,pady=10)
          self.l2.config(font=('verdana',14))

          self.l3=Label(self.m,text="IN THE BOX:Handset, Charger, USB Data Cable, Sim Ejector Tool, Safety Guide, Quick Guide, Protective Case")
          self.l3.pack(padx=15,pady=10)
          self.l3.config(font=('verdana',14))
      
          self.l4=Label(self.m,text="₹45,999")
          self.l4.pack(padx=15,pady=10)
          self.l4.config(font=('verdana',14))

          self.b=Button(self.m,text="ADD TO CART")
          self.b.place(x=30,y=25)
          self.b.config(font=('verdana',14))

          
          self.b1=Button(self.m,text="BUY NOW")
          self.b1.place(x=70,y=75)
          self.b1.config(font=('verdana',14))
        
          self.m.mainloop()
          
           
      
d=demo()