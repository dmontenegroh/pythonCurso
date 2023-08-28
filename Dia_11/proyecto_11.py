import bs4
import requests

# crear un url sin numero de pagina
url = base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):
    # crear sopa en cada pagina
    url_pagina = url.format(pagina)
    resultado = requests.get(url_pagina)
    soup = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = soup.select('.product_pod')

    # iterar libros
    for libro in libros:
        # chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver los libros de 4 u 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)


# resultado = requests.get(url.format('1'))
# sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


# libros = sopa.select('.product_pod')

# ejemplo = libros[0].select('a')[1]['title']
# print(ejemplo)


# for n in range(1, 11):
#     print(url.format(n))
