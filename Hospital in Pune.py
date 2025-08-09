import tkinter 
import tkinter as tk


from PIL import Image,ImageTk
root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))


image2=Image.open('Images/WhatsApp Image 2023-09-15 at 2.58.02 PM.jpeg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


label=tk.Label(root,text="Hospitals",font=("arial",30),
               bg="light blue",
               fg="red")
label.place(x=50,y=100)


label=tk.Label(root,text='''Apollo Jehangir Hospital-Bund Garden, Pune''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=200)

label=tk.Label(root,text="Hospital in pune:",font=("arial",13,),
               bg="light blue",
               fg="black")
label.place(x=50,y=200)



label=tk.Label(root,text=''' Kem Hospital-Rasta Peth, Pune''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=250)


label=tk.Label(root,text='''Deenanath Mangeshkar Hospital-Erandwane, Pune''''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=300)

label=tk.Label(root,text='''Sahyadri Super Speciality Hospital-Hadapsar, Pune''''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=350)

label=tk.Label(root,text='''Inamdar Multispeciality Hospital-Fatima Nagar, Pune''''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=400)

label=tk.Label(root,text='''Aims Hospital-Aundh, Pune''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=450)


root.mainloop()