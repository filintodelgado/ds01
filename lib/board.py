# contem as funções utilitarias relacionadas ao board

# importação de modulo
from color import colorir

branco = "○" # o caracter que será preenchido no espaço em branco
jogado = "●" # o caracter que será monstrado na tela (com cores)

cores = [
  "azul"     # cor de jogador 1
  "verde"    # cor de jogador 2
  "vermelho" # cor de jogada vencedora
]

def criarBoard(linhas: int, colunas: int) -> list:
  """
  Cria uma board usando as linhas e colunas especificadas em formato de array bidimensional
  """
  board = []

  for i in range(linhas):
    board.append([]) # adciona uma nova linha
    for j in range(colunas):
      board[i].append(branco)

  return board


def printBoard(board: list) -> None:
  """
  Imprime na tela a board formatado
  """
  for i in range(len(board)):
    for j in range(len(board[i])):
      casa = board[i][j]
      if type(casa) == int:
        # muda a casa para ser imprimido a cores e jogado
        casa = colorir(jogado, cores[casa])
      print(f' {casa} ', end="")
    print()


def jogar(board: list, coluna: int, jogador: int) -> bool:
  """
  Joga na primeira casa na disponivel na coluna de baixo para cima

  O jogador numero que será preenchido
  """
  for i in range(len(board), step=-1): # começamos por verificar de traz para frente
    if board[i][coluna] != branco:
      board[i][coluna] = jogador
      return True

  return False
  