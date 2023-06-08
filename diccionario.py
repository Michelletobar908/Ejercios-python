person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# 1. Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
person['twitter'] = '@nicobytes'

# 2. Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
person['name'] = 'Felipe'

# 3. Eliminar el elemento del diccionario con la llave "age".
del person['age']

# 4. Imprimir una lista con las llaves del diccionario.
print(list(person.keys()))

# 5. Imprimir una lista con los valores del diccionario.
print(list(person.values()))
