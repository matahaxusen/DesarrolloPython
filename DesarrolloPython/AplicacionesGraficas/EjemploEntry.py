from tkinter import *

root = Tk()

#variables necesarias para el programa
minombre = StringVar()

miFrame = Frame(root, width="800",height="900")
miFrame.pack()

#empezamos a trabajr con grid (rejillas en el mapa)
cuadroNombre = Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row="0",column="1",sticky="e",pady=2, padx=2)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row="1",column="1",sticky="e",pady=2, padx=2)

cuadroDNI = Entry(miFrame)
cuadroDNI.grid(row="2",column="1",sticky="e",pady=2, padx=2)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row="3",column="1",sticky="e",pady=2, padx=2)
#queremos que no se vea la contraseña mientras se escribe
cuadroPass.config(show="*")

textoComentario = Text(miFrame, width=20, height=8)
textoComentario.grid(row="4",column="1",sticky="e",pady=2, padx=2)
#añadimos scroll bar
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
#colocamos scroll bar
scrollVert.grid(row="4", column="2",sticky="nsew")
#adaptamos el Scrollbar
textoComentario.config(yscrollcommand=scrollVert.set)


#sticky se encarga de alinear los label en funcion e(este), w(oeste), n(norte), s(sur)
nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row="0",column="0",sticky="e",pady=2, padx=2)
#pady indica la separacion entre labels
apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row="1",column="0",sticky="e",pady=2, padx=2)

DNILabel = Label(miFrame, text="DNI-NIF: ")
DNILabel.grid(row="2",column="0",sticky="e",pady=2, padx=2)

PassLabel = Label(miFrame, text="Password: ")
PassLabel.grid(row="3",column="0",sticky="e",pady=2, padx=2)

#creamos una label para comentarios mas grande de lo normal
commentsLabel = Label(miFrame, text="Comentarios: ")
commentsLabel.grid(row="4",column="0",sticky="e",pady=2, padx=2)

#creamos nuestro primer boton
def codigoBoton():
    minombre.set("Eduardo")

botonEnvio = Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()
