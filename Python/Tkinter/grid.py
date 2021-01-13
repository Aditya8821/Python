from tkinter import*
root=Tk()
line1=Label(root,text="HELLO WORLD!!").grid(row=0,column=0)            #PACK always gives the output in the middle but grid do that by taking row and column values
line2=Label(root,text="MY NAME IS ADITYA TRIVEDI").grid(row=1,column=1)#GRID default starts from row=0 and column=0
root.mainloop()
