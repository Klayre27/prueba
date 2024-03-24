# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Jennyfer",
    "edad": 21,
    "ciudad": "Coca",
    "profesion": "Ingeniera"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Nueva Ciudad"

# Agregar una nueva clave-valor para representar la profesión
informacion_personal["profesion"] = "Ingeniera de Tegnologias de la Informacion"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0969933727"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario Final:")
print(informacion_personal)
