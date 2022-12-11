# Filinto Cassiano de Jesus Furtado Delgado
# 40220485
# Desafio 1: Jogo 4 em linha 1.0

# importação de modulos proprietarios
from lib.board import * # para funções de manipulação de board
from lib.utils import * # para funções utilitarios
from lib.color import * # para funções de cores

# modulos build-in
from os import system      # para limpar o terminal
from random import randint

# remove qualquer coloração que já exista no seu terminal
print(cores["end"], end="")

# Informações da board
boardLinhas  = 6
boardColunas = 7

# numero de fichas seguidas necessarias para vencer o jogo
sequencia_vencedora = 4 
vencedor = 0 # quem venceu a partida

jogadasPossiveis = boardLinhas * boardColunas # o numero de jogadas possivel na board
jogadasRestantes = jogadasPossiveis # no inicio do jogo as jogadas restantes são as mesmas das jogadas possiveis
jogadasEfetuadas = 0 

jogadores = [] # vai conter os nomes do jogadores
jogador   = 0 # o jogador que está a jogar

board = criarBoard(boardLinhas, boardColunas)
encontrados = [] # irá conter as posições vencedoras

mode = 0 # modo de jogo, 1 para singleplayer e 2 para multiplayer


def menu() -> None:
  """
  Imprime a mensagem inicial do jogo
  """
  printStyle("Jogo quatro em linha", "vermelho")
  print()
  printStyle("Regras gerais do jogo:", "amarelo")
  printStyle("Joga-se sempre entre 2 jogadores e sobre um tabuleiro de 7x6 espaços.")
  printStyle("Em cada turno cada jogador coloca uma ficha (símbolo) numa coluna e esta cai até à primeira casa disponível.")
  printStyle("O que conseguir colocar 4 fichas da mesma cor/Símbolo seguidas na horizontal, vertical ou diagonal ganha.")
  printStyle("Se ninguém conseguir a partida termina em empate.")


def esperar(prompt = "Pressiona <Enter> para continuar...") -> None:
  """
  Espera confirmação do usuario para continuar
  """

  print()
  input(prompt)


def get_mode():
  global mode

  system("clear")
  printStyle("Modos:", "amarelo")
  printStyle("Single Player - Solo [1]")
  printStyle("Multi Player - Contra computador [2]")

  mode = get_int(2, 1, "Em que modo deseja jogar: ", "Modo invalido. Digite 1 para single player e 2 para multiplayer.")


def iniciar() -> None:
  """
  Inicia o jogo imprimido uma mensagem inicial na tela e resetado algumas variaveis
  """
  global jogador, jogadasRestantes, jogadasEfetuadas, jogadores, boardColunas, boardLinhas, board, encontrados

  jogadasRestantes = jogadasPossiveis
  jogadasEfetuadas = 0
  board = criarBoard(boardLinhas, boardColunas)
  system("clear")
  menu()
  print()
  printBoard(board)
  jogadores = []
  jogador = randint(0, 1)
  board   = criarBoard(boardLinhas, boardColunas)
  encontrados = []
  esperar()


def printJogador(jogador:int) -> str:
  global jogadores

  return colorir(jogadores[jogador], coresBoard[0])


def predict() -> int:
  """
  O algoritmo que decide onde o computador vai jogar

  Primeiro procura uma sequencia de 3 de joga de ao lado se for horizontal ou em sima se for vertical
  Depois procura uma sequencia de 2 e caso não encontre joga aleatoriamente

  O valor retornado é a coluna
  """
  global board, branco

  sequencias = []
  numero_sequencias = 3

  while numero_sequencias > 1:
    if numero_sequencias:
      # se exitir sequencia for na vertical
      if vertical(board, numero_sequencias):
        sequencias = vertical(board, numero_sequencias)
        # se a linha de cima não for a primeira e a linha acima dela não estiver ocupada
        if sequencias[0][0] > 0:
          if board[sequencias[0][0] - 1][sequencias[0][1]] == branco:
            return sequencias[0][1]
      # se existir uma sequencia na horizontal
      if horizontal(board, numero_sequencias):
        sequencias = horizontal(board, numero_sequencias)
        # e a coluna do lado esquerdo estiver desocupada
        if sequencias[0][1] - 1 > -1:
          if board[sequencias[0][0]][sequencias[0][1] - 1] == branco:
            return sequencias[0][1] - 1 # retorna a coluna desocupada
        if sequencias[-1][1] < boardColunas - 1:
          if board[sequencias[-1][0]][sequencias[-1][1] + 1] == branco:
            return sequencias[-1][1] + 1
    numero_sequencias -= 1
  
  # caso não tenha encontrado uma sequencia
  tentativas = [] # numero de colunas que já tentou jogar
  while True:
    coluna = 0
    coluna = randint(0, 6) # escolhe uma coluna aleatoriamente

    # para evitar um loop infinito quando fizermos mais que 2 tentativas
    if len(tentativas) > 2:
      # vamos verificar apartir de 0 se este já foi tentado antes
      for i in range(6):
        # caso não vamos tentar
        if i not in tentativas:
          coluna = 1
          break
    if coluna not in tentativas: # se a coluna não foi tentada anteriormente 
      tentativas.append(coluna)  # adciona as tentativas
    else: # se já foi encontrada
      continue # pula para a proxima iteração

    if verificarColuna(board, coluna) != -1: # se a coluna está livre
      return coluna # retorna esta colua


def proximaJogada() -> None:
  """
  Faz a proxima jogada
  """
  global jogadasEfetuadas, jogadasRestantes, jogadores, jogador, board, mode

  system("clear")

  if jogadasEfetuadas == 0:
    print(f'{printJogador(jogador)} es o primeiro a jogar.')
  else:
    print(f'{printJogador(jogador)} é a sua vez de jogar.')
  
  print()
  print(f'Jogador 1: {jogadores[0]} ({colorir(jogado, coresBoard[0])})')
  print(f'Jogador 2: {jogadores[1]} ({colorir(jogado, coresBoard[1])})')

  print()
  printBoard(board)

  while True:
    coluna = predict() if (jogador == 1 and mode == 1) else get_coluna()
    if not jogar(board, coluna, jogador):
      print("Esta coluna está cheia. Jogue novamente.")
    else:
      break

  jogador = (jogador + 1) % 2 # um pouco de matématica, se o jogador for 1, 1+1 = 2%2 = 0 e assim por diante

  jogadasRestantes-=1
  jogadasEfetuadas-=1


def get_coluna():
  return get_int(max = boardColunas, min = 1, prompt="Em que coluna deseja inserir a ficha: ", error_prompt="Coluna invalida") - 1


def printVencedor():
  """
  Imprime o vencedor na tela
  """
  global board, encontrados, vencedor, joga

  vencedor = board[encontrados[0][0]][encontrados[0][1]]

  system("clear")

  print(f'O jogador vencedor é {printJogador(vencedor)}.')

  printBoard(board, encontrados)

  esperar()


def single_player():
  global jogadores, jogador, board, sequencia_vencedora, jogadasRestantes

  jogadores.append(get_str("Qual é o seu nome: ", "Nome invalido!", 3)) # pergunta o nome do jogador
  jogadores.append("Computador") # o segundo jogador é o computador

  while not encontrarSequencia(board, sequencia_vencedora) and jogadasRestantes:
    # Enquanto não existir um vencedor ou ainda há jogadas restantes
    proximaJogada()


def multi_player():
  jogadores.append(get_str("Jogador 1 digite o seu nome: ", "Nome de jogador 1 invalido.", 3))
  jogadores.append(get_str("Jogador 2 digite o seu nome: ", "Nome de jogador 2 invalido.", 3))

  while not encontrarSequencia(board, sequencia_vencedora) and jogadasRestantes:
    # Enquanto não existir um vencedor ou ainda há jogadas restantes
    proximaJogada(get_coluna()) # faz uma jogada


# loop principal do programa
while True:
  iniciar()

  get_mode()
  while not encontrarSequencia(board, sequencia_vencedora) and jogadasRestantes:
    if mode == 1:
      single_player()
    else:
      multi_player()

  if encontrarSequencia(board, sequencia_vencedora):
    encontrados = encontrarSequencia(board, sequencia_vencedora)
    printVencedor()
  else:
    print("Jogo terminado em impate")
    printBoard(board)
  
  escolha = get_str("Deseja continuar a jogar [Y/n]: ", "Escolha invalida.", 0)

  if escolha.lower() != "y":
    break