import tkinter 
import tkinter as tk


from PIL import Image,ImageTk
root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))


image2=Image.open('Images/WhatsApp Image 2023-09-15 at 3.00.22 PM.jpeg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


label=tk.Label(root,text="Prevention",font=("arial",30),
               bg="white",
               fg="red")
label.place(x=50,y=100)


label=tk.Label(root,text='''Maintain a healthy weight; it's one of the best things you can do for your knees.\n Every extra pound puts additional strain on your joints, increasing the risk of injuries and osteoarthritis.''',
               font=("arial",12,),
               bg="white",
               relief="solid",
               fg="black",
               anchor='center')
label.place(x=300,y=200)

label=tk.Label(root,text="Keep extra pounds off:",font=("arial",13, "bold"),
               bg="white",
               relief="solid",
               fg="black")
label.place(x=50,y=200)



label=tk.Label(root,text='''To prepare your muscles for the demands of sports participation, take time for conditioning.''',
               font=("arial",11),
               bg="white",
               relief="solid",
               fg="black",
               anchor='center')
label.place(x=300,y=300)

label=tk.Label(root,text="Be in shape to \n play your sport:",font=("arial",13, "bold"),
               bg="white",
               relief="solid",
               fg="black")
label.place(x=50,y=300)

label=tk.Label(root,text=''' Make sure the technique and movement patterns you use in your sports or\n  activity are the best they can be. \n Lessons from a professional can be very helpful.''',
               font=("arial",11),
               relief="solid",
               bg="white",
               fg="black",
               anchor='center')
label.place(x=300,y=400)

label=tk.Label(root,text="Practice perfectly:",font=("arial",13, "bold"),
               bg="white",
               relief="solid",
               fg="black")
label.place(x=50,y=400)


label=tk.Label(root,text='''Weak muscles are a leading cause of knee injuries. You'll benefit from building up your quadriceps and hamstrings,\n the muscles on the front and back of your thighs that help support your knees.\n Balance and stability training helps the muscles around your knees work together more effectively.''',
               font=("arial",11),
               relief="solid",
               bg="white",        ####
               fg="black",
               anchor='center')
label.place(x=300,y=500)


label=tk.Label(root,text="Get strong, stay flexible.:",
               font=("arial",13, "bold"),
               relief="solid",
               bg="white",
               fg="black",)
label.place(x=50,y=500)


label=tk.Label(root,text=''' If you have osteoarthritis, chronic knee pain or recurring injuries, you may need to change the way you exercise. \nConsider switching to swimming, water aerobics or other low-impact 
               activities — at least for a few days a week. \n Sometimes simply limiting high-impact activities will provide relief.''',
               font=("arial",11),
               relief="solid",
               bg="white",
               fg="black",
               anchor='center')
label.place(x=300,y=600)

label=tk.Label(root,text="Be smart about exercise:",font=("arial",13, "bold"),
               bg="white",
               relief="solid",
               fg="black",)
label.place(x=50,y=600)


root.mainloop()