from tkinter import*
root=Tk()                          #It creates the output window 
a=Label(root,text="HELLO WORLD!!") #This Label widget is used to display text or image in the screen
a.pack()                           #This pack is used to combine all the widgets in the GUI
root.mainloop()                    #mainloop() is used to tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or keypresses, and blocks any code that comes after it from running until the window it's called on is closed.
