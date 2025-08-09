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


label=tk.Label(root,text="Risk Factors",font=("arial",30),
               bg="black",
               fg="red")
label.place(x=50,y=100)



label=tk.Label(root,text='''Being overweight or obese increases stress on your knee joints, even during ordinary activities such as walking or going up and down stairs. It also puts you at increased risk of osteoarthritis 
               by accelerating the breakdown  of joint cartilage.''',
               font=("arial",10),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=400,y=200)

label=tk.Label(root,text="Excess weight:",font=("arial",13,'bold'),
               bg="black",
               fg="white")
label.place(x=50,y=200)



label=tk.Label(root,text=''' A lack of strength and flexibility can increase the risk of knee injuries. Strong muscles help stabilize and protect your joints, and muscle flexibility can help you achieve full range of motion.''',
               font=("arial",10),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=400,y=300)

label=tk.Label(root,text="Lack of muscle flexibility or strength:",font=("arial",13,'bold'),
               bg="black",
               fg="white")
label.place(x=50,y=300)

label=tk.Label(root,text=''' Some sports put greater stress on your knees than do others. Alpine skiing with its rigid ski boots and potential for falls, basketball's jumps and pivots, and the repeated pounding your
               knees take when you run or jog all increase your risk of knee injury. Jobs that require repetitive stress on the knees such as construction or farming also can increase your risk.''',
               font=("arial",10),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=400,y=400)

label=tk.Label(root,text=" Certain sports or occupation:",font=("arial",13,'bold'),
               bg="black",
               fg="white")
label.place(x=50,y=400)


label=tk.Label(root,text='''Having a previous knee injury makes it more likely that you'll injure your knee again.''',
               font=("arial",10),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=400,y=500)

label=tk.Label(root,text="Previous injury:",font=("arial",13,'bold'),
               bg="black",
               fg="white")
label.place(x=50,y=500)

root.mainloop()