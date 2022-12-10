# Filinto Cassiano de Jesus Furtado Delgado
# 40220485
# Desafio 1: Jogo 4 em linha 1.0

# importação de modulos
from lib.board import *
from lib.utils import *
from lib.color import cores
from os import system
from random import randint

# remove qualquer coloração que já exista no seu terminal
print(cores["end"], end="")

# Informações da board
boardLinhas      = 6
boardColunas     = 7

# numero de fichas seguidas necessarias para vencer o jogo
numeroVencedor  = 4 
vencedor        = 0 # quem venceu a partida

jogadasPossiveis = boardLinhas * boardColunas # o numero de jogadas possivel na board
jogadasRestantes = jogadasPossiveis # no inicio do jogo as jogadas restantes são as mesmas das jogadas possiveis
jogadasEfetuadas = 0 

jogadores = [] # vai conter os nomes do jogadores
jogador = 0 # o jogador que está a jogar

board = criarBoard(boardLinhas, boardColunas)
encontrados = [] # irá conter as posições vencedoras


def printStyle(mensagem:str, cor="end") -> str:
  """
  imprime a mensagem centralizado e colorido
  """
  print(colorir(center(mensagem), cor))


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


def iniciar() -> None:
  """
  Inicia o jogo imprimido uma mensagem inicial na tela e resetado algumas variaveis
  """
  global jogador, jogadasRestantes, jogadasEfetuadas, jogadores, boardColunas, boardLinhas, board

  jogadasRestantes = jogadasPossiveis
  jogadasEfetuadas = 0
  board = criarBoard(boardLinhas, boardColunas)
  system("clear")
  menu()
  print()
  printBoard(board)
  jgoadores = []
  jogadores.append(get_str("Jogador 1 digite o seu nome: ", "Nome de jogador 1 invalido.", 3))
  jogadores.append(get_str("Jogador 2 digite o seu nome: ", "Nome de jogador 2 invalido.", 3))
  jogador = randint(0, 1)
  board   = criarBoard(boardLinhas, boardColunas)
  encontrados = []
  esperar()


def printJogador(jogador:int) -> str:
  global jogadores

  return colorir(jogadores[jogador], coresBoard[0])


def proximaJogada() -> None:
  """
  Faz a proxima jogada
  """
  global jogadasEfetuadas, jogadasRestantes, jogadores, jogador, board

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
    coluna = get_int(max = boardColunas, min = 1, prompt="Em que coluna deseja inserir a ficha: ", error_prompt="Coluna invalida") - 1

    if not jogar(board, coluna, jogador):
      print("Esta coluna está cheia. Jogue novamente.")
    else:
      break

  jogador = (jogador + 1) % 2 # um pouco de matématica, se o jogador for 1, 1+1 = 2%2 = 0 e assim por diante

  jogadasRestantes-=1
  jogadasEfetuadas-=1


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


# loop principal do programa
while True:
  iniciar()
  # Enquanto não existir um vencedor ou ainda há jogadas restantes
  while not encontrarSequencia(board, numeroVencedor) and jogadasRestantes:
    proximaJogada() # faz uma jogada
  
  if encontrarSequencia(board, numeroVencedor):
    encontrados = encontrarSequencia(board, numeroVencedor)
    printVencedor()
  else:
    print("Jogo terminado em impate")
    printBoard(board)
  
  escolha = get_str("Deseja continuar a jogar [Y/n]: ", "Escolha invalida.", 0)

  if escolha.lower() != "y":
    break
