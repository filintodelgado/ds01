# contem as funções utilitarias relacionadas ao board

branco = "○" # o caracter que será preenchido no espaço em branco
jogado = "●" # o caracter que será na tela (com cores)


def criarBoard(linhas, colunas):
  board = []

  for i in range(linhas):
    board.append([]) # adciona uma nova linha
    for j in range(colunas):
      board[i].append(branco)

  return board


def printBoard(board):
  pass