# Pure Windows Path = Ruta de Windows Pura
from pathlib import Path, PureWindowsPath
carpeta = Path(
    'C:/Users/diego.montenegro/Desktop/PYTHON CURSO/Dia_6/prueba.txt')


ruta_windows = PureWindowsPath(carpeta)

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.stem)  # nombre sin extension
print(carpeta.suffix)  # extension

# metodo para saber si existe

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("SI EXISTE")

# .exists() devuelve True o False

print(ruta_windows)
