from tkinter import*
root=Tk()
def myclick():
    line=Label(root,text="HOLA MY FRIEND",fg="red",bg="yellow")
    line.pack()
mybutton=Button(root,text="CLICK HERE",padx=40,pady=30,fg="white",bg="black",command=myclick)
mybutton.pack()
root.mainloop()
#Padx and Pady is for adjusting the size of the button
#fg(foreground) is for colouring the text.
#bg(background) is for colouring the background.
#command is for the output when you click the button then after that what happens...it calls the myclick function and label that text after clicking
