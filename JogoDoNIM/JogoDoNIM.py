def computador_escolhe_jogada (n, m):
    computadorRemove = 1
    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove
        else:
            computadorRemove += 1
    return computadorRemove


def usuario_escolhe_jogada (n, m):
    jogadaValida = False 
    while not jogadaValida:
        jogadorRemove = int(input("informe o numero de peças a ser retirada?"))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print('jogada invalida, tente novamente')
            print()
        else:
            jogadaValida = True
        return jogadorRemove
    
def campeonato ():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('rodada:', numeroRodada)
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')
    
    
def partida ():
    n = int(input("Numero de peças?"))
    m = int(input("limite de peças por jogada?"))
    vezdoPC = False
    if n % (m+1) == 0:
        print()
        print("Você começa")
    else:
        print()
        print("computador começa!")
        vezdoPC = True
        
    while n > 0:
        if vezdoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print("computador removeu uma peça")
            else:
                print()
                print("computador removeu", computadorRemove, "peças")
            vezdoPC = False

        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print("você removeu uma peça")
            else:
                print()
                print("voce removeu", jogadorRemove, "peças")
            vezdoPC = True
        
    
        if  n == 1:
            print()
            print("restam apenas uma peça no tabuleiro")
        else:
            if n != 0:
                print("restam", n, "peças no tabuleiro")
                print()
    print("fim do jogo, o computador ganhou!")

print("bem vindo ao jogo do nim")
print()

print("1 - para jogar partida isolada")
tipoDePartida = int(input("2 - para jogar campeonato"))

if tipoDePartida == 2:
    print()
    print("você selecionou campeonato")
    print()
    campeonato()

else:
    if tipoDePartida == 1:
        print()
        partida()