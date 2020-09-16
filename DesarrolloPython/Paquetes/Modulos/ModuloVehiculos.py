class Vehiculos():
    #definimos los elementos comunes de la clase
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    #creamos clases para modificar las variables
    def Arrancar(self):
        self.enmarcha = True
    def Frenar(self):
        self.frena = True
        self.acelera = False
        wait(2)
        print("El coche ha frenado")
        self.frena = False
    def Acelerar(self):
        self.frena = False
        self.acelera = True
    #creamos una clase para imprimir el estado del vehiculo
    def Estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)
#creamos una clase hijo para ejecutarla
class Moto(Vehiculos):
    caballito = False
    def Caballito(self):
        self.caballito = True
    def Standard(self):
        self.caballito = False
    def Estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,"\nHaciendo el caballito: ",self.caballito)

#creamos nuevas clases hijos
class Furgoneta(Vehiculos):

    def Carga(self,cargar):
        self.cargado = cargar
        if self.cargado:
            print("La furgoneta esta cargada")
        else:
            print("La furgoneta no esta cargada")

#creamos clases nuevas de hijos
class Electricos(Vehiculos):

    def __init__(self):
        self.autonomia = 100
    def CargaEnergia(self):
        self.cargando = True

class BiciElectrica(Electricos, Vehiculos):

    pass
