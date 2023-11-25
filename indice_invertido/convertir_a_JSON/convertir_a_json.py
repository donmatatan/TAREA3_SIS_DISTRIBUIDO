import json

# Ruta del archivo de texto de entrada
archivo_txt = 'part-00000'

# Ruta del archivo JSON de salida
archivo_json = 'indice_invertido.json'

# Diccionario para almacenar el índice invertido
indice_invertido = {}

# Leer el archivo de texto y procesar cada línea
with open(archivo_txt, 'r', encoding='utf-8') as f:
    for linea in f:
        # Dividir la línea en partes utilizando espacios o tabs como separadores
        partes = linea.strip().split()

        # La primera parte es la palabra clave
        palabra_clave = partes[0]

        # Resto de las partes representan (documento, frecuencia)
        atributos = {}
        for parte in partes[1:]:
            doc, freq = map(int, parte.strip('()').split(','))
            atributos[str(doc)] = freq

        # Agregar la palabra clave y sus atributos al índice invertido
        indice_invertido[palabra_clave] = atributos

# Escribir el índice invertido en formato JSON
with open(archivo_json, 'w', encoding='utf-8') as f_json:
    json.dump(indice_invertido, f_json, ensure_ascii=False, indent=2)

print(f'Conversión completada. El índice invertido se ha guardado en: {archivo_json}')

