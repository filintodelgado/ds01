# contem as funções utilitarias relacionadas ao board
# definições de funções em ./board.pyi

branco = "○" # o caracter que será preenchido no espaço em branco
jogado = "●" # o caracter que será monstrado na tela (com cores)


def criarBoard(linhas, colunas):
  board = []

  for i in range(linhas):
    board.append([]) # adciona uma nova linha
    for j in range(colunas):
      board[i].append(branco)

  return board


def printBoard(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      print(f' {board[i][j]} ', end="")
    print()


def jogar(board, coluna, jogador):
  for i in range(len(board), step=-1): # começamos por verificar de traz para frente
    if board[i][coluna] != branco:
      board[i][coluna] = jogador
      return True

  return False
  