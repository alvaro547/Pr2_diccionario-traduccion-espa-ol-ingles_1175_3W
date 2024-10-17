print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Crear un diccionario vacío para almacenar las traducciones
diccionario_traduccion = {}

# Solicitar al usuario que ingrese las palabras en español e inglés
entrada = input("Ingrese las traducciones en el formato 'palabra_español:palabra_ingles' separadas por comas: ")

# Procesar la entrada del usuario
for par in entrada.split(","):
    # Separar la palabra en español y su traducción en inglés
    espanol, ingles = par.split(":")
    # Añadir al diccionario
    diccionario_traduccion[espanol.strip()] = ingles.strip()

# Mostrar el diccionario creado
print("Diccionario de traducción:", diccionario_traduccion)

# Pedir una frase en español para traducir
frase_espanol = input("Ingrese una frase en español para traducir: ")

# Traducir la frase palabra por palabra
frase_traducida = []

# Separar la frase en palabras y traducir cada una
for palabra in frase_espanol.split():
    # Traducir la palabra si está en el diccionario, si no, dejarla sin traducir
    traduccion = diccionario_traduccion.get(palabra, palabra)
    frase_traducida.append(traduccion)

# Unir las palabras traducidas en una frase
frase_final = ' '.join(frase_traducida)

# Mostrar la frase traducida
print("Frase traducida:", frase_final)
