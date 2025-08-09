import tkinter 
import tkinter as tk


from PIL import Image,ImageTk
root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))


image2=Image.open('Images/ambulance-ad.jpg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


label=tk.Label(root,text="Ambulance no:",font=("arial",20),
               bg="white",
               fg="black")
label.place(x=50,y=150)

label=tk.Label(root,text='''0000044''',
               bg="black",
               fg="white",
               font=("arial",40),
               anchor='center')
label.place(x=650,y=400)

root.mainloop()