mi_archivo = open('Material_PDF/DIA_6/Prueba.txt')


# print(mi_archivo.read())
# una_linea = (mi_archivo.readline())
# print(una_linea)
# mi_archivo.close()


todas = mi_archivo.readlines()

todas = todas.pop()

print(todas)
