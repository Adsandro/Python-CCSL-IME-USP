linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end = "\t") #\t da um tab a cada item impresso
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1

# repetições encaixadas (uso de while dentro de while)