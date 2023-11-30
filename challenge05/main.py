
import re

# Función para validar el formato del email
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

# Función para verificar la validez de la entrada
def validate_entry(entry):
    data = entry.split(',')
    if len(data) < 3:  # Verificar que hay al menos 3 elementos
        return False
    if not data[0].isalnum() or not data[1].isalnum():  # Validar id y username alfanuméricos
        return False
    if not validate_email(data[2]):  # Validar el formato del email
        return False
    if data[3] and not data[3].isdigit():  # Verificar si age está presente y es un número
        return False
    return True

# Lista para almacenar usuarios inválidos
invalid_users = []

# Leer el archivo de la base de datos
with open('challenge05/string.txt', 'r') as file:
    entries = file.readlines()
    for index, entry in enumerate(entries, start=1):
        if not validate_entry(entry.strip()):
            invalid_users.append(entry.strip())
            # print(f"Usuario inválido en la línea {index}: {entry.strip()}")

# Obtener el primer caracter del username de usuarios inválidos
first_chars = ''.join([user.split(',')[1][0] for user in invalid_users])

print("\nPrimer caracter del username de usuarios inválidos:")
print(first_chars)
