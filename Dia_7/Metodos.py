class Pajaro:

    alas = True

    def __init__(self, color, especie):

        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, mi color es {self.color}') 

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


mi_pajaro = Pajaro('rojo', 'canario')
mi_pajaro.piar()
mi_pajaro.volar(50)


