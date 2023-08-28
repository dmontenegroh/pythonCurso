import bs4
import requests

# resultado = requests.get('https://www.google.cl/?hl=es')
# resultado = requests.get('https://escueladirecta-blog.blogspot.com/2023/04/power-pivot-analisis-y-modelado-de.html')
# resultado = requests.get('https://www.biobiochile.cl/noticias/nacional/region-del-bio-bio/2023/08/28/queman-cinco-cabanas-de-veraneo-en-nuevo-ataque-incendiario-en-provincia-de-arauco.shtml')
# print(resultado.text)

# soup = bs4.BeautifulSoup(resultado.text, 'lxml')

# Imprimir el HTML formateado
# print(len(soup.select('a')))
# print(len(soup.select('h2')))

# print(soup.select('a')[0].getText())

# post_favoritos = soup.select('.PopularPosts')
# print(post_favoritos)
# creditos = soup.select('.autores span')
# print(creditos)

# for p in creditos:
#     print(p.getText())


pagina = requests.get('https://www.escueladirecta.com/courses')
sopa = bs4.BeautifulSoup(pagina.text, 'lxml')

img = sopa.select('.course-box-image')[0]['src']
# for i in img:
#     print(i['src'])


# print(img)
imagen_curso_1 = requests.get(img)
# print(imagen_curso_1.content)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()