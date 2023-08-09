texto = "ABCDEFGHIKJLM"
# fragmento = texto[2] # Solamente el indice 2
# fragmento = texto[2:] # Desde el indice 2 hasta el final
# fragmento = texto[:5] # Desde el inicio hasta el indice 5
# fragmento = texto[2:5] # Desde la posicison 2 hasta la 5
# fragmento = texto[2:10:3] # el ultimo valor son los saltos que dan desde el indice 0 hasta el ultimo
# fragmento = texto[::3] # Desde el 0 dando saltos de 3 en 3
fragmento = texto[::-1] # Negativo cambia el orden a inverso


print(fragmento)
