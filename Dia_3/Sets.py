# mi_set = set([1,2,3,4,5])
# print(type(mi_set))
# print(len(mi_set))
# print(2 in mi_set)


# otro_set = {1,2,3}
# print(type(otro_set))
# print(otro_set)

################################################################
# Union de Sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
# print(s3)

# Agregar
s1.add(2)
s1.add(4)

# Eliminar
s1.remove(1)

# Descartar
s1.discard(6)

# POP
# s1.pop()
# sorteo = s1.pop()

# Clear
s1.clear()
print(s1)
