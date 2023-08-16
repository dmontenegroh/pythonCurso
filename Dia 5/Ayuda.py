
# Práctica Métodos y Ayuda 1
# Remueve los caracteres a la izquierda de nuestro texto principal:

# ,

# :

# %

# _

# #

# Utiliza el método lstrip(). Imprime el resultado en pantalla:

# ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa. Puedes utilizar variables intermedias si las necesitas.



## INVESTIGACION: 
# lstrip() es un método en Python que se utiliza para eliminar caracteres específicos (espacios en blanco por defecto) del lado izquierdo (inicio) de una cadena (string). El nombre "lstrip" proviene de "left strip", lo que significa "recortar a la izquierda".

# Donde:
# 'string' es la cadena de texto en la que deseas realizar el recorte.
# 'chars' (opcional) es un argumento que especifica los caracteres que deben eliminarse del lado izquierdo de la cadena. Si no se proporciona, por defecto elimina espacios en blanco (espacios, tabulaciones y saltos de línea).
# Veamos algunos ejemplos para entender mejor cómo funciona lstrip():

# Ejemplo 1: Eliminar espacios en blanco del lado izquierdo de una cadena:
# text = "    Hola, mundo!"
# new_text = text.lstrip()
# print(new_text)  # Output: "Hola, mundo!"

# Ejemplo 2: Eliminar caracteres específicos del lado izquierdo de una cadena:
text = "!!!Hola, mundo!"
new_text = text.lstrip("!")
print(new_text)  # Output: "Hola, mundo!"

# Ejemplo 3: Eliminar diferentes tipos de caracteres del lado izquierdo:
text = "\t\t\tHola, mundo!"
new_text = text.lstrip("\t")
print(new_text)  # Output: "Hola, mundo!"
# En estos ejemplos, puedes ver cómo lstrip() elimina los caracteres proporcionados (en este caso, espacios en blanco o caracteres específicos) del lado izquierdo de la cadena. Es importante tener en cuenta que lstrip() no modifica la cadena original; en su lugar, devuelve una nueva cadena con los caracteres recortados.

# Cuando deseas eliminar varios caracteres especiales del lado izquierdo de una cadena, simplemente proporcionas todos esos caracteres como una cadena en el argumento chars de la función lstrip(). La función eliminará todos los caracteres en ese conjunto del lado izquierdo de la cadena hasta que encuentre un caracter que no esté en ese conjunto.

# Aquí hay un ejemplo para ilustrar esto:
text = "##**Hola, mundo!"
new_text = text.lstrip("#*")
print(new_text)  # Output: "Hola, mundo!"

# En este ejemplo, la función lstrip() elimina todos los caracteres "#" y "*" del lado izquierdo de la cadena hasta llegar a la letra "H", que no es un carácter en el conjunto "#*".

# Ten en cuenta que el orden de los caracteres en el argumento chars no afecta el resultado, ya que la función simplemente elimina cualquiera de esos caracteres en el orden en que aparecen en la cadena.


# ---------------------------------------------------------------- 

# Práctica Métodos y Ayuda 2
# Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando

# el método insert():

# frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.

# El método insert() se utiliza en Python para insertar un elemento en una lista en una posición específica. Toma dos argumentos: el índice en el que deseas insertar el elemento y el elemento que deseas insertar. Después de la inserción, los elementos existentes se desplazarán hacia la derecha para dar espacio al nuevo elemento.

# La sintaxis básica del método insert() es la siguiente:}
# lista.insert(indice, elemento)

# Donde:
# lista es la lista en la que deseas realizar la inserción.
# indice es la posición en la que deseas insertar el elemento. Debe ser un valor entre 0 y la longitud actual de la lista (inclusive).
# elemento es el valor que deseas insertar en la lista.

# frutas = ["manzana", "banana", "pera"]
# frutas.insert(1, "naranja")  # Insertar "naranja" en la posición 1
# print(frutas)  # Output: ["manzana", "naranja", "banana", "pera"]

# En este ejemplo, se ha insertado la cadena "naranja" en la posición 1 de la lista frutas, desplazando las otras frutas hacia la derecha.

# Si el índice proporcionado es mayor que la longitud actual de la lista, el elemento se agregará al final de la lista. Por ejemplo:

# numeros = [1, 2, 3]
# numeros.insert(10, 4)  # Insertar 4 en la posición 10 (más allá del final)
# print(numeros)  # Output: [1, 2, 3, 4]

# Recuerda que las listas en Python están indexadas desde 0, por lo que el primer elemento está en la posición 0, el segundo en la posición 1 y así sucesivamente.

# ----------------------------------------------------------------
# Práctica Métodos y Ayuda 3
# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:

# marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.

# El método isdisjoint() se utiliza en Python para determinar si dos conjuntos (sets) no tienen elementos en común. En otras palabras, devuelve True si los dos conjuntos son disjuntos (no comparten ningún elemento) y False si tienen al menos un elemento en común.

# La sintaxis del método isdisjoint() es la siguiente:
# set1.isdisjoint(set2)

# Donde:
# set1 y set2 son dos conjuntos que deseas comparar.
# Aquí hay un ejemplo para ilustrar el uso del método isdisjoint():

set_a = {1, 2, 3}
set_b = {4, 5, 6}
set_c = {3, 6, 9}

result_ab = set_a.isdisjoint(set_b)  # No tienen elementos en común
result_ac = set_a.isdisjoint(set_c)  # Tienen el elemento 3 en común

# print(result_ab)  # Output: True
# print(result_ac)  # Output: False

# En este ejemplo, set_a y set_b no tienen elementos en común, por lo que result_ab es True. Sin embargo, set_a y set_c comparten el elemento 3, por lo que result_ac es False.

# Recuerda que isdisjoint() se utiliza específicamente para conjuntos (sets) en Python. Si intentas usarlo con otros tipos de colecciones, como listas o tuplas, obtendrás un error, ya que este método está diseñado para trabajar con la estructura de datos de conjunto.