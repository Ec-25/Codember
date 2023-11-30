
def load_file(path:str):
    """Funcion encargada de cargar todos los datos de los archivos,\n
    path: es la ruta relativa desde donde se ejecuta el programa hasta el archivo a leer"""
    filesName = []
    filesChecksum = []

    with open("challenge04/string.txt", "r") as file:
        for line in file:
            if line:
                line = (line.split("\n")[0]).split("-")
                filesName.append(line[0])
                filesChecksum.append(line[1])

    return ( filesName, filesChecksum )


def is_file(fileName:str, fileChecksum:str):
    """fileName: cadena alfanumérica.\n
    fileChecksum: cadena formada por los caracteres que sólo aparecen una vez en la primera parte y en el orden en que aparecen."""
    
    if fileName == fileChecksum:
        return True
    
    req1 = fileName.count(fileChecksum) == 1
    req2 = True

    for i in range(len(fileChecksum)):
        req2 = req2 and fileChecksum.count(fileChecksum[i]) == fileName.count(fileChecksum[i])

    if req1 and req2:
        return True

    return False

if __name__ == "__main__":
    files = load_file("challenge04/string.txt")
    for i in range(len(files[0])):
        if is_file(files[0][i], files[1][i]):
            print(f"{i+1})- ", files[1][i])
