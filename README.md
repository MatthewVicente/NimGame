# NimGame
 This project was developed to exercise python skills and logic.

Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores
jogam alternadamente, retirando
pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1)
peças ao jogador oponente.

Objetivo
Você deverá escrever um programa na linguagem Python, que permita a uma "vítima" jogar o NIM contra o
computador. O computador,
é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir
que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você
começa"
Caso contrário, o computador toma a inciativa de começar o jogo.
Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja
múltiplo de (m+1) ao jogador.
Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

O programa deve implementar:

Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um
inteiro correspondente é próxima jogada do computador de acordo com a estratégia vencedora.

Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e
verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário,
deve solicitar novamente ao usuário que informe uma jogada válida.

Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia
o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha
da jogada inicial deve ser feita em função da  estratégia vencedora, como dito anteriormente. A cada jogada, deve ser
impresso na tela o estado atual do jogo, ou seja, quantas peças foram
removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela
a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.
Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no
tabuleiro e qual é o máximo de peças a retirar em cada jogada.

Campeonatos
Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador. 
Assim, uma vez que a função partida esteja funcionando, você deverá criar uma outra função chamada campeonato. 
Essa nova função deve realizar trás partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e 
indicar o vencedor do campeonato. O placar deve ser impresso na forma


Execução
Dado que é possével jogar partidas individuais ou campeonatos, seu programa deve começar solicitando ao usuário que
escolha se prefere jogar apenas uma partida (opção 1) ou um campeonato (opção 2).
