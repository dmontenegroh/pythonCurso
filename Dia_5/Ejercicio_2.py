# Escribe una función (puedes ponerle cualquier nombre quequieras) que reciba cualquier palabra como parámetro, y quedevuelva todas sus letras únicas (sin repetir) pero en ordenalfabético.
# Por ejemplo si al invocar esta función pasamos la palabra"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']


def letras_unicas(palabra):

    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista


print(letras_unicas('entretenido'))