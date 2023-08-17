# Escribe una función que requiera una cantidad indefinida deargumentos. Lo que hará esta función es devolver True si enalgún momento se ha ingresado al numero cero repetido dosveces consecutivas.
# Por ejemplo:(5,6,1,0,0,9,3,5) >>> True(6,0,5,1,0,3,0,1) >>> False

def ceros_vecinos(*args):

    contador = 0

    for num in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1

    return False


print(ceros_vecinos(5, 6, 3, 6, 2, 7, 9, 5, 9, 0))
