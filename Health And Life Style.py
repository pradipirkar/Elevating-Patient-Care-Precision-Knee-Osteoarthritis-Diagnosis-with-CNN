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
label=tk.Label(root,text="Health and Life Style",font=("arial",30),
               bg="black",
               fg="red")
label.place(x=50,y=100)



label=tk.Label(root,text='''
It's important to pick exercises that are gentle and safe to decrease your risk of joint injury and to try a combination of activities that promote flexibility and range of motion (such as yoga or exercises prescribed by a physical therapist),
muscle strengthening (such as working out with weight machines or resistance ...
               ''',
               font=("arial",10),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=52,y=250)

label=tk.Label(root,text="What keeps knees healthy?",font=("arial",13,"bold"),
               bg="light gray",
               fg="black")
label.place(x=50,y=200)



label=tk.Label(root,text=''' 
Because the knees play a pivotal role in keeping you not only mobile, but active and fit, it's easy to see why it's important to do everything you can to keep your knees healthy. Here's a closer look at some of the most common threats to knee
health and how to avoid them.''',
               font=("arial",10),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=52,y=400)

label=tk.Label(root,text="Why is knee health important?",font=("arial",13,"bold"),
               bg="light gray",
               fg="black")
label.place(x=50,y=350)

label=tk.Label(root,text='''  Here are a few examples of bad habits that can trigger your knee pain, accelerate arthritic changes, and aggravate an existing weakness following an injury:\n
    Wearing shoes that stress your knee.
  Eating foods that fuel inflammation.
      Engaging in the wrong type of exercise.
   Failing to warm up before running. ''',
               font=("arial",10),
               bg="black",
               fg="white",
               anchor='center')
label.place(x=52,y=550)

label=tk.Label(root,text=" What habits cause knee pain?",font=("arial",13,"bold"),
               bg="light gray",
               fg="black")
label.place(x=50,y=500)



root.mainloop()

