import tkinter 
import tkinter as tk


from PIL import Image,ImageTk
root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))


image2=Image.open('Images/WhatsApp Image 2023-09-15 at 2.53.31 PM.jpeg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


label=tk.Label(root,text="Detail:",font=("arial",20),
               bg="white",
               fg="black")
label.place(x=50,y=150)


label=tk.Label(root,text='''we are here to provide you the infrormation you need, Thankyou for trusting in our website''',
               bg="white",
               fg="black",
               font=("arial",15),
               anchor='center')

label.place(x=400,y=400)


label=tk.Label(root,text='''Our site was started in 2019,Here you know many infomation about knee and it's pain''',
               bg="white",
               fg="black",
               font=("arial",15),
               anchor='center')
label.place(x=400,y=450)

root.mainloop()