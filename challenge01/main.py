# Author: Ec25
def detectar_patrones(cadena:str):
    palabras_repeticiones = [[],[]]
    cadena = cadena.lower().split(' ')

    for palabra in cadena:
        if palabra not in palabras_repeticiones[0]:
            palabras_repeticiones[0].append(palabra)
            palabras_repeticiones[1].append(1)
        else:
            indice = palabras_repeticiones[0].index(palabra)
            palabras_repeticiones[1][indice] += 1

    return palabras_repeticiones


def construir_cadena(palabras_repeticiones:list):
    cadena = ""
    for i in range(len(palabras_repeticiones[0])):
        cadena += palabras_repeticiones[0][i] + str(palabras_repeticiones[1][i])
    return cadena


if __name__ == "__main__":
    cadena = input("Ingrese una cadena: ")
    print('\n'+construir_cadena(detectar_patrones(cadena))+'\n')