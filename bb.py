from tkinter import*
from PIL import ImageTk,Image

class demo:
    def __init__(self):


            self.root=Tk()

            self.root.title("login form")

            self.root.iconbitmap('bb.py')

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

            self.login_btn=Button(self.root,text='Login Here',bg='white',fg='black',width=20,height=2,command=self.onclick)
            self.login_btn.pack(pady=(10,20))
            self.login_btn.config(font=('verdana',10))




            self.root.mainloop()
    def onclick(self):
           self.root.destroy()
           self.win=Tk()
           self.win.geometry("700x700")
           self.win.resizable(0,0)

           self.win.iconbitmap('app.py')

           self.win.configure(background='yellow')

           self.img=Image.open('iphone.png')

           self.resized_img=self.img.resize((150,130))


           self.img=ImageTk.PhotoImage(self.resized_img)
           

           self.img_label=Label(self.win,image=self.img)
           self.img_label.place(x=30,y=25)

           self.b=Button(self.win,text="Click Here",command=self.onclick1)
           self.b.place(x=190,y=80)
           self.b.config(font=('verdana',14))

           

           self.img1=Image.open('camera.png')

           self.resized_img1=self.img1.resize((150,130))

           self.img1=ImageTk.PhotoImage(self.resized_img1)

           self.img1_label=Label(self.win,image=self.img1)
           self.img1_label.place(x=30,y=200)

           self.b1=Button(self.win,text="Click Here",command=self.onclick4)
           self.b1.place(x=190,y=250)
           self.b1.config(font=('verdana',14))

           self.img2=Image.open('airpods.png')

           self.resized_img2=self.img2.resize((150,130))

           self.img2=ImageTk.PhotoImage(self.resized_img2)

           self.img2_label=Label(self.win,image=self.img2)
           self.img2_label.place(x=30,y=370)

           self.b2=Button(self.win,text="Click Here")
           self.b2.place(x=190,y=405)
           self.b2.config(font=('verdana',14))






           
           self.win.mainloop()

    def onclick1(self):
           self.win.destroy()
           self.m=Tk()
           self.m.geometry('700x650')
           self.m.resizable(0,0)
           self.m.iconbitmap('bb.py')

           self.m.configure(background='pink')

           self.img=Image.open('iphone1.png.png')

           self.resized_img=self.img.resize((150,130))

           self.img=ImageTk.PhotoImage(self.resized_img)

           self.img_label=Label(self.m,image=self.img)
           self.img_label.place(x=30,y=25)
        
           self.img1=Image.open('iphone2.png')

           self.resized_img1=self.img1.resize((130,130))

           self.img1=ImageTk.PhotoImage(self.resized_img1)

           self.img1_label=Label(self.m,image=self.img1)
           self.img1_label.place(x=500,y=70)

           self.l=Label(self.m,text="APPLE iPhone 12 Pro (Blue, 512 GB1)")
           self.l.place(x=190,y=30)
           self.l.config(font=('verdana',14))

           self.l1=Label(self.m,text="Model Number:MGMV3HN/A")
           self.l1.place(x=190,y=65)
           self.l1.config(font=('verdana',14))

           self.l2=Label(self.m,text="Model Name:iPhone 12 Pro")
           self.l2.place(x=190,y=100)
           self.l2.config(font=('verdana',14))

           self.l3=Label(self.m,text="SIM Type:Dual Sim")
           self.l3.place(x=190,y=135)
           self.l3.config(font=('verdana',14))

           self.l4=Label(self.m,text="Price:₹1,06,699")
           self.l4.place(x=20,y=170)
           self.l4.config(font=('verdana',14))


           self.b=Button(self.m,text="ADD TO CART",command=self.onclick2)
           self.b.place(x=190,y=180)
           self.b.config(font=('verdana',14))

          
           self.b1=Button(self.m,text="BUY NOW")
           self.b1.place(x=370,y=180)
           self.b1.config(font=('verdana',14))


           


           self.m.mainloop()

    def onclick2(self):
           self.m.destroy()
           self.v=Tk()
           self.v.geometry('400x400')
           self.v.resizable(0,0)
           self.v.iconbitmap('bb.py')

           self.v.configure(background='green')

           self.text_Label=Label(self.v,text='Welcome Add To Cart')
           self.text_Label.pack(padx=10,pady=5)
           self.text_Label.config(font=('verdana',14))
           self.v.mainloop()

       
    def onclick3(self):
           self.v.destroy()
           self.k=Tk()
           self.k.geometry('400x400')
           self.k.resizable(0,0)
           self.k.iconbitmap('bb.py')

           self.k.configure(background='brown')

           self.text_Label=Label(self.k,text='')
           self.text_Label.pack(padx=10,pady=5)
           self.text_Label.config(font=('verdana',14))
           self.k.mainloop()
       
    def onclick4(self):
           self.win.destroy()
           self.l=Tk()
           self.l.geometry('400x400')
           self.l.resizable(0,0)
           self.l.iconbitmap('bb.py')

           self.img=Image.open('iphone2.png')

           self.resized_img=self.img.resize((130,130))

           self.img1=ImageTk.PhotoImage(self.resized_img)

           self.img1_label=Label(self.m,image=self.img)
           self.img1_label.place(x=500,y=70)

           self.l.configure(background='red')






           self.l.mainloop()
          
           
           
d=demo()