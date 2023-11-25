import json

def cargar_indice_desde_json(ruta_json):
    with open(ruta_json, 'r', encoding='utf-8') as f:
        indice_invertido = json.load(f)
    return indice_invertido

def buscar_en_indice(query, indice):
    resultados = {}

    # Buscar en el índice invertido
    if query in indice:
            for documento, frecuencia in indice[query].items():
                if documento not in resultados:
                    resultados[documento] = 0
                resultados[documento] += frecuencia

    # Ordenar los resultados por relevancia (mayor a menor)
    resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

    # Devolver los resultados ordenados
    return resultados_ordenados[:5]

# Ruta del archivo JSON con el índice invertido
ruta_json = '../convertir_a_JSON/indice_invertido.json'

# Cargar el índice invertido desde el archivo JSON
indice_invertido = cargar_indice_desde_json(ruta_json)

# Consulta del usuario
consulta_usuario = input("Ingrese la consulta de búsqueda: ")

# Realizar la búsqueda
resultados_busqueda = buscar_en_indice(consulta_usuario, indice_invertido)

paginas = ["Daddy_Yankee", "Héctor_el_Father", "J_Álvarez", "Ñengo_Flow", "Cosculluela", 
           "Julio_Voltio", "Ñejo_%26_Dálmata","Arcángel_%26_De_la_Ghetto", "Don_Omar", 
           "Tego_Calderón", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "1","2","3",
           "4","5","6","7","8","9","10"]

# Mostrar los resultados
print("\n...Las mejores 5 búsquedas:")
for resultado in resultados_busqueda:
    documento, puntaje = resultado
    url = 'https://es.wikipedia.org/wiki/'
    print(f'Número Documento: {documento}, Frecuencia: {puntaje}, URL: {url+paginas[int(documento)-1]}')
