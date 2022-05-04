def soma_elementos (lista):
    soma = 0
    for numero in lista: 
        soma += numero
    return soma
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = soma_elementos(lista)
print(lista) 


