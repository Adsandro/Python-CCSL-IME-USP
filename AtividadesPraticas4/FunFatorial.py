def fatorial(n):
    fat = 1 # trata-se de uma multiplicação, portante deve ser selecionado o 1 e não o 0, ja que 0X10= 0
    while (n > 1):
        fat = fat * n  #inicia multiplicando pelo valor selecionado
        n = n - 1 #subtrai 1 do valor selecionado para realizar o laço de repetição
    return fat
def NumBinominal(n, k):
    if k > n:
        print("Os valores estão incorretos,  N deve ser maior que K.")
    else:
        return fatorial(n)// (fatorial(k)*fatorial(n - k))
print(NumBinominal(200, 100))