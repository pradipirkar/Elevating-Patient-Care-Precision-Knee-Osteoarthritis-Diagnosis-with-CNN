import tkinter as tk
from PIL import Image,ImageTk



root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("hello")

image2=Image.open("Images/knee-Pain-new1.jpg")
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)

label=tk.Label(root,text="Knee Osteoarthitis Diagnosis with CNN",font=("Calibri",45),
               bg="red",
               width=50,
               height=1)
label.place(x=0,y=0)        



def reg():
    from subprocess import call
    call(['python','login.py'])

btn=tk.Button(root,text="Login",command=reg,font=("Arial",15),width=7,
              bg="light gray",
              #fg="white",
            )
btn.place(x=1080,y=400)

def reg():
    from subprocess import call
    call(['python','registration.py'])

btn=tk.Button(root,text="Register",command=reg,font=("Arial",15),width=7,
              bg="light gray",
              #fg="white",
            )
btn.place(x=1220,y=400)







#register1=tk.Label(root,text="Kindly register here...." ,font=('Cambria',10)).place(x=1230,y=350)





root.mainloop()