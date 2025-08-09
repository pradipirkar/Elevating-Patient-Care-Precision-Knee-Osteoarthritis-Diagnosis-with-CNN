from tkinter import *
from tkinter.ttk import *
from time import strftime
import tkinter as tk
from PIL import Image,ImageTk



root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
#root.title("hello")

image2=Image.open("Images/knee-pain.webp")
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)

label=tk.Label(root,text="",font=("Calibri",45),
               bg="white",
               width=50,
               height=0)
label.place(x=0,y=0)



label=tk.Label(root,text="Knee Osteoarthritis Detection using CNN ",font=("Calibri",45),
               bg="red",
               width=50,
               height=1)
label.place(x=0,y=0)
# btn=tk.Button(root,text="Login",font=("Arial",15),width=7,
#               bg="light gray",
#               #fg="white",
#             )
# btn.place(x=1200,y=20)

# btn=tk.Button(root,text="Register",font=("Arial",15),width=7,
#               bg="light gray",
#               #fg="white",
#             )
# btn.place(x=1320,y=20)

def reg():
    from subprocess import call
    call(['python','GUI_Master_old.py'])

btn=tk.Button(root,text="Detection",font=("Arial",15),width=18,command=reg,
              bg="light gray",
              #fg="white",
            )
btn.place(x=200,y=500)

def reg():
    from subprocess import call
    call(['python','Prevention.py'])
    
btn=tk.Button(root,text="Prevention",font=("Arial",15),width=18,command=reg,
              bg="light gray",
              #fg="white",
            )
btn.place(x=700,y=500)

def reg():
    from subprocess import call
    call(['python','Contact us.py'])
btn=tk.Button(root,text="Contact us",font=("Arial",15),width=18,command=reg,
              bg="light gray",
              #fg="white",
            )
btn.place(x=1100,y=500)

def reg():
    from subprocess import call
    call(['python','Ambulance.py'])
    
#btn=tk.Button(root,text="Ambulance no",font=("Arial",15),width=14,command=reg,
#              bg="light gray",
              #fg="white",
#            )
#btn.place(x=1200,y=600)

btn=tk.Button(root,text="Log Out",font=("Arial",15),width=14,command=root.destroy,
              bg="light gray",
              #fg="white",
            )
btn.place(x=1300,y=80)


#creating menubar
menubar=Menu(root)

def reg1():
    from subprocess import call
    call(['python','Injuri.py'])
    
def reg2():
    from subprocess import call
    call(['python','DISEASES.py'])

def reg3():
    from subprocess import call
    call(['python','risk factor.py'])

#adding file Menu and Command
file=Menu(menubar,tearoff=15)
menubar.add_cascade(label='Health information',menu=file)
file.add_command(label='Diseases',command=reg2)
file.add_command(label='Risk factor',command=reg3)
file.add_command(label='Injuries',command=reg1)
file.add_separator()
#file.add_command(label='Exit',command=root.destroy)
#menubar.add_cascade(label='Logout',menu=file,command=root.destroy)

def reg4():
    from subprocess import call
    call(['python','Prevention.py'])

def reg5():
    from subprocess import call
    call(['python','Health And Life Style.py'])

edit=Menu(menubar,tearoff=15)
menubar.add_cascade(label='Patient Care',menu=edit)
edit.add_command(label='Prevention',command=reg4)
edit.add_command(label='Health and Lifestyle',command=reg5)
edit.add_separator()
#edit.add_command(label='Find...',command=None)
#edit.add_command(label='Find Again',command=None)

def reg6():
    from subprocess import call
    call(['python','Hospital in Pune.py'])
    
def reg7():
        from subprocess import call
        call(['python','Hospital in mumbai.py'])

#Adding Help Menu
h=Menu(menubar,tearoff=15)
menubar.add_cascade(label='Hospitals',menu=h)
h.add_command(label='Hospital in pune',command=reg6)
h.add_command(label='Hospital in mumbai',command=reg7)
h.add_separator()
#h.add_command(label='About Tk',command=None)

def reg8():
    from subprocess import call
    call(['python','Contact us.py'])

def reg9():
    from subprocess import call
    call(['python','Detail_About us.py'])

v=Menu(menubar,tearoff=15)
menubar.add_cascade(label='About us',menu=v)
v.add_command(label='Detail',command=reg9)
v.add_command(label='Contact us',command=reg8)
v.add_separator()
#v.add_command(label='About Tk',command=None)

def reg10():
    from subprocess import call
    call(['python','Ambulance.py'])

help=Menu(menubar,tearoff=15)
menubar.add_cascade(label='Help',menu=help)
help.add_command(label='Ambulance no',command=reg10)
#help.add_command(label='Demo',command=None)
#help.add_separator()
#help.add_command(label='About Tk',command=None)



root.config(menu=menubar)



root.mainloop()