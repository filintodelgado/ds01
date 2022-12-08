# Filinto Cassiano de Jesus Furtado Delgado
# 40220485
# Desafio 1: Jogo 4 em linha 1.0

# importação de modulos
from lib.board import *
from lib.utils import *
from lib.color import cores

# remove qualquer coloração que já exista no seu terminal
print(cores["end"], end="")

# Informações da board
boardLinhas      = 6
boardColunas     = 7
numeroDeJogadas  = 4 # numero de fichas seguidas necessarias para vencer o jogo

jogadasPossiveis = boardLinhas * boardColunas # o numero de jogadas possivel na board
jogadasRestantes = jogadasPossiveis # no inicio do jogo as jogadas restantes são as mesmas das jogadas possiveis
jogadasEfetuadas = 0 

jogadores = [] # vai conter os nomes do jogadores
jogador = 0 # o jogador que está a jogar

board = criarBoard(boardLinhas, boardColunas)


def menu():
  print("Jogo quatro em linha"+"="*10)

while True:
  

  break