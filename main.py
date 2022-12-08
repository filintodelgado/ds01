# Filinto Cassiano de Jesus Furtado Delgado
# 40220485
# Desafio 1: Jogo 4 em linha 1.0

# importação de modulos
from board import *

# Informações da board
boardLinhas  = 6
boardColunas = 7
print(criarBoard(6, 7))

jogadasPossiveis = boardLinhas * boardColunas # o numero de jogadas possivel na board
jogadasRestantes = jogadasPossiveis # no inicio do jogo as jogadas restantes são as mesmas das jogadas possiveis
