def chequear_3_cifras(lista):
    # return numero in range(100,1000)
    lista_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras


# suma = 886 + 305
# resultado = chequear_3_cifras(suma)
# resultado = chequear_3_cifras([55, 99, 100])
# print(resultado)


# Práctica Funciones Dinámicas 1
# Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

# No invoques la función, solo es necesario definirla.

# def todos_positivos(lista):
#     for n in lista:
#         if (n < 0):
#             return False

#     return True


# resultado = todos_positivos([-1, 0, 5, 5, 2, 64])
# print(resultado)


# Práctica Funciones Dinámicas 2
# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

# def suma_menores(lista):
#     suma = 0
#     for n in lista:
#         if n > 0 and n < 1000:
#             suma = suma + n
#     return suma
# lista_numeros = [-1,50,99,1000]
# resultado = suma_menores(lista_numeros)
# print(resultado)


# Práctica Funciones Dinámicas 3
# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.

def cantidad_pares(lista):
    cantidad = 0
    for n in lista:
        if n % 2 == 0: 
            cantidad += 1
    
    return cantidad

lista_numeros = [2,5,7]
resultado = cantidad_pares(lista_numeros)
print(resultado)