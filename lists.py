# LISTS __________________________________ (CAN CHANGE VALUES)
lista = [1, 2, 7, 3]
listaB = [3, 4, 5, 6]
lista[0] = 1.1

# Add elements
lista.append(4)
print(lista)
# Change values
lista[3] = 3
print(lista)
# Delete last value
lista.pop()
print(lista)
# Concat values
lista.extend(listaB)
print(lista)
# Delete value
del lista[5]
# or
lista.remove(1.1)  # Use an specific value
print(lista)
# Count values
print(lista.count(3))
# Sort
lista.sort()
lista.sort(reverse=True)
print(lista)
# Get last elements
print(lista[-1])
print(lista[-2])
