import tkinter 
import tkinter as tk


from PIL import Image,ImageTk
root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))


image2=Image.open('Images/WhatsApp Image 2023-09-15 at 2.56.20 PM.jpeg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


label=tk.Label(root,text="Contact us:",font=("arial",50),
               bg="light blue",
               fg="black")
label.place(x=50,y=200)


label=tk.Label(root,text='''93534777898 / 66687788888''',
               bg="light blue",
               fg="black",
               font=("arial",30),
               anchor='center')
label.place(x=400,y=400)

root.mainloop()