from tkinter import *
#se crea una ventana raiz
raiz = Tk()
#añadir titulo a la ventana
raiz.title("Ventana de pruebas")
#elegir si se puede cambiar tamaño de la ventana raiz (ancho[width],alto[height])
raiz.resizable(True,True)
#Tamaño de la Ventana (es mejor darle tamaño al frame)
#raiz.geometry("800x800")
#color del fondo de la pantalla
raiz.config(bg="white")
#crear y empaquetar un frame
miFrame = Frame()
#rellenar toda la raiz con el frame
miFrame.pack(fill="both", expand="True")
#fondo del frame en blanco
miFrame.config(bg="white")
#tamaño inicial del frame y por lo tanto de la raiz
miFrame.config(width="600",height="600")
#decorar los bordes
miFrame.config(relief="groove")
#grosor del borde
miFrame.config(bd=4)
#se crea la segunda ventana que es la de ejecucion
raiz.mainloop()
