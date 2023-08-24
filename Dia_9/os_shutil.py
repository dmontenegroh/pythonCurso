import os
import shutil
import send2trash

# shutil.move('curso.txt', 'C:\\Users\\diego.montenegro\\Desktop\\PYTHON CURSO\\Dia_9')


# archivo = open('curso.txt', 'w')
# archivo.write('Texto de prueba')
# archivo.close()


# print(os.listdir())


# send2trash.send2trash('./Dia_9/curso.txt')

ruta = "C:\\Users\\diego.montenegro\\Desktop\\PYTHON CURSO"
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'en la carpeta: {carpeta}')
    print(f'Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')


