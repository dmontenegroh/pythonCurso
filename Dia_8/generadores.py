# def mi_funcion():

#     lista = []
#     for x in range(1, 5):
#         lista.append(x*10)
#     return lista


# def mi_generador():

#     for x in range(1, 5):
#         yield x*10


# print(mi_funcion())
# print(mi_generador())

# g = mi_generador()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def mi_generador():

#     x = 1
#     yield x

#     x += 1

#     yield x

#     x += 1

#     yield x


# g = mi_generador()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def mi_generador():
#     x = 1
#     yield x
#     while True:
#         x += 1
#         yield x


# generador = mi_generador()

# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))


# def mi_generador():
#     x = 7
#     while True:
#         yield x
#         x += 7


# generador = mi_generador()

# print(next(generador))
# print(next(generador))


# def mi_generador():

#     for x in range(1, 5):
#         x -= 1
#         if (x == 3):
#             yield "Te quedan 3 vidas"
#         elif (x == 2):
#             yield "Te quedan 2 vidas"
#         elif (x == 1):
#             yield "Te quedan 1 vidas"
#         elif (x == 0):
#             yield "Game Over"


# g = mi_generador()

# print(next(g))

def mi_generator():
    vidas = "Te quedan 3 vidas"
    yield vidas
   
    vidas = "Te quedan 2 vidas"
    yield vidas
   
    vidas = "Te queda 1 vida"
    yield vidas
   
    vidas = "Game Over"
    yield vidas
    
perder_vida = mi_generator()

