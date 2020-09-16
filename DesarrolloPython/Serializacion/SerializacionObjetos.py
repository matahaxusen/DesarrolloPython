import pickle
import time

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

coche1 = Vehiculos("Renault","Megane")
coche2 = Vehiculos("Seat","Ibiza")
coche3 = Vehiculos("Mercedez","CLK500")

coches = [coche1,coche2,coche3]

fichero = open ("ficheroCoches","wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

ficheroApertura = open ("ficheroCoches", "rb")

lista = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in lista:
    print(c.Estado())
