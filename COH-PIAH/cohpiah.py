import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma_temp = 0
    for i in range(0,6):
        soma_temp = soma_temp + (abs(as_a[i] - as_b[i]))
    
    return soma_temp / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    meia_palavras = 0
    meio_sentencas = 0
    comp_sentenca = 0
    rel_type_token = 0
    hapax = 0
    soma_car_sentenca = 0
    soma_pal = 0
    soma_car_frase = 0
    tam_meio_frase = 0

    for sentenca in sentencas:      
        soma_car_sentenca = soma_car_sentenca + len(sentenca)        
        l_frases = separa_frases(sentenca)

        for f in l_frases:
            frases.append(f)

    for frase in frases:
        soma_car_frase = soma_car_frase + len(frase)
        l_pal = separa_palavras(frase)

        for palavra in l_pal:
            palavras.append(palavra)    
    
    for palavra in palavras:
        soma_pal = soma_pal + len(palavra)
    
    meia_palavras = soma_pal/len(palavras)
    rel_type_token = n_palavras_diferentes(palavras)/len(palavras)
    hapax = n_palavras_unicas(palavras)/len(palavras)
    meio_sentencas = soma_car_sentenca / len(sentencas)
    comp_sentenca = len(frases) / len(sentencas)
    tam_meio_frase = soma_car_frase / len(frases)

    return [meia_palavras, rel_type_token, hapax, meio_sentencas, comp_sentenca, tam_meio_frase]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    inf = []
    
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        inf.append(compara_assinatura(ass_texto, ass_cp))

    menor = inf[0]
    c = 1

    for i in range(1, len(inf)):
        if (menor > inf[i]):
            c = i
    return c

def main():        
    assinatura = le_assinatura()
    textos = le_textos()
    c = avalia_textos(textos, assinatura)
    print("O autor do texto {} está infectado com COH-PIAH".format(c))

main()
 
