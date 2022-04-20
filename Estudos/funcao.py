# :def = define
def soma(x , y):
    return x + y #retorna o valor

def multiplica(x, y, z):
    return x * y * z

print(soma(10, 20))
print(soma(-19, 12))

print(soma(12345, 4567))

print(multiplica(2,5,7))
print(multiplica(soma(10, 5), soma(2, 3), multiplica(2, 5, 1)))




# função não definida
def nome_do_seu_time ():
    return "Palmeiras, fiu fiu fiu"

print(nome_do_seu_time())

