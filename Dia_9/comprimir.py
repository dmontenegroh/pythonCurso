# import zipfile
import shutil


# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

# mi_zip.write('Dia_9/mi_texto_A.txt')
# mi_zip.write('Dia_9/mi_texto_B.txt')

# mi_zip.close()


# zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

# zip_abierto.extractall()

# carpeta_origen = 'C:\\Users\\diego.montenegro\\Desktop\\PYTHON CURSO'

# archivo_destino = 'Todo_Comprimido'

# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('Todo_Comprimido.zip', 'Extraccion_Todo', 'zip')
