import pickle
import time

listaNombres = ["karla","sara","maria","andrea","irene"]

ficheroBinario = open ("listaNombres","wb")

pickle.dump(listaNombres, ficheroBinario)

print("Fichero volcado con exito")
time.sleep(1)

ficheroBinario.close()
print("...Fichero cerrado...")
time.sleep(0.5)
print("Abriendo el fichero creado...")
time.sleep(2)

fichero = open("listaNombres","rb")

lista = pickle.load(fichero)

print(lista)
