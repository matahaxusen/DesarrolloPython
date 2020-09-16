from random import *

def matriz (posY, posX):
    coorY = int(posY)
    coorX = int(posX)

    matriz = []

    for i in range(posY):
        matriz.append([])
        for j in range (posX):
            matriz[i].append(j)
            print(matriz [i][j])

    print(coorX,coorY,numRandom)

def LetraRandom():

    numRandom = int(random()*9 + 1)

    if numRandom == 1:
        return "M"
    elif numRandom == 2:
        return "O"
    elif numRandom == 3:
        return "T"
    elif numRandom == 4:
        return "L"
    elif numRandom == 5:
        return "R"
    elif numRandom == 6:
        return "V"
    elif numRandom == 7:
        return "P"
    elif numRandom == 8:
        return "C"
    elif numRandom == 9:
        return "I"

def codigo


print(LetraRandom())
