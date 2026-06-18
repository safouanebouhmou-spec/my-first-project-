from tkinter import *

root= Tk()

def Hydrogene():
    Label(text="",font=30).place(x=180, y=380)
    Label(text="Hydrogene : Numero atomic = 1, symbole chimique : H,Masse atomique : 1.01 ", font=30).place(x=80,y=380)
    Label()

root.geometry("800x600") #pixel
root.resizable(False,False)
root.title("iks chemistry")

photo = PhotoImage(file="")
myimage = Label(image=photo)
myimage.pack(padx=0,pady=15)

Label(text="L'element chimique :",font=23).place(x=100,y=250)
nameValue=StringVar()
nameEntry=Entry(root,textvariable=nameValue,width=30,bd=3,font=20)
nameEntry.place(x=300,y=250)

def iks_print():
    if nameValue.get() == "Hydrogene" :

       Hydrogene()

button= Button(text="check",font=20,bg="black",fg="white",width=11,height=2,command=iks_print).place(x=300,y=450)

root.mainloop()