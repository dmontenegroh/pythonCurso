# import os

# ruta = os.getcwd()

# cambiar directorio
# ruta = os.chdir('C:\\Users\\diego.montenegro\\Desktop\\Documentos')


# CREAR directorio
# ruta = os.makedirs('C:\\Users\\diego.montenegro\\Desktop\\Documentos\\otra')

# archivo = open('otro_archivo.txt')

# print(archivo)


# ruta = 'C:\\Users\\diego.montenegro\\Desktop\\Documentos\\otro_archivo.txt'
# # elemento = os.path.dirname(ruta)
# elemento = os.path.split(ruta)
# print(elemento)

# eliminar directorio
# os.rmdir('C:\\Users\\diego.montenegro\\Desktop\\Documentos\\otra')

# otro_archivo = open('C:\\Users\\diego.montenegro\\Desktop\\Documentos\\otro_archivo.txt')

# print(otro_archivo.read())


from pathlib import Path

# carpeta = Path('C:/Users/diego.montenegro/Desktop/Documentos')
# archivo = carpeta / 'otro_archivo.txt'
carpeta = Path('C:/Users/diego.montenegro/Desktop/Documentos') / 'otro_archivo.txt'

mi_archivo = open(carpeta)
print(mi_archivo.read())
