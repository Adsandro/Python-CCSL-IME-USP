# Enquanto = while
print("Digite uma sequencia de valores terminadas por zero.")
soma = 0
valor = 1
while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor
print("a soma dos valores digitados é", soma)