# Com parênteses significa conjunto
a = (0,1,2,3,4,5,6,7)
b = (0,2,4,6,8)

# Interseção
print(set(a) & set(b))

# União
print(set(a) | set(b))

# Diferença
print(set(a).difference(set(b)))
print(set(b).difference(set(a)))