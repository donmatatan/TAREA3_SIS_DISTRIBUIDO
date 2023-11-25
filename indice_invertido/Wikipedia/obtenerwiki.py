import wikipedia

paginas = ["Daddy_Yankee", "Héctor_el_Father", "J_Álvarez", "Ñengo_Flow", "Cosculluela", "Julio_Voltio", "Ñejo_y_Dálmata","Arcángel_y_De_la_Ghetto", "Don_Omar", "Tego_Calderón", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "1","2","3","4","5","6","7","8","9","10"]
cuenta = 0

# Proporciona un user agent, por ejemplo, el nombre de tu aplicación o biblioteca
user_agent = "MiAplicacion/1.0 (https://github.com/tu_usuario/tu_repositorio)"


wikipedia.set_lang("es")
wikipedia.set_user_agent(user_agent)

#print(wikipedia.page("a").content )
for pagina in paginas:
    try:
        texto = wikipedia.page(pagina).content
        cuenta += 1
        if cuenta <= 15:
            nombre = "carpetaUno/" + pagina + ".txt"
        else:
            nombre = "carpetaDos/" + pagina + ".txt"
        print(nombre + " - " + str(cuenta))
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(str(cuenta) + ".txt" + "\n")
            f.write(texto)
            f.write("\n")
    except wikipedia.exceptions.WikipediaException as e:
        print(f"Error al obtener la página {pagina}: {e}")


