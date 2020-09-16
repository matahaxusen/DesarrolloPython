from tkinter import *

root = Tk()

root.title("Practicas Label")

miFrame = Frame(root, width="600", height="600", bg="white")
miFrame.pack()
#introducimos una imagen
miImagen = PhotoImage(file="raton.gif")
#si vamos a utilizar el label una sola vez podemos eliminar "miLabel = "
miLabel = Label(miFrame,image=miImagen,bg="white",font=("Comic Sans MS", 18)).place(x=0,y=0)

root.mainloop()
