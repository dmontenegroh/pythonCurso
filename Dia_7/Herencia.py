# class Animal:

#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color

#     def nacer(self):
#         print("Este animal ha nacido")


# class Pajaro(Animal):
#     pass


# piolin = Pajaro(2, 'amarillo')


# HERENCIA EXTENDIDA
from os import system
system('cls')


# class Animal:

#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color

#     def nacer(self):
#         print("Este animal ha nacido")

#     def hablar(self):
#         print("Este animal emite un sonido")


# class Pajaro(Animal):

#     # def __init__(self, edad, color, altura_vuelo):
#     #     self.edad = edad
#     #     self.color = color
#     #     self.altura_vuelo = altura_vuelo

#     def __init__(self, edad, color, altura_vuelo):
#         super().__init__(edad, color)
#         self.altura_vuelo = altura_vuelo

#     def hablar(self):
#         print("pio")

#     def volar(self, metros):
#         print(f"el pajaro vuela {metros} metros")


# piolin = Pajaro(2, 'amarillo', 60)
# mi_animal = Animal(5, 'negro')

# mi_animal.nacer()


class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print('ja ja')

    def hablar(self):
        print("Que tal")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


