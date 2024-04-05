
perro = {}

perro['nombre'] = 'caiser'
perro['color'] = 'blanco'
perro['raza'] = 'hosky'
perro['patas'] = 4
perro['edad'] = 2

estudiante = {
    'nombre': 'sebastian',
    'apellido': 'herrera',
    'sexo': 'Masculino',
    'edad': 20,
    'estado civil': 'Soltero',
    'habilidades': ['Programación', 'Diseño gráfico'],
    'país': 'colombia',
    'ciudad': ' cartagena',
    'dirección': 'parques de bolivar'
}

longitud_estudiante = len(estudiante)
print("Longitud del diccionario del estudiante:", longitud_estudiante)

habilidades_valor = estudiante['habilidades']
print("Valor de las habilidades:", habilidades_valor)
print("Tipo de datos de las habilidades:", type(habilidades_valor))

estudiante['habilidades'].extend(['Gestión de proyectos', 'Inglés'])
print("Habilidades actualizadas:", estudiante['habilidades'])

claves_estudiante = list(estudiante.keys())
print("Claves del diccionario del estudiante:", claves_estudiante)

valores_estudiante = list(estudiante.values())
print("Valores del diccionario del estudiante:", valores_estudiante)

estudiante_lista_tuplas = list(estudiante.items())
print("Diccionario del estudiante como lista de tuplas:", estudiante_lista_tuplas)

del estudiante['dirección']
print("Diccionario del estudiante después de eliminar dirección:", estudiante)

del perro
print("El diccionario 'perro' ha sido eliminado.")
