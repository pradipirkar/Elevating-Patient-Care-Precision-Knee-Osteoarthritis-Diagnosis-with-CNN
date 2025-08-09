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




label=tk.Label(root,text="Hospital in mumbai:",font=("arial",13),
               bg="light blue",
               fg="black")
label.place(x=50,y=200)


label=tk.Label(root,text=''''Nanavati Hospital-Vileparle West, Mumbai''',
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=200)





label=tk.Label(root,text=''' S L Raheja Hospital-Mahim, Mumbai''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=250)


label=tk.Label(root,text='''Bombay Hospital & Medical Research Centre-Marine Lines, Mumbai''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=300)

label=tk.Label(root,text='''Breach Candy Hospital-Breach Candy, Mumbai''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=350)

label=tk.Label(root,text='''Kokilaben Dhirubhai Ambani Hospital Kokilaben Dhirubhai Ambani Hospital-Andheri West, Mumbai''',
               font=("arial",10),
               bg="light blue",
               fg="black",
               anchor='center')
label.place(x=300,y=400)

root.mainloop()