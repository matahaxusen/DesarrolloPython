import pickle

class Persona():
    def __init__(self,nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona con el nombre de: ",self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas():

    personas = []

    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)
        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas en el fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del (listaDePersonas)

    def agregar(self, ppl):
        self.personas.append(ppl)
        self.agregarFE()

    def imprimir(self):
        for i in self.personas:
            print(i)

    def agregarFE (self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)

    def imprimirFE (self):
        print("Informacion del fichero externo: ")
        for x in self.personas:
            print(x)


miLista = ListaPersonas()
nombre = str(input("Indica tu nombre: "))
sexo = str(input("Indica tu sexo: "))
edad = str(input("Indica tu edad: "))
persona = Persona(nombre, sexo,edad)
miLista.agregar(persona)
miLista.imprimirFE()
