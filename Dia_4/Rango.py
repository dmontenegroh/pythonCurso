# for numero in range(1,5):
#     print(numero)


# lista = list(range(1,101))
# print(lista)

# lista = list(range(3,301, 3)) # Ultimo parametro son los saltos, tambien podria decirse que son los multiplos este caso multiplos de 3
# print(lista)


# Práctica Rango 3
# Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.

# Para ello:

# Crea un rango de valores que puedas recorrer en un loop

# Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).

# Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.

# 1240 RESULTADO ESPERADO

suma_cuadrados = 0
for i in range(1, 16):
    # valor_cuadrado = i**2
    # suma_cuadrados = suma_cuadrados + valor_cuadrado
    suma_cuadrados += int(i**2)

print(suma_cuadrados)
