import tkinter 
import tkinter as tk


from PIL import Image,ImageTk
root=tk.Tk()
root.configure(background='white')

w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))


image2=Image.open('Images/WhatsApp Image 2023-09-15 at 3.11.13 PM.jpeg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


label=tk.Label(root,text="DISEASES & CONDITIONS",font=("arial",30),
               bg="black",
               fg="red")
label.place(x=50,y=100)



label=tk.Label(root,text='''Schlatter disease is a common cause of knee pain in growing adolescents. It is an inflammation of the area just below the knee where
               the tendon from the kneecap (patellar tendon) attaches tothe shinbone (tibia).''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=320,y=200)

label=tk.Label(root,text="Osgood:",font=("arial",13,"bold"),
               bg="light gray",
               fg="black")
label.place(x=50,y=200)



label=tk.Label(root,text=''' Achondroplasia is a bone disorder that results in dwarfism. Children who are born with achondroplasia typically have short arms and legs
               a large head, and an average-sized trunk. They are shorter than most other people because of their  bone abnormalities.''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=320,y=300)

label=tk.Label(root,text="Achondroplasia:",font=("arial",13,"bold"),
               bg="light gray",
               fg="black")
label.place(x=50,y=300)

label=tk.Label(root,text='''  Achilles tendinitis is a common condition that occurs when the large tendon that runs down the back of the lower leg becomes irritated and inflamed. ''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=320,y=400)

label=tk.Label(root,text=" Achilles Tendinitis:",font=("arial",13,"bold"),
               bg="light gray",
               fg="black")
label.place(x=50,y=400)


"""label=tk.Label(root,text='''Having a previous knee injury makes it more likely that you'll injure your knee again.''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=180,y=500)"""

label=tk.Label(root,text="The Achilles tendon is the largest tendon in the body. It connects your calf muscles to your heel bone and is used when you walk, run, and jump.",
               font=("arial",10,),
               bg="light gray",
               fg="black",)
label.place(x=320,y=500)


label=tk.Label(root,text="Achilles Tendon Rupture (Tear):",font=("arial",13,"bold"),
               bg="light gray",
               fg="black",)
label.place(x=50,y=500)


label=tk.Label(root,text=''' This article addresses pain in the front and center of the knee. Pain located in the upper shinbone area, just below the kneecap, is a different 
               condition and is discussed in Osgood-Schlatter Disease (Knee Pain).''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=320,y=600)

label=tk.Label(root,text="Adolescent Anterior Knee Pain:",font=("arial",13,"bold"),
               bg="light gray",
               fg="black",)
label.place(x=50,y=600)


root.mainloop()
