import re

# texto = "Si necesitas ayuda llama al (658)-598-9977 las 24horas al servicio de ayuda online"

# # palabra = 'ayuda' in texto
# # print (palabra)

# patron = 'ayuda'

# busqueda = re.search(patron, texto)
# print (busqueda)


# texto = "Llama al 567-566-3435 ya mismo"
# # patron = r'\d{3}-\d{3}-\d{4}'
# patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# resultado = re.search(patron, texto)
# print(resultado.group())


# clave = input("Clave: ")
# patron = r'\D{1}\w{7}'

# chequear = re.search(patron, clave)
# print(chequear)


texto = "5No atendemos los lunes por la tarde6"

# buscar = re.search(r'lunes|martes', texto)
# buscar = re.search(r'....demos', texto)
# buscar = re.search(r'^\D$', texto)
buscar = re.findall(r'[^\s]+', texto)

print(''.join(buscar))


def verificar_email(email):
    patron = r'\w+\@\w+\.com'

    resultado = re.search(patron, email)

    if resultado:

        print("Ok")

    else:

        print("La dirección de email es incorrecta")


def verificar_saludo(frase):
    patron = r'hola|Hola|HOLA'

    if re.match(patron, frase):
        print("Ok")

    else:
        print("No has saludado")


def verificar_cp(cp):
    patron = r"CP\d{4}"
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp("CP5000")  # Ok
verificar_cp("C50000")  # El código postal ingresado no es correcto
verificar_cp("95542634")  # El código postal ingresado no es correcto
