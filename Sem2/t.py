from Tkinter import *                         # Import tkinter
root=Tk()                                     # Create an instance using Tk()
b=Button(root,justify = LEFT)                 # Create a button
photo=PhotoImage(file="flower.jpeg")           # Give photo an image
b.config(image=photo,width="10",height="10")  # Configure the earlier instance to use the photo
b.pack(side=LEFT)                             # Pack up the button
root.mainloop()                               # Create everything
