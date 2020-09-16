import math

#primera funcion que define si es mayor o menor

def MayorMenor(num1, num2):

    #los (if) funcionan de este modo
    if num1 > num2:
        print ("El numero 1 es mayor")
    else:
        print ("El numero 2 es mayor")

#ejecucion de una funcion
#MayorMenor(3,33)

#como definir listas (Array) en python
def Familia ():
    #asi se crea una lista con strings
    miLista=["Edu","Alex","Mila","Braulio"]
    #asi ser imprime un espacio de la lista
    print (miLista[0])
    #imprime desde el numero que queramos de la lista hasta EL NUMERO ANTERIORt
    #que pongamos al final (imprime desde pos 0 a pos 3)
    print (miLista[0:4])
    #añadir un dato nuevo creando espacio al final de la lista
    miLista.append("Raquel")
    #añadir nuevo elemento en una posicion y desplazar a los demas hacia detras
    miLista.insert(1,"Andrea")
    print (miLista[0:6])
    #añadir nuevos elementos al final de la listas
    miLista.extend(["Alberto", "Merce", "Julio", "Mamen"])
    print (miLista[0:10])
    #conocer el indice de un elemento
    print(miLista.index("Alberto"))
    #imprime true o false dependiendo si el elemento se encuentra en la lista
    nombre1 = "Tomas"
    print("¿El nombre de "+nombre1+" se encuentra en la lista?")
    print(nombre1 in miLista)
    #eliminar elemento de una lista
    miLista.remove("Andrea")
    print (miLista[0:9])
    #contar cuantas veces aparece un elemento en la lista
    print(miLista.count("Edu"))
#ejecucion de la funcion
#Familia()

#como definir diccionarios en python
def Diccionario():
    #creamos el diccionario
    miDiccionario = {"España":"Madrid","Francia":"Paris","Holanda":"Amsterdam","Islandia":"Reikiavic"}
    #imprimir clave - valor de un diccionario
    print(miDiccionario["Islandia"])
    #imprimir todo el diccionario
    print(miDiccionario)
    #añadir nuevos elementos al diccionario
    miDiccionario["Italia"]="Beijing"
    #modificar una valor de una clave
    miDiccionario["Italia"]="Roma"
    print(miDiccionario)
    #eliminar elementos del diccionario
    del miDiccionario["Francia"]
    print(miDiccionario)
    #imprimir las claves de un diccionario
    print(miDiccionario.keys())
    #imprimir los valores de un diccionario
    print(miDiccionario.values())
    #imprimir longitud del diccionario
    print(len(miDiccionario))
#ejecucion de la funcion
#Diccionario()


#comenzamos con las practicas de condicionales IF
def EvaluacionNotas():

    #Vamos a introducir informacion por teclado
    print("Programa de evaluacion de notas, introduce tu nota:")
    nota_alumno=input()
    #damos por hecho que todos estan aprobados
    valoracion = "aprobado"
    #comprobamos si esta aprobado o suspenso
    if float(nota_alumno) < 4.95:
        valoracion = "suspenso"
    return valoracion
#ejecucion de la funcion
#print(EvaluacionNotas())

def Verificacion():
    #preguntamos la edad al usuario
    edad_user = int(input("Introduce tu edad:"))
    #clausula seguridad
    if edad_user > 122:
        print("Edad fuera de rango")
    #verificamos si es mayor de 18 años
    elif edad_user > 18:
        print("Acesso permitido")
    #clausula de seguridad
    elif edad_user < 0:
        print("Edad fuera de rango")
    #restringimos si es menor de edad
    else:
        print("Acesso restringido")
#ejecucion de programa
#Verificacion()

def Condicionales3():
    #introducimos una edad de referencia
    edad = 145
    #clausula de seguridad concatenando varios condicionales
    if 0 < edad < 122:
        print("La edad es correcta")
    else:
        print("La edad es incorrecta")
#ejecucion de programa
#Condicionales3()

def Condicionales4():
    print("Programa de calculo de becas")
    #pedimos los datos para saber si accede a la beca o no
    distanciaEscuela = int(input("Introduce distancia a la escuela en km: "))
    numeroHermanos = int(input("Introduce numero de hermanos en la escuela: "))
    salarioFamiliar = int(input("Introduce el salario familiar anual: "))
    #creamos el condicional para saber si la recibe o no
    if distanciaEscuela > 40 and numeroHermanos > 1 or salarioFamiliar < 20000:
        print("Tienes derecho a Beca")
    else:
        print("No tienes derecho a beca")
#ejecucion de programa
#Condicionales4()

def Bucles():
    #estas variables se utilizan solo en alguno
    email = False
    miEmail = input("Introduce tu email: ")
    contA = 0
    contP = 0
    #definicion de un bucle normal
    for i in [1,2,3]:
        if i < 3:
            #esto hace que se imprima hacia la derecha y no hacia abajo
            print(i, end=" ")
        else:
            print(i)
    #explicaciones bucles
    #Imprime una palabra tantas veces como letras tenga el correo dentro del bucle
    for i in "matahaxusen92@gmail.com":
        print (i)
    #comprobamos si es un correo electronico de verdad mediante un @
    for i in "matahaxusen92@gmail.com":
        if i == "@":
            email = True
    if email == True:
        print("El email es correcto")
        email = False
    else:
        print("El email es incorrecto")
    #comprobar que una direccion de email es valida
    for i in miEmail:
        if i == "@":
            contA += 1
        elif i == ".":
            contP += 1
    if contA == 1 and contP > 0:
        print("Correo de confirmacion enviado")
    else:
        print("Error a la hora de escribir el correo")
    #crear bucles clasicos de Java
    for i in range(5): #[0,1,2,3,4]
        #la "f" sirve para imprimir texto con variables
        print (f"posicion de la lista {i}")
    #bucle con numeros diferentes
    for i in range(5,10):
        print(i)
    #bucle pero saltandote numeros
    for i in range(10,100,15):
        print (i)
#ejecucion de programa
#Bucles()

def BucleWhile():
    #variables
    i = 1
    #definimos el primer grupo while
    while i <= 10:
        print("ejecucion " + str(i))
        i += 1

    print("Ha terminado la ejecucion")
    #pedir introducir un dato hasta que cumpla características
    edad = int(input("Introduce tu edad: "))
    while edad < 8 or edad > 122:
        print("Introduce una fecha de edad correcta")
        edad = int(input("Introduce tu edad (real) por favor: "))

    print("Gracias por colaborar")
    print("Edad del usuario: " + str(edad))
    #bucles con limite de intentos
    print("Calculo de raices cuadradas...")
    #primera vez que se pide introducir un numero
    numero = int(input("Introduce un numero: "))
    intentos = 0
    #mientras que tenga menos de 3 intentos se mantiene en el bucle
    while numero < 0:
        print("Número no reconocible ")
        #si ha llegado al numero maximo se le saca del programa
        if intentos == 2:
            print("Has llegado al límite de intentos")
            break;
            #si lo introduce mal que lo vuelva a introducir
        numero = int(input("Introduce un numero: "))
        if numero < 0:
            intentos += 1
    #si escribe un numero correcto se escribe la función que ha pedido
    if intentos < 2:
        solucion = math.sqrt(numero)
        print("La raiz cuadrada es :" + str(solucion))
#ejecucion de programa
#BucleWhile()

#Generador de numeros pares en una lista
def GenerarPares():
    #pedimos el limite de la lista por teclado
    #clausula "try de seguridad si introduce un elemento no valido tiene que volver a escribirlo"
    try:
        numMax = int(input("¿Cuantos numeros pares quieres?: "))
    except ValueError:
        print("Has introducido un numero incorrecto")
        print("Volviendo a la ejecucion del programa...")
        return GenerarPares()
    #creamos las variables necesarias
    contador = 0
    miLista = []
    #Bucle para ir añadiendo elementos a la lista
    while contador < numMax:
        #añadimos un numero par a la lista
        miLista.append(contador * 2 + 2)
        contador += 1
    #queremos que nos devuelva la lista
    return miLista
#ejecucion de programa
#print(GenerarPares())

#generador de ciudades el "*" representa que no sabes el numero de ciudades que van a entrar
def GenerarCiudades(*ciudades):

    for elemento in ciudades:
        #esta linea se suprime porque la sustituye "yield from"
        #for subelemento in elemento:
            yield from elemento

ciudades_devueltas = GenerarCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
#print(next(ciudades_devueltas))
#print(next(ciudades_devueltas))
#print(next(ciudades_devueltas))

#calculador de raices cuadradas
def RaicesCuadradas():
    #pedimos un numero por teclado
    num = float(input("Introduce un número y te digo su raiz: "))
    #
    if num < 0:
        #si el numero es menor que 0 creamos un error de sistema
        raise ValueError ("No se pueden introducir numeros negativos")
    else:
        #si el elemento es un numerpo valido realizamos la operacion
        return math.sqrt(num)
#Si salta el error de ValueError creamos una variable con el string contenido en el error
try:
    print(RaicesCuadradas())
except ValueError as ErrorDeNumerosNegativos:
    print(ErrorDeNumerosNegativos)
    print("Programa cancelado")
