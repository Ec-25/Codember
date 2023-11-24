from os.path import exists


def separar_valores(line: str):
    """Devuelve una tupla de forma Int,Int,Str,
    siendo el primer entero el minimo valor,
    el segundo el maximo valor y el tercero la letra a buscar"""
    val1 = line.split("-")[0]
    val2 = (line.split("-")[1]).split(" ")[0]
    val3 = (line.split("-")[1]).split(" ")[1]
    return (int(val1), int(val2), val3)


def detectar_linea(line: str):
    """Devuelve la clave que cumple con la condicion obtenida en separar_valores(),
    o nada en caso de que no cumpla lo requerido"""
    bloc = line.split(": ")
    key = bloc[1][:-1]
    cond = separar_valores(bloc[0])

    if cond[0] <= key.count(cond[2]) <= cond[1]:
        return (True, key)

    return (False, key)


def read_file(path: str):
    """Lee y valida las cadenas del documento"""
    valids = []
    invalids = []

    if exists(path):
        with open(path, "r") as file:
            for line in file:
                cad = detectar_linea(line)
                if cad[0]:
                    valids.append(cad[1])

                else:
                    invalids.append(cad[1])

    return (valids, invalids)


def main():
    # leer y comprobar cadena de texto
    valids, invalids = read_file("challenge03\string.txt")

    # mostrar resultados
    print("Total Valids Passwords: ", len(valids))
    print("Password Selected: ", invalids[41])
    print("Secret Password: ", invalids[12])


if __name__ == "__main__":
    main()
