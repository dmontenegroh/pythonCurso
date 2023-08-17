# monedas = 5

# while monedas > 0:
#     print(f"Tengo {monedas} monedas")
#     # monedas = monedas - 1 # opcion 1
#     monedas -= 1  # opcion 2
# else:
#     print("No tengo más dinero")

respuesta = 's'

# while respuesta == 's':
#     respuesta = input("quieres seguir? (s/n)")
# else:
#     print("Gracias")

# PASS
# while respuesta == 's':
#     pass

# print("hola")

# BREAK
# nombre = input("Tu nombre: ")
# for letra in nombre:
#     if letra == 'r':
#         break
#     print(letra)

# CONTINUE
# nombre = input("Tu nombre: ")
# for letra in nombre:
#     if letra == 'r':
#         continue
#     print(letra)

# numero = 50


# while numero >= 0:
#     if numero % 5 != 0:
#         numero -= 1
#         continue
    
#     print(numero)
#     numero -= 1


# Práctica Interrupción de Flujo
# Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# No debes cambiar el orden de la lista.
for a in lista_numeros:
    if(a >= 0):
        print(a)
    else:
        break

