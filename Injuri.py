import tkinter 
import tkinter as tk


from PIL import Image,ImageTk
root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))


image2=Image.open('Images/images (5).jpeg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


label=tk.Label(root,text="Injuries",font=("arial",30),
               bg="black",
               fg="red")
label.place(x=50,y=100)



label=tk.Label(root,text='''An ACL injury is a tear of the anterior cruciate ligament (ACL) — one of four ligaments that connect your shinbone to your thighbone. An ACL injury is particularly common in people who play basketball, soccer or other
               sports that require sudden changes in direction.''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=200,y=200)

label=tk.Label(root,text="ACL injury:",font=("arial",13),
               bg="light gray",
               fg="black")
label.place(x=50,y=200)



label=tk.Label(root,text='''The bones of the knee, including the kneecap (patella), can be broken during falls or auto accidents. Also, people whose bones have been weakened by osteoporosis can sometimes knee fracture simply by stepping wrong.''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=200,y=300)

label=tk.Label(root,text="Fractures.:",font=("arial",13),
               bg="light gray",
               fg="black")
label.place(x=50,y=300)

label=tk.Label(root,text=''' The meniscus is the tough, rubbery cartilage that acts as a shock absorber between your shinbone and thighbone. It can be torn if you suddenly twist your knee while bearing weight on it.''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=200,y=400)

label=tk.Label(root,text=" Torn meniscus:",font=("arial",13),
               bg="light gray",
               fg="black")
label.place(x=50,y=400)


label=tk.Label(root,text='''Having a previous knee injury makes it more likely that you'll injure your knee again.''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=200,y=500)

label=tk.Label(root,text="Some knee injuries cause inflammation in the bursae, the small sacs of fluid that cushion the outside of your knee joint so that tendons and ligaments glide smoothly over the joint",font=("arial",13),
               bg="light gray",
               fg="black",)
label.place(x=200,y=500)


label=tk.Label(root,text="Knee bursitis:",font=("arial",13),
               bg="light gray",
               fg="black",)
label.place(x=50,y=500)


label=tk.Label(root,text='''Tendinitis causes irritation and inflammation of one or more tendons — the thick, fibrous tissues that attach muscles to bones. This inflammation can happen when there's an injury to the patellar tendon, 
               which runs from the kneecap (patella) to the shinbone and allows you to kick, run and jump. Runners, skiers, cyclists, and those involved in jumping sports and activities may develop patellar tendinitis.''',
               font=("arial",10),
               bg="light gray",
               fg="black",
               anchor='center')
label.place(x=200,y=600)

label=tk.Label(root,text="Patellar tendinitis:",font=("arial",13),
               bg="light gray",
               fg="black",)
label.place(x=50,y=600)


root.mainloop()