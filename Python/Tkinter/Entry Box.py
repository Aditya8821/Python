from tkinter import*
root=Tk()
e=Entry(root,relief="ridge",width=50,borderwidth=10,fg="white",bg="black")
e.insert(0,"Enter your name:- ")
def some_callback(event): # note that you must include the event as an arg, even if you don't use it.
    e.delete(0, "end")
e.bind("<Button-1>", some_callback)
e.pack()
def click():
    line=Label(root,text="Hello "+e.get())
    line.pack()
button=Button(root,text="CLICK HERE",command=click)
button.pack()
root.mainloop()
