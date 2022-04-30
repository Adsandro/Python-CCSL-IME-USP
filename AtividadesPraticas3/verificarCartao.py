meucartao = int(input("informe seu cartão de crédito"))
cartaoaveriguado = 1

while meucartao != cartaoaveriguado and cartaoaveriguado != 0:
    cartaoaveriguado = int(input("informe os cartoes para averiguar"))

if meucartao != cartaoaveriguado:
    print("ufa, meu cartão não foi clonado")
else:
    print("Droga meu cartão foi clonado")
    
