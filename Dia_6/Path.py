from pathlib import Path


# base = Path.home()  # Ruta absoluta ej: C:\Users\user_name
# # C:\Users\user_name\Barcelona\Sagrada_Familia.txt
# guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))

# guia2 = guia.with_name("La_Pedrera.txt")

# print(base)
# print(guia)
# print(guia.parent.parent.parent)
# print(guia2)


# guia = Path(Path.home(), "Europa")

# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)

# guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
# en_europa = guia.relative_to(Path("Europa"))
# en_espania = guia.relative_to(Path("Europa", "España"))

# print(en_europa)
# print(en_espania)
