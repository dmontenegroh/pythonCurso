# def suma(**kwargs):
#     # print(type(kwargs))

#     total = 0


#     for clave, valor in kwargs.items():
#         print(f"{clave} = {valor}")

#         total += valor

#     return total

# print(suma(x=3, y=5, z=2))

# def prueba(num1, num2, *args, **kwargs):

#     print(f'El primer valor es {num1}')
#     print(f'El segundo valor es {num2}')

#     for arg in args:
#         print(f'arg = {arg}')

#     for clave, valor in kwargs.items():
#         print(f"{clave} = {valor}")


# args = [100, 200, 300, 400]
# kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}

# prueba(15, 50, *args, **kwargs)


# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.


# def cantidad_atributos(**kwargs):

#     return len(kwargs)

# cantidad_atributos(x=10,t=40,g=22)


# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

# def lista_atributos(**kwargs):
#     lista = []
#     for valor in kwargs.values():
#         lista.append(valor)

#     return lista


# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:

# describir_persona("María", color_ojos="azules", color_pelo="rubio")

# Mostrará en pantalla:

# Características de María:
# color_ojos: azules
# color_pelo: rubio


# def describir_persona(nombre, **kwargs):

#     print(f'Características de {nombre}:')

#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# describir_persona('Diego', color_ojos="azules", color_pelo="rubio")