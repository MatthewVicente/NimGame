# FUNCTIONS

#Checa se o numero passado é multiplo do total de peças
def ehMultiplo(n, m):
    aux = m+1
    if n % aux == 0:
        return True

    return False

# Computador decide jogada a ser feita
def  computador_escolhe_jogada(pecasTabuleiro, maxPecas):
    i = 1
    while i < maxPecas:
        resto_pecas = pecasTabuleiro - i

        if ehMultiplo(resto_pecas, maxPecas):
            print("")
            print("PC tira "+str(i)+" pecas")
            return i

        i += 1

    print("COMP tira " + str(maxPecas) + " pecas")
    return maxPecas

# Jogador decide jogada a ser feita
def  usuario_escolhe_jogada(pecasTabuleiro, maxPecas):
    num_retira = int(input("Escolha quantas peças deseja retirar, lembre-se que deve estar entre o limite estabelecido: "))

    while num_retira > maxPecas or num_retira <= 0:
        num_retira = int(input("Digite um valor válido, lembre-se que deve estar entre o limite estabelecido: "))

    return num_retira

# Exibe status do jogo
def mostra_status(vezJogador):
    print("")
    print("------------------------------")
    print("NIM")
    print("Pecas em campo: " + str(pecaEmJogo))
    print("------------------------------")
    print("")
    print("SUA VEZ" if vezJogador else "VEZ DO PC")

# GAME

print("Bem vindo ao Jogo Nim!")

numPecas = int(input("Digite o número de peças: "))
maxTiraPecas = int(input("Digite o número máximo de peças que podem ser tiradas por jogada: "))
pecaEmJogo = numPecas
vezJogador = False

if not ehMultiplo(pecaEmJogo, maxTiraPecas):
    mostra_status(False)
    pecaEmJogo -= computador_escolhe_jogada(pecaEmJogo, maxTiraPecas)
    vezJogador = True
else:
    mostra_status(True)
    pecaEmJogo -= usuario_escolhe_jogada(pecaEmJogo, maxTiraPecas)
    vezJogador = False

while pecaEmJogo > 0:
    mostra_status(vezJogador)
    if vezJogador:
        pecaEmJogo -= usuario_escolhe_jogada(pecaEmJogo, maxTiraPecas)
        vezJogador = False
    else :
        pecaEmJogo -= computador_escolhe_jogada(pecaEmJogo, maxTiraPecas)
        vezJogador = True

if vezJogador:
    vencedor = "PC"
else:
    vencedor = "VOCE"

print("O jogo acabou, o vencedor foi: "+vencedor)

# ESTRATEGIA: DEIXAR SEMPRE NUMERO DE PECAS NO TABULEIRO IGUAL A N MULTIPLO DE M+1, SENDO N = PECAS NO TABULEIRO E M = MAX QUE POSSO TIRAR