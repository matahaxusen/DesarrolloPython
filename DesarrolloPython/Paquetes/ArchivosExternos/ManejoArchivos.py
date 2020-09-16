from io import open

archivoTexto = open ("archivo.txt","r+")#el + indica que esta en modo lectura escritura
#print(archivoTexto.seek(len(archivoTexto.readline())))
#colocamos el puntero en al principio de la segunda linea (nos saltamos la primera)
listaTexto = archivoTexto.readlines()
#escribimos por cada atributo de la lista lo que queramos escribir en la linea
listaTexto[1] = "Esta linea se ha incluido desde el programa \n"
listaTexto[2] = "Que bien se vive cuando no se vive mal"
#colocamos el pontero en la posicion 0 de la segunda linea
archivoTexto.seek(0)
#reescribimos las lineas
archivoTexto.writelines(listaTexto)
#cerramos el archivo
archivoTexto.close()
