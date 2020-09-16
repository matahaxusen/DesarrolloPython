#creamos nuestra primera clase
class Coche():
    #se utiliza para asignar un valor predefinido a los objetos que se crean
    def __init__(self):
    #creamos los elementos que tenga la clase
        self.__largoCoche = 250
        self.__anchoCoche = 130
        self.__ruedas = 4
        self.__enmarcha = False
    #con "defs" creamos un metodo no una funcion la "s" marca la diferencia
    def __Check(self):
        print("Realizando chequeo interno")
        #introducimos nuevos datos
        self.__gasolina = "ok"
        self.__aceite = "ok"
        self.__puertas = "cerradas"
        #funcion para comprobar que todo esta bien
        if self.__gasolina == "ok" and self.__aceite == "ok" and self.__puertas == "cerradas":
            return True
        else:
            return False
    #arrancamos el coche
    def Arrancar(self):
        self.__enmarcha = True
    #comprobamos si el coche esta parado o arrancado
    def Estado(self):
        if(self.__enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche esta parado"
    #recibimos un objeto "self" y una variable de ese objeto "arrancamos"
    def CompleteStart (self, arrancamos):
        self.__enmarcha = arrancamos
        if self.__enmarcha:
            chequeo = self.__Check()
        if self.__enmarcha and chequeo:
            return "El coche esta en marcha"
        elif self.__enmarcha and chequeo == False:
            self.__enmarcha = False
            return "Algo ha fallado no se puede arrancar"
        else:
            return "El coche esta parado"
    #imprime los datos del vehiculo
    def Datos(self):
        return "El largo del coche es: " + str(self.__largoCoche) + " cm\nEl ancho del coche es: " + str(self.__anchoCoche) + " cm\nEL numero de ruedas es: " + str(self.__ruedas)
    #realiza un chek del coche


#creamos un objeto de coche (es decir creamos un coche con las caractaristicas indicadas)
miCoche = Coche()
print(miCoche.Estado())
#bloque que "arranca el coche" y muestra que estado sea arrancado
print(miCoche.CompleteStart(True))
#bloque de impresion de los datos del vehiculo
print(miCoche.Datos())
#comenzamos la creacion del segundo Coche
miCoche2 = Coche()
print("---> Se ha creado segundo vehículo <---")
#como la variable ruedas esta encapsulada no se puede cambiar su valor
miCoche2.__ruedas = 2;
print(miCoche.Datos())
#creamos un error si se intenta ejecutar Check() desde fuera de programa
try:
    print(miCoche2.__Check())
except AttributeError:
    print("No se puede acceder a comando interno")
#creamos nuevos metodos mejorando los anteriores
print(miCoche2.CompleteStart(False))
