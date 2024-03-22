# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
lista_mas_cinco = [1, 2, 3, 4, 5, 6]

# 3. Encuentre la longitud de las dos listas creadas anteriormente.
longitud_lista_vacia = len(lista_vacia)
longitud_lista_mas_cinco = len(lista_mas_cinco)

# 4. Obtener el primer elemento, el elemento central y el último elemento de la lista.
primer_elemento = lista_mas_cinco[0]
elemento_central = lista_mas_cinco[len(lista_mas_cinco) // 2]
ultimo_elemento = lista_mas_cinco[-1]

# 5. Crear una lista llamada Datos_personales que contenga (nombre, edad, altura, estado civil, dirección), y agrega datos utilizando la funcion append().
datos_personales = []
datos_personales.append("Juan")  # Nombre
datos_personales.append(30)  # Edad
datos_personales.append(1.75)  # Altura
datos_personales.append("Soltero")  # Estado civil
datos_personales.append("Calle Falsa 123")  # Dirección

# 6. Crea una lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Añadir una empresa a la lista it_companies utilizando la funcion insert().
it_companies.insert(1, "Samsung")  # Insertando "Samsung" en la posición 1

# 8. Comprobar si una determinada empresa existe en la lista it_companies.
empresa_busqueda = "Apple"
existe_empresa = empresa_busqueda in it_companies

# 9. Ordena la lista con el método sort()
it_companies.sort()

# 10. Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()

# 11. Elimine la primera empresa informática de la lista utilizando el método pop y delete.
primer_empresa = it_companies.pop(0)  # Elimina y devuelve el primer elemento
# Otra opción: del it_companies[0]

# 12. Eliminar todas las empresas de la lista it_companies en python
it_companies.clear()

# Imprimir resultados
print("Lista vacía:", lista_vacia)
print("Lista con más de 5 elementos:", lista_mas_cinco)
print("Longitud de lista vacía:", longitud_lista_vacia)
print("Longitud de lista con más de 5 elementos:", longitud_lista_mas_cinco)
print("Primer elemento de lista_mas_cinco:", primer_elemento)
print("Elemento central de lista_mas_cinco:", elemento_central)
print("Último elemento de lista_mas_cinco:", ultimo_elemento)
print("Datos personales:", datos_personales)
print("Lista de empresas de tecnología:", it_companies)
print("¿La empresa", empresa_busqueda, "existe en la lista de empresas de tecnología?:", existe_empresa)
print("Lista de empresas de tecnología ordenada alfabéticamente:", it_companies)
print("Lista de empresas de tecnología en orden descendente:", it_companies)
print("Primera empresa eliminada:", primer_empresa)
