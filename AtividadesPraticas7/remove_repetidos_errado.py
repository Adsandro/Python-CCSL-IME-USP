def remove_repetidos (lista):
    lista_ordenada = sorted(lista)
    if lista_ordenada[0] == lista_ordenada[1]:
        del lista_ordenada[1]
    else:
        lista_ordenada[0] = lista_ordenada[0] + 1
        lista_ordenada[1] = lista_ordenada[1] + 1


lista = [5, 4, 6, 2, 6, 3, 7, 3, 6, 2, 6]

lista = remove_repetidos (lista_ordenada)
print(lista)

print(pype(lista))