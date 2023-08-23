# from collections import Counter
# from collections import defaultdict
from collections import namedtuple

# numeros = [8, 7, 4, 7, 2, 5, 5, 2, 1, 7, 8, 2, 4, 7, 5,
#            3, 1, 6, 8, 9, 5, 3, 56, 7, 9, 6, 4, 634, 6, 4, 6]

# print(Counter(numeros))


# serie = Counter([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4])
# print(serie.most_common(2))
# print(list(serie))


# mi_dic = defaultdict(lambda: 'nada')

# mi_dic['uno'] = 'verde'
# print(mi_dic['dos'])

# print(mi_dic)

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 69)
print(ariel.altura)
