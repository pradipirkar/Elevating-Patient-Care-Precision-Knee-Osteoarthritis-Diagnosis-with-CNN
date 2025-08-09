import tkinter 
import tkinter as tk


from PIL import Image,ImageTk
root=tk.Tk()
root.geometry("3000x1000")
root.configure(background='black')
"""
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("hello")

image2=Image.open('F:/.m2/python/GUI/Project/download.jpeg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)

"""
label=tk.Label(root,text="Doctors Recommendation",font=("arial",30),
               bg="black",
               fg="red")
label.place(x=50,y=100)



label=tk.Label(root,text='''
Mobile No.= +91 3434343434
Dr Name = Dr.Nikhil Panpatte
               ''',
               font=("arial",15),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=52,y=250)

label=tk.Label(root,text="ACL injury and Torn meniscus",font=("arial",13,"bold"),
               bg="light gray",
               fg="black")
label.place(x=50,y=200)



label=tk.Label(root,text=''' 
Mobile No.= +91 3434343434
Dr Name = Dr. Aniket Patil ''',
               font=("arial",15),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=52,y=400)

label=tk.Label(root,text="Fractures and Knee bursitis",font=("arial",13,"bold"),
               bg="light gray",
               fg="black")
label.place(x=50,y=350)

label=tk.Label(root,text='''  
Mobile No.= +91 3434343434
Dr Name = Dr. Rahul Chaudhari ''',
               font=("arial",15),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=52,y=550)

label=tk.Label(root,text=" Patellar tendinitis",font=("arial",13,"bold"),
               bg="light gray",
               fg="black")
label.place(x=50,y=500)



root.mainloop()

